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

class CreateTerritoryResponse(object):
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
        'did_perform_update': 'bool',
        'conflicts': 'TerritoryUpdateConflicts',
        'changes_to_other_territories': 'ChangesToTerritories',
        'territory_pos': 'TerritoryPosDTO'
    }

    attribute_map = {
        'did_perform_update': 'didPerformUpdate',
        'conflicts': 'conflicts',
        'changes_to_other_territories': 'changesToOtherTerritories',
        'territory_pos': 'territoryPos'
    }

    def __init__(self, did_perform_update=None, conflicts=None, changes_to_other_territories=None, territory_pos=None):  # noqa: E501
        """CreateTerritoryResponse - a model defined in Swagger"""  # noqa: E501
        self._did_perform_update = None
        self._conflicts = None
        self._changes_to_other_territories = None
        self._territory_pos = None
        self.discriminator = None
        if did_perform_update is not None:
            self.did_perform_update = did_perform_update
        if conflicts is not None:
            self.conflicts = conflicts
        if changes_to_other_territories is not None:
            self.changes_to_other_territories = changes_to_other_territories
        if territory_pos is not None:
            self.territory_pos = territory_pos

    @property
    def did_perform_update(self):
        """Gets the did_perform_update of this CreateTerritoryResponse.  # noqa: E501


        :return: The did_perform_update of this CreateTerritoryResponse.  # noqa: E501
        :rtype: bool
        """
        return self._did_perform_update

    @did_perform_update.setter
    def did_perform_update(self, did_perform_update):
        """Sets the did_perform_update of this CreateTerritoryResponse.


        :param did_perform_update: The did_perform_update of this CreateTerritoryResponse.  # noqa: E501
        :type: bool
        """

        self._did_perform_update = did_perform_update

    @property
    def conflicts(self):
        """Gets the conflicts of this CreateTerritoryResponse.  # noqa: E501


        :return: The conflicts of this CreateTerritoryResponse.  # noqa: E501
        :rtype: TerritoryUpdateConflicts
        """
        return self._conflicts

    @conflicts.setter
    def conflicts(self, conflicts):
        """Sets the conflicts of this CreateTerritoryResponse.


        :param conflicts: The conflicts of this CreateTerritoryResponse.  # noqa: E501
        :type: TerritoryUpdateConflicts
        """

        self._conflicts = conflicts

    @property
    def changes_to_other_territories(self):
        """Gets the changes_to_other_territories of this CreateTerritoryResponse.  # noqa: E501


        :return: The changes_to_other_territories of this CreateTerritoryResponse.  # noqa: E501
        :rtype: ChangesToTerritories
        """
        return self._changes_to_other_territories

    @changes_to_other_territories.setter
    def changes_to_other_territories(self, changes_to_other_territories):
        """Sets the changes_to_other_territories of this CreateTerritoryResponse.


        :param changes_to_other_territories: The changes_to_other_territories of this CreateTerritoryResponse.  # noqa: E501
        :type: ChangesToTerritories
        """

        self._changes_to_other_territories = changes_to_other_territories

    @property
    def territory_pos(self):
        """Gets the territory_pos of this CreateTerritoryResponse.  # noqa: E501


        :return: The territory_pos of this CreateTerritoryResponse.  # noqa: E501
        :rtype: TerritoryPosDTO
        """
        return self._territory_pos

    @territory_pos.setter
    def territory_pos(self, territory_pos):
        """Sets the territory_pos of this CreateTerritoryResponse.


        :param territory_pos: The territory_pos of this CreateTerritoryResponse.  # noqa: E501
        :type: TerritoryPosDTO
        """

        self._territory_pos = territory_pos

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
        if issubclass(CreateTerritoryResponse, dict):
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
        if not isinstance(other, CreateTerritoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other