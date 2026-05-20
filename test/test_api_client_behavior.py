# coding: utf-8

from __future__ import absolute_import

import datetime
import unittest

from cartovista_cloud_clients.api_client import ApiClient
from cartovista_cloud_clients.configuration import Configuration
from cartovista_cloud_clients.models.coordinate import Coordinate


class FakeResponse(object):
    status = 200
    data = b"{}"

    def getheaders(self):
        return {"Content-Type": "application/json"}


class RecordingApiClient(ApiClient):
    def __init__(self, configuration=None, header_name=None,
                 header_value=None, cookie=None):
        super(RecordingApiClient, self).__init__(
            configuration=configuration,
            header_name=header_name,
            header_value=header_value,
            cookie=cookie)
        self.requests = []

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None):
        self.requests.append({
            "method": method,
            "url": url,
            "query_params": query_params,
            "headers": headers,
            "post_params": post_params,
            "body": body,
            "_preload_content": _preload_content,
            "_request_timeout": _request_timeout,
        })
        return FakeResponse()


class TestApiClientBehavior(unittest.TestCase):
    def test_sanitize_for_serialization_uses_json_attribute_names(self):
        client = ApiClient()
        serialized = client.sanitize_for_serialization({
            "coordinate": Coordinate(longitude=-73.56),
            "created": datetime.date(2026, 5, 15),
            "items": [Coordinate(latitude=45.5)],
        })

        self.assertEqual(
            serialized,
            {
                "coordinate": {"longitude": -73.56},
                "created": "2026-05-15",
                "items": [{"latitude": 45.5}],
            })

    def test_parameters_to_tuples_formats_collection_values(self):
        client = ApiClient()
        params = {
            "csv": [1, 2],
            "ssv": [1, 2],
            "tsv": [1, 2],
            "pipes": [1, 2],
            "multi": [1, 2],
            "plain": "value",
        }

        self.assertEqual(
            client.parameters_to_tuples(
                params,
                {
                    "csv": "csv",
                    "ssv": "ssv",
                    "tsv": "tsv",
                    "pipes": "pipes",
                    "multi": "multi",
                }),
            [
                ("csv", "1,2"),
                ("ssv", "1 2"),
                ("tsv", "1\t2"),
                ("pipes", "1|2"),
                ("multi", 1),
                ("multi", 2),
                ("plain", "value"),
            ])

    def test_update_params_for_auth_adds_configured_header_tokens(self):
        configuration = Configuration()
        configuration.api_key["apiKey"] = "api-key"
        configuration.api_key["Authorization"] = "access-token"
        configuration.api_key_prefix["Authorization"] = "Bearer"
        client = ApiClient(configuration=configuration)

        headers = {}
        client.update_params_for_auth(headers, [], ["apiKey", "bearer"])

        self.assertEqual(headers["apiKey"], "api-key")
        self.assertEqual(headers["Authorization"], "Bearer access-token")

    def test_call_api_encodes_paths_and_merges_headers_without_network(self):
        client = RecordingApiClient(
            header_name="X-Client",
            header_value="client-value",
            cookie="session=abc")

        result = client.call_api(
            "/tenants/{tenantId}/items/{itemId}",
            "GET",
            path_params={"tenantId": "a/b", "itemId": "x y"},
            query_params=[("q", "value")],
            header_params={"X-Test": "1"},
            response_type=None,
            auth_settings=[],
            _return_http_data_only=False,
            collection_formats={})

        request = client.requests[0]
        self.assertEqual(
            request["url"],
            "https://cloud.cartovista.com/tenants/a%2Fb/items/x%20y")
        self.assertEqual(request["query_params"], [("q", "value")])
        self.assertEqual(request["headers"]["X-Test"], "1")
        self.assertEqual(request["headers"]["X-Client"], "client-value")
        self.assertEqual(request["headers"]["Cookie"], "session=abc")
        self.assertIsNone(result[0])
        self.assertEqual(result[1], 200)

    def test_call_api_sanitizes_model_body_before_request(self):
        client = RecordingApiClient()

        client.call_api(
            "/coordinates",
            "POST",
            body=Coordinate(longitude=-73.56, latitude=45.5),
            header_params={"Content-Type": "application/json"},
            response_type=None,
            auth_settings=[],
            _return_http_data_only=True,
            collection_formats={})

        self.assertEqual(
            client.requests[0]["body"],
            {"longitude": -73.56, "latitude": 45.5})


if __name__ == "__main__":
    unittest.main()
