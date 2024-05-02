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

class DataQueryColumnDTO(object):
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
        'layer_id': 'str',
        'column_id_alias': 'str',
        'table_id_alias': 'str',
        'data_table_join_id': 'str',
        'data_table_join_id2': 'str',
        'filters': 'list[DataFilterDTO]',
        'filter_logic': 'str',
        'not_available_value': 'str',
        'decimal_places': 'int'
    }

    attribute_map = {
        'id': 'id',
        'data_table_id': 'dataTableId',
        'layer_id': 'layerId',
        'column_id_alias': 'columnIdAlias',
        'table_id_alias': 'tableIdAlias',
        'data_table_join_id': 'dataTableJoinId',
        'data_table_join_id2': 'dataTableJoinId2',
        'filters': 'filters',
        'filter_logic': 'filterLogic',
        'not_available_value': 'notAvailableValue',
        'decimal_places': 'decimalPlaces'
    }

    def __init__(self, id=None, data_table_id=None, layer_id=None, column_id_alias=None, table_id_alias=None, data_table_join_id=None, data_table_join_id2=None, filters=None, filter_logic=None, not_available_value=None, decimal_places=None):  # noqa: E501
        """DataQueryColumnDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._data_table_id = None
        self._layer_id = None
        self._column_id_alias = None
        self._table_id_alias = None
        self._data_table_join_id = None
        self._data_table_join_id2 = None
        self._filters = None
        self._filter_logic = None
        self._not_available_value = None
        self._decimal_places = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if data_table_id is not None:
            self.data_table_id = data_table_id
        if layer_id is not None:
            self.layer_id = layer_id
        if column_id_alias is not None:
            self.column_id_alias = column_id_alias
        if table_id_alias is not None:
            self.table_id_alias = table_id_alias
        if data_table_join_id is not None:
            self.data_table_join_id = data_table_join_id
        if data_table_join_id2 is not None:
            self.data_table_join_id2 = data_table_join_id2
        if filters is not None:
            self.filters = filters
        if filter_logic is not None:
            self.filter_logic = filter_logic
        if not_available_value is not None:
            self.not_available_value = not_available_value
        if decimal_places is not None:
            self.decimal_places = decimal_places

    @property
    def id(self):
        """Gets the id of this DataQueryColumnDTO.  # noqa: E501


        :return: The id of this DataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataQueryColumnDTO.


        :param id: The id of this DataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def data_table_id(self):
        """Gets the data_table_id of this DataQueryColumnDTO.  # noqa: E501


        :return: The data_table_id of this DataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._data_table_id

    @data_table_id.setter
    def data_table_id(self, data_table_id):
        """Sets the data_table_id of this DataQueryColumnDTO.


        :param data_table_id: The data_table_id of this DataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._data_table_id = data_table_id

    @property
    def layer_id(self):
        """Gets the layer_id of this DataQueryColumnDTO.  # noqa: E501


        :return: The layer_id of this DataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._layer_id

    @layer_id.setter
    def layer_id(self, layer_id):
        """Sets the layer_id of this DataQueryColumnDTO.


        :param layer_id: The layer_id of this DataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._layer_id = layer_id

    @property
    def column_id_alias(self):
        """Gets the column_id_alias of this DataQueryColumnDTO.  # noqa: E501


        :return: The column_id_alias of this DataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._column_id_alias

    @column_id_alias.setter
    def column_id_alias(self, column_id_alias):
        """Sets the column_id_alias of this DataQueryColumnDTO.


        :param column_id_alias: The column_id_alias of this DataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._column_id_alias = column_id_alias

    @property
    def table_id_alias(self):
        """Gets the table_id_alias of this DataQueryColumnDTO.  # noqa: E501


        :return: The table_id_alias of this DataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._table_id_alias

    @table_id_alias.setter
    def table_id_alias(self, table_id_alias):
        """Sets the table_id_alias of this DataQueryColumnDTO.


        :param table_id_alias: The table_id_alias of this DataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._table_id_alias = table_id_alias

    @property
    def data_table_join_id(self):
        """Gets the data_table_join_id of this DataQueryColumnDTO.  # noqa: E501


        :return: The data_table_join_id of this DataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._data_table_join_id

    @data_table_join_id.setter
    def data_table_join_id(self, data_table_join_id):
        """Sets the data_table_join_id of this DataQueryColumnDTO.


        :param data_table_join_id: The data_table_join_id of this DataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._data_table_join_id = data_table_join_id

    @property
    def data_table_join_id2(self):
        """Gets the data_table_join_id2 of this DataQueryColumnDTO.  # noqa: E501


        :return: The data_table_join_id2 of this DataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._data_table_join_id2

    @data_table_join_id2.setter
    def data_table_join_id2(self, data_table_join_id2):
        """Sets the data_table_join_id2 of this DataQueryColumnDTO.


        :param data_table_join_id2: The data_table_join_id2 of this DataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._data_table_join_id2 = data_table_join_id2

    @property
    def filters(self):
        """Gets the filters of this DataQueryColumnDTO.  # noqa: E501


        :return: The filters of this DataQueryColumnDTO.  # noqa: E501
        :rtype: list[DataFilterDTO]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this DataQueryColumnDTO.


        :param filters: The filters of this DataQueryColumnDTO.  # noqa: E501
        :type: list[DataFilterDTO]
        """

        self._filters = filters

    @property
    def filter_logic(self):
        """Gets the filter_logic of this DataQueryColumnDTO.  # noqa: E501


        :return: The filter_logic of this DataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._filter_logic

    @filter_logic.setter
    def filter_logic(self, filter_logic):
        """Sets the filter_logic of this DataQueryColumnDTO.


        :param filter_logic: The filter_logic of this DataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._filter_logic = filter_logic

    @property
    def not_available_value(self):
        """Gets the not_available_value of this DataQueryColumnDTO.  # noqa: E501


        :return: The not_available_value of this DataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._not_available_value

    @not_available_value.setter
    def not_available_value(self, not_available_value):
        """Sets the not_available_value of this DataQueryColumnDTO.


        :param not_available_value: The not_available_value of this DataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._not_available_value = not_available_value

    @property
    def decimal_places(self):
        """Gets the decimal_places of this DataQueryColumnDTO.  # noqa: E501


        :return: The decimal_places of this DataQueryColumnDTO.  # noqa: E501
        :rtype: int
        """
        return self._decimal_places

    @decimal_places.setter
    def decimal_places(self, decimal_places):
        """Sets the decimal_places of this DataQueryColumnDTO.


        :param decimal_places: The decimal_places of this DataQueryColumnDTO.  # noqa: E501
        :type: int
        """

        self._decimal_places = decimal_places

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
        if issubclass(DataQueryColumnDTO, dict):
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
        if not isinstance(other, DataQueryColumnDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
