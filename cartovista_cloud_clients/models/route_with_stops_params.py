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

class RouteWithStopsParams(object):
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
        'origin_latitude': 'float',
        'origin_longitude': 'float',
        'destination_latitude': 'float',
        'destination_longitude': 'float',
        'mode': 'str',
        'departure': 'str',
        'traffic': 'bool',
        'viewer_readable_coordinates': 'bool',
        'stops': 'list[Coordinate]'
    }

    attribute_map = {
        'origin_latitude': 'originLatitude',
        'origin_longitude': 'originLongitude',
        'destination_latitude': 'destinationLatitude',
        'destination_longitude': 'destinationLongitude',
        'mode': 'mode',
        'departure': 'departure',
        'traffic': 'traffic',
        'viewer_readable_coordinates': 'viewerReadableCoordinates',
        'stops': 'stops'
    }

    def __init__(self, origin_latitude=None, origin_longitude=None, destination_latitude=None, destination_longitude=None, mode=None, departure=None, traffic=None, viewer_readable_coordinates=None, stops=None):  # noqa: E501
        """RouteWithStopsParams - a model defined in Swagger"""  # noqa: E501
        self._origin_latitude = None
        self._origin_longitude = None
        self._destination_latitude = None
        self._destination_longitude = None
        self._mode = None
        self._departure = None
        self._traffic = None
        self._viewer_readable_coordinates = None
        self._stops = None
        self.discriminator = None
        if origin_latitude is not None:
            self.origin_latitude = origin_latitude
        if origin_longitude is not None:
            self.origin_longitude = origin_longitude
        if destination_latitude is not None:
            self.destination_latitude = destination_latitude
        if destination_longitude is not None:
            self.destination_longitude = destination_longitude
        if mode is not None:
            self.mode = mode
        if departure is not None:
            self.departure = departure
        if traffic is not None:
            self.traffic = traffic
        if viewer_readable_coordinates is not None:
            self.viewer_readable_coordinates = viewer_readable_coordinates
        if stops is not None:
            self.stops = stops

    @property
    def origin_latitude(self):
        """Gets the origin_latitude of this RouteWithStopsParams.  # noqa: E501


        :return: The origin_latitude of this RouteWithStopsParams.  # noqa: E501
        :rtype: float
        """
        return self._origin_latitude

    @origin_latitude.setter
    def origin_latitude(self, origin_latitude):
        """Sets the origin_latitude of this RouteWithStopsParams.


        :param origin_latitude: The origin_latitude of this RouteWithStopsParams.  # noqa: E501
        :type: float
        """

        self._origin_latitude = origin_latitude

    @property
    def origin_longitude(self):
        """Gets the origin_longitude of this RouteWithStopsParams.  # noqa: E501


        :return: The origin_longitude of this RouteWithStopsParams.  # noqa: E501
        :rtype: float
        """
        return self._origin_longitude

    @origin_longitude.setter
    def origin_longitude(self, origin_longitude):
        """Sets the origin_longitude of this RouteWithStopsParams.


        :param origin_longitude: The origin_longitude of this RouteWithStopsParams.  # noqa: E501
        :type: float
        """

        self._origin_longitude = origin_longitude

    @property
    def destination_latitude(self):
        """Gets the destination_latitude of this RouteWithStopsParams.  # noqa: E501


        :return: The destination_latitude of this RouteWithStopsParams.  # noqa: E501
        :rtype: float
        """
        return self._destination_latitude

    @destination_latitude.setter
    def destination_latitude(self, destination_latitude):
        """Sets the destination_latitude of this RouteWithStopsParams.


        :param destination_latitude: The destination_latitude of this RouteWithStopsParams.  # noqa: E501
        :type: float
        """

        self._destination_latitude = destination_latitude

    @property
    def destination_longitude(self):
        """Gets the destination_longitude of this RouteWithStopsParams.  # noqa: E501


        :return: The destination_longitude of this RouteWithStopsParams.  # noqa: E501
        :rtype: float
        """
        return self._destination_longitude

    @destination_longitude.setter
    def destination_longitude(self, destination_longitude):
        """Sets the destination_longitude of this RouteWithStopsParams.


        :param destination_longitude: The destination_longitude of this RouteWithStopsParams.  # noqa: E501
        :type: float
        """

        self._destination_longitude = destination_longitude

    @property
    def mode(self):
        """Gets the mode of this RouteWithStopsParams.  # noqa: E501


        :return: The mode of this RouteWithStopsParams.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this RouteWithStopsParams.


        :param mode: The mode of this RouteWithStopsParams.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def departure(self):
        """Gets the departure of this RouteWithStopsParams.  # noqa: E501


        :return: The departure of this RouteWithStopsParams.  # noqa: E501
        :rtype: str
        """
        return self._departure

    @departure.setter
    def departure(self, departure):
        """Sets the departure of this RouteWithStopsParams.


        :param departure: The departure of this RouteWithStopsParams.  # noqa: E501
        :type: str
        """

        self._departure = departure

    @property
    def traffic(self):
        """Gets the traffic of this RouteWithStopsParams.  # noqa: E501


        :return: The traffic of this RouteWithStopsParams.  # noqa: E501
        :rtype: bool
        """
        return self._traffic

    @traffic.setter
    def traffic(self, traffic):
        """Sets the traffic of this RouteWithStopsParams.


        :param traffic: The traffic of this RouteWithStopsParams.  # noqa: E501
        :type: bool
        """

        self._traffic = traffic

    @property
    def viewer_readable_coordinates(self):
        """Gets the viewer_readable_coordinates of this RouteWithStopsParams.  # noqa: E501


        :return: The viewer_readable_coordinates of this RouteWithStopsParams.  # noqa: E501
        :rtype: bool
        """
        return self._viewer_readable_coordinates

    @viewer_readable_coordinates.setter
    def viewer_readable_coordinates(self, viewer_readable_coordinates):
        """Sets the viewer_readable_coordinates of this RouteWithStopsParams.


        :param viewer_readable_coordinates: The viewer_readable_coordinates of this RouteWithStopsParams.  # noqa: E501
        :type: bool
        """

        self._viewer_readable_coordinates = viewer_readable_coordinates

    @property
    def stops(self):
        """Gets the stops of this RouteWithStopsParams.  # noqa: E501


        :return: The stops of this RouteWithStopsParams.  # noqa: E501
        :rtype: list[Coordinate]
        """
        return self._stops

    @stops.setter
    def stops(self, stops):
        """Sets the stops of this RouteWithStopsParams.


        :param stops: The stops of this RouteWithStopsParams.  # noqa: E501
        :type: list[Coordinate]
        """

        self._stops = stops

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
        if issubclass(RouteWithStopsParams, dict):
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
        if not isinstance(other, RouteWithStopsParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
