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
from cartovista_cloud_clients.api.folder_api import FolderApi  # noqa: E501
from cartovista_cloud_clients.rest import ApiException


class TestFolderApi(unittest.TestCase):
    """FolderApi unit test stubs"""

    def setUp(self):
        self.api = FolderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_folder_create_folder(self):
        """Test case for folder_create_folder

        Creates a new folder.  # noqa: E501
        """
        pass

    def test_folder_delete_folder(self):
        """Test case for folder_delete_folder

        Deletes a folder.  # noqa: E501
        """
        pass

    def test_folder_get_folder(self):
        """Test case for folder_get_folder

        Gets a specific folder.  # noqa: E501
        """
        pass

    def test_folder_get_folders(self):
        """Test case for folder_get_folders

        Searches all the folders inside a parent.  # noqa: E501
        """
        pass

    def test_folder_get_folders_with_path(self):
        """Test case for folder_get_folders_with_path

        Gets all the folders in a given parent and the path to that parent.  # noqa: E501
        """
        pass

    def test_folder_update_folder(self):
        """Test case for folder_update_folder

        Updates a folder's properties.  # noqa: E501
        """
        pass

    def test_folder_update_item_parent_folder(self):
        """Test case for folder_update_item_parent_folder

        Moves an item to a different folder.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
