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

class PermissionPairDTO(object):
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
        'permission': 'PermissionDTO',
        'secure_object_id': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'permission': 'permission',
        'secure_object_id': 'secureObjectId',
        'user_id': 'userId'
    }

    def __init__(self, permission=None, secure_object_id=None, user_id=None):  # noqa: E501
        """PermissionPairDTO - a model defined in Swagger"""  # noqa: E501
        self._permission = None
        self._secure_object_id = None
        self._user_id = None
        self.discriminator = None
        if permission is not None:
            self.permission = permission
        if secure_object_id is not None:
            self.secure_object_id = secure_object_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def permission(self):
        """Gets the permission of this PermissionPairDTO.  # noqa: E501


        :return: The permission of this PermissionPairDTO.  # noqa: E501
        :rtype: PermissionDTO
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this PermissionPairDTO.


        :param permission: The permission of this PermissionPairDTO.  # noqa: E501
        :type: PermissionDTO
        """

        self._permission = permission

    @property
    def secure_object_id(self):
        """Gets the secure_object_id of this PermissionPairDTO.  # noqa: E501


        :return: The secure_object_id of this PermissionPairDTO.  # noqa: E501
        :rtype: str
        """
        return self._secure_object_id

    @secure_object_id.setter
    def secure_object_id(self, secure_object_id):
        """Sets the secure_object_id of this PermissionPairDTO.


        :param secure_object_id: The secure_object_id of this PermissionPairDTO.  # noqa: E501
        :type: str
        """

        self._secure_object_id = secure_object_id

    @property
    def user_id(self):
        """Gets the user_id of this PermissionPairDTO.  # noqa: E501


        :return: The user_id of this PermissionPairDTO.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PermissionPairDTO.


        :param user_id: The user_id of this PermissionPairDTO.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(PermissionPairDTO, dict):
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
        if not isinstance(other, PermissionPairDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
