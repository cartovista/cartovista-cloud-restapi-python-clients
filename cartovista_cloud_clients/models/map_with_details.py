# coding: utf-8

"""
    CartoVista REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MapWithDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'map': 'Map',
        'layers': 'list[Layer]',
        'data_tables': 'list[DataTable]',
        'grid_layers': 'list[GridLayer]',
        'wmts_layers': 'list[WmtsLayer]',
        'wms_layers': 'list[WmsLayer]',
        'permissions': 'list[PermissionPairComplexDTO]'
    }

    attribute_map = {
        'map': 'map',
        'layers': 'layers',
        'data_tables': 'dataTables',
        'grid_layers': 'gridLayers',
        'wmts_layers': 'wmtsLayers',
        'wms_layers': 'wmsLayers',
        'permissions': 'permissions'
    }

    def __init__(self, map=None, layers=None, data_tables=None, grid_layers=None, wmts_layers=None, wms_layers=None, permissions=None):  # noqa: E501
        """MapWithDetails - a model defined in Swagger"""  # noqa: E501
        self._map = None
        self._layers = None
        self._data_tables = None
        self._grid_layers = None
        self._wmts_layers = None
        self._wms_layers = None
        self._permissions = None
        self.discriminator = None
        if map is not None:
            self.map = map
        if layers is not None:
            self.layers = layers
        if data_tables is not None:
            self.data_tables = data_tables
        if grid_layers is not None:
            self.grid_layers = grid_layers
        if wmts_layers is not None:
            self.wmts_layers = wmts_layers
        if wms_layers is not None:
            self.wms_layers = wms_layers
        if permissions is not None:
            self.permissions = permissions

    @property
    def map(self):
        """Gets the map of this MapWithDetails.  # noqa: E501


        :return: The map of this MapWithDetails.  # noqa: E501
        :rtype: Map
        """
        return self._map

    @map.setter
    def map(self, map):
        """Sets the map of this MapWithDetails.


        :param map: The map of this MapWithDetails.  # noqa: E501
        :type: Map
        """

        self._map = map

    @property
    def layers(self):
        """Gets the layers of this MapWithDetails.  # noqa: E501


        :return: The layers of this MapWithDetails.  # noqa: E501
        :rtype: list[Layer]
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """Sets the layers of this MapWithDetails.


        :param layers: The layers of this MapWithDetails.  # noqa: E501
        :type: list[Layer]
        """

        self._layers = layers

    @property
    def data_tables(self):
        """Gets the data_tables of this MapWithDetails.  # noqa: E501


        :return: The data_tables of this MapWithDetails.  # noqa: E501
        :rtype: list[DataTable]
        """
        return self._data_tables

    @data_tables.setter
    def data_tables(self, data_tables):
        """Sets the data_tables of this MapWithDetails.


        :param data_tables: The data_tables of this MapWithDetails.  # noqa: E501
        :type: list[DataTable]
        """

        self._data_tables = data_tables

    @property
    def grid_layers(self):
        """Gets the grid_layers of this MapWithDetails.  # noqa: E501


        :return: The grid_layers of this MapWithDetails.  # noqa: E501
        :rtype: list[GridLayer]
        """
        return self._grid_layers

    @grid_layers.setter
    def grid_layers(self, grid_layers):
        """Sets the grid_layers of this MapWithDetails.


        :param grid_layers: The grid_layers of this MapWithDetails.  # noqa: E501
        :type: list[GridLayer]
        """

        self._grid_layers = grid_layers

    @property
    def wmts_layers(self):
        """Gets the wmts_layers of this MapWithDetails.  # noqa: E501


        :return: The wmts_layers of this MapWithDetails.  # noqa: E501
        :rtype: list[WmtsLayer]
        """
        return self._wmts_layers

    @wmts_layers.setter
    def wmts_layers(self, wmts_layers):
        """Sets the wmts_layers of this MapWithDetails.


        :param wmts_layers: The wmts_layers of this MapWithDetails.  # noqa: E501
        :type: list[WmtsLayer]
        """

        self._wmts_layers = wmts_layers

    @property
    def wms_layers(self):
        """Gets the wms_layers of this MapWithDetails.  # noqa: E501


        :return: The wms_layers of this MapWithDetails.  # noqa: E501
        :rtype: list[WmsLayer]
        """
        return self._wms_layers

    @wms_layers.setter
    def wms_layers(self, wms_layers):
        """Sets the wms_layers of this MapWithDetails.


        :param wms_layers: The wms_layers of this MapWithDetails.  # noqa: E501
        :type: list[WmsLayer]
        """

        self._wms_layers = wms_layers

    @property
    def permissions(self):
        """Gets the permissions of this MapWithDetails.  # noqa: E501


        :return: The permissions of this MapWithDetails.  # noqa: E501
        :rtype: list[PermissionPairComplexDTO]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this MapWithDetails.


        :param permissions: The permissions of this MapWithDetails.  # noqa: E501
        :type: list[PermissionPairComplexDTO]
        """

        self._permissions = permissions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MapWithDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MapWithDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other