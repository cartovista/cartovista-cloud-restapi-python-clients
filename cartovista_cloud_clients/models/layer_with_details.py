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

class LayerWithDetails(object):
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
        'layer': 'Layer',
        'maps': 'list[Map]',
        'permissions': 'list[PermissionPairComplexDTO]',
        'settings': 'LayerSettings',
        'data_tables': 'list[LayerDataTable]',
        'data_columns': 'list[DataColumn]',
        'grid_layers': 'list[GridLayer]'
    }

    attribute_map = {
        'layer': 'layer',
        'maps': 'maps',
        'permissions': 'permissions',
        'settings': 'settings',
        'data_tables': 'dataTables',
        'data_columns': 'dataColumns',
        'grid_layers': 'gridLayers'
    }

    def __init__(self, layer=None, maps=None, permissions=None, settings=None, data_tables=None, data_columns=None, grid_layers=None):  # noqa: E501
        """LayerWithDetails - a model defined in Swagger"""  # noqa: E501
        self._layer = None
        self._maps = None
        self._permissions = None
        self._settings = None
        self._data_tables = None
        self._data_columns = None
        self._grid_layers = None
        self.discriminator = None
        if layer is not None:
            self.layer = layer
        if maps is not None:
            self.maps = maps
        if permissions is not None:
            self.permissions = permissions
        if settings is not None:
            self.settings = settings
        if data_tables is not None:
            self.data_tables = data_tables
        if data_columns is not None:
            self.data_columns = data_columns
        if grid_layers is not None:
            self.grid_layers = grid_layers

    @property
    def layer(self):
        """Gets the layer of this LayerWithDetails.  # noqa: E501


        :return: The layer of this LayerWithDetails.  # noqa: E501
        :rtype: Layer
        """
        return self._layer

    @layer.setter
    def layer(self, layer):
        """Sets the layer of this LayerWithDetails.


        :param layer: The layer of this LayerWithDetails.  # noqa: E501
        :type: Layer
        """

        self._layer = layer

    @property
    def maps(self):
        """Gets the maps of this LayerWithDetails.  # noqa: E501


        :return: The maps of this LayerWithDetails.  # noqa: E501
        :rtype: list[Map]
        """
        return self._maps

    @maps.setter
    def maps(self, maps):
        """Sets the maps of this LayerWithDetails.


        :param maps: The maps of this LayerWithDetails.  # noqa: E501
        :type: list[Map]
        """

        self._maps = maps

    @property
    def permissions(self):
        """Gets the permissions of this LayerWithDetails.  # noqa: E501


        :return: The permissions of this LayerWithDetails.  # noqa: E501
        :rtype: list[PermissionPairComplexDTO]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this LayerWithDetails.


        :param permissions: The permissions of this LayerWithDetails.  # noqa: E501
        :type: list[PermissionPairComplexDTO]
        """

        self._permissions = permissions

    @property
    def settings(self):
        """Gets the settings of this LayerWithDetails.  # noqa: E501


        :return: The settings of this LayerWithDetails.  # noqa: E501
        :rtype: LayerSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this LayerWithDetails.


        :param settings: The settings of this LayerWithDetails.  # noqa: E501
        :type: LayerSettings
        """

        self._settings = settings

    @property
    def data_tables(self):
        """Gets the data_tables of this LayerWithDetails.  # noqa: E501


        :return: The data_tables of this LayerWithDetails.  # noqa: E501
        :rtype: list[LayerDataTable]
        """
        return self._data_tables

    @data_tables.setter
    def data_tables(self, data_tables):
        """Sets the data_tables of this LayerWithDetails.


        :param data_tables: The data_tables of this LayerWithDetails.  # noqa: E501
        :type: list[LayerDataTable]
        """

        self._data_tables = data_tables

    @property
    def data_columns(self):
        """Gets the data_columns of this LayerWithDetails.  # noqa: E501


        :return: The data_columns of this LayerWithDetails.  # noqa: E501
        :rtype: list[DataColumn]
        """
        return self._data_columns

    @data_columns.setter
    def data_columns(self, data_columns):
        """Sets the data_columns of this LayerWithDetails.


        :param data_columns: The data_columns of this LayerWithDetails.  # noqa: E501
        :type: list[DataColumn]
        """

        self._data_columns = data_columns

    @property
    def grid_layers(self):
        """Gets the grid_layers of this LayerWithDetails.  # noqa: E501


        :return: The grid_layers of this LayerWithDetails.  # noqa: E501
        :rtype: list[GridLayer]
        """
        return self._grid_layers

    @grid_layers.setter
    def grid_layers(self, grid_layers):
        """Sets the grid_layers of this LayerWithDetails.


        :param grid_layers: The grid_layers of this LayerWithDetails.  # noqa: E501
        :type: list[GridLayer]
        """

        self._grid_layers = grid_layers

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
        if issubclass(LayerWithDetails, dict):
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
        if not isinstance(other, LayerWithDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other