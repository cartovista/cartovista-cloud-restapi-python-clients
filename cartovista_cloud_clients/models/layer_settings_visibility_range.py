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

class LayerSettingsVisibilityRange(object):
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
        'is_zoom_layered': 'bool',
        'is_max_infinity': 'bool',
        'min': 'int',
        'max': 'int'
    }

    attribute_map = {
        'is_zoom_layered': 'isZoomLayered',
        'is_max_infinity': 'isMaxInfinity',
        'min': 'min',
        'max': 'max'
    }

    def __init__(self, is_zoom_layered=None, is_max_infinity=None, min=None, max=None):  # noqa: E501
        """LayerSettingsVisibilityRange - a model defined in Swagger"""  # noqa: E501
        self._is_zoom_layered = None
        self._is_max_infinity = None
        self._min = None
        self._max = None
        self.discriminator = None
        if is_zoom_layered is not None:
            self.is_zoom_layered = is_zoom_layered
        if is_max_infinity is not None:
            self.is_max_infinity = is_max_infinity
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

    @property
    def is_zoom_layered(self):
        """Gets the is_zoom_layered of this LayerSettingsVisibilityRange.  # noqa: E501


        :return: The is_zoom_layered of this LayerSettingsVisibilityRange.  # noqa: E501
        :rtype: bool
        """
        return self._is_zoom_layered

    @is_zoom_layered.setter
    def is_zoom_layered(self, is_zoom_layered):
        """Sets the is_zoom_layered of this LayerSettingsVisibilityRange.


        :param is_zoom_layered: The is_zoom_layered of this LayerSettingsVisibilityRange.  # noqa: E501
        :type: bool
        """

        self._is_zoom_layered = is_zoom_layered

    @property
    def is_max_infinity(self):
        """Gets the is_max_infinity of this LayerSettingsVisibilityRange.  # noqa: E501


        :return: The is_max_infinity of this LayerSettingsVisibilityRange.  # noqa: E501
        :rtype: bool
        """
        return self._is_max_infinity

    @is_max_infinity.setter
    def is_max_infinity(self, is_max_infinity):
        """Sets the is_max_infinity of this LayerSettingsVisibilityRange.


        :param is_max_infinity: The is_max_infinity of this LayerSettingsVisibilityRange.  # noqa: E501
        :type: bool
        """

        self._is_max_infinity = is_max_infinity

    @property
    def min(self):
        """Gets the min of this LayerSettingsVisibilityRange.  # noqa: E501


        :return: The min of this LayerSettingsVisibilityRange.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this LayerSettingsVisibilityRange.


        :param min: The min of this LayerSettingsVisibilityRange.  # noqa: E501
        :type: int
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this LayerSettingsVisibilityRange.  # noqa: E501


        :return: The max of this LayerSettingsVisibilityRange.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this LayerSettingsVisibilityRange.


        :param max: The max of this LayerSettingsVisibilityRange.  # noqa: E501
        :type: int
        """

        self._max = max

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
        if issubclass(LayerSettingsVisibilityRange, dict):
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
        if not isinstance(other, LayerSettingsVisibilityRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
