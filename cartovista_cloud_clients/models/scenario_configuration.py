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

class ScenarioConfiguration(object):
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
        'territory_id': 'str',
        'source_id': 'str',
        'pos_id': 'str',
        'column_id': 'str',
        'territory_table_id': 'str',
        'columns': 'list[TerritoryColumnDTO]',
        'data_column_configuration': 'list[ScenarioDataColumnConfigurationDTO]',
        'territory_themeset_id': 'str',
        'source_themeset_id': 'str',
        'promote_territory_data_column_id': 'str',
        'pos_column_id_for_territory_name': 'str',
        'search_polygon_column_id': 'str',
        'block_distance_to_pos_column_id': 'str',
        'territory_pos_xref_table_id': 'str',
        'territory_pos_table_xref_territory_column_id': 'str',
        'territory_pos_table_xref_pos_column_id': 'str',
        'territory_block_xref_table_id': 'str',
        'territory_block_table_xref_territory_column_id': 'str',
        'territory_block_table_xref_block_column_id': 'str',
        'territory_pos_data_table_join_id': 'str',
        'zone_table_id': 'str'
    }

    attribute_map = {
        'territory_id': 'territoryId',
        'source_id': 'sourceId',
        'pos_id': 'posId',
        'column_id': 'columnId',
        'territory_table_id': 'territoryTableId',
        'columns': 'columns',
        'data_column_configuration': 'dataColumnConfiguration',
        'territory_themeset_id': 'territoryThemesetId',
        'source_themeset_id': 'sourceThemesetId',
        'promote_territory_data_column_id': 'promoteTerritoryDataColumnId',
        'pos_column_id_for_territory_name': 'posColumnIdForTerritoryName',
        'search_polygon_column_id': 'searchPolygonColumnId',
        'block_distance_to_pos_column_id': 'blockDistanceToPosColumnId',
        'territory_pos_xref_table_id': 'territoryPos_XREF_TableId',
        'territory_pos_table_xref_territory_column_id': 'territoryPosTable_XREF_TerritoryColumnId',
        'territory_pos_table_xref_pos_column_id': 'territoryPosTable_XREF_POSColumnId',
        'territory_block_xref_table_id': 'territoryBlock_XREF_TableId',
        'territory_block_table_xref_territory_column_id': 'territoryBlockTable_XREF_TerritoryColumnId',
        'territory_block_table_xref_block_column_id': 'territoryBlockTable_XREF_BlockColumnId',
        'territory_pos_data_table_join_id': 'territoryPosDataTableJoinId',
        'zone_table_id': 'zoneTableId'
    }

    def __init__(self, territory_id=None, source_id=None, pos_id=None, column_id=None, territory_table_id=None, columns=None, data_column_configuration=None, territory_themeset_id=None, source_themeset_id=None, promote_territory_data_column_id=None, pos_column_id_for_territory_name=None, search_polygon_column_id=None, block_distance_to_pos_column_id=None, territory_pos_xref_table_id=None, territory_pos_table_xref_territory_column_id=None, territory_pos_table_xref_pos_column_id=None, territory_block_xref_table_id=None, territory_block_table_xref_territory_column_id=None, territory_block_table_xref_block_column_id=None, territory_pos_data_table_join_id=None, zone_table_id=None):  # noqa: E501
        """ScenarioConfiguration - a model defined in Swagger"""  # noqa: E501
        self._territory_id = None
        self._source_id = None
        self._pos_id = None
        self._column_id = None
        self._territory_table_id = None
        self._columns = None
        self._data_column_configuration = None
        self._territory_themeset_id = None
        self._source_themeset_id = None
        self._promote_territory_data_column_id = None
        self._pos_column_id_for_territory_name = None
        self._search_polygon_column_id = None
        self._block_distance_to_pos_column_id = None
        self._territory_pos_xref_table_id = None
        self._territory_pos_table_xref_territory_column_id = None
        self._territory_pos_table_xref_pos_column_id = None
        self._territory_block_xref_table_id = None
        self._territory_block_table_xref_territory_column_id = None
        self._territory_block_table_xref_block_column_id = None
        self._territory_pos_data_table_join_id = None
        self._zone_table_id = None
        self.discriminator = None
        if territory_id is not None:
            self.territory_id = territory_id
        if source_id is not None:
            self.source_id = source_id
        if pos_id is not None:
            self.pos_id = pos_id
        if column_id is not None:
            self.column_id = column_id
        if territory_table_id is not None:
            self.territory_table_id = territory_table_id
        if columns is not None:
            self.columns = columns
        if data_column_configuration is not None:
            self.data_column_configuration = data_column_configuration
        if territory_themeset_id is not None:
            self.territory_themeset_id = territory_themeset_id
        if source_themeset_id is not None:
            self.source_themeset_id = source_themeset_id
        if promote_territory_data_column_id is not None:
            self.promote_territory_data_column_id = promote_territory_data_column_id
        if pos_column_id_for_territory_name is not None:
            self.pos_column_id_for_territory_name = pos_column_id_for_territory_name
        if search_polygon_column_id is not None:
            self.search_polygon_column_id = search_polygon_column_id
        if block_distance_to_pos_column_id is not None:
            self.block_distance_to_pos_column_id = block_distance_to_pos_column_id
        if territory_pos_xref_table_id is not None:
            self.territory_pos_xref_table_id = territory_pos_xref_table_id
        if territory_pos_table_xref_territory_column_id is not None:
            self.territory_pos_table_xref_territory_column_id = territory_pos_table_xref_territory_column_id
        if territory_pos_table_xref_pos_column_id is not None:
            self.territory_pos_table_xref_pos_column_id = territory_pos_table_xref_pos_column_id
        if territory_block_xref_table_id is not None:
            self.territory_block_xref_table_id = territory_block_xref_table_id
        if territory_block_table_xref_territory_column_id is not None:
            self.territory_block_table_xref_territory_column_id = territory_block_table_xref_territory_column_id
        if territory_block_table_xref_block_column_id is not None:
            self.territory_block_table_xref_block_column_id = territory_block_table_xref_block_column_id
        if territory_pos_data_table_join_id is not None:
            self.territory_pos_data_table_join_id = territory_pos_data_table_join_id
        if zone_table_id is not None:
            self.zone_table_id = zone_table_id

    @property
    def territory_id(self):
        """Gets the territory_id of this ScenarioConfiguration.  # noqa: E501


        :return: The territory_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._territory_id

    @territory_id.setter
    def territory_id(self, territory_id):
        """Sets the territory_id of this ScenarioConfiguration.


        :param territory_id: The territory_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._territory_id = territory_id

    @property
    def source_id(self):
        """Gets the source_id of this ScenarioConfiguration.  # noqa: E501


        :return: The source_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this ScenarioConfiguration.


        :param source_id: The source_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def pos_id(self):
        """Gets the pos_id of this ScenarioConfiguration.  # noqa: E501


        :return: The pos_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._pos_id

    @pos_id.setter
    def pos_id(self, pos_id):
        """Sets the pos_id of this ScenarioConfiguration.


        :param pos_id: The pos_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._pos_id = pos_id

    @property
    def column_id(self):
        """Gets the column_id of this ScenarioConfiguration.  # noqa: E501


        :return: The column_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._column_id

    @column_id.setter
    def column_id(self, column_id):
        """Sets the column_id of this ScenarioConfiguration.


        :param column_id: The column_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._column_id = column_id

    @property
    def territory_table_id(self):
        """Gets the territory_table_id of this ScenarioConfiguration.  # noqa: E501


        :return: The territory_table_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._territory_table_id

    @territory_table_id.setter
    def territory_table_id(self, territory_table_id):
        """Sets the territory_table_id of this ScenarioConfiguration.


        :param territory_table_id: The territory_table_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._territory_table_id = territory_table_id

    @property
    def columns(self):
        """Gets the columns of this ScenarioConfiguration.  # noqa: E501


        :return: The columns of this ScenarioConfiguration.  # noqa: E501
        :rtype: list[TerritoryColumnDTO]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this ScenarioConfiguration.


        :param columns: The columns of this ScenarioConfiguration.  # noqa: E501
        :type: list[TerritoryColumnDTO]
        """

        self._columns = columns

    @property
    def data_column_configuration(self):
        """Gets the data_column_configuration of this ScenarioConfiguration.  # noqa: E501


        :return: The data_column_configuration of this ScenarioConfiguration.  # noqa: E501
        :rtype: list[ScenarioDataColumnConfigurationDTO]
        """
        return self._data_column_configuration

    @data_column_configuration.setter
    def data_column_configuration(self, data_column_configuration):
        """Sets the data_column_configuration of this ScenarioConfiguration.


        :param data_column_configuration: The data_column_configuration of this ScenarioConfiguration.  # noqa: E501
        :type: list[ScenarioDataColumnConfigurationDTO]
        """

        self._data_column_configuration = data_column_configuration

    @property
    def territory_themeset_id(self):
        """Gets the territory_themeset_id of this ScenarioConfiguration.  # noqa: E501


        :return: The territory_themeset_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._territory_themeset_id

    @territory_themeset_id.setter
    def territory_themeset_id(self, territory_themeset_id):
        """Sets the territory_themeset_id of this ScenarioConfiguration.


        :param territory_themeset_id: The territory_themeset_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._territory_themeset_id = territory_themeset_id

    @property
    def source_themeset_id(self):
        """Gets the source_themeset_id of this ScenarioConfiguration.  # noqa: E501


        :return: The source_themeset_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._source_themeset_id

    @source_themeset_id.setter
    def source_themeset_id(self, source_themeset_id):
        """Sets the source_themeset_id of this ScenarioConfiguration.


        :param source_themeset_id: The source_themeset_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._source_themeset_id = source_themeset_id

    @property
    def promote_territory_data_column_id(self):
        """Gets the promote_territory_data_column_id of this ScenarioConfiguration.  # noqa: E501


        :return: The promote_territory_data_column_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._promote_territory_data_column_id

    @promote_territory_data_column_id.setter
    def promote_territory_data_column_id(self, promote_territory_data_column_id):
        """Sets the promote_territory_data_column_id of this ScenarioConfiguration.


        :param promote_territory_data_column_id: The promote_territory_data_column_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._promote_territory_data_column_id = promote_territory_data_column_id

    @property
    def pos_column_id_for_territory_name(self):
        """Gets the pos_column_id_for_territory_name of this ScenarioConfiguration.  # noqa: E501


        :return: The pos_column_id_for_territory_name of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._pos_column_id_for_territory_name

    @pos_column_id_for_territory_name.setter
    def pos_column_id_for_territory_name(self, pos_column_id_for_territory_name):
        """Sets the pos_column_id_for_territory_name of this ScenarioConfiguration.


        :param pos_column_id_for_territory_name: The pos_column_id_for_territory_name of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._pos_column_id_for_territory_name = pos_column_id_for_territory_name

    @property
    def search_polygon_column_id(self):
        """Gets the search_polygon_column_id of this ScenarioConfiguration.  # noqa: E501


        :return: The search_polygon_column_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._search_polygon_column_id

    @search_polygon_column_id.setter
    def search_polygon_column_id(self, search_polygon_column_id):
        """Sets the search_polygon_column_id of this ScenarioConfiguration.


        :param search_polygon_column_id: The search_polygon_column_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._search_polygon_column_id = search_polygon_column_id

    @property
    def block_distance_to_pos_column_id(self):
        """Gets the block_distance_to_pos_column_id of this ScenarioConfiguration.  # noqa: E501


        :return: The block_distance_to_pos_column_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._block_distance_to_pos_column_id

    @block_distance_to_pos_column_id.setter
    def block_distance_to_pos_column_id(self, block_distance_to_pos_column_id):
        """Sets the block_distance_to_pos_column_id of this ScenarioConfiguration.


        :param block_distance_to_pos_column_id: The block_distance_to_pos_column_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._block_distance_to_pos_column_id = block_distance_to_pos_column_id

    @property
    def territory_pos_xref_table_id(self):
        """Gets the territory_pos_xref_table_id of this ScenarioConfiguration.  # noqa: E501


        :return: The territory_pos_xref_table_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._territory_pos_xref_table_id

    @territory_pos_xref_table_id.setter
    def territory_pos_xref_table_id(self, territory_pos_xref_table_id):
        """Sets the territory_pos_xref_table_id of this ScenarioConfiguration.


        :param territory_pos_xref_table_id: The territory_pos_xref_table_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._territory_pos_xref_table_id = territory_pos_xref_table_id

    @property
    def territory_pos_table_xref_territory_column_id(self):
        """Gets the territory_pos_table_xref_territory_column_id of this ScenarioConfiguration.  # noqa: E501


        :return: The territory_pos_table_xref_territory_column_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._territory_pos_table_xref_territory_column_id

    @territory_pos_table_xref_territory_column_id.setter
    def territory_pos_table_xref_territory_column_id(self, territory_pos_table_xref_territory_column_id):
        """Sets the territory_pos_table_xref_territory_column_id of this ScenarioConfiguration.


        :param territory_pos_table_xref_territory_column_id: The territory_pos_table_xref_territory_column_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._territory_pos_table_xref_territory_column_id = territory_pos_table_xref_territory_column_id

    @property
    def territory_pos_table_xref_pos_column_id(self):
        """Gets the territory_pos_table_xref_pos_column_id of this ScenarioConfiguration.  # noqa: E501


        :return: The territory_pos_table_xref_pos_column_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._territory_pos_table_xref_pos_column_id

    @territory_pos_table_xref_pos_column_id.setter
    def territory_pos_table_xref_pos_column_id(self, territory_pos_table_xref_pos_column_id):
        """Sets the territory_pos_table_xref_pos_column_id of this ScenarioConfiguration.


        :param territory_pos_table_xref_pos_column_id: The territory_pos_table_xref_pos_column_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._territory_pos_table_xref_pos_column_id = territory_pos_table_xref_pos_column_id

    @property
    def territory_block_xref_table_id(self):
        """Gets the territory_block_xref_table_id of this ScenarioConfiguration.  # noqa: E501


        :return: The territory_block_xref_table_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._territory_block_xref_table_id

    @territory_block_xref_table_id.setter
    def territory_block_xref_table_id(self, territory_block_xref_table_id):
        """Sets the territory_block_xref_table_id of this ScenarioConfiguration.


        :param territory_block_xref_table_id: The territory_block_xref_table_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._territory_block_xref_table_id = territory_block_xref_table_id

    @property
    def territory_block_table_xref_territory_column_id(self):
        """Gets the territory_block_table_xref_territory_column_id of this ScenarioConfiguration.  # noqa: E501


        :return: The territory_block_table_xref_territory_column_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._territory_block_table_xref_territory_column_id

    @territory_block_table_xref_territory_column_id.setter
    def territory_block_table_xref_territory_column_id(self, territory_block_table_xref_territory_column_id):
        """Sets the territory_block_table_xref_territory_column_id of this ScenarioConfiguration.


        :param territory_block_table_xref_territory_column_id: The territory_block_table_xref_territory_column_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._territory_block_table_xref_territory_column_id = territory_block_table_xref_territory_column_id

    @property
    def territory_block_table_xref_block_column_id(self):
        """Gets the territory_block_table_xref_block_column_id of this ScenarioConfiguration.  # noqa: E501


        :return: The territory_block_table_xref_block_column_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._territory_block_table_xref_block_column_id

    @territory_block_table_xref_block_column_id.setter
    def territory_block_table_xref_block_column_id(self, territory_block_table_xref_block_column_id):
        """Sets the territory_block_table_xref_block_column_id of this ScenarioConfiguration.


        :param territory_block_table_xref_block_column_id: The territory_block_table_xref_block_column_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._territory_block_table_xref_block_column_id = territory_block_table_xref_block_column_id

    @property
    def territory_pos_data_table_join_id(self):
        """Gets the territory_pos_data_table_join_id of this ScenarioConfiguration.  # noqa: E501


        :return: The territory_pos_data_table_join_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._territory_pos_data_table_join_id

    @territory_pos_data_table_join_id.setter
    def territory_pos_data_table_join_id(self, territory_pos_data_table_join_id):
        """Sets the territory_pos_data_table_join_id of this ScenarioConfiguration.


        :param territory_pos_data_table_join_id: The territory_pos_data_table_join_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._territory_pos_data_table_join_id = territory_pos_data_table_join_id

    @property
    def zone_table_id(self):
        """Gets the zone_table_id of this ScenarioConfiguration.  # noqa: E501


        :return: The zone_table_id of this ScenarioConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._zone_table_id

    @zone_table_id.setter
    def zone_table_id(self, zone_table_id):
        """Sets the zone_table_id of this ScenarioConfiguration.


        :param zone_table_id: The zone_table_id of this ScenarioConfiguration.  # noqa: E501
        :type: str
        """

        self._zone_table_id = zone_table_id

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
        if issubclass(ScenarioConfiguration, dict):
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
        if not isinstance(other, ScenarioConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
