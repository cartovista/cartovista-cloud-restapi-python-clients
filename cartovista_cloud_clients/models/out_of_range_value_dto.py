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

class OutOfRangeValueDTO(object):
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
        'min_value': 'float',
        'max_value': 'float',
        'count': 'int'
    }

    attribute_map = {
        'min_value': 'minValue',
        'max_value': 'maxValue',
        'count': 'count'
    }

    def __init__(self, min_value=None, max_value=None, count=None):  # noqa: E501
        """OutOfRangeValueDTO - a model defined in Swagger"""  # noqa: E501
        self._min_value = None
        self._max_value = None
        self._count = None
        self.discriminator = None
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value
        if count is not None:
            self.count = count

    @property
    def min_value(self):
        """Gets the min_value of this OutOfRangeValueDTO.  # noqa: E501


        :return: The min_value of this OutOfRangeValueDTO.  # noqa: E501
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this OutOfRangeValueDTO.


        :param min_value: The min_value of this OutOfRangeValueDTO.  # noqa: E501
        :type: float
        """

        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this OutOfRangeValueDTO.  # noqa: E501


        :return: The max_value of this OutOfRangeValueDTO.  # noqa: E501
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this OutOfRangeValueDTO.


        :param max_value: The max_value of this OutOfRangeValueDTO.  # noqa: E501
        :type: float
        """

        self._max_value = max_value

    @property
    def count(self):
        """Gets the count of this OutOfRangeValueDTO.  # noqa: E501


        :return: The count of this OutOfRangeValueDTO.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this OutOfRangeValueDTO.


        :param count: The count of this OutOfRangeValueDTO.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if issubclass(OutOfRangeValueDTO, dict):
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
        if not isinstance(other, OutOfRangeValueDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
