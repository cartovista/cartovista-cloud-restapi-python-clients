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

class TerritoryZoneDTO(object):
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
        'id': 'int',
        'pos_id': 'str',
        'status': 'TerritoryStatusEnum',
        'block_territories': 'list[BlockTerritoryDTO]',
        'search_polygon_wkt': 'str',
        'block_distance_to_pos': 'dict(str, DistanceToPosDTO)',
        'zone_id': 'int',
        'are_blocks_exclusive': 'bool',
        'is_zone_in_pta': 'bool',
        'is_implantation_territory': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'pos_id': 'posId',
        'status': 'status',
        'block_territories': 'blockTerritories',
        'search_polygon_wkt': 'searchPolygonWKT',
        'block_distance_to_pos': 'blockDistanceToPos',
        'zone_id': 'zoneId',
        'are_blocks_exclusive': 'areBlocksExclusive',
        'is_zone_in_pta': 'isZoneInPta',
        'is_implantation_territory': 'isImplantationTerritory'
    }

    def __init__(self, id=None, pos_id=None, status=None, block_territories=None, search_polygon_wkt=None, block_distance_to_pos=None, zone_id=None, are_blocks_exclusive=None, is_zone_in_pta=None, is_implantation_territory=None):  # noqa: E501
        """TerritoryZoneDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._pos_id = None
        self._status = None
        self._block_territories = None
        self._search_polygon_wkt = None
        self._block_distance_to_pos = None
        self._zone_id = None
        self._are_blocks_exclusive = None
        self._is_zone_in_pta = None
        self._is_implantation_territory = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if pos_id is not None:
            self.pos_id = pos_id
        if status is not None:
            self.status = status
        if block_territories is not None:
            self.block_territories = block_territories
        if search_polygon_wkt is not None:
            self.search_polygon_wkt = search_polygon_wkt
        if block_distance_to_pos is not None:
            self.block_distance_to_pos = block_distance_to_pos
        if zone_id is not None:
            self.zone_id = zone_id
        if are_blocks_exclusive is not None:
            self.are_blocks_exclusive = are_blocks_exclusive
        if is_zone_in_pta is not None:
            self.is_zone_in_pta = is_zone_in_pta
        if is_implantation_territory is not None:
            self.is_implantation_territory = is_implantation_territory

    @property
    def id(self):
        """Gets the id of this TerritoryZoneDTO.  # noqa: E501


        :return: The id of this TerritoryZoneDTO.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TerritoryZoneDTO.


        :param id: The id of this TerritoryZoneDTO.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def pos_id(self):
        """Gets the pos_id of this TerritoryZoneDTO.  # noqa: E501


        :return: The pos_id of this TerritoryZoneDTO.  # noqa: E501
        :rtype: str
        """
        return self._pos_id

    @pos_id.setter
    def pos_id(self, pos_id):
        """Sets the pos_id of this TerritoryZoneDTO.


        :param pos_id: The pos_id of this TerritoryZoneDTO.  # noqa: E501
        :type: str
        """

        self._pos_id = pos_id

    @property
    def status(self):
        """Gets the status of this TerritoryZoneDTO.  # noqa: E501


        :return: The status of this TerritoryZoneDTO.  # noqa: E501
        :rtype: TerritoryStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TerritoryZoneDTO.


        :param status: The status of this TerritoryZoneDTO.  # noqa: E501
        :type: TerritoryStatusEnum
        """

        self._status = status

    @property
    def block_territories(self):
        """Gets the block_territories of this TerritoryZoneDTO.  # noqa: E501


        :return: The block_territories of this TerritoryZoneDTO.  # noqa: E501
        :rtype: list[BlockTerritoryDTO]
        """
        return self._block_territories

    @block_territories.setter
    def block_territories(self, block_territories):
        """Sets the block_territories of this TerritoryZoneDTO.


        :param block_territories: The block_territories of this TerritoryZoneDTO.  # noqa: E501
        :type: list[BlockTerritoryDTO]
        """

        self._block_territories = block_territories

    @property
    def search_polygon_wkt(self):
        """Gets the search_polygon_wkt of this TerritoryZoneDTO.  # noqa: E501


        :return: The search_polygon_wkt of this TerritoryZoneDTO.  # noqa: E501
        :rtype: str
        """
        return self._search_polygon_wkt

    @search_polygon_wkt.setter
    def search_polygon_wkt(self, search_polygon_wkt):
        """Sets the search_polygon_wkt of this TerritoryZoneDTO.


        :param search_polygon_wkt: The search_polygon_wkt of this TerritoryZoneDTO.  # noqa: E501
        :type: str
        """

        self._search_polygon_wkt = search_polygon_wkt

    @property
    def block_distance_to_pos(self):
        """Gets the block_distance_to_pos of this TerritoryZoneDTO.  # noqa: E501


        :return: The block_distance_to_pos of this TerritoryZoneDTO.  # noqa: E501
        :rtype: dict(str, DistanceToPosDTO)
        """
        return self._block_distance_to_pos

    @block_distance_to_pos.setter
    def block_distance_to_pos(self, block_distance_to_pos):
        """Sets the block_distance_to_pos of this TerritoryZoneDTO.


        :param block_distance_to_pos: The block_distance_to_pos of this TerritoryZoneDTO.  # noqa: E501
        :type: dict(str, DistanceToPosDTO)
        """

        self._block_distance_to_pos = block_distance_to_pos

    @property
    def zone_id(self):
        """Gets the zone_id of this TerritoryZoneDTO.  # noqa: E501


        :return: The zone_id of this TerritoryZoneDTO.  # noqa: E501
        :rtype: int
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this TerritoryZoneDTO.


        :param zone_id: The zone_id of this TerritoryZoneDTO.  # noqa: E501
        :type: int
        """

        self._zone_id = zone_id

    @property
    def are_blocks_exclusive(self):
        """Gets the are_blocks_exclusive of this TerritoryZoneDTO.  # noqa: E501


        :return: The are_blocks_exclusive of this TerritoryZoneDTO.  # noqa: E501
        :rtype: bool
        """
        return self._are_blocks_exclusive

    @are_blocks_exclusive.setter
    def are_blocks_exclusive(self, are_blocks_exclusive):
        """Sets the are_blocks_exclusive of this TerritoryZoneDTO.


        :param are_blocks_exclusive: The are_blocks_exclusive of this TerritoryZoneDTO.  # noqa: E501
        :type: bool
        """

        self._are_blocks_exclusive = are_blocks_exclusive

    @property
    def is_zone_in_pta(self):
        """Gets the is_zone_in_pta of this TerritoryZoneDTO.  # noqa: E501


        :return: The is_zone_in_pta of this TerritoryZoneDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_zone_in_pta

    @is_zone_in_pta.setter
    def is_zone_in_pta(self, is_zone_in_pta):
        """Sets the is_zone_in_pta of this TerritoryZoneDTO.


        :param is_zone_in_pta: The is_zone_in_pta of this TerritoryZoneDTO.  # noqa: E501
        :type: bool
        """

        self._is_zone_in_pta = is_zone_in_pta

    @property
    def is_implantation_territory(self):
        """Gets the is_implantation_territory of this TerritoryZoneDTO.  # noqa: E501


        :return: The is_implantation_territory of this TerritoryZoneDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_implantation_territory

    @is_implantation_territory.setter
    def is_implantation_territory(self, is_implantation_territory):
        """Sets the is_implantation_territory of this TerritoryZoneDTO.


        :param is_implantation_territory: The is_implantation_territory of this TerritoryZoneDTO.  # noqa: E501
        :type: bool
        """

        self._is_implantation_territory = is_implantation_territory

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
        if issubclass(TerritoryZoneDTO, dict):
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
        if not isinstance(other, TerritoryZoneDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
