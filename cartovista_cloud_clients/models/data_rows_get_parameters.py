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

class DataRowsGetParameters(object):
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
        'start_at': 'int',
        'row_count': 'int',
        'data_filters': 'list[DataColumnFilters]',
        'data_sort': 'OneOfDataRowsGetParametersDataSort'
    }

    attribute_map = {
        'start_at': 'startAt',
        'row_count': 'rowCount',
        'data_filters': 'dataFilters',
        'data_sort': 'dataSort'
    }

    def __init__(self, start_at=None, row_count=None, data_filters=None, data_sort=None):  # noqa: E501
        """DataRowsGetParameters - a model defined in Swagger"""  # noqa: E501
        self._start_at = None
        self._row_count = None
        self._data_filters = None
        self._data_sort = None
        self.discriminator = None
        if start_at is not None:
            self.start_at = start_at
        if row_count is not None:
            self.row_count = row_count
        if data_filters is not None:
            self.data_filters = data_filters
        if data_sort is not None:
            self.data_sort = data_sort

    @property
    def start_at(self):
        """Gets the start_at of this DataRowsGetParameters.  # noqa: E501


        :return: The start_at of this DataRowsGetParameters.  # noqa: E501
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this DataRowsGetParameters.


        :param start_at: The start_at of this DataRowsGetParameters.  # noqa: E501
        :type: int
        """

        self._start_at = start_at

    @property
    def row_count(self):
        """Gets the row_count of this DataRowsGetParameters.  # noqa: E501


        :return: The row_count of this DataRowsGetParameters.  # noqa: E501
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this DataRowsGetParameters.


        :param row_count: The row_count of this DataRowsGetParameters.  # noqa: E501
        :type: int
        """

        self._row_count = row_count

    @property
    def data_filters(self):
        """Gets the data_filters of this DataRowsGetParameters.  # noqa: E501


        :return: The data_filters of this DataRowsGetParameters.  # noqa: E501
        :rtype: list[DataColumnFilters]
        """
        return self._data_filters

    @data_filters.setter
    def data_filters(self, data_filters):
        """Sets the data_filters of this DataRowsGetParameters.


        :param data_filters: The data_filters of this DataRowsGetParameters.  # noqa: E501
        :type: list[DataColumnFilters]
        """

        self._data_filters = data_filters

    @property
    def data_sort(self):
        """Gets the data_sort of this DataRowsGetParameters.  # noqa: E501


        :return: The data_sort of this DataRowsGetParameters.  # noqa: E501
        :rtype: OneOfDataRowsGetParametersDataSort
        """
        return self._data_sort

    @data_sort.setter
    def data_sort(self, data_sort):
        """Sets the data_sort of this DataRowsGetParameters.


        :param data_sort: The data_sort of this DataRowsGetParameters.  # noqa: E501
        :type: OneOfDataRowsGetParametersDataSort
        """

        self._data_sort = data_sort

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
        if issubclass(DataRowsGetParameters, dict):
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
        if not isinstance(other, DataRowsGetParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
