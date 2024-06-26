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
from cartovista_cloud_clients.api.layer_settings_api import LayerSettingsApi  # noqa: E501
from cartovista_cloud_clients.rest import ApiException


class TestLayerSettingsApi(unittest.TestCase):
    """LayerSettingsApi unit test stubs"""

    def setUp(self):
        self.api = LayerSettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_layer_settings_get_default_layer_settings(self):
        """Test case for layer_settings_get_default_layer_settings

        Gets the default settings for the layer.  # noqa: E501
        """
        pass

    def test_layer_settings_get_layer_settings(self):
        """Test case for layer_settings_get_layer_settings

        Gets a specific layer settings.  # noqa: E501
        """
        pass

    def test_layer_settings_get_map_layer_settings(self):
        """Test case for layer_settings_get_map_layer_settings

        Gets the layer settings for a specific map.  # noqa: E501
        """
        pass

    def test_layer_settings_update_alias(self):
        """Test case for layer_settings_update_alias

        Updates the layer settings' alias.  # noqa: E501
        """
        pass

    def test_layer_settings_update_effect(self):
        """Test case for layer_settings_update_effect

        Updates the layer settings' effects.  # noqa: E501
        """
        pass

    def test_layer_settings_update_general(self):
        """Test case for layer_settings_update_general

        Updates the layer settings' general settings.  # noqa: E501
        """
        pass

    def test_layer_settings_update_geometry_style(self):
        """Test case for layer_settings_update_geometry_style

        Updates the layer settings' geometry style. The style object must match the layer's geometry type.  # noqa: E501
        """
        pass

    def test_layer_settings_update_interactivity(self):
        """Test case for layer_settings_update_interactivity

        Updates the layer settings' interactivity settings.  # noqa: E501
        """
        pass

    def test_layer_settings_update_label(self):
        """Test case for layer_settings_update_label

        Updates the layer settings' label settings.  # noqa: E501
        """
        pass

    def test_layer_settings_update_rendering(self):
        """Test case for layer_settings_update_rendering

        Updates the layer settings' rendering settings.  # noqa: E501
        """
        pass

    def test_layer_settings_update_visibility_ranges(self):
        """Test case for layer_settings_update_visibility_ranges

        Updates the layer settings' visibility ranges.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
