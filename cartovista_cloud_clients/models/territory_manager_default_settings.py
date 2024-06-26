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

class TerritoryManagerDefaultSettings(object):
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
        'area_type': 'TerritoryAreaByEnum',
        'transportation_type': 'TerritoryTransportTypeEnum',
        'consider_traffic': 'bool',
        'selection_color': 'str',
        'maximum_nearest_for_distance_analysis': 'int',
        'spatial_selection_type': 'TerritoryScenarioSpatialSelectionTypeEnum',
        'zone_themeset_colors': 'list[str]',
        'mapping_zone_themeset_names': 'str',
        'max_zones': 'int'
    }

    attribute_map = {
        'area_type': 'areaType',
        'transportation_type': 'transportationType',
        'consider_traffic': 'considerTraffic',
        'selection_color': 'selectionColor',
        'maximum_nearest_for_distance_analysis': 'maximumNearestForDistanceAnalysis',
        'spatial_selection_type': 'spatialSelectionType',
        'zone_themeset_colors': 'zoneThemesetColors',
        'mapping_zone_themeset_names': 'mappingZoneThemesetNames',
        'max_zones': 'maxZones'
    }

    def __init__(self, area_type=None, transportation_type=None, consider_traffic=None, selection_color=None, maximum_nearest_for_distance_analysis=None, spatial_selection_type=None, zone_themeset_colors=None, mapping_zone_themeset_names=None, max_zones=None):  # noqa: E501
        """TerritoryManagerDefaultSettings - a model defined in Swagger"""  # noqa: E501
        self._area_type = None
        self._transportation_type = None
        self._consider_traffic = None
        self._selection_color = None
        self._maximum_nearest_for_distance_analysis = None
        self._spatial_selection_type = None
        self._zone_themeset_colors = None
        self._mapping_zone_themeset_names = None
        self._max_zones = None
        self.discriminator = None
        if area_type is not None:
            self.area_type = area_type
        if transportation_type is not None:
            self.transportation_type = transportation_type
        if consider_traffic is not None:
            self.consider_traffic = consider_traffic
        if selection_color is not None:
            self.selection_color = selection_color
        if maximum_nearest_for_distance_analysis is not None:
            self.maximum_nearest_for_distance_analysis = maximum_nearest_for_distance_analysis
        if spatial_selection_type is not None:
            self.spatial_selection_type = spatial_selection_type
        if zone_themeset_colors is not None:
            self.zone_themeset_colors = zone_themeset_colors
        if mapping_zone_themeset_names is not None:
            self.mapping_zone_themeset_names = mapping_zone_themeset_names
        if max_zones is not None:
            self.max_zones = max_zones

    @property
    def area_type(self):
        """Gets the area_type of this TerritoryManagerDefaultSettings.  # noqa: E501


        :return: The area_type of this TerritoryManagerDefaultSettings.  # noqa: E501
        :rtype: TerritoryAreaByEnum
        """
        return self._area_type

    @area_type.setter
    def area_type(self, area_type):
        """Sets the area_type of this TerritoryManagerDefaultSettings.


        :param area_type: The area_type of this TerritoryManagerDefaultSettings.  # noqa: E501
        :type: TerritoryAreaByEnum
        """

        self._area_type = area_type

    @property
    def transportation_type(self):
        """Gets the transportation_type of this TerritoryManagerDefaultSettings.  # noqa: E501


        :return: The transportation_type of this TerritoryManagerDefaultSettings.  # noqa: E501
        :rtype: TerritoryTransportTypeEnum
        """
        return self._transportation_type

    @transportation_type.setter
    def transportation_type(self, transportation_type):
        """Sets the transportation_type of this TerritoryManagerDefaultSettings.


        :param transportation_type: The transportation_type of this TerritoryManagerDefaultSettings.  # noqa: E501
        :type: TerritoryTransportTypeEnum
        """

        self._transportation_type = transportation_type

    @property
    def consider_traffic(self):
        """Gets the consider_traffic of this TerritoryManagerDefaultSettings.  # noqa: E501


        :return: The consider_traffic of this TerritoryManagerDefaultSettings.  # noqa: E501
        :rtype: bool
        """
        return self._consider_traffic

    @consider_traffic.setter
    def consider_traffic(self, consider_traffic):
        """Sets the consider_traffic of this TerritoryManagerDefaultSettings.


        :param consider_traffic: The consider_traffic of this TerritoryManagerDefaultSettings.  # noqa: E501
        :type: bool
        """

        self._consider_traffic = consider_traffic

    @property
    def selection_color(self):
        """Gets the selection_color of this TerritoryManagerDefaultSettings.  # noqa: E501


        :return: The selection_color of this TerritoryManagerDefaultSettings.  # noqa: E501
        :rtype: str
        """
        return self._selection_color

    @selection_color.setter
    def selection_color(self, selection_color):
        """Sets the selection_color of this TerritoryManagerDefaultSettings.


        :param selection_color: The selection_color of this TerritoryManagerDefaultSettings.  # noqa: E501
        :type: str
        """

        self._selection_color = selection_color

    @property
    def maximum_nearest_for_distance_analysis(self):
        """Gets the maximum_nearest_for_distance_analysis of this TerritoryManagerDefaultSettings.  # noqa: E501


        :return: The maximum_nearest_for_distance_analysis of this TerritoryManagerDefaultSettings.  # noqa: E501
        :rtype: int
        """
        return self._maximum_nearest_for_distance_analysis

    @maximum_nearest_for_distance_analysis.setter
    def maximum_nearest_for_distance_analysis(self, maximum_nearest_for_distance_analysis):
        """Sets the maximum_nearest_for_distance_analysis of this TerritoryManagerDefaultSettings.


        :param maximum_nearest_for_distance_analysis: The maximum_nearest_for_distance_analysis of this TerritoryManagerDefaultSettings.  # noqa: E501
        :type: int
        """

        self._maximum_nearest_for_distance_analysis = maximum_nearest_for_distance_analysis

    @property
    def spatial_selection_type(self):
        """Gets the spatial_selection_type of this TerritoryManagerDefaultSettings.  # noqa: E501


        :return: The spatial_selection_type of this TerritoryManagerDefaultSettings.  # noqa: E501
        :rtype: TerritoryScenarioSpatialSelectionTypeEnum
        """
        return self._spatial_selection_type

    @spatial_selection_type.setter
    def spatial_selection_type(self, spatial_selection_type):
        """Sets the spatial_selection_type of this TerritoryManagerDefaultSettings.


        :param spatial_selection_type: The spatial_selection_type of this TerritoryManagerDefaultSettings.  # noqa: E501
        :type: TerritoryScenarioSpatialSelectionTypeEnum
        """

        self._spatial_selection_type = spatial_selection_type

    @property
    def zone_themeset_colors(self):
        """Gets the zone_themeset_colors of this TerritoryManagerDefaultSettings.  # noqa: E501


        :return: The zone_themeset_colors of this TerritoryManagerDefaultSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._zone_themeset_colors

    @zone_themeset_colors.setter
    def zone_themeset_colors(self, zone_themeset_colors):
        """Sets the zone_themeset_colors of this TerritoryManagerDefaultSettings.


        :param zone_themeset_colors: The zone_themeset_colors of this TerritoryManagerDefaultSettings.  # noqa: E501
        :type: list[str]
        """

        self._zone_themeset_colors = zone_themeset_colors

    @property
    def mapping_zone_themeset_names(self):
        """Gets the mapping_zone_themeset_names of this TerritoryManagerDefaultSettings.  # noqa: E501


        :return: The mapping_zone_themeset_names of this TerritoryManagerDefaultSettings.  # noqa: E501
        :rtype: str
        """
        return self._mapping_zone_themeset_names

    @mapping_zone_themeset_names.setter
    def mapping_zone_themeset_names(self, mapping_zone_themeset_names):
        """Sets the mapping_zone_themeset_names of this TerritoryManagerDefaultSettings.


        :param mapping_zone_themeset_names: The mapping_zone_themeset_names of this TerritoryManagerDefaultSettings.  # noqa: E501
        :type: str
        """

        self._mapping_zone_themeset_names = mapping_zone_themeset_names

    @property
    def max_zones(self):
        """Gets the max_zones of this TerritoryManagerDefaultSettings.  # noqa: E501


        :return: The max_zones of this TerritoryManagerDefaultSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_zones

    @max_zones.setter
    def max_zones(self, max_zones):
        """Sets the max_zones of this TerritoryManagerDefaultSettings.


        :param max_zones: The max_zones of this TerritoryManagerDefaultSettings.  # noqa: E501
        :type: int
        """

        self._max_zones = max_zones

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
        if issubclass(TerritoryManagerDefaultSettings, dict):
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
        if not isinstance(other, TerritoryManagerDefaultSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
