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

class GetRangesMessageDTOOfDataQueryColumnDTO(object):
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
        'data_column': 'OneOfGetRangesMessageDTOOfDataQueryColumnDTODataColumn',
        'filter_data_columns': 'list[DataQueryColumnDTO]',
        'number_of_ranges': 'int',
        'range_calculation_method': 'str',
        'exclude_not_available_value': 'bool',
        'server_cache_enabled': 'bool',
        'spatial_filter': 'OneOfGetRangesMessageDTOOfDataQueryColumnDTOSpatialFilter'
    }

    attribute_map = {
        'data_column': 'dataColumn',
        'filter_data_columns': 'filterDataColumns',
        'number_of_ranges': 'numberOfRanges',
        'range_calculation_method': 'rangeCalculationMethod',
        'exclude_not_available_value': 'excludeNotAvailableValue',
        'server_cache_enabled': 'serverCacheEnabled',
        'spatial_filter': 'spatialFilter'
    }

    def __init__(self, data_column=None, filter_data_columns=None, number_of_ranges=None, range_calculation_method=None, exclude_not_available_value=None, server_cache_enabled=None, spatial_filter=None):  # noqa: E501
        """GetRangesMessageDTOOfDataQueryColumnDTO - a model defined in Swagger"""  # noqa: E501
        self._data_column = None
        self._filter_data_columns = None
        self._number_of_ranges = None
        self._range_calculation_method = None
        self._exclude_not_available_value = None
        self._server_cache_enabled = None
        self._spatial_filter = None
        self.discriminator = None
        if data_column is not None:
            self.data_column = data_column
        if filter_data_columns is not None:
            self.filter_data_columns = filter_data_columns
        if number_of_ranges is not None:
            self.number_of_ranges = number_of_ranges
        if range_calculation_method is not None:
            self.range_calculation_method = range_calculation_method
        if exclude_not_available_value is not None:
            self.exclude_not_available_value = exclude_not_available_value
        if server_cache_enabled is not None:
            self.server_cache_enabled = server_cache_enabled
        if spatial_filter is not None:
            self.spatial_filter = spatial_filter

    @property
    def data_column(self):
        """Gets the data_column of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501


        :return: The data_column of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501
        :rtype: OneOfGetRangesMessageDTOOfDataQueryColumnDTODataColumn
        """
        return self._data_column

    @data_column.setter
    def data_column(self, data_column):
        """Sets the data_column of this GetRangesMessageDTOOfDataQueryColumnDTO.


        :param data_column: The data_column of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501
        :type: OneOfGetRangesMessageDTOOfDataQueryColumnDTODataColumn
        """

        self._data_column = data_column

    @property
    def filter_data_columns(self):
        """Gets the filter_data_columns of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501


        :return: The filter_data_columns of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501
        :rtype: list[DataQueryColumnDTO]
        """
        return self._filter_data_columns

    @filter_data_columns.setter
    def filter_data_columns(self, filter_data_columns):
        """Sets the filter_data_columns of this GetRangesMessageDTOOfDataQueryColumnDTO.


        :param filter_data_columns: The filter_data_columns of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501
        :type: list[DataQueryColumnDTO]
        """

        self._filter_data_columns = filter_data_columns

    @property
    def number_of_ranges(self):
        """Gets the number_of_ranges of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501


        :return: The number_of_ranges of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501
        :rtype: int
        """
        return self._number_of_ranges

    @number_of_ranges.setter
    def number_of_ranges(self, number_of_ranges):
        """Sets the number_of_ranges of this GetRangesMessageDTOOfDataQueryColumnDTO.


        :param number_of_ranges: The number_of_ranges of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501
        :type: int
        """

        self._number_of_ranges = number_of_ranges

    @property
    def range_calculation_method(self):
        """Gets the range_calculation_method of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501


        :return: The range_calculation_method of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._range_calculation_method

    @range_calculation_method.setter
    def range_calculation_method(self, range_calculation_method):
        """Sets the range_calculation_method of this GetRangesMessageDTOOfDataQueryColumnDTO.


        :param range_calculation_method: The range_calculation_method of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._range_calculation_method = range_calculation_method

    @property
    def exclude_not_available_value(self):
        """Gets the exclude_not_available_value of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501


        :return: The exclude_not_available_value of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_not_available_value

    @exclude_not_available_value.setter
    def exclude_not_available_value(self, exclude_not_available_value):
        """Sets the exclude_not_available_value of this GetRangesMessageDTOOfDataQueryColumnDTO.


        :param exclude_not_available_value: The exclude_not_available_value of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501
        :type: bool
        """

        self._exclude_not_available_value = exclude_not_available_value

    @property
    def server_cache_enabled(self):
        """Gets the server_cache_enabled of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501


        :return: The server_cache_enabled of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501
        :rtype: bool
        """
        return self._server_cache_enabled

    @server_cache_enabled.setter
    def server_cache_enabled(self, server_cache_enabled):
        """Sets the server_cache_enabled of this GetRangesMessageDTOOfDataQueryColumnDTO.


        :param server_cache_enabled: The server_cache_enabled of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501
        :type: bool
        """

        self._server_cache_enabled = server_cache_enabled

    @property
    def spatial_filter(self):
        """Gets the spatial_filter of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501


        :return: The spatial_filter of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501
        :rtype: OneOfGetRangesMessageDTOOfDataQueryColumnDTOSpatialFilter
        """
        return self._spatial_filter

    @spatial_filter.setter
    def spatial_filter(self, spatial_filter):
        """Sets the spatial_filter of this GetRangesMessageDTOOfDataQueryColumnDTO.


        :param spatial_filter: The spatial_filter of this GetRangesMessageDTOOfDataQueryColumnDTO.  # noqa: E501
        :type: OneOfGetRangesMessageDTOOfDataQueryColumnDTOSpatialFilter
        """

        self._spatial_filter = spatial_filter

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
        if issubclass(GetRangesMessageDTOOfDataQueryColumnDTO, dict):
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
        if not isinstance(other, GetRangesMessageDTOOfDataQueryColumnDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other