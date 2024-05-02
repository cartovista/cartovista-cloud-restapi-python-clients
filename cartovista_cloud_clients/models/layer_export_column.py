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

class LayerExportColumn(object):
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
        'column_id': 'str',
        'filters': 'list[DataFilter]',
        'filter_logic': 'FilterLogic'
    }

    attribute_map = {
        'column_id': 'columnId',
        'filters': 'filters',
        'filter_logic': 'filterLogic'
    }

    def __init__(self, column_id=None, filters=None, filter_logic=None):  # noqa: E501
        """LayerExportColumn - a model defined in Swagger"""  # noqa: E501
        self._column_id = None
        self._filters = None
        self._filter_logic = None
        self.discriminator = None
        if column_id is not None:
            self.column_id = column_id
        if filters is not None:
            self.filters = filters
        if filter_logic is not None:
            self.filter_logic = filter_logic

    @property
    def column_id(self):
        """Gets the column_id of this LayerExportColumn.  # noqa: E501


        :return: The column_id of this LayerExportColumn.  # noqa: E501
        :rtype: str
        """
        return self._column_id

    @column_id.setter
    def column_id(self, column_id):
        """Sets the column_id of this LayerExportColumn.


        :param column_id: The column_id of this LayerExportColumn.  # noqa: E501
        :type: str
        """

        self._column_id = column_id

    @property
    def filters(self):
        """Gets the filters of this LayerExportColumn.  # noqa: E501


        :return: The filters of this LayerExportColumn.  # noqa: E501
        :rtype: list[DataFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this LayerExportColumn.


        :param filters: The filters of this LayerExportColumn.  # noqa: E501
        :type: list[DataFilter]
        """

        self._filters = filters

    @property
    def filter_logic(self):
        """Gets the filter_logic of this LayerExportColumn.  # noqa: E501


        :return: The filter_logic of this LayerExportColumn.  # noqa: E501
        :rtype: FilterLogic
        """
        return self._filter_logic

    @filter_logic.setter
    def filter_logic(self, filter_logic):
        """Sets the filter_logic of this LayerExportColumn.


        :param filter_logic: The filter_logic of this LayerExportColumn.  # noqa: E501
        :type: FilterLogic
        """

        self._filter_logic = filter_logic

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
        if issubclass(LayerExportColumn, dict):
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
        if not isinstance(other, LayerExportColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other