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

class MapSettings(object):
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
        'distance_unit': 'str',
        'area_unit': 'str',
        'zoom_on_map_load': 'bool'
    }

    attribute_map = {
        'distance_unit': 'distanceUnit',
        'area_unit': 'areaUnit',
        'zoom_on_map_load': 'zoomOnMapLoad'
    }

    def __init__(self, distance_unit=None, area_unit=None, zoom_on_map_load=None):  # noqa: E501
        """MapSettings - a model defined in Swagger"""  # noqa: E501
        self._distance_unit = None
        self._area_unit = None
        self._zoom_on_map_load = None
        self.discriminator = None
        if distance_unit is not None:
            self.distance_unit = distance_unit
        if area_unit is not None:
            self.area_unit = area_unit
        if zoom_on_map_load is not None:
            self.zoom_on_map_load = zoom_on_map_load

    @property
    def distance_unit(self):
        """Gets the distance_unit of this MapSettings.  # noqa: E501


        :return: The distance_unit of this MapSettings.  # noqa: E501
        :rtype: str
        """
        return self._distance_unit

    @distance_unit.setter
    def distance_unit(self, distance_unit):
        """Sets the distance_unit of this MapSettings.


        :param distance_unit: The distance_unit of this MapSettings.  # noqa: E501
        :type: str
        """

        self._distance_unit = distance_unit

    @property
    def area_unit(self):
        """Gets the area_unit of this MapSettings.  # noqa: E501


        :return: The area_unit of this MapSettings.  # noqa: E501
        :rtype: str
        """
        return self._area_unit

    @area_unit.setter
    def area_unit(self, area_unit):
        """Sets the area_unit of this MapSettings.


        :param area_unit: The area_unit of this MapSettings.  # noqa: E501
        :type: str
        """

        self._area_unit = area_unit

    @property
    def zoom_on_map_load(self):
        """Gets the zoom_on_map_load of this MapSettings.  # noqa: E501


        :return: The zoom_on_map_load of this MapSettings.  # noqa: E501
        :rtype: bool
        """
        return self._zoom_on_map_load

    @zoom_on_map_load.setter
    def zoom_on_map_load(self, zoom_on_map_load):
        """Sets the zoom_on_map_load of this MapSettings.


        :param zoom_on_map_load: The zoom_on_map_load of this MapSettings.  # noqa: E501
        :type: bool
        """

        self._zoom_on_map_load = zoom_on_map_load

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
        if issubclass(MapSettings, dict):
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
        if not isinstance(other, MapSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
