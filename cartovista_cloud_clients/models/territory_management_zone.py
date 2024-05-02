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

class TerritoryManagementZone(object):
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
        'name': 'str',
        'drive_time': 'int',
        'is_implantation_zone': 'bool',
        'id': 'int',
        'type': 'TerritoryZoneTypeEnum'
    }

    attribute_map = {
        'name': 'name',
        'drive_time': 'driveTime',
        'is_implantation_zone': 'isImplantationZone',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, name=None, drive_time=None, is_implantation_zone=None, id=None, type=None):  # noqa: E501
        """TerritoryManagementZone - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._drive_time = None
        self._is_implantation_zone = None
        self._id = None
        self._type = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if drive_time is not None:
            self.drive_time = drive_time
        if is_implantation_zone is not None:
            self.is_implantation_zone = is_implantation_zone
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this TerritoryManagementZone.  # noqa: E501


        :return: The name of this TerritoryManagementZone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TerritoryManagementZone.


        :param name: The name of this TerritoryManagementZone.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def drive_time(self):
        """Gets the drive_time of this TerritoryManagementZone.  # noqa: E501


        :return: The drive_time of this TerritoryManagementZone.  # noqa: E501
        :rtype: int
        """
        return self._drive_time

    @drive_time.setter
    def drive_time(self, drive_time):
        """Sets the drive_time of this TerritoryManagementZone.


        :param drive_time: The drive_time of this TerritoryManagementZone.  # noqa: E501
        :type: int
        """

        self._drive_time = drive_time

    @property
    def is_implantation_zone(self):
        """Gets the is_implantation_zone of this TerritoryManagementZone.  # noqa: E501


        :return: The is_implantation_zone of this TerritoryManagementZone.  # noqa: E501
        :rtype: bool
        """
        return self._is_implantation_zone

    @is_implantation_zone.setter
    def is_implantation_zone(self, is_implantation_zone):
        """Sets the is_implantation_zone of this TerritoryManagementZone.


        :param is_implantation_zone: The is_implantation_zone of this TerritoryManagementZone.  # noqa: E501
        :type: bool
        """

        self._is_implantation_zone = is_implantation_zone

    @property
    def id(self):
        """Gets the id of this TerritoryManagementZone.  # noqa: E501


        :return: The id of this TerritoryManagementZone.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TerritoryManagementZone.


        :param id: The id of this TerritoryManagementZone.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this TerritoryManagementZone.  # noqa: E501


        :return: The type of this TerritoryManagementZone.  # noqa: E501
        :rtype: TerritoryZoneTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TerritoryManagementZone.


        :param type: The type of this TerritoryManagementZone.  # noqa: E501
        :type: TerritoryZoneTypeEnum
        """

        self._type = type

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
        if issubclass(TerritoryManagementZone, dict):
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
        if not isinstance(other, TerritoryManagementZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
