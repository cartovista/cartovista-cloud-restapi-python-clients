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

class AttributeDataQueryResultDTO(object):
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
        'total': 'int',
        'linking_ids': 'list[str]',
        'values': 'list[AttributeDataValues]',
        'statistics_values': 'list[AttributeDataStatistics]'
    }

    attribute_map = {
        'total': 'total',
        'linking_ids': 'linkingIds',
        'values': 'values',
        'statistics_values': 'statisticsValues'
    }

    def __init__(self, total=None, linking_ids=None, values=None, statistics_values=None):  # noqa: E501
        """AttributeDataQueryResultDTO - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._linking_ids = None
        self._values = None
        self._statistics_values = None
        self.discriminator = None
        if total is not None:
            self.total = total
        if linking_ids is not None:
            self.linking_ids = linking_ids
        if values is not None:
            self.values = values
        if statistics_values is not None:
            self.statistics_values = statistics_values

    @property
    def total(self):
        """Gets the total of this AttributeDataQueryResultDTO.  # noqa: E501


        :return: The total of this AttributeDataQueryResultDTO.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this AttributeDataQueryResultDTO.


        :param total: The total of this AttributeDataQueryResultDTO.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def linking_ids(self):
        """Gets the linking_ids of this AttributeDataQueryResultDTO.  # noqa: E501


        :return: The linking_ids of this AttributeDataQueryResultDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._linking_ids

    @linking_ids.setter
    def linking_ids(self, linking_ids):
        """Sets the linking_ids of this AttributeDataQueryResultDTO.


        :param linking_ids: The linking_ids of this AttributeDataQueryResultDTO.  # noqa: E501
        :type: list[str]
        """

        self._linking_ids = linking_ids

    @property
    def values(self):
        """Gets the values of this AttributeDataQueryResultDTO.  # noqa: E501


        :return: The values of this AttributeDataQueryResultDTO.  # noqa: E501
        :rtype: list[AttributeDataValues]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this AttributeDataQueryResultDTO.


        :param values: The values of this AttributeDataQueryResultDTO.  # noqa: E501
        :type: list[AttributeDataValues]
        """

        self._values = values

    @property
    def statistics_values(self):
        """Gets the statistics_values of this AttributeDataQueryResultDTO.  # noqa: E501


        :return: The statistics_values of this AttributeDataQueryResultDTO.  # noqa: E501
        :rtype: list[AttributeDataStatistics]
        """
        return self._statistics_values

    @statistics_values.setter
    def statistics_values(self, statistics_values):
        """Sets the statistics_values of this AttributeDataQueryResultDTO.


        :param statistics_values: The statistics_values of this AttributeDataQueryResultDTO.  # noqa: E501
        :type: list[AttributeDataStatistics]
        """

        self._statistics_values = statistics_values

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
        if issubclass(AttributeDataQueryResultDTO, dict):
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
        if not isinstance(other, AttributeDataQueryResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
