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
from cartovista_cloud_clients.api.view_api import ViewApi  # noqa: E501
from cartovista_cloud_clients.rest import ApiException


class TestViewApi(unittest.TestCase):
    """ViewApi unit test stubs"""

    def setUp(self):
        self.api = ViewApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_view_create_view_by_expression(self):
        """Test case for view_create_view_by_expression

        Creates a view based on an expression.  # noqa: E501
        """
        pass

    def test_view_create_views_from_column(self):
        """Test case for view_create_views_from_column

        Creates views based on a layer column id. This will generate one view for each unique value of the selected column.  # noqa: E501
        """
        pass

    def test_view_delete_views(self):
        """Test case for view_delete_views

        Deletes all the views associated with the layer.  # noqa: E501
        """
        pass

    def test_view_get_view(self):
        """Test case for view_get_view

        Gets a specific view by id.  # noqa: E501
        """
        pass

    def test_view_get_views(self):
        """Test case for view_get_views

        Gets the list of views associated with a layer.  # noqa: E501
        """
        pass

    def test_view_update_view(self):
        """Test case for view_update_view

        Updates the view parameters.  # noqa: E501
        """
        pass

    def test_view_update_view_permissions(self):
        """Test case for view_update_view_permissions

        Updates the view permissions. Note: This needs to list all the permissions on the view as the missing permissions will be deleted.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
