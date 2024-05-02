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

class UpdateTerritoryPosExclusivityParameter(object):
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
        'resolutions': 'OneOfUpdateTerritoryPosExclusivityParameterResolutions',
        'exclusive_zone_id': 'int',
        'is_implantation_block_exclusive': 'bool'
    }

    attribute_map = {
        'acknowledged_implantation_conflicts': 'acknowledgedImplantationConflicts',
        'resolutions': 'resolutions',
        'exclusive_zone_id': 'exclusiveZoneId',
        'is_implantation_block_exclusive': 'isImplantationBlockExclusive'
    }

    def __init__(self, acknowledged_implantation_conflicts=None, resolutions=None, exclusive_zone_id=None, is_implantation_block_exclusive=None):  # noqa: E501
        """UpdateTerritoryPosExclusivityParameter - a model defined in Swagger"""  # noqa: E501
        self._acknowledged_implantation_conflicts = None
        self._resolutions = None
        self._exclusive_zone_id = None
        self._is_implantation_block_exclusive = None
        self.discriminator = None
        if acknowledged_implantation_conflicts is not None:
            self.acknowledged_implantation_conflicts = acknowledged_implantation_conflicts
        if resolutions is not None:
            self.resolutions = resolutions
        if exclusive_zone_id is not None:
            self.exclusive_zone_id = exclusive_zone_id
        if is_implantation_block_exclusive is not None:
            self.is_implantation_block_exclusive = is_implantation_block_exclusive

    @property
    def acknowledged_implantation_conflicts(self):
        """Gets the acknowledged_implantation_conflicts of this UpdateTerritoryPosExclusivityParameter.  # noqa: E501


        :return: The acknowledged_implantation_conflicts of this UpdateTerritoryPosExclusivityParameter.  # noqa: E501
        :rtype: bool
        """
        return self._acknowledged_implantation_conflicts

    @acknowledged_implantation_conflicts.setter
    def acknowledged_implantation_conflicts(self, acknowledged_implantation_conflicts):
        """Sets the acknowledged_implantation_conflicts of this UpdateTerritoryPosExclusivityParameter.


        :param acknowledged_implantation_conflicts: The acknowledged_implantation_conflicts of this UpdateTerritoryPosExclusivityParameter.  # noqa: E501
        :type: bool
        """

        self._acknowledged_implantation_conflicts = acknowledged_implantation_conflicts

    @property
    def resolutions(self):
        """Gets the resolutions of this UpdateTerritoryPosExclusivityParameter.  # noqa: E501


        :return: The resolutions of this UpdateTerritoryPosExclusivityParameter.  # noqa: E501
        :rtype: OneOfUpdateTerritoryPosExclusivityParameterResolutions
        """
        return self._resolutions

    @resolutions.setter
    def resolutions(self, resolutions):
        """Sets the resolutions of this UpdateTerritoryPosExclusivityParameter.


        :param resolutions: The resolutions of this UpdateTerritoryPosExclusivityParameter.  # noqa: E501
        :type: OneOfUpdateTerritoryPosExclusivityParameterResolutions
        """

        self._resolutions = resolutions

    @property
    def exclusive_zone_id(self):
        """Gets the exclusive_zone_id of this UpdateTerritoryPosExclusivityParameter.  # noqa: E501


        :return: The exclusive_zone_id of this UpdateTerritoryPosExclusivityParameter.  # noqa: E501
        :rtype: int
        """
        return self._exclusive_zone_id

    @exclusive_zone_id.setter
    def exclusive_zone_id(self, exclusive_zone_id):
        """Sets the exclusive_zone_id of this UpdateTerritoryPosExclusivityParameter.


        :param exclusive_zone_id: The exclusive_zone_id of this UpdateTerritoryPosExclusivityParameter.  # noqa: E501
        :type: int
        """

        self._exclusive_zone_id = exclusive_zone_id

    @property
    def is_implantation_block_exclusive(self):
        """Gets the is_implantation_block_exclusive of this UpdateTerritoryPosExclusivityParameter.  # noqa: E501


        :return: The is_implantation_block_exclusive of this UpdateTerritoryPosExclusivityParameter.  # noqa: E501
        :rtype: bool
        """
        return self._is_implantation_block_exclusive

    @is_implantation_block_exclusive.setter
    def is_implantation_block_exclusive(self, is_implantation_block_exclusive):
        """Sets the is_implantation_block_exclusive of this UpdateTerritoryPosExclusivityParameter.


        :param is_implantation_block_exclusive: The is_implantation_block_exclusive of this UpdateTerritoryPosExclusivityParameter.  # noqa: E501
        :type: bool
        """

        self._is_implantation_block_exclusive = is_implantation_block_exclusive

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
        if issubclass(UpdateTerritoryPosExclusivityParameter, dict):
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
        if not isinstance(other, UpdateTerritoryPosExclusivityParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
