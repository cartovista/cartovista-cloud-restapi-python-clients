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

class TerritoryAnalyzedDistanceDatatable(object):
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
        'layer_id': 'str',
        'data_table_id': 'str',
        'column_and_value': 'list[TerritoryAnalyzedDistanceDataColumnAndValue]'
    }

    attribute_map = {
        'name': 'name',
        'layer_id': 'layerId',
        'data_table_id': 'dataTableId',
        'column_and_value': 'columnAndValue'
    }

    def __init__(self, name=None, layer_id=None, data_table_id=None, column_and_value=None):  # noqa: E501
        """TerritoryAnalyzedDistanceDatatable - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._layer_id = None
        self._data_table_id = None
        self._column_and_value = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if layer_id is not None:
            self.layer_id = layer_id
        if data_table_id is not None:
            self.data_table_id = data_table_id
        if column_and_value is not None:
            self.column_and_value = column_and_value

    @property
    def name(self):
        """Gets the name of this TerritoryAnalyzedDistanceDatatable.  # noqa: E501


        :return: The name of this TerritoryAnalyzedDistanceDatatable.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TerritoryAnalyzedDistanceDatatable.


        :param name: The name of this TerritoryAnalyzedDistanceDatatable.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def layer_id(self):
        """Gets the layer_id of this TerritoryAnalyzedDistanceDatatable.  # noqa: E501


        :return: The layer_id of this TerritoryAnalyzedDistanceDatatable.  # noqa: E501
        :rtype: str
        """
        return self._layer_id

    @layer_id.setter
    def layer_id(self, layer_id):
        """Sets the layer_id of this TerritoryAnalyzedDistanceDatatable.


        :param layer_id: The layer_id of this TerritoryAnalyzedDistanceDatatable.  # noqa: E501
        :type: str
        """

        self._layer_id = layer_id

    @property
    def data_table_id(self):
        """Gets the data_table_id of this TerritoryAnalyzedDistanceDatatable.  # noqa: E501


        :return: The data_table_id of this TerritoryAnalyzedDistanceDatatable.  # noqa: E501
        :rtype: str
        """
        return self._data_table_id

    @data_table_id.setter
    def data_table_id(self, data_table_id):
        """Sets the data_table_id of this TerritoryAnalyzedDistanceDatatable.


        :param data_table_id: The data_table_id of this TerritoryAnalyzedDistanceDatatable.  # noqa: E501
        :type: str
        """

        self._data_table_id = data_table_id

    @property
    def column_and_value(self):
        """Gets the column_and_value of this TerritoryAnalyzedDistanceDatatable.  # noqa: E501


        :return: The column_and_value of this TerritoryAnalyzedDistanceDatatable.  # noqa: E501
        :rtype: list[TerritoryAnalyzedDistanceDataColumnAndValue]
        """
        return self._column_and_value

    @column_and_value.setter
    def column_and_value(self, column_and_value):
        """Sets the column_and_value of this TerritoryAnalyzedDistanceDatatable.


        :param column_and_value: The column_and_value of this TerritoryAnalyzedDistanceDatatable.  # noqa: E501
        :type: list[TerritoryAnalyzedDistanceDataColumnAndValue]
        """

        self._column_and_value = column_and_value

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
        if issubclass(TerritoryAnalyzedDistanceDatatable, dict):
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
        if not isinstance(other, TerritoryAnalyzedDistanceDatatable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
