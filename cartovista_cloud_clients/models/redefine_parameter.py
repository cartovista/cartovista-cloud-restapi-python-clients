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

class RedefineParameter(object):
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
        'acknowledged_implantation_conflicts': 'bool',
        'resolutions': 'OneOfRedefineParameterResolutions',
        'longitude': 'float',
        'latitude': 'float',
        'area_by': 'TerritoryAreaByEnum',
        'zones': 'list[CreateTerritoryZoneDTO]',
        'transport_mode': 'TerritoryTransportTypeEnum',
        'mode': 'TerritoryScenarioModeEnum'
    }

    attribute_map = {
        'acknowledged_implantation_conflicts': 'acknowledgedImplantationConflicts',
        'resolutions': 'resolutions',
        'longitude': 'longitude',
        'latitude': 'latitude',
        'area_by': 'areaBy',
        'zones': 'zones',
        'transport_mode': 'transportMode',
        'mode': 'mode'
    }

    def __init__(self, acknowledged_implantation_conflicts=None, resolutions=None, longitude=None, latitude=None, area_by=None, zones=None, transport_mode=None, mode=None):  # noqa: E501
        """RedefineParameter - a model defined in Swagger"""  # noqa: E501
        self._acknowledged_implantation_conflicts = None
        self._resolutions = None
        self._longitude = None
        self._latitude = None
        self._area_by = None
        self._zones = None
        self._transport_mode = None
        self._mode = None
        self.discriminator = None
        if acknowledged_implantation_conflicts is not None:
            self.acknowledged_implantation_conflicts = acknowledged_implantation_conflicts
        if resolutions is not None:
            self.resolutions = resolutions
        if longitude is not None:
            self.longitude = longitude
        if latitude is not None:
            self.latitude = latitude
        if area_by is not None:
            self.area_by = area_by
        if zones is not None:
            self.zones = zones
        if transport_mode is not None:
            self.transport_mode = transport_mode
        if mode is not None:
            self.mode = mode

    @property
    def acknowledged_implantation_conflicts(self):
        """Gets the acknowledged_implantation_conflicts of this RedefineParameter.  # noqa: E501


        :return: The acknowledged_implantation_conflicts of this RedefineParameter.  # noqa: E501
        :rtype: bool
        """
        return self._acknowledged_implantation_conflicts

    @acknowledged_implantation_conflicts.setter
    def acknowledged_implantation_conflicts(self, acknowledged_implantation_conflicts):
        """Sets the acknowledged_implantation_conflicts of this RedefineParameter.


        :param acknowledged_implantation_conflicts: The acknowledged_implantation_conflicts of this RedefineParameter.  # noqa: E501
        :type: bool
        """

        self._acknowledged_implantation_conflicts = acknowledged_implantation_conflicts

    @property
    def resolutions(self):
        """Gets the resolutions of this RedefineParameter.  # noqa: E501


        :return: The resolutions of this RedefineParameter.  # noqa: E501
        :rtype: OneOfRedefineParameterResolutions
        """
        return self._resolutions

    @resolutions.setter
    def resolutions(self, resolutions):
        """Sets the resolutions of this RedefineParameter.


        :param resolutions: The resolutions of this RedefineParameter.  # noqa: E501
        :type: OneOfRedefineParameterResolutions
        """

        self._resolutions = resolutions

    @property
    def longitude(self):
        """Gets the longitude of this RedefineParameter.  # noqa: E501


        :return: The longitude of this RedefineParameter.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this RedefineParameter.


        :param longitude: The longitude of this RedefineParameter.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this RedefineParameter.  # noqa: E501


        :return: The latitude of this RedefineParameter.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this RedefineParameter.


        :param latitude: The latitude of this RedefineParameter.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def area_by(self):
        """Gets the area_by of this RedefineParameter.  # noqa: E501


        :return: The area_by of this RedefineParameter.  # noqa: E501
        :rtype: TerritoryAreaByEnum
        """
        return self._area_by

    @area_by.setter
    def area_by(self, area_by):
        """Sets the area_by of this RedefineParameter.


        :param area_by: The area_by of this RedefineParameter.  # noqa: E501
        :type: TerritoryAreaByEnum
        """

        self._area_by = area_by

    @property
    def zones(self):
        """Gets the zones of this RedefineParameter.  # noqa: E501


        :return: The zones of this RedefineParameter.  # noqa: E501
        :rtype: list[CreateTerritoryZoneDTO]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """Sets the zones of this RedefineParameter.


        :param zones: The zones of this RedefineParameter.  # noqa: E501
        :type: list[CreateTerritoryZoneDTO]
        """

        self._zones = zones

    @property
    def transport_mode(self):
        """Gets the transport_mode of this RedefineParameter.  # noqa: E501


        :return: The transport_mode of this RedefineParameter.  # noqa: E501
        :rtype: TerritoryTransportTypeEnum
        """
        return self._transport_mode

    @transport_mode.setter
    def transport_mode(self, transport_mode):
        """Sets the transport_mode of this RedefineParameter.


        :param transport_mode: The transport_mode of this RedefineParameter.  # noqa: E501
        :type: TerritoryTransportTypeEnum
        """

        self._transport_mode = transport_mode

    @property
    def mode(self):
        """Gets the mode of this RedefineParameter.  # noqa: E501


        :return: The mode of this RedefineParameter.  # noqa: E501
        :rtype: TerritoryScenarioModeEnum
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this RedefineParameter.


        :param mode: The mode of this RedefineParameter.  # noqa: E501
        :type: TerritoryScenarioModeEnum
        """

        self._mode = mode

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
        if issubclass(RedefineParameter, dict):
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
        if not isinstance(other, RedefineParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other