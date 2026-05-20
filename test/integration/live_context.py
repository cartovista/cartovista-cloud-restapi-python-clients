# coding: utf-8

from __future__ import absolute_import

import json
import unittest

import cartovista_cloud_clients.api as api_package
from cartovista_cloud_clients.api.authentication_api import AuthenticationApi
from cartovista_cloud_clients.api_client import ApiClient
from cartovista_cloud_clients.configuration import Configuration
from cartovista_cloud_clients.models.login_credential_dto import LoginCredentialDTO
from cartovista_cloud_clients.models.security_provider import SecurityProvider
from cartovista_cloud_clients.rest import ApiException

from integration.live_assertions import candidate_identifier, first_item


class LiveApiContext(object):
    def __init__(self, config):
        self.config = config
        self.tenant = config.tenant
        self.configuration = Configuration()
        self.configuration.host = config.host
        if config.api_key:
            self.configuration.api_key["apiKey"] = config.api_key
        if config.secret_key:
            self.configuration.api_key["secretKey"] = config.secret_key
        self.api_client = ApiClient(self.configuration)
        self._api_cache = {}
        self._response_cache = {}
        self._cleanups = []

    def authenticate(self):
        response = AuthenticationApi(self.api_client).authentication_global_login(
            self.login_body()
        )
        token = extract_token(response)
        if not token:
            raise AssertionError(
                "Login succeeded but no bearer token could be extracted")

        if token.lower().startswith("bearer "):
            self.configuration.api_key["Authorization"] = token[7:]
        else:
            self.configuration.api_key["Authorization"] = token
        self.configuration.api_key_prefix["Authorization"] = "Bearer"
        return token

    def login_body(self):
        return LoginCredentialDTO(
            provider=SecurityProvider.CARTOVISTA,
            provider_name=SecurityProvider.CARTOVISTA,
            username_or_email_address=self.config.email,
            password_or_token=self.config.password,
            keep_me_signed=True,
        )

    def api(self, class_name):
        if class_name not in self._api_cache:
            api_class = getattr(api_package, class_name)
            self._api_cache[class_name] = api_class(self.api_client)
        return self._api_cache[class_name]

    def call(self, class_name, method_name, *args, **kwargs):
        return getattr(self.api(class_name), method_name)(*args, **kwargs)

    def cached(self, key, factory):
        if key not in self._response_cache:
            self._response_cache[key] = factory()
        return self._response_cache[key]

    def unique_name(self, suffix):
        return "python-api-test-{0}-{1}".format(
            self.config.run_id, suffix).replace("_", "-")[:120]

    def register_cleanup(self, func):
        self._cleanups.append(func)

    def cleanup_all(self):
        errors = []
        while self._cleanups:
            cleanup = self._cleanups.pop()
            try:
                cleanup()
            except ApiException as exc:
                # Deleted resources may legitimately disappear during cleanup.
                if getattr(exc, "status", None) not in (404, 410):
                    errors.append(exc)
            except Exception as exc:  # noqa: B902 - py2 compatible tests
                errors.append(exc)
        if errors:
            raise AssertionError(
                "Live API cleanup failed: {0}".format(errors))

    def first_identifier_from(self, cache_key, factory, resource_name):
        collection = self.cached(cache_key, factory)
        item = first_item(collection)
        identifier = candidate_identifier(item)
        if not identifier:
            raise unittest.SkipTest(
                "No {0} available in tenant {1}".format(
                    resource_name, self.tenant))
        return identifier


def extract_token(response):
    if response is None:
        return None
    if isinstance(response, str):
        stripped = response.strip()
        if not stripped:
            return None
        try:
            parsed = json.loads(stripped)
        except ValueError:
            return stripped.strip('"')
        return extract_token(parsed)
    if isinstance(response, dict):
        for key in (
                "accessToken",
                "access_token",
                "token",
                "bearerToken",
                "bearer_token"):
            if response.get(key):
                return response[key]
        return None
    for attr in (
            "access_token",
            "accessToken",
            "token",
            "bearer_token",
            "bearerToken"):
        value = getattr(response, attr, None)
        if value:
            return value
    return str(response)
