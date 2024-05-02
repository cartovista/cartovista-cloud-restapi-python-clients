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

class InfoToolSettings(object):
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
        'as_panel': 'bool',
        'display_coordinates': 'bool',
        'type': 'CoordinatesType'
    }

    attribute_map = {
        'as_panel': 'asPanel',
        'display_coordinates': 'displayCoordinates',
        'type': 'type'
    }

    def __init__(self, as_panel=None, display_coordinates=None, type=None):  # noqa: E501
        """InfoToolSettings - a model defined in Swagger"""  # noqa: E501
        self._as_panel = None
        self._display_coordinates = None
        self._type = None
        self.discriminator = None
        if as_panel is not None:
            self.as_panel = as_panel
        if display_coordinates is not None:
            self.display_coordinates = display_coordinates
        if type is not None:
            self.type = type

    @property
    def as_panel(self):
        """Gets the as_panel of this InfoToolSettings.  # noqa: E501


        :return: The as_panel of this InfoToolSettings.  # noqa: E501
        :rtype: bool
        """
        return self._as_panel

    @as_panel.setter
    def as_panel(self, as_panel):
        """Sets the as_panel of this InfoToolSettings.


        :param as_panel: The as_panel of this InfoToolSettings.  # noqa: E501
        :type: bool
        """

        self._as_panel = as_panel

    @property
    def display_coordinates(self):
        """Gets the display_coordinates of this InfoToolSettings.  # noqa: E501


        :return: The display_coordinates of this InfoToolSettings.  # noqa: E501
        :rtype: bool
        """
        return self._display_coordinates

    @display_coordinates.setter
    def display_coordinates(self, display_coordinates):
        """Sets the display_coordinates of this InfoToolSettings.


        :param display_coordinates: The display_coordinates of this InfoToolSettings.  # noqa: E501
        :type: bool
        """

        self._display_coordinates = display_coordinates

    @property
    def type(self):
        """Gets the type of this InfoToolSettings.  # noqa: E501


        :return: The type of this InfoToolSettings.  # noqa: E501
        :rtype: CoordinatesType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InfoToolSettings.


        :param type: The type of this InfoToolSettings.  # noqa: E501
        :type: CoordinatesType
        """

        self._type = type

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
        if issubclass(InfoToolSettings, dict):
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
        if not isinstance(other, InfoToolSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other