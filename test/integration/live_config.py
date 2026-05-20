# coding: utf-8

from __future__ import absolute_import

import os
import uuid


DEFAULT_UPLOAD_FILE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "fixtures", "Supermarches.zip"))
DEFAULT_EXCEL_FILE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "fixtures", "live_data_table.xlsx"))
DEFAULT_EXCEL_SHEET_NAME = "Sheet1"


class LiveConfig(object):
    REQUIRED_ENV = {
        "host": ("CARTOVISTA_HOST", "Host"),
        "tenant": ("CARTOVISTA_TENANT", "Tenant"),
        "email": ("CARTOVISTA_API_ADMIN_EMAIL", "API_ADMIN_TEST_EMAIL"),
        "password": ("CARTOVISTA_API_TEST_PASSWORD", "API_TEST_PASSWORD"),
    }
    API_KEY_ENV = (
        "CARTOVISTA_PORTAL_API_KEY",
        "PORTAL_TEST_API_KEY",
        "apiKey",
    )
    SECRET_KEY_ENV = (
        "CARTOVISTA_PORTAL_SECRET_KEY",
        "PORTAL_TEST_SECRET_KEY",
        "secretKey",
    )

    def __init__(self, host, tenant, email, password, run_id,
                 allow_mutation=True, upload_file=None, api_key=None,
                 secret_key=None, excel_file=None, excel_sheet_name=None):
        self.host = normalize_host(host)
        self.tenant = tenant
        self.email = email
        self.password = password
        self.run_id = run_id
        self.allow_mutation = allow_mutation
        self.upload_file = upload_file
        self.api_key = api_key
        self.secret_key = secret_key
        self.excel_file = excel_file
        self.excel_sheet_name = excel_sheet_name

    @classmethod
    def from_environment(cls):
        values = {}
        missing = []
        for key, env_names in cls.REQUIRED_ENV.items():
            value = first_env(env_names)
            if value:
                values[key] = value
            else:
                missing.append("/".join(env_names))

        if missing:
            return None, (
                "Live API tests skipped. Missing environment variables: "
                + ", ".join(missing)
            )

        api_key = first_env(cls.API_KEY_ENV)
        secret_key = first_env(cls.SECRET_KEY_ENV)
        upload_file = first_env(("CARTOVISTA_LIVE_UPLOAD_FILE",))
        if not upload_file:
            upload_file = DEFAULT_UPLOAD_FILE
        excel_file = first_env(("CARTOVISTA_LIVE_EXCEL_FILE",))
        if not excel_file:
            excel_file = DEFAULT_EXCEL_FILE
        if require_live_config():
            if not api_key:
                missing.append("/".join(cls.API_KEY_ENV))
            if not secret_key:
                missing.append("/".join(cls.SECRET_KEY_ENV))
            if not upload_file or not os.path.exists(upload_file):
                missing.append("CARTOVISTA_LIVE_UPLOAD_FILE or {0}".format(
                    DEFAULT_UPLOAD_FILE))
            if not excel_file or not os.path.exists(excel_file):
                missing.append("CARTOVISTA_LIVE_EXCEL_FILE or {0}".format(
                    DEFAULT_EXCEL_FILE))
            if missing:
                return None, (
                    "Live API tests require environment variables: "
                    + ", ".join(missing)
                )

        run_id = first_env(("GITHUB_RUN_ID", "BUILD_BUILDID"))
        if not run_id:
            run_id = uuid.uuid4().hex

        allow_mutation = first_env(("CARTOVISTA_LIVE_ALLOW_MUTATION",))
        if allow_mutation is None:
            allow_mutation = "true"
        excel_sheet_name = (
            first_env(("CARTOVISTA_LIVE_EXCEL_SHEET_NAME",)) or
            DEFAULT_EXCEL_SHEET_NAME
        )

        return cls(
            host=values["host"],
            tenant=values["tenant"],
            email=values["email"],
            password=values["password"],
            run_id=run_id,
            allow_mutation=allow_mutation.lower() in ("1", "true", "yes"),
            upload_file=upload_file,
            api_key=api_key,
            secret_key=secret_key,
            excel_file=excel_file,
            excel_sheet_name=excel_sheet_name,
        ), None


def first_env(names):
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    return None


def require_live_config():
    value = first_env(("CARTOVISTA_REQUIRE_LIVE_CONFIG",))
    return value and value.lower() in ("1", "true", "yes")


def normalize_host(host):
    if host.startswith("http://") or host.startswith("https://"):
        return host.rstrip("/")
    return "https://{0}".format(host.rstrip("/"))
