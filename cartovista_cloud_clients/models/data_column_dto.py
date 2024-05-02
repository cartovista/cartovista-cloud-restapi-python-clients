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

class DataColumnDTO(object):
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
        'internal_sys_column': 'bool',
        'database_name': 'str',
        'data_type': 'CartoVistaPortalDataType',
        'filters': 'list[DataFilterDTO]',
        'filter_logic': 'str',
        'id': 'str',
        'data_table_id': 'str',
        'source_object_id': 'str',
        'column_id_alias': 'str',
        'table_id_alias': 'str',
        'name': 'str',
        'decimal_places': 'int',
        'not_available_value': 'str',
        'data_table_join_id': 'str',
        'data_table_join_id2': 'str',
        'internal_alias': 'str'
    }

    attribute_map = {
        'internal_sys_column': 'internalSysColumn',
        'database_name': 'databaseName',
        'data_type': 'dataType',
        'filters': 'filters',
        'filter_logic': 'filterLogic',
        'id': 'id',
        'data_table_id': 'dataTableId',
        'source_object_id': 'sourceObjectId',
        'column_id_alias': 'columnIdAlias',
        'table_id_alias': 'tableIdAlias',
        'name': 'name',
        'decimal_places': 'decimalPlaces',
        'not_available_value': 'notAvailableValue',
        'data_table_join_id': 'dataTableJoinId',
        'data_table_join_id2': 'dataTableJoinId2',
        'internal_alias': 'internalAlias'
    }

    def __init__(self, internal_sys_column=None, database_name=None, data_type=None, filters=None, filter_logic=None, id=None, data_table_id=None, source_object_id=None, column_id_alias=None, table_id_alias=None, name=None, decimal_places=None, not_available_value=None, data_table_join_id=None, data_table_join_id2=None, internal_alias=None):  # noqa: E501
        """DataColumnDTO - a model defined in Swagger"""  # noqa: E501
        self._internal_sys_column = None
        self._database_name = None
        self._data_type = None
        self._filters = None
        self._filter_logic = None
        self._id = None
        self._data_table_id = None
        self._source_object_id = None
        self._column_id_alias = None
        self._table_id_alias = None
        self._name = None
        self._decimal_places = None
        self._not_available_value = None
        self._data_table_join_id = None
        self._data_table_join_id2 = None
        self._internal_alias = None
        self.discriminator = None
        if internal_sys_column is not None:
            self.internal_sys_column = internal_sys_column
        if database_name is not None:
            self.database_name = database_name
        if data_type is not None:
            self.data_type = data_type
        if filters is not None:
            self.filters = filters
        if filter_logic is not None:
            self.filter_logic = filter_logic
        if id is not None:
            self.id = id
        if data_table_id is not None:
            self.data_table_id = data_table_id
        if source_object_id is not None:
            self.source_object_id = source_object_id
        if column_id_alias is not None:
            self.column_id_alias = column_id_alias
        if table_id_alias is not None:
            self.table_id_alias = table_id_alias
        if name is not None:
            self.name = name
        if decimal_places is not None:
            self.decimal_places = decimal_places
        if not_available_value is not None:
            self.not_available_value = not_available_value
        if data_table_join_id is not None:
            self.data_table_join_id = data_table_join_id
        if data_table_join_id2 is not None:
            self.data_table_join_id2 = data_table_join_id2
        if internal_alias is not None:
            self.internal_alias = internal_alias

    @property
    def internal_sys_column(self):
        """Gets the internal_sys_column of this DataColumnDTO.  # noqa: E501


        :return: The internal_sys_column of this DataColumnDTO.  # noqa: E501
        :rtype: bool
        """
        return self._internal_sys_column

    @internal_sys_column.setter
    def internal_sys_column(self, internal_sys_column):
        """Sets the internal_sys_column of this DataColumnDTO.


        :param internal_sys_column: The internal_sys_column of this DataColumnDTO.  # noqa: E501
        :type: bool
        """

        self._internal_sys_column = internal_sys_column

    @property
    def database_name(self):
        """Gets the database_name of this DataColumnDTO.  # noqa: E501


        :return: The database_name of this DataColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this DataColumnDTO.


        :param database_name: The database_name of this DataColumnDTO.  # noqa: E501
        :type: str
        """

        self._database_name = database_name

    @property
    def data_type(self):
        """Gets the data_type of this DataColumnDTO.  # noqa: E501


        :return: The data_type of this DataColumnDTO.  # noqa: E501
        :rtype: CartoVistaPortalDataType
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this DataColumnDTO.


        :param data_type: The data_type of this DataColumnDTO.  # noqa: E501
        :type: CartoVistaPortalDataType
        """

        self._data_type = data_type

    @property
    def filters(self):
        """Gets the filters of this DataColumnDTO.  # noqa: E501


        :return: The filters of this DataColumnDTO.  # noqa: E501
        :rtype: list[DataFilterDTO]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this DataColumnDTO.


        :param filters: The filters of this DataColumnDTO.  # noqa: E501
        :type: list[DataFilterDTO]
        """

        self._filters = filters

    @property
    def filter_logic(self):
        """Gets the filter_logic of this DataColumnDTO.  # noqa: E501


        :return: The filter_logic of this DataColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._filter_logic

    @filter_logic.setter
    def filter_logic(self, filter_logic):
        """Sets the filter_logic of this DataColumnDTO.


        :param filter_logic: The filter_logic of this DataColumnDTO.  # noqa: E501
        :type: str
        """

        self._filter_logic = filter_logic

    @property
    def id(self):
        """Gets the id of this DataColumnDTO.  # noqa: E501


        :return: The id of this DataColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataColumnDTO.


        :param id: The id of this DataColumnDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def data_table_id(self):
        """Gets the data_table_id of this DataColumnDTO.  # noqa: E501


        :return: The data_table_id of this DataColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._data_table_id

    @data_table_id.setter
    def data_table_id(self, data_table_id):
        """Sets the data_table_id of this DataColumnDTO.


        :param data_table_id: The data_table_id of this DataColumnDTO.  # noqa: E501
        :type: str
        """

        self._data_table_id = data_table_id

    @property
    def source_object_id(self):
        """Gets the source_object_id of this DataColumnDTO.  # noqa: E501


        :return: The source_object_id of this DataColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._source_object_id

    @source_object_id.setter
    def source_object_id(self, source_object_id):
        """Sets the source_object_id of this DataColumnDTO.


        :param source_object_id: The source_object_id of this DataColumnDTO.  # noqa: E501
        :type: str
        """

        self._source_object_id = source_object_id

    @property
    def column_id_alias(self):
        """Gets the column_id_alias of this DataColumnDTO.  # noqa: E501


        :return: The column_id_alias of this DataColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._column_id_alias

    @column_id_alias.setter
    def column_id_alias(self, column_id_alias):
        """Sets the column_id_alias of this DataColumnDTO.


        :param column_id_alias: The column_id_alias of this DataColumnDTO.  # noqa: E501
        :type: str
        """

        self._column_id_alias = column_id_alias

    @property
    def table_id_alias(self):
        """Gets the table_id_alias of this DataColumnDTO.  # noqa: E501


        :return: The table_id_alias of this DataColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._table_id_alias

    @table_id_alias.setter
    def table_id_alias(self, table_id_alias):
        """Sets the table_id_alias of this DataColumnDTO.


        :param table_id_alias: The table_id_alias of this DataColumnDTO.  # noqa: E501
        :type: str
        """

        self._table_id_alias = table_id_alias

    @property
    def name(self):
        """Gets the name of this DataColumnDTO.  # noqa: E501


        :return: The name of this DataColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataColumnDTO.


        :param name: The name of this DataColumnDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def decimal_places(self):
        """Gets the decimal_places of this DataColumnDTO.  # noqa: E501


        :return: The decimal_places of this DataColumnDTO.  # noqa: E501
        :rtype: int
        """
        return self._decimal_places

    @decimal_places.setter
    def decimal_places(self, decimal_places):
        """Sets the decimal_places of this DataColumnDTO.


        :param decimal_places: The decimal_places of this DataColumnDTO.  # noqa: E501
        :type: int
        """

        self._decimal_places = decimal_places

    @property
    def not_available_value(self):
        """Gets the not_available_value of this DataColumnDTO.  # noqa: E501


        :return: The not_available_value of this DataColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._not_available_value

    @not_available_value.setter
    def not_available_value(self, not_available_value):
        """Sets the not_available_value of this DataColumnDTO.


        :param not_available_value: The not_available_value of this DataColumnDTO.  # noqa: E501
        :type: str
        """

        self._not_available_value = not_available_value

    @property
    def data_table_join_id(self):
        """Gets the data_table_join_id of this DataColumnDTO.  # noqa: E501


        :return: The data_table_join_id of this DataColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._data_table_join_id

    @data_table_join_id.setter
    def data_table_join_id(self, data_table_join_id):
        """Sets the data_table_join_id of this DataColumnDTO.


        :param data_table_join_id: The data_table_join_id of this DataColumnDTO.  # noqa: E501
        :type: str
        """

        self._data_table_join_id = data_table_join_id

    @property
    def data_table_join_id2(self):
        """Gets the data_table_join_id2 of this DataColumnDTO.  # noqa: E501


        :return: The data_table_join_id2 of this DataColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._data_table_join_id2

    @data_table_join_id2.setter
    def data_table_join_id2(self, data_table_join_id2):
        """Sets the data_table_join_id2 of this DataColumnDTO.


        :param data_table_join_id2: The data_table_join_id2 of this DataColumnDTO.  # noqa: E501
        :type: str
        """

        self._data_table_join_id2 = data_table_join_id2

    @property
    def internal_alias(self):
        """Gets the internal_alias of this DataColumnDTO.  # noqa: E501


        :return: The internal_alias of this DataColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._internal_alias

    @internal_alias.setter
    def internal_alias(self, internal_alias):
        """Sets the internal_alias of this DataColumnDTO.


        :param internal_alias: The internal_alias of this DataColumnDTO.  # noqa: E501
        :type: str
        """

        self._internal_alias = internal_alias

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
        if issubclass(DataColumnDTO, dict):
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
        if not isinstance(other, DataColumnDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
