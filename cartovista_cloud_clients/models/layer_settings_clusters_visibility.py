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

class LayerSettingsClustersVisibility(object):
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
        'min': 'int'
    }

    attribute_map = {
        'is_zoom_layered': 'isZoomLayered',
        'min': 'min'
    }

    def __init__(self, is_zoom_layered=None, min=None):  # noqa: E501
        """LayerSettingsClustersVisibility - a model defined in Swagger"""  # noqa: E501
        self._is_zoom_layered = None
        self._min = None
        self.discriminator = None
        if is_zoom_layered is not None:
            self.is_zoom_layered = is_zoom_layered
        if min is not None:
            self.min = min

    @property
    def is_zoom_layered(self):
        """Gets the is_zoom_layered of this LayerSettingsClustersVisibility.  # noqa: E501


        :return: The is_zoom_layered of this LayerSettingsClustersVisibility.  # noqa: E501
        :rtype: bool
        """
        return self._is_zoom_layered

    @is_zoom_layered.setter
    def is_zoom_layered(self, is_zoom_layered):
        """Sets the is_zoom_layered of this LayerSettingsClustersVisibility.


        :param is_zoom_layered: The is_zoom_layered of this LayerSettingsClustersVisibility.  # noqa: E501
        :type: bool
        """

        self._is_zoom_layered = is_zoom_layered

    @property
    def min(self):
        """Gets the min of this LayerSettingsClustersVisibility.  # noqa: E501


        :return: The min of this LayerSettingsClustersVisibility.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this LayerSettingsClustersVisibility.


        :param min: The min of this LayerSettingsClustersVisibility.  # noqa: E501
        :type: int
        """

        self._min = min

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
        if issubclass(LayerSettingsClustersVisibility, dict):
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
        if not isinstance(other, LayerSettingsClustersVisibility):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
