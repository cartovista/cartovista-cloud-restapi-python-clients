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
from cartovista_cloud_clients.api.slide_api import SlideApi  # noqa: E501
from cartovista_cloud_clients.rest import ApiException


class TestSlideApi(unittest.TestCase):
    """SlideApi unit test stubs"""

    def setUp(self):
        self.api = SlideApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_slide_delete_slide(self):
        """Test case for slide_delete_slide

        Deletes the slide.  # noqa: E501
        """
        pass

    def test_slide_delete_slide_analysis(self):
        """Test case for slide_delete_slide_analysis

        Deletes the analysis from the slide.  # noqa: E501
        """
        pass

    def test_slide_get_slide(self):
        """Test case for slide_get_slide

        Gets a specific slide.  # noqa: E501
        """
        pass

    def test_slide_reorder_slides(self):
        """Test case for slide_reorder_slides

        Changes the order of a slide in the slide details view. The order will be the same in the slide ids list.  # noqa: E501
        """
        pass

    def test_slide_update_default_slide_thumbnail(self):
        """Test case for slide_update_default_slide_thumbnail

        Updates the map's default slide's thumbnail.  # noqa: E501
        """
        pass

    def test_slide_update_slide(self):
        """Test case for slide_update_slide

        Updates the slide.  # noqa: E501
        """
        pass

    def test_slide_update_slide_extent_from_layers(self):
        """Test case for slide_update_slide_extent_from_layers

        Updates the slide's extent by combining the layers' extents.  # noqa: E501
        """
        pass

    def test_slide_update_slide_theme_set(self):
        """Test case for slide_update_slide_theme_set

        Updates the slide's theme set.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()