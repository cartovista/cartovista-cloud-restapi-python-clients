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

class ThumbnailLink(object):
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
        'url': 'str',
        'expiry_date': 'datetime'
    }

    attribute_map = {
        'url': 'url',
        'expiry_date': 'expiryDate'
    }

    def __init__(self, url=None, expiry_date=None):  # noqa: E501
        """ThumbnailLink - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._expiry_date = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if expiry_date is not None:
            self.expiry_date = expiry_date

    @property
    def url(self):
        """Gets the url of this ThumbnailLink.  # noqa: E501


        :return: The url of this ThumbnailLink.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ThumbnailLink.


        :param url: The url of this ThumbnailLink.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def expiry_date(self):
        """Gets the expiry_date of this ThumbnailLink.  # noqa: E501


        :return: The expiry_date of this ThumbnailLink.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this ThumbnailLink.


        :param expiry_date: The expiry_date of this ThumbnailLink.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

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
        if issubclass(ThumbnailLink, dict):
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
        if not isinstance(other, ThumbnailLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other