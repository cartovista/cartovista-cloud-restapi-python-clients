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

class ScenarioDTO(object):
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
        'map_id': 'str',
        'name': 'str',
        'user_name': 'str',
        'user_display_name': 'str',
        'author_username': 'str',
        'last_date': 'datetime',
        'territories_pos': 'list[TerritoryPosDTO]',
        'scenario_configuration': 'ScenarioConfiguration',
        'scenario_permission': 'ScenarioPermissionDTO',
        'settings': 'TerritoryManagerSettings'
    }

    attribute_map = {
        'id': 'id',
        'map_id': 'mapId',
        'name': 'name',
        'user_name': 'userName',
        'user_display_name': 'userDisplayName',
        'author_username': 'authorUsername',
        'last_date': 'lastDate',
        'territories_pos': 'territoriesPos',
        'scenario_configuration': 'scenarioConfiguration',
        'scenario_permission': 'scenarioPermission',
        'settings': 'settings'
    }

    def __init__(self, id=None, map_id=None, name=None, user_name=None, user_display_name=None, author_username=None, last_date=None, territories_pos=None, scenario_configuration=None, scenario_permission=None, settings=None):  # noqa: E501
        """ScenarioDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._map_id = None
        self._name = None
        self._user_name = None
        self._user_display_name = None
        self._author_username = None
        self._last_date = None
        self._territories_pos = None
        self._scenario_configuration = None
        self._scenario_permission = None
        self._settings = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if map_id is not None:
            self.map_id = map_id
        if name is not None:
            self.name = name
        if user_name is not None:
            self.user_name = user_name
        if user_display_name is not None:
            self.user_display_name = user_display_name
        if author_username is not None:
            self.author_username = author_username
        if last_date is not None:
            self.last_date = last_date
        if territories_pos is not None:
            self.territories_pos = territories_pos
        if scenario_configuration is not None:
            self.scenario_configuration = scenario_configuration
        if scenario_permission is not None:
            self.scenario_permission = scenario_permission
        if settings is not None:
            self.settings = settings

    @property
    def id(self):
        """Gets the id of this ScenarioDTO.  # noqa: E501


        :return: The id of this ScenarioDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScenarioDTO.


        :param id: The id of this ScenarioDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def map_id(self):
        """Gets the map_id of this ScenarioDTO.  # noqa: E501


        :return: The map_id of this ScenarioDTO.  # noqa: E501
        :rtype: str
        """
        return self._map_id

    @map_id.setter
    def map_id(self, map_id):
        """Sets the map_id of this ScenarioDTO.


        :param map_id: The map_id of this ScenarioDTO.  # noqa: E501
        :type: str
        """

        self._map_id = map_id

    @property
    def name(self):
        """Gets the name of this ScenarioDTO.  # noqa: E501


        :return: The name of this ScenarioDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScenarioDTO.


        :param name: The name of this ScenarioDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def user_name(self):
        """Gets the user_name of this ScenarioDTO.  # noqa: E501


        :return: The user_name of this ScenarioDTO.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ScenarioDTO.


        :param user_name: The user_name of this ScenarioDTO.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def user_display_name(self):
        """Gets the user_display_name of this ScenarioDTO.  # noqa: E501


        :return: The user_display_name of this ScenarioDTO.  # noqa: E501
        :rtype: str
        """
        return self._user_display_name

    @user_display_name.setter
    def user_display_name(self, user_display_name):
        """Sets the user_display_name of this ScenarioDTO.


        :param user_display_name: The user_display_name of this ScenarioDTO.  # noqa: E501
        :type: str
        """

        self._user_display_name = user_display_name

    @property
    def author_username(self):
        """Gets the author_username of this ScenarioDTO.  # noqa: E501


        :return: The author_username of this ScenarioDTO.  # noqa: E501
        :rtype: str
        """
        return self._author_username

    @author_username.setter
    def author_username(self, author_username):
        """Sets the author_username of this ScenarioDTO.


        :param author_username: The author_username of this ScenarioDTO.  # noqa: E501
        :type: str
        """

        self._author_username = author_username

    @property
    def last_date(self):
        """Gets the last_date of this ScenarioDTO.  # noqa: E501


        :return: The last_date of this ScenarioDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_date

    @last_date.setter
    def last_date(self, last_date):
        """Sets the last_date of this ScenarioDTO.


        :param last_date: The last_date of this ScenarioDTO.  # noqa: E501
        :type: datetime
        """

        self._last_date = last_date

    @property
    def territories_pos(self):
        """Gets the territories_pos of this ScenarioDTO.  # noqa: E501


        :return: The territories_pos of this ScenarioDTO.  # noqa: E501
        :rtype: list[TerritoryPosDTO]
        """
        return self._territories_pos

    @territories_pos.setter
    def territories_pos(self, territories_pos):
        """Sets the territories_pos of this ScenarioDTO.


        :param territories_pos: The territories_pos of this ScenarioDTO.  # noqa: E501
        :type: list[TerritoryPosDTO]
        """

        self._territories_pos = territories_pos

    @property
    def scenario_configuration(self):
        """Gets the scenario_configuration of this ScenarioDTO.  # noqa: E501


        :return: The scenario_configuration of this ScenarioDTO.  # noqa: E501
        :rtype: ScenarioConfiguration
        """
        return self._scenario_configuration

    @scenario_configuration.setter
    def scenario_configuration(self, scenario_configuration):
        """Sets the scenario_configuration of this ScenarioDTO.


        :param scenario_configuration: The scenario_configuration of this ScenarioDTO.  # noqa: E501
        :type: ScenarioConfiguration
        """

        self._scenario_configuration = scenario_configuration

    @property
    def scenario_permission(self):
        """Gets the scenario_permission of this ScenarioDTO.  # noqa: E501


        :return: The scenario_permission of this ScenarioDTO.  # noqa: E501
        :rtype: ScenarioPermissionDTO
        """
        return self._scenario_permission

    @scenario_permission.setter
    def scenario_permission(self, scenario_permission):
        """Sets the scenario_permission of this ScenarioDTO.


        :param scenario_permission: The scenario_permission of this ScenarioDTO.  # noqa: E501
        :type: ScenarioPermissionDTO
        """

        self._scenario_permission = scenario_permission

    @property
    def settings(self):
        """Gets the settings of this ScenarioDTO.  # noqa: E501


        :return: The settings of this ScenarioDTO.  # noqa: E501
        :rtype: TerritoryManagerSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this ScenarioDTO.


        :param settings: The settings of this ScenarioDTO.  # noqa: E501
        :type: TerritoryManagerSettings
        """

        self._settings = settings

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
        if issubclass(ScenarioDTO, dict):
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
        if not isinstance(other, ScenarioDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other