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

class TerritoryManagerSummary(object):
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
        'blocks_id': 'str',
        'points_id': 'str',
        'territories_id': 'str',
        'blocks_name': 'str',
        'points_name': 'str',
        'territories_name': 'str',
        'settings': 'TerritoryManagerSettings',
        'ground_units': 'str',
        'urbanicity_candidate_columns': 'list[DataTableColumnDTO]'
    }

    attribute_map = {
        'id': 'id',
        'blocks_id': 'blocksId',
        'points_id': 'pointsId',
        'territories_id': 'territoriesId',
        'blocks_name': 'blocksName',
        'points_name': 'pointsName',
        'territories_name': 'territoriesName',
        'settings': 'settings',
        'ground_units': 'groundUnits',
        'urbanicity_candidate_columns': 'urbanicityCandidateColumns'
    }

    def __init__(self, id=None, blocks_id=None, points_id=None, territories_id=None, blocks_name=None, points_name=None, territories_name=None, settings=None, ground_units=None, urbanicity_candidate_columns=None):  # noqa: E501
        """TerritoryManagerSummary - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._blocks_id = None
        self._points_id = None
        self._territories_id = None
        self._blocks_name = None
        self._points_name = None
        self._territories_name = None
        self._settings = None
        self._ground_units = None
        self._urbanicity_candidate_columns = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if blocks_id is not None:
            self.blocks_id = blocks_id
        if points_id is not None:
            self.points_id = points_id
        if territories_id is not None:
            self.territories_id = territories_id
        if blocks_name is not None:
            self.blocks_name = blocks_name
        if points_name is not None:
            self.points_name = points_name
        if territories_name is not None:
            self.territories_name = territories_name
        if settings is not None:
            self.settings = settings
        if ground_units is not None:
            self.ground_units = ground_units
        if urbanicity_candidate_columns is not None:
            self.urbanicity_candidate_columns = urbanicity_candidate_columns

    @property
    def id(self):
        """Gets the id of this TerritoryManagerSummary.  # noqa: E501


        :return: The id of this TerritoryManagerSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TerritoryManagerSummary.


        :param id: The id of this TerritoryManagerSummary.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def blocks_id(self):
        """Gets the blocks_id of this TerritoryManagerSummary.  # noqa: E501


        :return: The blocks_id of this TerritoryManagerSummary.  # noqa: E501
        :rtype: str
        """
        return self._blocks_id

    @blocks_id.setter
    def blocks_id(self, blocks_id):
        """Sets the blocks_id of this TerritoryManagerSummary.


        :param blocks_id: The blocks_id of this TerritoryManagerSummary.  # noqa: E501
        :type: str
        """

        self._blocks_id = blocks_id

    @property
    def points_id(self):
        """Gets the points_id of this TerritoryManagerSummary.  # noqa: E501


        :return: The points_id of this TerritoryManagerSummary.  # noqa: E501
        :rtype: str
        """
        return self._points_id

    @points_id.setter
    def points_id(self, points_id):
        """Sets the points_id of this TerritoryManagerSummary.


        :param points_id: The points_id of this TerritoryManagerSummary.  # noqa: E501
        :type: str
        """

        self._points_id = points_id

    @property
    def territories_id(self):
        """Gets the territories_id of this TerritoryManagerSummary.  # noqa: E501


        :return: The territories_id of this TerritoryManagerSummary.  # noqa: E501
        :rtype: str
        """
        return self._territories_id

    @territories_id.setter
    def territories_id(self, territories_id):
        """Sets the territories_id of this TerritoryManagerSummary.


        :param territories_id: The territories_id of this TerritoryManagerSummary.  # noqa: E501
        :type: str
        """

        self._territories_id = territories_id

    @property
    def blocks_name(self):
        """Gets the blocks_name of this TerritoryManagerSummary.  # noqa: E501


        :return: The blocks_name of this TerritoryManagerSummary.  # noqa: E501
        :rtype: str
        """
        return self._blocks_name

    @blocks_name.setter
    def blocks_name(self, blocks_name):
        """Sets the blocks_name of this TerritoryManagerSummary.


        :param blocks_name: The blocks_name of this TerritoryManagerSummary.  # noqa: E501
        :type: str
        """

        self._blocks_name = blocks_name

    @property
    def points_name(self):
        """Gets the points_name of this TerritoryManagerSummary.  # noqa: E501


        :return: The points_name of this TerritoryManagerSummary.  # noqa: E501
        :rtype: str
        """
        return self._points_name

    @points_name.setter
    def points_name(self, points_name):
        """Sets the points_name of this TerritoryManagerSummary.


        :param points_name: The points_name of this TerritoryManagerSummary.  # noqa: E501
        :type: str
        """

        self._points_name = points_name

    @property
    def territories_name(self):
        """Gets the territories_name of this TerritoryManagerSummary.  # noqa: E501


        :return: The territories_name of this TerritoryManagerSummary.  # noqa: E501
        :rtype: str
        """
        return self._territories_name

    @territories_name.setter
    def territories_name(self, territories_name):
        """Sets the territories_name of this TerritoryManagerSummary.


        :param territories_name: The territories_name of this TerritoryManagerSummary.  # noqa: E501
        :type: str
        """

        self._territories_name = territories_name

    @property
    def settings(self):
        """Gets the settings of this TerritoryManagerSummary.  # noqa: E501


        :return: The settings of this TerritoryManagerSummary.  # noqa: E501
        :rtype: TerritoryManagerSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this TerritoryManagerSummary.


        :param settings: The settings of this TerritoryManagerSummary.  # noqa: E501
        :type: TerritoryManagerSettings
        """

        self._settings = settings

    @property
    def ground_units(self):
        """Gets the ground_units of this TerritoryManagerSummary.  # noqa: E501


        :return: The ground_units of this TerritoryManagerSummary.  # noqa: E501
        :rtype: str
        """
        return self._ground_units

    @ground_units.setter
    def ground_units(self, ground_units):
        """Sets the ground_units of this TerritoryManagerSummary.


        :param ground_units: The ground_units of this TerritoryManagerSummary.  # noqa: E501
        :type: str
        """

        self._ground_units = ground_units

    @property
    def urbanicity_candidate_columns(self):
        """Gets the urbanicity_candidate_columns of this TerritoryManagerSummary.  # noqa: E501


        :return: The urbanicity_candidate_columns of this TerritoryManagerSummary.  # noqa: E501
        :rtype: list[DataTableColumnDTO]
        """
        return self._urbanicity_candidate_columns

    @urbanicity_candidate_columns.setter
    def urbanicity_candidate_columns(self, urbanicity_candidate_columns):
        """Sets the urbanicity_candidate_columns of this TerritoryManagerSummary.


        :param urbanicity_candidate_columns: The urbanicity_candidate_columns of this TerritoryManagerSummary.  # noqa: E501
        :type: list[DataTableColumnDTO]
        """

        self._urbanicity_candidate_columns = urbanicity_candidate_columns

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
        if issubclass(TerritoryManagerSummary, dict):
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
        if not isinstance(other, TerritoryManagerSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other