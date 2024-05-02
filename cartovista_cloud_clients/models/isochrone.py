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

class Isochrone(object):
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
        'range': 'str',
        'range_type': 'str',
        'mode': 'str',
        'departure_time': 'str',
        'isoline_coordinates': 'list[float]'
    }

    attribute_map = {
        'longitude': 'longitude',
        'latitude': 'latitude',
        'range': 'range',
        'range_type': 'rangeType',
        'mode': 'mode',
        'departure_time': 'departureTime',
        'isoline_coordinates': 'isolineCoordinates'
    }

    def __init__(self, longitude=None, latitude=None, range=None, range_type=None, mode=None, departure_time=None, isoline_coordinates=None):  # noqa: E501
        """Isochrone - a model defined in Swagger"""  # noqa: E501
        self._longitude = None
        self._latitude = None
        self._range = None
        self._range_type = None
        self._mode = None
        self._departure_time = None
        self._isoline_coordinates = None
        self.discriminator = None
        if longitude is not None:
            self.longitude = longitude
        if latitude is not None:
            self.latitude = latitude
        if range is not None:
            self.range = range
        if range_type is not None:
            self.range_type = range_type
        if mode is not None:
            self.mode = mode
        if departure_time is not None:
            self.departure_time = departure_time
        if isoline_coordinates is not None:
            self.isoline_coordinates = isoline_coordinates

    @property
    def longitude(self):
        """Gets the longitude of this Isochrone.  # noqa: E501


        :return: The longitude of this Isochrone.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Isochrone.


        :param longitude: The longitude of this Isochrone.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this Isochrone.  # noqa: E501


        :return: The latitude of this Isochrone.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Isochrone.


        :param latitude: The latitude of this Isochrone.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def range(self):
        """Gets the range of this Isochrone.  # noqa: E501


        :return: The range of this Isochrone.  # noqa: E501
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this Isochrone.


        :param range: The range of this Isochrone.  # noqa: E501
        :type: str
        """

        self._range = range

    @property
    def range_type(self):
        """Gets the range_type of this Isochrone.  # noqa: E501


        :return: The range_type of this Isochrone.  # noqa: E501
        :rtype: str
        """
        return self._range_type

    @range_type.setter
    def range_type(self, range_type):
        """Sets the range_type of this Isochrone.


        :param range_type: The range_type of this Isochrone.  # noqa: E501
        :type: str
        """

        self._range_type = range_type

    @property
    def mode(self):
        """Gets the mode of this Isochrone.  # noqa: E501


        :return: The mode of this Isochrone.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Isochrone.


        :param mode: The mode of this Isochrone.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def departure_time(self):
        """Gets the departure_time of this Isochrone.  # noqa: E501


        :return: The departure_time of this Isochrone.  # noqa: E501
        :rtype: str
        """
        return self._departure_time

    @departure_time.setter
    def departure_time(self, departure_time):
        """Sets the departure_time of this Isochrone.


        :param departure_time: The departure_time of this Isochrone.  # noqa: E501
        :type: str
        """

        self._departure_time = departure_time

    @property
    def isoline_coordinates(self):
        """Gets the isoline_coordinates of this Isochrone.  # noqa: E501


        :return: The isoline_coordinates of this Isochrone.  # noqa: E501
        :rtype: list[float]
        """
        return self._isoline_coordinates

    @isoline_coordinates.setter
    def isoline_coordinates(self, isoline_coordinates):
        """Sets the isoline_coordinates of this Isochrone.


        :param isoline_coordinates: The isoline_coordinates of this Isochrone.  # noqa: E501
        :type: list[float]
        """

        self._isoline_coordinates = isoline_coordinates

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
        if issubclass(Isochrone, dict):
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
        if not isinstance(other, Isochrone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
