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
from cartovista_cloud_clients.api.portal_api import PortalApi  # noqa: E501
from cartovista_cloud_clients.rest import ApiException


class TestPortalApi(unittest.TestCase):
    """PortalApi unit test stubs"""

    def setUp(self):
        self.api = PortalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_portal_cancel_upload(self):
        """Test case for portal_cancel_upload

        Cancels the file upload.  # noqa: E501
        """
        pass

    def test_portal_finalize_upload(self):
        """Test case for portal_finalize_upload

        Finalizes a data import with a file uploaded using `upload`.  # noqa: E501
        """
        pass

    def test_portal_get_definition(self):
        """Test case for portal_get_definition

        Gets a description of the file's content.  # noqa: E501
        """
        pass

    def test_portal_get_subscription_and_user(self):
        """Test case for portal_get_subscription_and_user

        Gets the current user and the organization's subscription/license details.  # noqa: E501
        """
        pass

    def test_portal_upload(self):
        """Test case for portal_upload

        Uploads a temporary file for layer use.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
