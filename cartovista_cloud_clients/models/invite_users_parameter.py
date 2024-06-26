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

class InviteUsersParameter(object):
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
        'emails': 'list[str]',
        'role': 'OneOfInviteUsersParameterRole',
        'group_ids': 'list[str]'
    }

    attribute_map = {
        'emails': 'emails',
        'role': 'role',
        'group_ids': 'groupIds'
    }

    def __init__(self, emails=None, role=None, group_ids=None):  # noqa: E501
        """InviteUsersParameter - a model defined in Swagger"""  # noqa: E501
        self._emails = None
        self._role = None
        self._group_ids = None
        self.discriminator = None
        if emails is not None:
            self.emails = emails
        if role is not None:
            self.role = role
        if group_ids is not None:
            self.group_ids = group_ids

    @property
    def emails(self):
        """Gets the emails of this InviteUsersParameter.  # noqa: E501


        :return: The emails of this InviteUsersParameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this InviteUsersParameter.


        :param emails: The emails of this InviteUsersParameter.  # noqa: E501
        :type: list[str]
        """

        self._emails = emails

    @property
    def role(self):
        """Gets the role of this InviteUsersParameter.  # noqa: E501


        :return: The role of this InviteUsersParameter.  # noqa: E501
        :rtype: OneOfInviteUsersParameterRole
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this InviteUsersParameter.


        :param role: The role of this InviteUsersParameter.  # noqa: E501
        :type: OneOfInviteUsersParameterRole
        """

        self._role = role

    @property
    def group_ids(self):
        """Gets the group_ids of this InviteUsersParameter.  # noqa: E501


        :return: The group_ids of this InviteUsersParameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this InviteUsersParameter.


        :param group_ids: The group_ids of this InviteUsersParameter.  # noqa: E501
        :type: list[str]
        """

        self._group_ids = group_ids

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
        if issubclass(InviteUsersParameter, dict):
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
        if not isinstance(other, InviteUsersParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
