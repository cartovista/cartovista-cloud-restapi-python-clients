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

class GeocodedLocation(object):
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
        'longitude': 'float',
        'latitude': 'float',
        'address': 'str',
        'bounding_box': 'BoundingBox',
        'accuracy': 'GeocodingAccuracy',
        'query_score': 'float'
    }

    attribute_map = {
        'longitude': 'longitude',
        'latitude': 'latitude',
        'address': 'address',
        'bounding_box': 'boundingBox',
        'accuracy': 'accuracy',
        'query_score': 'queryScore'
    }

    def __init__(self, longitude=None, latitude=None, address=None, bounding_box=None, accuracy=None, query_score=None):  # noqa: E501
        """GeocodedLocation - a model defined in Swagger"""  # noqa: E501
        self._longitude = None
        self._latitude = None
        self._address = None
        self._bounding_box = None
        self._accuracy = None
        self._query_score = None
        self.discriminator = None
        if longitude is not None:
            self.longitude = longitude
        if latitude is not None:
            self.latitude = latitude
        if address is not None:
            self.address = address
        if bounding_box is not None:
            self.bounding_box = bounding_box
        if accuracy is not None:
            self.accuracy = accuracy
        if query_score is not None:
            self.query_score = query_score

    @property
    def longitude(self):
        """Gets the longitude of this GeocodedLocation.  # noqa: E501


        :return: The longitude of this GeocodedLocation.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this GeocodedLocation.


        :param longitude: The longitude of this GeocodedLocation.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this GeocodedLocation.  # noqa: E501


        :return: The latitude of this GeocodedLocation.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this GeocodedLocation.


        :param latitude: The latitude of this GeocodedLocation.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def address(self):
        """Gets the address of this GeocodedLocation.  # noqa: E501


        :return: The address of this GeocodedLocation.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this GeocodedLocation.


        :param address: The address of this GeocodedLocation.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def bounding_box(self):
        """Gets the bounding_box of this GeocodedLocation.  # noqa: E501


        :return: The bounding_box of this GeocodedLocation.  # noqa: E501
        :rtype: BoundingBox
        """
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, bounding_box):
        """Sets the bounding_box of this GeocodedLocation.


        :param bounding_box: The bounding_box of this GeocodedLocation.  # noqa: E501
        :type: BoundingBox
        """

        self._bounding_box = bounding_box

    @property
    def accuracy(self):
        """Gets the accuracy of this GeocodedLocation.  # noqa: E501


        :return: The accuracy of this GeocodedLocation.  # noqa: E501
        :rtype: GeocodingAccuracy
        """
        return self._accuracy

    @accuracy.setter
    def accuracy(self, accuracy):
        """Sets the accuracy of this GeocodedLocation.


        :param accuracy: The accuracy of this GeocodedLocation.  # noqa: E501
        :type: GeocodingAccuracy
        """

        self._accuracy = accuracy

    @property
    def query_score(self):
        """Gets the query_score of this GeocodedLocation.  # noqa: E501


        :return: The query_score of this GeocodedLocation.  # noqa: E501
        :rtype: float
        """
        return self._query_score

    @query_score.setter
    def query_score(self, query_score):
        """Sets the query_score of this GeocodedLocation.


        :param query_score: The query_score of this GeocodedLocation.  # noqa: E501
        :type: float
        """

        self._query_score = query_score

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
        if issubclass(GeocodedLocation, dict):
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
        if not isinstance(other, GeocodedLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
