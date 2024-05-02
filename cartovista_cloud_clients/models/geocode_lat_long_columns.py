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

class GeocodeLatLongColumns(object):
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
        'lat_column_number': 'int',
        'long_column_number': 'int'
    }

    attribute_map = {
        'lat_column_number': 'latColumnNumber',
        'long_column_number': 'longColumnNumber'
    }

    def __init__(self, lat_column_number=None, long_column_number=None):  # noqa: E501
        """GeocodeLatLongColumns - a model defined in Swagger"""  # noqa: E501
        self._lat_column_number = None
        self._long_column_number = None
        self.discriminator = None
        if lat_column_number is not None:
            self.lat_column_number = lat_column_number
        if long_column_number is not None:
            self.long_column_number = long_column_number

    @property
    def lat_column_number(self):
        """Gets the lat_column_number of this GeocodeLatLongColumns.  # noqa: E501


        :return: The lat_column_number of this GeocodeLatLongColumns.  # noqa: E501
        :rtype: int
        """
        return self._lat_column_number

    @lat_column_number.setter
    def lat_column_number(self, lat_column_number):
        """Sets the lat_column_number of this GeocodeLatLongColumns.


        :param lat_column_number: The lat_column_number of this GeocodeLatLongColumns.  # noqa: E501
        :type: int
        """

        self._lat_column_number = lat_column_number

    @property
    def long_column_number(self):
        """Gets the long_column_number of this GeocodeLatLongColumns.  # noqa: E501


        :return: The long_column_number of this GeocodeLatLongColumns.  # noqa: E501
        :rtype: int
        """
        return self._long_column_number

    @long_column_number.setter
    def long_column_number(self, long_column_number):
        """Sets the long_column_number of this GeocodeLatLongColumns.


        :param long_column_number: The long_column_number of this GeocodeLatLongColumns.  # noqa: E501
        :type: int
        """

        self._long_column_number = long_column_number

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
        if issubclass(GeocodeLatLongColumns, dict):
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
        if not isinstance(other, GeocodeLatLongColumns):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
