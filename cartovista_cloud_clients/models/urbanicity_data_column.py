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

class UrbanicityDataColumn(object):
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
        'id': 'str',
        'data_table_id': 'str',
        'number_of_null_values': 'int',
        'number_of_unique_values': 'int'
    }

    attribute_map = {
        'id': 'id',
        'data_table_id': 'dataTableId',
        'number_of_null_values': 'numberOfNullValues',
        'number_of_unique_values': 'numberOfUniqueValues'
    }

    def __init__(self, id=None, data_table_id=None, number_of_null_values=None, number_of_unique_values=None):  # noqa: E501
        """UrbanicityDataColumn - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._data_table_id = None
        self._number_of_null_values = None
        self._number_of_unique_values = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if data_table_id is not None:
            self.data_table_id = data_table_id
        if number_of_null_values is not None:
            self.number_of_null_values = number_of_null_values
        if number_of_unique_values is not None:
            self.number_of_unique_values = number_of_unique_values

    @property
    def id(self):
        """Gets the id of this UrbanicityDataColumn.  # noqa: E501


        :return: The id of this UrbanicityDataColumn.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UrbanicityDataColumn.


        :param id: The id of this UrbanicityDataColumn.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def data_table_id(self):
        """Gets the data_table_id of this UrbanicityDataColumn.  # noqa: E501


        :return: The data_table_id of this UrbanicityDataColumn.  # noqa: E501
        :rtype: str
        """
        return self._data_table_id

    @data_table_id.setter
    def data_table_id(self, data_table_id):
        """Sets the data_table_id of this UrbanicityDataColumn.


        :param data_table_id: The data_table_id of this UrbanicityDataColumn.  # noqa: E501
        :type: str
        """

        self._data_table_id = data_table_id

    @property
    def number_of_null_values(self):
        """Gets the number_of_null_values of this UrbanicityDataColumn.  # noqa: E501


        :return: The number_of_null_values of this UrbanicityDataColumn.  # noqa: E501
        :rtype: int
        """
        return self._number_of_null_values

    @number_of_null_values.setter
    def number_of_null_values(self, number_of_null_values):
        """Sets the number_of_null_values of this UrbanicityDataColumn.


        :param number_of_null_values: The number_of_null_values of this UrbanicityDataColumn.  # noqa: E501
        :type: int
        """

        self._number_of_null_values = number_of_null_values

    @property
    def number_of_unique_values(self):
        """Gets the number_of_unique_values of this UrbanicityDataColumn.  # noqa: E501


        :return: The number_of_unique_values of this UrbanicityDataColumn.  # noqa: E501
        :rtype: int
        """
        return self._number_of_unique_values

    @number_of_unique_values.setter
    def number_of_unique_values(self, number_of_unique_values):
        """Sets the number_of_unique_values of this UrbanicityDataColumn.


        :param number_of_unique_values: The number_of_unique_values of this UrbanicityDataColumn.  # noqa: E501
        :type: int
        """

        self._number_of_unique_values = number_of_unique_values

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
        if issubclass(UrbanicityDataColumn, dict):
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
        if not isinstance(other, UrbanicityDataColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
