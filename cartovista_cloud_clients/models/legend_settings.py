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

class LegendSettings(object):
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
        'show_not_available': 'bool',
        'show_out_of_range': 'bool',
        'show_feature_count': 'bool',
        'show_layer_visibility_control': 'bool'
    }

    attribute_map = {
        'show_not_available': 'showNotAvailable',
        'show_out_of_range': 'showOutOfRange',
        'show_feature_count': 'showFeatureCount',
        'show_layer_visibility_control': 'showLayerVisibilityControl'
    }

    def __init__(self, show_not_available=None, show_out_of_range=None, show_feature_count=None, show_layer_visibility_control=None):  # noqa: E501
        """LegendSettings - a model defined in Swagger"""  # noqa: E501
        self._show_not_available = None
        self._show_out_of_range = None
        self._show_feature_count = None
        self._show_layer_visibility_control = None
        self.discriminator = None
        if show_not_available is not None:
            self.show_not_available = show_not_available
        if show_out_of_range is not None:
            self.show_out_of_range = show_out_of_range
        if show_feature_count is not None:
            self.show_feature_count = show_feature_count
        if show_layer_visibility_control is not None:
            self.show_layer_visibility_control = show_layer_visibility_control

    @property
    def show_not_available(self):
        """Gets the show_not_available of this LegendSettings.  # noqa: E501


        :return: The show_not_available of this LegendSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_not_available

    @show_not_available.setter
    def show_not_available(self, show_not_available):
        """Sets the show_not_available of this LegendSettings.


        :param show_not_available: The show_not_available of this LegendSettings.  # noqa: E501
        :type: bool
        """

        self._show_not_available = show_not_available

    @property
    def show_out_of_range(self):
        """Gets the show_out_of_range of this LegendSettings.  # noqa: E501


        :return: The show_out_of_range of this LegendSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_out_of_range

    @show_out_of_range.setter
    def show_out_of_range(self, show_out_of_range):
        """Sets the show_out_of_range of this LegendSettings.


        :param show_out_of_range: The show_out_of_range of this LegendSettings.  # noqa: E501
        :type: bool
        """

        self._show_out_of_range = show_out_of_range

    @property
    def show_feature_count(self):
        """Gets the show_feature_count of this LegendSettings.  # noqa: E501


        :return: The show_feature_count of this LegendSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_feature_count

    @show_feature_count.setter
    def show_feature_count(self, show_feature_count):
        """Sets the show_feature_count of this LegendSettings.


        :param show_feature_count: The show_feature_count of this LegendSettings.  # noqa: E501
        :type: bool
        """

        self._show_feature_count = show_feature_count

    @property
    def show_layer_visibility_control(self):
        """Gets the show_layer_visibility_control of this LegendSettings.  # noqa: E501


        :return: The show_layer_visibility_control of this LegendSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_layer_visibility_control

    @show_layer_visibility_control.setter
    def show_layer_visibility_control(self, show_layer_visibility_control):
        """Sets the show_layer_visibility_control of this LegendSettings.


        :param show_layer_visibility_control: The show_layer_visibility_control of this LegendSettings.  # noqa: E501
        :type: bool
        """

        self._show_layer_visibility_control = show_layer_visibility_control

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
        if issubclass(LegendSettings, dict):
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
        if not isinstance(other, LegendSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
