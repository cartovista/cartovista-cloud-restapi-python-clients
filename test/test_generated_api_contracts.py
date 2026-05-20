# coding: utf-8

from __future__ import absolute_import

import inspect
import unittest

import cartovista_cloud_clients.api as api_package


class RecordingApiClient(object):
    RETURN_VALUE = object()
    ALLOWED_METHODS = {
        "GET", "HEAD", "DELETE", "POST", "PUT", "PATCH", "OPTIONS"
    }

    def __init__(self):
        self.calls = []

    def select_header_accept(self, accepts):
        if not accepts:
            return None
        lowered = [accept.lower() for accept in accepts]
        if "application/json" in lowered:
            return "application/json"
        return ", ".join(lowered)

    def select_header_content_type(self, content_types):
        if not content_types:
            return "application/json"
        lowered = [content_type.lower() for content_type in content_types]
        if "application/json" in lowered or "*/*" in lowered:
            return "application/json"
        return lowered[0]

    def call_api(self, resource_path, method, path_params=None,
                 query_params=None, header_params=None, body=None,
                 post_params=None, files=None, response_type=None,
                 auth_settings=None, async_req=None,
                 _return_http_data_only=None, collection_formats=None,
                 _preload_content=True, _request_timeout=None):
        self.calls.append({
            "resource_path": resource_path,
            "method": method,
            "path_params": path_params,
            "query_params": query_params,
            "header_params": header_params,
            "body": body,
            "post_params": post_params,
            "files": files,
            "response_type": response_type,
            "auth_settings": auth_settings,
            "async_req": async_req,
            "_return_http_data_only": _return_http_data_only,
            "collection_formats": collection_formats,
            "_preload_content": _preload_content,
            "_request_timeout": _request_timeout,
        })
        return self.RETURN_VALUE


def _api_classes():
    classes = []
    for name, cls in vars(api_package).items():
        if (inspect.isclass(cls) and
                getattr(cls, "__module__", "").startswith(
                    "cartovista_cloud_clients.api.")):
            classes.append((name, cls))
    return sorted(classes)


def _operation_methods(api_cls):
    for name, member in inspect.getmembers(api_cls, inspect.isfunction):
        if name.startswith("_") or name.endswith("_with_http_info"):
            continue
        if name == "__init__":
            continue
        yield name


def _sample_argument(parameter_name):
    if parameter_name.endswith("_id") or parameter_name == "id":
        return "sample-id"
    if parameter_name in ("tenant_url_code", "tenant"):
        return "tenant"
    if parameter_name in ("selected_language", "language"):
        return "en"
    if parameter_name in ("page", "page_index", "limit", "offset"):
        return 1
    if parameter_name in ("active", "enabled", "recursive"):
        return True
    return "sample"


class TestGeneratedApiContracts(unittest.TestCase):
    def test_all_api_methods_delegate_to_api_client(self):
        for api_name, api_cls in _api_classes():
            for method_name in _operation_methods(api_cls):
                with self.subTest(api=api_name, method=method_name):
                    client = RecordingApiClient()
                    api = api_cls(api_client=client)
                    method = getattr(api, method_name)
                    signature = inspect.signature(method)
                    args = [
                        _sample_argument(param.name)
                        for param in signature.parameters.values()
                        if param.default is inspect._empty and
                        param.kind in (
                            param.POSITIONAL_ONLY,
                            param.POSITIONAL_OR_KEYWORD,
                            param.KEYWORD_ONLY)
                    ]

                    result = method(*args)

                    self.assertIs(result, RecordingApiClient.RETURN_VALUE)
                    self.assertEqual(1, len(client.calls))
                    call = client.calls[0]
                    self.assertTrue(call["resource_path"].startswith("/"))
                    self.assertIn(
                        call["method"],
                        RecordingApiClient.ALLOWED_METHODS)
                    self.assertTrue(call["_return_http_data_only"])
                    self.assertIsInstance(call["collection_formats"], dict)

    def test_all_api_methods_reject_unexpected_keyword_arguments(self):
        for api_name, api_cls in _api_classes():
            for method_name in _operation_methods(api_cls):
                with self.subTest(api=api_name, method=method_name):
                    api = api_cls(api_client=RecordingApiClient())
                    method = getattr(api, method_name)
                    signature = inspect.signature(method)
                    args = [
                        _sample_argument(param.name)
                        for param in signature.parameters.values()
                        if param.default is inspect._empty and
                        param.kind in (
                            param.POSITIONAL_ONLY,
                            param.POSITIONAL_OR_KEYWORD,
                            param.KEYWORD_ONLY)
                    ]

                    with self.assertRaises(TypeError):
                        method(*args, unexpected=True)

    def test_all_api_methods_reject_none_for_required_arguments(self):
        for api_name, api_cls in _api_classes():
            for method_name in _operation_methods(api_cls):
                api = api_cls(api_client=RecordingApiClient())
                method = getattr(api, method_name)
                signature = inspect.signature(method)
                required_params = [
                    param
                    for param in signature.parameters.values()
                    if param.default is inspect._empty and
                    param.kind in (
                        param.POSITIONAL_ONLY,
                        param.POSITIONAL_OR_KEYWORD,
                        param.KEYWORD_ONLY)
                ]
                if not required_params:
                    continue

                for index, required_param in enumerate(required_params):
                    with self.subTest(
                            api=api_name,
                            method=method_name,
                            parameter=required_param.name):
                        args = [
                            _sample_argument(param.name)
                            for param in required_params
                        ]
                        args[index] = None

                        with self.assertRaises(ValueError):
                            method(*args)


if __name__ == "__main__":
    unittest.main()
