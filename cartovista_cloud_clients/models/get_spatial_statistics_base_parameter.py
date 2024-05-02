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

class GetSpatialStatisticsBaseParameter(object):
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
        'data_query_filters': 'list[DataQueryFilterDTOOfDataQueryColumnDTO]',
        'alternate_proj4': 'str'
    }

    attribute_map = {
        'data_query_filters': 'dataQueryFilters',
        'alternate_proj4': 'alternateProj4'
    }

    def __init__(self, data_query_filters=None, alternate_proj4=None):  # noqa: E501
        """GetSpatialStatisticsBaseParameter - a model defined in Swagger"""  # noqa: E501
        self._data_query_filters = None
        self._alternate_proj4 = None
        self.discriminator = None
        if data_query_filters is not None:
            self.data_query_filters = data_query_filters
        if alternate_proj4 is not None:
            self.alternate_proj4 = alternate_proj4

    @property
    def data_query_filters(self):
        """Gets the data_query_filters of this GetSpatialStatisticsBaseParameter.  # noqa: E501


        :return: The data_query_filters of this GetSpatialStatisticsBaseParameter.  # noqa: E501
        :rtype: list[DataQueryFilterDTOOfDataQueryColumnDTO]
        """
        return self._data_query_filters

    @data_query_filters.setter
    def data_query_filters(self, data_query_filters):
        """Sets the data_query_filters of this GetSpatialStatisticsBaseParameter.


        :param data_query_filters: The data_query_filters of this GetSpatialStatisticsBaseParameter.  # noqa: E501
        :type: list[DataQueryFilterDTOOfDataQueryColumnDTO]
        """

        self._data_query_filters = data_query_filters

    @property
    def alternate_proj4(self):
        """Gets the alternate_proj4 of this GetSpatialStatisticsBaseParameter.  # noqa: E501


        :return: The alternate_proj4 of this GetSpatialStatisticsBaseParameter.  # noqa: E501
        :rtype: str
        """
        return self._alternate_proj4

    @alternate_proj4.setter
    def alternate_proj4(self, alternate_proj4):
        """Sets the alternate_proj4 of this GetSpatialStatisticsBaseParameter.


        :param alternate_proj4: The alternate_proj4 of this GetSpatialStatisticsBaseParameter.  # noqa: E501
        :type: str
        """

        self._alternate_proj4 = alternate_proj4

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
        if issubclass(GetSpatialStatisticsBaseParameter, dict):
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
        if not isinstance(other, GetSpatialStatisticsBaseParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
