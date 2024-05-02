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
from cartovista_cloud_clients.api.symbol_api import SymbolApi  # noqa: E501
from cartovista_cloud_clients.rest import ApiException


class TestSymbolApi(unittest.TestCase):
    """SymbolApi unit test stubs"""

    def setUp(self):
        self.api = SymbolApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_symbol_create_symbol(self):
        """Test case for symbol_create_symbol

        Creates a new custom symbol from a file.  # noqa: E501
        """
        pass

    def test_symbol_delete_symbol(self):
        """Test case for symbol_delete_symbol

        Deletes the symbol.  # noqa: E501
        """
        pass

    def test_symbol_get_symbols(self):
        """Test case for symbol_get_symbols

        Gets all the custom symbols.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()