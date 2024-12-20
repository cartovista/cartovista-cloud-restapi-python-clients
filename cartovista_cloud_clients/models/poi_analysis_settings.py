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

class PoiAnalysisSettings(object):
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
        'layers': 'list[PoiLayer]',
        'tables': 'dict(str, list[PoiTable])',
        'footprint_layers': 'list[PoiLayer]',
        'transmission_lines_layers': 'list[PoiLayer]',
        'transmission_points_layers': 'list[PoiLayer]'
    }

    attribute_map = {
        'layers': 'layers',
        'tables': 'tables',
        'footprint_layers': 'footprintLayers',
        'transmission_lines_layers': 'transmissionLinesLayers',
        'transmission_points_layers': 'transmissionPointsLayers'
    }

    def __init__(self, layers=None, tables=None, footprint_layers=None, transmission_lines_layers=None, transmission_points_layers=None):  # noqa: E501
        """PoiAnalysisSettings - a model defined in Swagger"""  # noqa: E501
        self._layers = None
        self._tables = None
        self._footprint_layers = None
        self._transmission_lines_layers = None
        self._transmission_points_layers = None
        self.discriminator = None
        if layers is not None:
            self.layers = layers
        if tables is not None:
            self.tables = tables
        if footprint_layers is not None:
            self.footprint_layers = footprint_layers
        if transmission_lines_layers is not None:
            self.transmission_lines_layers = transmission_lines_layers
        if transmission_points_layers is not None:
            self.transmission_points_layers = transmission_points_layers

    @property
    def layers(self):
        """Gets the layers of this PoiAnalysisSettings.  # noqa: E501


        :return: The layers of this PoiAnalysisSettings.  # noqa: E501
        :rtype: list[PoiLayer]
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """Sets the layers of this PoiAnalysisSettings.


        :param layers: The layers of this PoiAnalysisSettings.  # noqa: E501
        :type: list[PoiLayer]
        """

        self._layers = layers

    @property
    def tables(self):
        """Gets the tables of this PoiAnalysisSettings.  # noqa: E501


        :return: The tables of this PoiAnalysisSettings.  # noqa: E501
        :rtype: dict(str, list[PoiTable])
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this PoiAnalysisSettings.


        :param tables: The tables of this PoiAnalysisSettings.  # noqa: E501
        :type: dict(str, list[PoiTable])
        """

        self._tables = tables

    @property
    def footprint_layers(self):
        """Gets the footprint_layers of this PoiAnalysisSettings.  # noqa: E501


        :return: The footprint_layers of this PoiAnalysisSettings.  # noqa: E501
        :rtype: list[PoiLayer]
        """
        return self._footprint_layers

    @footprint_layers.setter
    def footprint_layers(self, footprint_layers):
        """Sets the footprint_layers of this PoiAnalysisSettings.


        :param footprint_layers: The footprint_layers of this PoiAnalysisSettings.  # noqa: E501
        :type: list[PoiLayer]
        """

        self._footprint_layers = footprint_layers

    @property
    def transmission_lines_layers(self):
        """Gets the transmission_lines_layers of this PoiAnalysisSettings.  # noqa: E501


        :return: The transmission_lines_layers of this PoiAnalysisSettings.  # noqa: E501
        :rtype: list[PoiLayer]
        """
        return self._transmission_lines_layers

    @transmission_lines_layers.setter
    def transmission_lines_layers(self, transmission_lines_layers):
        """Sets the transmission_lines_layers of this PoiAnalysisSettings.


        :param transmission_lines_layers: The transmission_lines_layers of this PoiAnalysisSettings.  # noqa: E501
        :type: list[PoiLayer]
        """

        self._transmission_lines_layers = transmission_lines_layers

    @property
    def transmission_points_layers(self):
        """Gets the transmission_points_layers of this PoiAnalysisSettings.  # noqa: E501


        :return: The transmission_points_layers of this PoiAnalysisSettings.  # noqa: E501
        :rtype: list[PoiLayer]
        """
        return self._transmission_points_layers

    @transmission_points_layers.setter
    def transmission_points_layers(self, transmission_points_layers):
        """Sets the transmission_points_layers of this PoiAnalysisSettings.


        :param transmission_points_layers: The transmission_points_layers of this PoiAnalysisSettings.  # noqa: E501
        :type: list[PoiLayer]
        """

        self._transmission_points_layers = transmission_points_layers

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
        if issubclass(PoiAnalysisSettings, dict):
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
        if not isinstance(other, PoiAnalysisSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
