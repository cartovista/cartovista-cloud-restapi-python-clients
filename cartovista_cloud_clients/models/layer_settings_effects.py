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

class LayerSettingsEffects(object):
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
        'drop_shadow': 'OneOfLayerSettingsEffectsDropShadow',
        'inner_glow': 'OneOfLayerSettingsEffectsInnerGlow',
        'outer_glow': 'OneOfLayerSettingsEffectsOuterGlow'
    }

    attribute_map = {
        'drop_shadow': 'dropShadow',
        'inner_glow': 'innerGlow',
        'outer_glow': 'outerGlow'
    }

    def __init__(self, drop_shadow=None, inner_glow=None, outer_glow=None):  # noqa: E501
        """LayerSettingsEffects - a model defined in Swagger"""  # noqa: E501
        self._drop_shadow = None
        self._inner_glow = None
        self._outer_glow = None
        self.discriminator = None
        if drop_shadow is not None:
            self.drop_shadow = drop_shadow
        if inner_glow is not None:
            self.inner_glow = inner_glow
        if outer_glow is not None:
            self.outer_glow = outer_glow

    @property
    def drop_shadow(self):
        """Gets the drop_shadow of this LayerSettingsEffects.  # noqa: E501


        :return: The drop_shadow of this LayerSettingsEffects.  # noqa: E501
        :rtype: OneOfLayerSettingsEffectsDropShadow
        """
        return self._drop_shadow

    @drop_shadow.setter
    def drop_shadow(self, drop_shadow):
        """Sets the drop_shadow of this LayerSettingsEffects.


        :param drop_shadow: The drop_shadow of this LayerSettingsEffects.  # noqa: E501
        :type: OneOfLayerSettingsEffectsDropShadow
        """

        self._drop_shadow = drop_shadow

    @property
    def inner_glow(self):
        """Gets the inner_glow of this LayerSettingsEffects.  # noqa: E501


        :return: The inner_glow of this LayerSettingsEffects.  # noqa: E501
        :rtype: OneOfLayerSettingsEffectsInnerGlow
        """
        return self._inner_glow

    @inner_glow.setter
    def inner_glow(self, inner_glow):
        """Sets the inner_glow of this LayerSettingsEffects.


        :param inner_glow: The inner_glow of this LayerSettingsEffects.  # noqa: E501
        :type: OneOfLayerSettingsEffectsInnerGlow
        """

        self._inner_glow = inner_glow

    @property
    def outer_glow(self):
        """Gets the outer_glow of this LayerSettingsEffects.  # noqa: E501


        :return: The outer_glow of this LayerSettingsEffects.  # noqa: E501
        :rtype: OneOfLayerSettingsEffectsOuterGlow
        """
        return self._outer_glow

    @outer_glow.setter
    def outer_glow(self, outer_glow):
        """Sets the outer_glow of this LayerSettingsEffects.


        :param outer_glow: The outer_glow of this LayerSettingsEffects.  # noqa: E501
        :type: OneOfLayerSettingsEffectsOuterGlow
        """

        self._outer_glow = outer_glow

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
        if issubclass(LayerSettingsEffects, dict):
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
        if not isinstance(other, LayerSettingsEffects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other