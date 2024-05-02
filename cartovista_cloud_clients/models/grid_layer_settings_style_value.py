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

class GridLayerSettingsStyleValue(object):
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
        'label': 'str',
        'value': 'float',
        'min_value': 'float',
        'max_value': 'float'
    }

    attribute_map = {
        'color': 'color',
        'label': 'label',
        'value': 'value',
        'min_value': 'minValue',
        'max_value': 'maxValue'
    }

    def __init__(self, color=None, label=None, value=None, min_value=None, max_value=None):  # noqa: E501
        """GridLayerSettingsStyleValue - a model defined in Swagger"""  # noqa: E501
        self._color = None
        self._label = None
        self._value = None
        self._min_value = None
        self._max_value = None
        self.discriminator = None
        if color is not None:
            self.color = color
        if label is not None:
            self.label = label
        if value is not None:
            self.value = value
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value

    @property
    def color(self):
        """Gets the color of this GridLayerSettingsStyleValue.  # noqa: E501


        :return: The color of this GridLayerSettingsStyleValue.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this GridLayerSettingsStyleValue.


        :param color: The color of this GridLayerSettingsStyleValue.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def label(self):
        """Gets the label of this GridLayerSettingsStyleValue.  # noqa: E501


        :return: The label of this GridLayerSettingsStyleValue.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this GridLayerSettingsStyleValue.


        :param label: The label of this GridLayerSettingsStyleValue.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def value(self):
        """Gets the value of this GridLayerSettingsStyleValue.  # noqa: E501


        :return: The value of this GridLayerSettingsStyleValue.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GridLayerSettingsStyleValue.


        :param value: The value of this GridLayerSettingsStyleValue.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def min_value(self):
        """Gets the min_value of this GridLayerSettingsStyleValue.  # noqa: E501


        :return: The min_value of this GridLayerSettingsStyleValue.  # noqa: E501
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this GridLayerSettingsStyleValue.


        :param min_value: The min_value of this GridLayerSettingsStyleValue.  # noqa: E501
        :type: float
        """

        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this GridLayerSettingsStyleValue.  # noqa: E501


        :return: The max_value of this GridLayerSettingsStyleValue.  # noqa: E501
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this GridLayerSettingsStyleValue.


        :param max_value: The max_value of this GridLayerSettingsStyleValue.  # noqa: E501
        :type: float
        """

        self._max_value = max_value

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
        if issubclass(GridLayerSettingsStyleValue, dict):
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
        if not isinstance(other, GridLayerSettingsStyleValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other