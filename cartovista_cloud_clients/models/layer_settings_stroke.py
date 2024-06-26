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

class LayerSettingsStroke(object):
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
        'color': 'str',
        'width': 'int',
        'pattern': 'str'
    }

    attribute_map = {
        'color': 'color',
        'width': 'width',
        'pattern': 'pattern'
    }

    def __init__(self, color=None, width=None, pattern=None):  # noqa: E501
        """LayerSettingsStroke - a model defined in Swagger"""  # noqa: E501
        self._color = None
        self._width = None
        self._pattern = None
        self.discriminator = None
        if color is not None:
            self.color = color
        if width is not None:
            self.width = width
        if pattern is not None:
            self.pattern = pattern

    @property
    def color(self):
        """Gets the color of this LayerSettingsStroke.  # noqa: E501


        :return: The color of this LayerSettingsStroke.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this LayerSettingsStroke.


        :param color: The color of this LayerSettingsStroke.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def width(self):
        """Gets the width of this LayerSettingsStroke.  # noqa: E501


        :return: The width of this LayerSettingsStroke.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this LayerSettingsStroke.


        :param width: The width of this LayerSettingsStroke.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def pattern(self):
        """Gets the pattern of this LayerSettingsStroke.  # noqa: E501


        :return: The pattern of this LayerSettingsStroke.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this LayerSettingsStroke.


        :param pattern: The pattern of this LayerSettingsStroke.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

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
        if issubclass(LayerSettingsStroke, dict):
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
        if not isinstance(other, LayerSettingsStroke):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
