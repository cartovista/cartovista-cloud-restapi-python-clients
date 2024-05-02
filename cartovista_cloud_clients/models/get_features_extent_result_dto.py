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

class GetFeaturesExtentResultDTO(object):
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
        'feature_ids': 'list[str]',
        'extents': 'list[ExtentDto]'
    }

    attribute_map = {
        'feature_ids': 'featureIds',
        'extents': 'extents'
    }

    def __init__(self, feature_ids=None, extents=None):  # noqa: E501
        """GetFeaturesExtentResultDTO - a model defined in Swagger"""  # noqa: E501
        self._feature_ids = None
        self._extents = None
        self.discriminator = None
        if feature_ids is not None:
            self.feature_ids = feature_ids
        if extents is not None:
            self.extents = extents

    @property
    def feature_ids(self):
        """Gets the feature_ids of this GetFeaturesExtentResultDTO.  # noqa: E501


        :return: The feature_ids of this GetFeaturesExtentResultDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._feature_ids

    @feature_ids.setter
    def feature_ids(self, feature_ids):
        """Sets the feature_ids of this GetFeaturesExtentResultDTO.


        :param feature_ids: The feature_ids of this GetFeaturesExtentResultDTO.  # noqa: E501
        :type: list[str]
        """

        self._feature_ids = feature_ids

    @property
    def extents(self):
        """Gets the extents of this GetFeaturesExtentResultDTO.  # noqa: E501


        :return: The extents of this GetFeaturesExtentResultDTO.  # noqa: E501
        :rtype: list[ExtentDto]
        """
        return self._extents

    @extents.setter
    def extents(self, extents):
        """Sets the extents of this GetFeaturesExtentResultDTO.


        :param extents: The extents of this GetFeaturesExtentResultDTO.  # noqa: E501
        :type: list[ExtentDto]
        """

        self._extents = extents

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
        if issubclass(GetFeaturesExtentResultDTO, dict):
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
        if not isinstance(other, GetFeaturesExtentResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
