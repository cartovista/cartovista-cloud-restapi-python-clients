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
from cartovista_cloud_clients.api.data_api import DataApi  # noqa: E501
from cartovista_cloud_clients.rest import ApiException


class TestDataApi(unittest.TestCase):
    """DataApi unit test stubs"""

    def setUp(self):
        self.api = DataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_data_export_data_elements(self):
        """Test case for data_export_data_elements

        Exports an Excel sheet of all the layers and tables. The file can be downloaded with `DownloadFile/download`. The language is used to localized the sheet's name and columns.  # noqa: E501
        """
        pass

    def test_data_export_data_table(self):
        """Test case for data_export_data_table

        Exports a table in an Excel file. The file can be downloaded with `DownloadFile/download`.  # noqa: E501
        """
        pass

    def test_data_export_layer(self):
        """Test case for data_export_layer

        Exports a layer in a specific format. The file can be downloaded with `DownloadFile/download`.  # noqa: E501
        """
        pass

    def test_data_get_data_elements(self):
        """Test case for data_get_data_elements

        Gets all the layers, tables and folders the user has access to in a specific folder. If the folder id is omitted, the root folder is used.  # noqa: E501
        """
        pass

    def test_data_search_all_data_elements(self):
        """Test case for data_search_all_data_elements

        Searches and retrieves all the layers and tables the user has access to.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
