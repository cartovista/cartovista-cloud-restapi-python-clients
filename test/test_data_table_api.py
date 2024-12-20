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
from cartovista_cloud_clients.api.data_table_api import DataTableApi  # noqa: E501
from cartovista_cloud_clients.rest import ApiException


class TestDataTableApi(unittest.TestCase):
    """DataTableApi unit test stubs"""

    def setUp(self):
        self.api = DataTableApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_data_table_append_data_to_data_table(self):
        """Test case for data_table_append_data_to_data_table

        Appends the content of a file at the end of the table. The file format must match the table.  # noqa: E501
        """
        pass

    def test_data_table_create_data_table(self):
        """Test case for data_table_create_data_table

        Creates a new empty table.  # noqa: E501
        """
        pass

    def test_data_table_create_from_csv(self):
        """Test case for data_table_create_from_csv

        Creates a table from a CSV file.  # noqa: E501
        """
        pass

    def test_data_table_create_from_excel(self):
        """Test case for data_table_create_from_excel

        Creates a new table from an Excel file. If the files has multiple sheets, only the first one is used.  # noqa: E501
        """
        pass

    def test_data_table_create_from_excel2(self):
        """Test case for data_table_create_from_excel2

        Creates a new table from an Excel file using a specific sheet.  # noqa: E501
        """
        pass

    def test_data_table_de_optimize_data_table(self):
        """Test case for data_table_de_optimize_data_table

        Disable the ClickHouse optimization for this table.  # noqa: E501
        """
        pass

    def test_data_table_delete_data_table(self):
        """Test case for data_table_delete_data_table

        Deletes the table.  # noqa: E501
        """
        pass

    def test_data_table_delete_join(self):
        """Test case for data_table_delete_join

        Deletes a join between a table and a layer.  # noqa: E501
        """
        pass

    def test_data_table_geocode_data_table(self):
        """Test case for data_table_geocode_data_table

        Converts a table to a point by building addresses using the list of columns.  # noqa: E501
        """
        pass

    def test_data_table_georeference_data_table(self):
        """Test case for data_table_georeference_data_table

        Converts a table to a point layer using two of its columns as latitude and longitude.  # noqa: E501
        """
        pass

    def test_data_table_get_data_table_by_identifier(self):
        """Test case for data_table_get_data_table_by_identifier

        Gets a specifc table.  # noqa: E501
        """
        pass

    def test_data_table_get_data_table_details(self):
        """Test case for data_table_get_data_table_details

        Gets the table, its related maps, tables, columns and settings.  # noqa: E501
        """
        pass

    def test_data_table_get_data_tables(self):
        """Test case for data_table_get_data_tables

        Gets all the tables the user has access to.  # noqa: E501
        """
        pass

    def test_data_table_get_expected_join_count(self):
        """Test case for data_table_get_expected_join_count

        Gets the number of links between a table and a layer. The result can be for a 1-to-1 or 1-to-n join.  # noqa: E501
        """
        pass

    def test_data_table_get_file_description(self):
        """Test case for data_table_get_file_description

        Stores a temporary file for an upcoming data insert or update and returns a description of the file's content.  # noqa: E501
        """
        pass

    def test_data_table_get_layers_by_data_table_identifier(self):
        """Test case for data_table_get_layers_by_data_table_identifier

        Gets all the layers associated to the table (joins or parent layer, if any).  # noqa: E501
        """
        pass

    def test_data_table_get_maps_by_data_table_identifier(self):
        """Test case for data_table_get_maps_by_data_table_identifier

        Gets all the maps that use the table.  # noqa: E501
        """
        pass

    def test_data_table_get_time_range_by_data_table_identifier(self):
        """Test case for data_table_get_time_range_by_data_table_identifier

        Gets the table's time range. The time series column must be set.  # noqa: E501
        """
        pass

    def test_data_table_get_time_series_data(self):
        """Test case for data_table_get_time_series_data

        Returns an aggregation of the table's data using the time series column.  # noqa: E501
        """
        pass

    def test_data_table_get_time_series_data_many_features(self):
        """Test case for data_table_get_time_series_data_many_features

        Returns an aggregation of the table's data using the time series column.  # noqa: E501
        """
        pass

    def test_data_table_get_time_series_dates(self):
        """Test case for data_table_get_time_series_dates

        Returns a list of all the dates in the time series table.  # noqa: E501
        """
        pass

    def test_data_table_join_data_table(self):
        """Test case for data_table_join_data_table

        Joins a table to a layer. The number of valid links must be greater than 0.  # noqa: E501
        """
        pass

    def test_data_table_optimize_data_table(self):
        """Test case for data_table_optimize_data_table

        Optimizes the table queries with ClickHouse. If the table belongs to a layer, the layer must be tiled.  # noqa: E501
        """
        pass

    def test_data_table_set_data_column_unique_id(self):
        """Test case for data_table_set_data_column_unique_id

        Sets the table's unique identifier column. The column becomes the primary way to identify its rows.  # noqa: E501
        """
        pass

    def test_data_table_set_time_series_column(self):
        """Test case for data_table_set_time_series_column

        Sets the time series column for a table. The column is required for time analyses in maps.  # noqa: E501
        """
        pass

    def test_data_table_set_unique_identifier(self):
        """Test case for data_table_set_unique_identifier

        Sets the table's identifier.  # noqa: E501
        """
        pass

    def test_data_table_update_data_table(self):
        """Test case for data_table_update_data_table

        Updates the table's properties.  # noqa: E501
        """
        pass

    def test_data_table_update_data_table_from_file(self):
        """Test case for data_table_update_data_table_from_file

        Updates a table's data with a file. The file's format must match the table.  # noqa: E501
        """
        pass

    def test_data_table_update_data_table_from_file_description(self):
        """Test case for data_table_update_data_table_from_file_description

        Updates a table with a file uploaded using `DataTable/{dataTableIdentifier}/getFileDescription`.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
