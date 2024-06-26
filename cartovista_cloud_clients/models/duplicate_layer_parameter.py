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

class DuplicateLayerParameter(object):
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
        'name': 'str',
        'identifier': 'str',
        'data_column_filters': 'list[DataColumnFilters]'
    }

    attribute_map = {
        'name': 'name',
        'identifier': 'identifier',
        'data_column_filters': 'dataColumnFilters'
    }

    def __init__(self, name=None, identifier=None, data_column_filters=None):  # noqa: E501
        """DuplicateLayerParameter - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._identifier = None
        self._data_column_filters = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if identifier is not None:
            self.identifier = identifier
        if data_column_filters is not None:
            self.data_column_filters = data_column_filters

    @property
    def name(self):
        """Gets the name of this DuplicateLayerParameter.  # noqa: E501


        :return: The name of this DuplicateLayerParameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DuplicateLayerParameter.


        :param name: The name of this DuplicateLayerParameter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def identifier(self):
        """Gets the identifier of this DuplicateLayerParameter.  # noqa: E501


        :return: The identifier of this DuplicateLayerParameter.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this DuplicateLayerParameter.


        :param identifier: The identifier of this DuplicateLayerParameter.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def data_column_filters(self):
        """Gets the data_column_filters of this DuplicateLayerParameter.  # noqa: E501


        :return: The data_column_filters of this DuplicateLayerParameter.  # noqa: E501
        :rtype: list[DataColumnFilters]
        """
        return self._data_column_filters

    @data_column_filters.setter
    def data_column_filters(self, data_column_filters):
        """Sets the data_column_filters of this DuplicateLayerParameter.


        :param data_column_filters: The data_column_filters of this DuplicateLayerParameter.  # noqa: E501
        :type: list[DataColumnFilters]
        """

        self._data_column_filters = data_column_filters

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
        if issubclass(DuplicateLayerParameter, dict):
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
        if not isinstance(other, DuplicateLayerParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
