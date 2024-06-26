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

class ConfirmInvitationParameter(object):
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
        'user_id': 'str',
        'invitation_code': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'provider': 'SecurityProvider',
        'provider_id': 'str',
        'email': 'str',
        'password': 'str'
    }

    attribute_map = {
        'user_id': 'userId',
        'invitation_code': 'invitationCode',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'provider': 'provider',
        'provider_id': 'providerId',
        'email': 'email',
        'password': 'password'
    }

    def __init__(self, user_id=None, invitation_code=None, first_name=None, last_name=None, provider=None, provider_id=None, email=None, password=None):  # noqa: E501
        """ConfirmInvitationParameter - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._invitation_code = None
        self._first_name = None
        self._last_name = None
        self._provider = None
        self._provider_id = None
        self._email = None
        self._password = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if invitation_code is not None:
            self.invitation_code = invitation_code
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if provider is not None:
            self.provider = provider
        if provider_id is not None:
            self.provider_id = provider_id
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password

    @property
    def user_id(self):
        """Gets the user_id of this ConfirmInvitationParameter.  # noqa: E501


        :return: The user_id of this ConfirmInvitationParameter.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ConfirmInvitationParameter.


        :param user_id: The user_id of this ConfirmInvitationParameter.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def invitation_code(self):
        """Gets the invitation_code of this ConfirmInvitationParameter.  # noqa: E501


        :return: The invitation_code of this ConfirmInvitationParameter.  # noqa: E501
        :rtype: str
        """
        return self._invitation_code

    @invitation_code.setter
    def invitation_code(self, invitation_code):
        """Sets the invitation_code of this ConfirmInvitationParameter.


        :param invitation_code: The invitation_code of this ConfirmInvitationParameter.  # noqa: E501
        :type: str
        """

        self._invitation_code = invitation_code

    @property
    def first_name(self):
        """Gets the first_name of this ConfirmInvitationParameter.  # noqa: E501


        :return: The first_name of this ConfirmInvitationParameter.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ConfirmInvitationParameter.


        :param first_name: The first_name of this ConfirmInvitationParameter.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ConfirmInvitationParameter.  # noqa: E501


        :return: The last_name of this ConfirmInvitationParameter.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ConfirmInvitationParameter.


        :param last_name: The last_name of this ConfirmInvitationParameter.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def provider(self):
        """Gets the provider of this ConfirmInvitationParameter.  # noqa: E501


        :return: The provider of this ConfirmInvitationParameter.  # noqa: E501
        :rtype: SecurityProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ConfirmInvitationParameter.


        :param provider: The provider of this ConfirmInvitationParameter.  # noqa: E501
        :type: SecurityProvider
        """

        self._provider = provider

    @property
    def provider_id(self):
        """Gets the provider_id of this ConfirmInvitationParameter.  # noqa: E501


        :return: The provider_id of this ConfirmInvitationParameter.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this ConfirmInvitationParameter.


        :param provider_id: The provider_id of this ConfirmInvitationParameter.  # noqa: E501
        :type: str
        """

        self._provider_id = provider_id

    @property
    def email(self):
        """Gets the email of this ConfirmInvitationParameter.  # noqa: E501


        :return: The email of this ConfirmInvitationParameter.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ConfirmInvitationParameter.


        :param email: The email of this ConfirmInvitationParameter.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def password(self):
        """Gets the password of this ConfirmInvitationParameter.  # noqa: E501


        :return: The password of this ConfirmInvitationParameter.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ConfirmInvitationParameter.


        :param password: The password of this ConfirmInvitationParameter.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(ConfirmInvitationParameter, dict):
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
        if not isinstance(other, ConfirmInvitationParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
