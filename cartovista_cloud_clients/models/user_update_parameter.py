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

class UserUpdateParameter(object):
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
        'email_address': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'notes': 'str',
        'enabled': 'bool',
        'password': 'str',
        'roles': 'list[PermissionDTO]'
    }

    attribute_map = {
        'email_address': 'emailAddress',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'notes': 'notes',
        'enabled': 'enabled',
        'password': 'password',
        'roles': 'roles'
    }

    def __init__(self, email_address=None, first_name=None, last_name=None, notes=None, enabled=None, password=None, roles=None):  # noqa: E501
        """UserUpdateParameter - a model defined in Swagger"""  # noqa: E501
        self._email_address = None
        self._first_name = None
        self._last_name = None
        self._notes = None
        self._enabled = None
        self._password = None
        self._roles = None
        self.discriminator = None
        if email_address is not None:
            self.email_address = email_address
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if notes is not None:
            self.notes = notes
        if enabled is not None:
            self.enabled = enabled
        if password is not None:
            self.password = password
        if roles is not None:
            self.roles = roles

    @property
    def email_address(self):
        """Gets the email_address of this UserUpdateParameter.  # noqa: E501


        :return: The email_address of this UserUpdateParameter.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UserUpdateParameter.


        :param email_address: The email_address of this UserUpdateParameter.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def first_name(self):
        """Gets the first_name of this UserUpdateParameter.  # noqa: E501


        :return: The first_name of this UserUpdateParameter.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserUpdateParameter.


        :param first_name: The first_name of this UserUpdateParameter.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserUpdateParameter.  # noqa: E501


        :return: The last_name of this UserUpdateParameter.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserUpdateParameter.


        :param last_name: The last_name of this UserUpdateParameter.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def notes(self):
        """Gets the notes of this UserUpdateParameter.  # noqa: E501


        :return: The notes of this UserUpdateParameter.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this UserUpdateParameter.


        :param notes: The notes of this UserUpdateParameter.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def enabled(self):
        """Gets the enabled of this UserUpdateParameter.  # noqa: E501


        :return: The enabled of this UserUpdateParameter.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UserUpdateParameter.


        :param enabled: The enabled of this UserUpdateParameter.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def password(self):
        """Gets the password of this UserUpdateParameter.  # noqa: E501


        :return: The password of this UserUpdateParameter.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserUpdateParameter.


        :param password: The password of this UserUpdateParameter.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def roles(self):
        """Gets the roles of this UserUpdateParameter.  # noqa: E501


        :return: The roles of this UserUpdateParameter.  # noqa: E501
        :rtype: list[PermissionDTO]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserUpdateParameter.


        :param roles: The roles of this UserUpdateParameter.  # noqa: E501
        :type: list[PermissionDTO]
        """

        self._roles = roles

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
        if issubclass(UserUpdateParameter, dict):
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
        if not isinstance(other, UserUpdateParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
