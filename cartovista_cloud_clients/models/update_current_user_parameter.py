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

class UpdateCurrentUserParameter(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'email_address': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email_address': 'emailAddress'
    }

    def __init__(self, first_name=None, last_name=None, email_address=None):  # noqa: E501
        """UpdateCurrentUserParameter - a model defined in Swagger"""  # noqa: E501
        self._first_name = None
        self._last_name = None
        self._email_address = None
        self.discriminator = None
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email_address is not None:
            self.email_address = email_address

    @property
    def first_name(self):
        """Gets the first_name of this UpdateCurrentUserParameter.  # noqa: E501


        :return: The first_name of this UpdateCurrentUserParameter.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UpdateCurrentUserParameter.


        :param first_name: The first_name of this UpdateCurrentUserParameter.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UpdateCurrentUserParameter.  # noqa: E501


        :return: The last_name of this UpdateCurrentUserParameter.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UpdateCurrentUserParameter.


        :param last_name: The last_name of this UpdateCurrentUserParameter.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email_address(self):
        """Gets the email_address of this UpdateCurrentUserParameter.  # noqa: E501


        :return: The email_address of this UpdateCurrentUserParameter.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UpdateCurrentUserParameter.


        :param email_address: The email_address of this UpdateCurrentUserParameter.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

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
        if issubclass(UpdateCurrentUserParameter, dict):
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
        if not isinstance(other, UpdateCurrentUserParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
