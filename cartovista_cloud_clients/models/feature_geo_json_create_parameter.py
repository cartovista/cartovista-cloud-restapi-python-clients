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

class FeatureGeoJSONCreateParameter(object):
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
        'data_columns_identifiers': 'list[str]',
        'values': 'list[object]',
        'proj4': 'str',
        'feature_type': 'FeatureType',
        'geo_json': 'str'
    }

    attribute_map = {
        'data_columns_identifiers': 'dataColumnsIdentifiers',
        'values': 'values',
        'proj4': 'proj4',
        'feature_type': 'featureType',
        'geo_json': 'geoJSON'
    }

    def __init__(self, data_columns_identifiers=None, values=None, proj4=None, feature_type=None, geo_json=None):  # noqa: E501
        """FeatureGeoJSONCreateParameter - a model defined in Swagger"""  # noqa: E501
        self._data_columns_identifiers = None
        self._values = None
        self._proj4 = None
        self._feature_type = None
        self._geo_json = None
        self.discriminator = None
        if data_columns_identifiers is not None:
            self.data_columns_identifiers = data_columns_identifiers
        if values is not None:
            self.values = values
        if proj4 is not None:
            self.proj4 = proj4
        if feature_type is not None:
            self.feature_type = feature_type
        if geo_json is not None:
            self.geo_json = geo_json

    @property
    def data_columns_identifiers(self):
        """Gets the data_columns_identifiers of this FeatureGeoJSONCreateParameter.  # noqa: E501


        :return: The data_columns_identifiers of this FeatureGeoJSONCreateParameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_columns_identifiers

    @data_columns_identifiers.setter
    def data_columns_identifiers(self, data_columns_identifiers):
        """Sets the data_columns_identifiers of this FeatureGeoJSONCreateParameter.


        :param data_columns_identifiers: The data_columns_identifiers of this FeatureGeoJSONCreateParameter.  # noqa: E501
        :type: list[str]
        """

        self._data_columns_identifiers = data_columns_identifiers

    @property
    def values(self):
        """Gets the values of this FeatureGeoJSONCreateParameter.  # noqa: E501


        :return: The values of this FeatureGeoJSONCreateParameter.  # noqa: E501
        :rtype: list[object]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this FeatureGeoJSONCreateParameter.


        :param values: The values of this FeatureGeoJSONCreateParameter.  # noqa: E501
        :type: list[object]
        """

        self._values = values

    @property
    def proj4(self):
        """Gets the proj4 of this FeatureGeoJSONCreateParameter.  # noqa: E501


        :return: The proj4 of this FeatureGeoJSONCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._proj4

    @proj4.setter
    def proj4(self, proj4):
        """Sets the proj4 of this FeatureGeoJSONCreateParameter.


        :param proj4: The proj4 of this FeatureGeoJSONCreateParameter.  # noqa: E501
        :type: str
        """

        self._proj4 = proj4

    @property
    def feature_type(self):
        """Gets the feature_type of this FeatureGeoJSONCreateParameter.  # noqa: E501


        :return: The feature_type of this FeatureGeoJSONCreateParameter.  # noqa: E501
        :rtype: FeatureType
        """
        return self._feature_type

    @feature_type.setter
    def feature_type(self, feature_type):
        """Sets the feature_type of this FeatureGeoJSONCreateParameter.


        :param feature_type: The feature_type of this FeatureGeoJSONCreateParameter.  # noqa: E501
        :type: FeatureType
        """

        self._feature_type = feature_type

    @property
    def geo_json(self):
        """Gets the geo_json of this FeatureGeoJSONCreateParameter.  # noqa: E501


        :return: The geo_json of this FeatureGeoJSONCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._geo_json

    @geo_json.setter
    def geo_json(self, geo_json):
        """Sets the geo_json of this FeatureGeoJSONCreateParameter.


        :param geo_json: The geo_json of this FeatureGeoJSONCreateParameter.  # noqa: E501
        :type: str
        """

        self._geo_json = geo_json

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
        if issubclass(FeatureGeoJSONCreateParameter, dict):
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
        if not isinstance(other, FeatureGeoJSONCreateParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
