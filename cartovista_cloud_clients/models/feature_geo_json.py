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

class FeatureGeoJSON(object):
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
        'geometry_type': 'str',
        'identifier': 'str',
        'values': 'list[object]',
        'data_columns_identifiers': 'list[str]',
        'data_columns_system_identifiers': 'list[str]',
        'geo_json': 'str'
    }

    attribute_map = {
        'geometry_type': 'geometryType',
        'identifier': 'identifier',
        'values': 'values',
        'data_columns_identifiers': 'dataColumnsIdentifiers',
        'data_columns_system_identifiers': 'dataColumnsSystemIdentifiers',
        'geo_json': 'geoJSON'
    }

    def __init__(self, geometry_type=None, identifier=None, values=None, data_columns_identifiers=None, data_columns_system_identifiers=None, geo_json=None):  # noqa: E501
        """FeatureGeoJSON - a model defined in Swagger"""  # noqa: E501
        self._geometry_type = None
        self._identifier = None
        self._values = None
        self._data_columns_identifiers = None
        self._data_columns_system_identifiers = None
        self._geo_json = None
        self.discriminator = None
        if geometry_type is not None:
            self.geometry_type = geometry_type
        if identifier is not None:
            self.identifier = identifier
        if values is not None:
            self.values = values
        if data_columns_identifiers is not None:
            self.data_columns_identifiers = data_columns_identifiers
        if data_columns_system_identifiers is not None:
            self.data_columns_system_identifiers = data_columns_system_identifiers
        if geo_json is not None:
            self.geo_json = geo_json

    @property
    def geometry_type(self):
        """Gets the geometry_type of this FeatureGeoJSON.  # noqa: E501


        :return: The geometry_type of this FeatureGeoJSON.  # noqa: E501
        :rtype: str
        """
        return self._geometry_type

    @geometry_type.setter
    def geometry_type(self, geometry_type):
        """Sets the geometry_type of this FeatureGeoJSON.


        :param geometry_type: The geometry_type of this FeatureGeoJSON.  # noqa: E501
        :type: str
        """

        self._geometry_type = geometry_type

    @property
    def identifier(self):
        """Gets the identifier of this FeatureGeoJSON.  # noqa: E501


        :return: The identifier of this FeatureGeoJSON.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this FeatureGeoJSON.


        :param identifier: The identifier of this FeatureGeoJSON.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def values(self):
        """Gets the values of this FeatureGeoJSON.  # noqa: E501


        :return: The values of this FeatureGeoJSON.  # noqa: E501
        :rtype: list[object]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this FeatureGeoJSON.


        :param values: The values of this FeatureGeoJSON.  # noqa: E501
        :type: list[object]
        """

        self._values = values

    @property
    def data_columns_identifiers(self):
        """Gets the data_columns_identifiers of this FeatureGeoJSON.  # noqa: E501


        :return: The data_columns_identifiers of this FeatureGeoJSON.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_columns_identifiers

    @data_columns_identifiers.setter
    def data_columns_identifiers(self, data_columns_identifiers):
        """Sets the data_columns_identifiers of this FeatureGeoJSON.


        :param data_columns_identifiers: The data_columns_identifiers of this FeatureGeoJSON.  # noqa: E501
        :type: list[str]
        """

        self._data_columns_identifiers = data_columns_identifiers

    @property
    def data_columns_system_identifiers(self):
        """Gets the data_columns_system_identifiers of this FeatureGeoJSON.  # noqa: E501


        :return: The data_columns_system_identifiers of this FeatureGeoJSON.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_columns_system_identifiers

    @data_columns_system_identifiers.setter
    def data_columns_system_identifiers(self, data_columns_system_identifiers):
        """Sets the data_columns_system_identifiers of this FeatureGeoJSON.


        :param data_columns_system_identifiers: The data_columns_system_identifiers of this FeatureGeoJSON.  # noqa: E501
        :type: list[str]
        """

        self._data_columns_system_identifiers = data_columns_system_identifiers

    @property
    def geo_json(self):
        """Gets the geo_json of this FeatureGeoJSON.  # noqa: E501


        :return: The geo_json of this FeatureGeoJSON.  # noqa: E501
        :rtype: str
        """
        return self._geo_json

    @geo_json.setter
    def geo_json(self, geo_json):
        """Sets the geo_json of this FeatureGeoJSON.


        :param geo_json: The geo_json of this FeatureGeoJSON.  # noqa: E501
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
        if issubclass(FeatureGeoJSON, dict):
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
        if not isinstance(other, FeatureGeoJSON):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
