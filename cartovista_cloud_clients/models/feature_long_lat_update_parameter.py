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

class FeatureLongLatUpdateParameter(object):
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
        'proj4': 'str',
        'feature_type': 'FeatureType',
        'longitude': 'float',
        'latitude': 'float'
    }

    attribute_map = {
        'proj4': 'proj4',
        'feature_type': 'featureType',
        'longitude': 'longitude',
        'latitude': 'latitude'
    }

    def __init__(self, proj4=None, feature_type=None, longitude=None, latitude=None):  # noqa: E501
        """FeatureLongLatUpdateParameter - a model defined in Swagger"""  # noqa: E501
        self._proj4 = None
        self._feature_type = None
        self._longitude = None
        self._latitude = None
        self.discriminator = None
        if proj4 is not None:
            self.proj4 = proj4
        if feature_type is not None:
            self.feature_type = feature_type
        if longitude is not None:
            self.longitude = longitude
        if latitude is not None:
            self.latitude = latitude

    @property
    def proj4(self):
        """Gets the proj4 of this FeatureLongLatUpdateParameter.  # noqa: E501


        :return: The proj4 of this FeatureLongLatUpdateParameter.  # noqa: E501
        :rtype: str
        """
        return self._proj4

    @proj4.setter
    def proj4(self, proj4):
        """Sets the proj4 of this FeatureLongLatUpdateParameter.


        :param proj4: The proj4 of this FeatureLongLatUpdateParameter.  # noqa: E501
        :type: str
        """

        self._proj4 = proj4

    @property
    def feature_type(self):
        """Gets the feature_type of this FeatureLongLatUpdateParameter.  # noqa: E501


        :return: The feature_type of this FeatureLongLatUpdateParameter.  # noqa: E501
        :rtype: FeatureType
        """
        return self._feature_type

    @feature_type.setter
    def feature_type(self, feature_type):
        """Sets the feature_type of this FeatureLongLatUpdateParameter.


        :param feature_type: The feature_type of this FeatureLongLatUpdateParameter.  # noqa: E501
        :type: FeatureType
        """

        self._feature_type = feature_type

    @property
    def longitude(self):
        """Gets the longitude of this FeatureLongLatUpdateParameter.  # noqa: E501


        :return: The longitude of this FeatureLongLatUpdateParameter.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this FeatureLongLatUpdateParameter.


        :param longitude: The longitude of this FeatureLongLatUpdateParameter.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this FeatureLongLatUpdateParameter.  # noqa: E501


        :return: The latitude of this FeatureLongLatUpdateParameter.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this FeatureLongLatUpdateParameter.


        :param latitude: The latitude of this FeatureLongLatUpdateParameter.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

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
        if issubclass(FeatureLongLatUpdateParameter, dict):
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
        if not isinstance(other, FeatureLongLatUpdateParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
