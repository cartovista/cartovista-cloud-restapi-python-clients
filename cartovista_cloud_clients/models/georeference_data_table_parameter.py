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

class GeoreferenceDataTableParameter(object):
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
        'latitude_column_id': 'str',
        'longitude_column_id': 'str'
    }

    attribute_map = {
        'latitude_column_id': 'latitudeColumnId',
        'longitude_column_id': 'longitudeColumnId'
    }

    def __init__(self, latitude_column_id=None, longitude_column_id=None):  # noqa: E501
        """GeoreferenceDataTableParameter - a model defined in Swagger"""  # noqa: E501
        self._latitude_column_id = None
        self._longitude_column_id = None
        self.discriminator = None
        if latitude_column_id is not None:
            self.latitude_column_id = latitude_column_id
        if longitude_column_id is not None:
            self.longitude_column_id = longitude_column_id

    @property
    def latitude_column_id(self):
        """Gets the latitude_column_id of this GeoreferenceDataTableParameter.  # noqa: E501


        :return: The latitude_column_id of this GeoreferenceDataTableParameter.  # noqa: E501
        :rtype: str
        """
        return self._latitude_column_id

    @latitude_column_id.setter
    def latitude_column_id(self, latitude_column_id):
        """Sets the latitude_column_id of this GeoreferenceDataTableParameter.


        :param latitude_column_id: The latitude_column_id of this GeoreferenceDataTableParameter.  # noqa: E501
        :type: str
        """

        self._latitude_column_id = latitude_column_id

    @property
    def longitude_column_id(self):
        """Gets the longitude_column_id of this GeoreferenceDataTableParameter.  # noqa: E501


        :return: The longitude_column_id of this GeoreferenceDataTableParameter.  # noqa: E501
        :rtype: str
        """
        return self._longitude_column_id

    @longitude_column_id.setter
    def longitude_column_id(self, longitude_column_id):
        """Sets the longitude_column_id of this GeoreferenceDataTableParameter.


        :param longitude_column_id: The longitude_column_id of this GeoreferenceDataTableParameter.  # noqa: E501
        :type: str
        """

        self._longitude_column_id = longitude_column_id

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
        if issubclass(GeoreferenceDataTableParameter, dict):
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
        if not isinstance(other, GeoreferenceDataTableParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other