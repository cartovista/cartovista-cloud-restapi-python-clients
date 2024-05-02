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
from cartovista_cloud_clients.api.organization_api import OrganizationApi  # noqa: E501
from cartovista_cloud_clients.rest import ApiException


class TestOrganizationApi(unittest.TestCase):
    """OrganizationApi unit test stubs"""

    def setUp(self):
        self.api = OrganizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_organization_accept_organization_disclaimer(self):
        """Test case for organization_accept_organization_disclaimer

        Marks the organization's disclaimer as seen for the current user.  # noqa: E501
        """
        pass

    def test_organization_delete_organization(self):
        """Test case for organization_delete_organization

        Deletes the current organization.  # noqa: E501
        """
        pass

    def test_organization_get_organization(self):
        """Test case for organization_get_organization

        Gets the current organization.  # noqa: E501
        """
        pass

    def test_organization_get_organization_disclaimers(self):
        """Test case for organization_get_organization_disclaimers

        Gets the current organization's disclaimer.  # noqa: E501
        """
        pass

    def test_organization_set_organization_disclaimers(self):
        """Test case for organization_set_organization_disclaimers

        Updates the current organization's disclaimer.  # noqa: E501
        """
        pass

    def test_organization_update_license(self):
        """Test case for organization_update_license

        Updates the current organization's license.  # noqa: E501
        """
        pass

    def test_organization_update_organization(self):
        """Test case for organization_update_organization

        Updates the current organization.  # noqa: E501
        """
        pass

    def test_organization_update_organization_logo(self):
        """Test case for organization_update_organization_logo

        Updates the current organization's logo.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
