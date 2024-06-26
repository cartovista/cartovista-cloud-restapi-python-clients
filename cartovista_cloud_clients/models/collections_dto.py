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

class CollectionsDto(object):
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
        'links': 'list[LinkDto]',
        'collections': 'list[FeatureDto]'
    }

    attribute_map = {
        'links': 'links',
        'collections': 'collections'
    }

    def __init__(self, links=None, collections=None):  # noqa: E501
        """CollectionsDto - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._collections = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if collections is not None:
            self.collections = collections

    @property
    def links(self):
        """Gets the links of this CollectionsDto.  # noqa: E501


        :return: The links of this CollectionsDto.  # noqa: E501
        :rtype: list[LinkDto]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CollectionsDto.


        :param links: The links of this CollectionsDto.  # noqa: E501
        :type: list[LinkDto]
        """

        self._links = links

    @property
    def collections(self):
        """Gets the collections of this CollectionsDto.  # noqa: E501


        :return: The collections of this CollectionsDto.  # noqa: E501
        :rtype: list[FeatureDto]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this CollectionsDto.


        :param collections: The collections of this CollectionsDto.  # noqa: E501
        :type: list[FeatureDto]
        """

        self._collections = collections

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
        if issubclass(CollectionsDto, dict):
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
        if not isinstance(other, CollectionsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
