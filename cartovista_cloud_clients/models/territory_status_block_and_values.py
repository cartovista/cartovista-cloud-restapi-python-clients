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

class TerritoryStatusBlockAndValues(object):
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
        'deleted_blocks': 'list[BlockTerritoryDTO]',
        'updated_values': 'list[TerritoryValuesDTO]'
    }

    attribute_map = {
        'deleted_blocks': 'deletedBlocks',
        'updated_values': 'updatedValues'
    }

    def __init__(self, deleted_blocks=None, updated_values=None):  # noqa: E501
        """TerritoryStatusBlockAndValues - a model defined in Swagger"""  # noqa: E501
        self._deleted_blocks = None
        self._updated_values = None
        self.discriminator = None
        if deleted_blocks is not None:
            self.deleted_blocks = deleted_blocks
        if updated_values is not None:
            self.updated_values = updated_values

    @property
    def deleted_blocks(self):
        """Gets the deleted_blocks of this TerritoryStatusBlockAndValues.  # noqa: E501


        :return: The deleted_blocks of this TerritoryStatusBlockAndValues.  # noqa: E501
        :rtype: list[BlockTerritoryDTO]
        """
        return self._deleted_blocks

    @deleted_blocks.setter
    def deleted_blocks(self, deleted_blocks):
        """Sets the deleted_blocks of this TerritoryStatusBlockAndValues.


        :param deleted_blocks: The deleted_blocks of this TerritoryStatusBlockAndValues.  # noqa: E501
        :type: list[BlockTerritoryDTO]
        """

        self._deleted_blocks = deleted_blocks

    @property
    def updated_values(self):
        """Gets the updated_values of this TerritoryStatusBlockAndValues.  # noqa: E501


        :return: The updated_values of this TerritoryStatusBlockAndValues.  # noqa: E501
        :rtype: list[TerritoryValuesDTO]
        """
        return self._updated_values

    @updated_values.setter
    def updated_values(self, updated_values):
        """Sets the updated_values of this TerritoryStatusBlockAndValues.


        :param updated_values: The updated_values of this TerritoryStatusBlockAndValues.  # noqa: E501
        :type: list[TerritoryValuesDTO]
        """

        self._updated_values = updated_values

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
        if issubclass(TerritoryStatusBlockAndValues, dict):
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
        if not isinstance(other, TerritoryStatusBlockAndValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other