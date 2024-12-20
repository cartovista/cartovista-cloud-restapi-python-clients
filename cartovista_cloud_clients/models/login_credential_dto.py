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

class LoginCredentialDTO(object):
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
        'provider': 'SecurityProvider',
        'provider_name': 'str',
        'username_or_email_address': 'str',
        'token_claims': 'str',
        'password_or_token': 'str',
        're_captcha_response': 'str',
        'keep_me_signed': 'bool',
        'device_id': 'str'
    }

    attribute_map = {
        'provider': 'provider',
        'provider_name': 'providerName',
        'username_or_email_address': 'usernameOrEmailAddress',
        'token_claims': 'tokenClaims',
        'password_or_token': 'passwordOrToken',
        're_captcha_response': 'reCaptchaResponse',
        'keep_me_signed': 'keepMeSigned',
        'device_id': 'deviceId'
    }

    def __init__(self, provider=None, provider_name=None, username_or_email_address=None, token_claims=None, password_or_token=None, re_captcha_response=None, keep_me_signed=None, device_id=None):  # noqa: E501
        """LoginCredentialDTO - a model defined in Swagger"""  # noqa: E501
        self._provider = None
        self._provider_name = None
        self._username_or_email_address = None
        self._token_claims = None
        self._password_or_token = None
        self._re_captcha_response = None
        self._keep_me_signed = None
        self._device_id = None
        self.discriminator = None
        if provider is not None:
            self.provider = provider
        if provider_name is not None:
            self.provider_name = provider_name
        if username_or_email_address is not None:
            self.username_or_email_address = username_or_email_address
        if token_claims is not None:
            self.token_claims = token_claims
        if password_or_token is not None:
            self.password_or_token = password_or_token
        if re_captcha_response is not None:
            self.re_captcha_response = re_captcha_response
        if keep_me_signed is not None:
            self.keep_me_signed = keep_me_signed
        if device_id is not None:
            self.device_id = device_id

    @property
    def provider(self):
        """Gets the provider of this LoginCredentialDTO.  # noqa: E501


        :return: The provider of this LoginCredentialDTO.  # noqa: E501
        :rtype: SecurityProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this LoginCredentialDTO.


        :param provider: The provider of this LoginCredentialDTO.  # noqa: E501
        :type: SecurityProvider
        """

        self._provider = provider

    @property
    def provider_name(self):
        """Gets the provider_name of this LoginCredentialDTO.  # noqa: E501


        :return: The provider_name of this LoginCredentialDTO.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this LoginCredentialDTO.


        :param provider_name: The provider_name of this LoginCredentialDTO.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def username_or_email_address(self):
        """Gets the username_or_email_address of this LoginCredentialDTO.  # noqa: E501


        :return: The username_or_email_address of this LoginCredentialDTO.  # noqa: E501
        :rtype: str
        """
        return self._username_or_email_address

    @username_or_email_address.setter
    def username_or_email_address(self, username_or_email_address):
        """Sets the username_or_email_address of this LoginCredentialDTO.


        :param username_or_email_address: The username_or_email_address of this LoginCredentialDTO.  # noqa: E501
        :type: str
        """

        self._username_or_email_address = username_or_email_address

    @property
    def token_claims(self):
        """Gets the token_claims of this LoginCredentialDTO.  # noqa: E501


        :return: The token_claims of this LoginCredentialDTO.  # noqa: E501
        :rtype: str
        """
        return self._token_claims

    @token_claims.setter
    def token_claims(self, token_claims):
        """Sets the token_claims of this LoginCredentialDTO.


        :param token_claims: The token_claims of this LoginCredentialDTO.  # noqa: E501
        :type: str
        """

        self._token_claims = token_claims

    @property
    def password_or_token(self):
        """Gets the password_or_token of this LoginCredentialDTO.  # noqa: E501


        :return: The password_or_token of this LoginCredentialDTO.  # noqa: E501
        :rtype: str
        """
        return self._password_or_token

    @password_or_token.setter
    def password_or_token(self, password_or_token):
        """Sets the password_or_token of this LoginCredentialDTO.


        :param password_or_token: The password_or_token of this LoginCredentialDTO.  # noqa: E501
        :type: str
        """

        self._password_or_token = password_or_token

    @property
    def re_captcha_response(self):
        """Gets the re_captcha_response of this LoginCredentialDTO.  # noqa: E501


        :return: The re_captcha_response of this LoginCredentialDTO.  # noqa: E501
        :rtype: str
        """
        return self._re_captcha_response

    @re_captcha_response.setter
    def re_captcha_response(self, re_captcha_response):
        """Sets the re_captcha_response of this LoginCredentialDTO.


        :param re_captcha_response: The re_captcha_response of this LoginCredentialDTO.  # noqa: E501
        :type: str
        """

        self._re_captcha_response = re_captcha_response

    @property
    def keep_me_signed(self):
        """Gets the keep_me_signed of this LoginCredentialDTO.  # noqa: E501


        :return: The keep_me_signed of this LoginCredentialDTO.  # noqa: E501
        :rtype: bool
        """
        return self._keep_me_signed

    @keep_me_signed.setter
    def keep_me_signed(self, keep_me_signed):
        """Sets the keep_me_signed of this LoginCredentialDTO.


        :param keep_me_signed: The keep_me_signed of this LoginCredentialDTO.  # noqa: E501
        :type: bool
        """

        self._keep_me_signed = keep_me_signed

    @property
    def device_id(self):
        """Gets the device_id of this LoginCredentialDTO.  # noqa: E501


        :return: The device_id of this LoginCredentialDTO.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this LoginCredentialDTO.


        :param device_id: The device_id of this LoginCredentialDTO.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

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
        if issubclass(LoginCredentialDTO, dict):
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
        if not isinstance(other, LoginCredentialDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
