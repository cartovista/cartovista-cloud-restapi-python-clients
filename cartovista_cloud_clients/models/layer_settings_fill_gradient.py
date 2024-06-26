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

class LayerSettingsFillGradient(object):
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
        'gradient_color': 'str',
        'is_linear': 'bool'
    }

    attribute_map = {
        'color': 'color',
        'gradient_color': 'gradientColor',
        'is_linear': 'isLinear'
    }

    def __init__(self, color=None, gradient_color=None, is_linear=None):  # noqa: E501
        """LayerSettingsFillGradient - a model defined in Swagger"""  # noqa: E501
        self._color = None
        self._gradient_color = None
        self._is_linear = None
        self.discriminator = None
        if color is not None:
            self.color = color
        if gradient_color is not None:
            self.gradient_color = gradient_color
        if is_linear is not None:
            self.is_linear = is_linear

    @property
    def color(self):
        """Gets the color of this LayerSettingsFillGradient.  # noqa: E501


        :return: The color of this LayerSettingsFillGradient.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this LayerSettingsFillGradient.


        :param color: The color of this LayerSettingsFillGradient.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def gradient_color(self):
        """Gets the gradient_color of this LayerSettingsFillGradient.  # noqa: E501


        :return: The gradient_color of this LayerSettingsFillGradient.  # noqa: E501
        :rtype: str
        """
        return self._gradient_color

    @gradient_color.setter
    def gradient_color(self, gradient_color):
        """Sets the gradient_color of this LayerSettingsFillGradient.


        :param gradient_color: The gradient_color of this LayerSettingsFillGradient.  # noqa: E501
        :type: str
        """

        self._gradient_color = gradient_color

    @property
    def is_linear(self):
        """Gets the is_linear of this LayerSettingsFillGradient.  # noqa: E501


        :return: The is_linear of this LayerSettingsFillGradient.  # noqa: E501
        :rtype: bool
        """
        return self._is_linear

    @is_linear.setter
    def is_linear(self, is_linear):
        """Sets the is_linear of this LayerSettingsFillGradient.


        :param is_linear: The is_linear of this LayerSettingsFillGradient.  # noqa: E501
        :type: bool
        """

        self._is_linear = is_linear

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
        if issubclass(LayerSettingsFillGradient, dict):
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
        if not isinstance(other, LayerSettingsFillGradient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
