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
from cartovista_cloud_clients.api.statistics_api import StatisticsApi  # noqa: E501
from cartovista_cloud_clients.rest import ApiException


class TestStatisticsApi(unittest.TestCase):
    """StatisticsApi unit test stubs"""

    def setUp(self):
        self.api = StatisticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_statistics_get_statistics(self):
        """Test case for statistics_get_statistics

        Gets the usage statistics of the organization.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
