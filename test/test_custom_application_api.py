# coding: utf-8

"""
    CartoVista REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import cartovista_cloud_clients
from cartovista_cloud_clients.api.custom_application_api import CustomApplicationApi  # noqa: E501
from cartovista_cloud_clients.rest import ApiException


class TestCustomApplicationApi(unittest.TestCase):
    """CustomApplicationApi unit test stubs"""

    def setUp(self):
        self.api = CustomApplicationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_custom_application_get_custom_application_settings(self):
        """Test case for custom_application_get_custom_application_settings

        """
        pass

    def test_custom_application_toggle_custom_application(self):
        """Test case for custom_application_toggle_custom_application

        """
        pass

    def test_custom_application_update_custom_application_settings(self):
        """Test case for custom_application_update_custom_application_settings

        """
        pass


if __name__ == '__main__':
    unittest.main()
