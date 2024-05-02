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

class GetVectorTileParameters(object):
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
        'quadkeys': 'list[str]',
        'column_ids': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'quadkeys': 'quadkeys',
        'column_ids': 'columnIds'
    }

    def __init__(self, id=None, quadkeys=None, column_ids=None):  # noqa: E501
        """GetVectorTileParameters - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._quadkeys = None
        self._column_ids = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if quadkeys is not None:
            self.quadkeys = quadkeys
        if column_ids is not None:
            self.column_ids = column_ids

    @property
    def id(self):
        """Gets the id of this GetVectorTileParameters.  # noqa: E501


        :return: The id of this GetVectorTileParameters.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetVectorTileParameters.


        :param id: The id of this GetVectorTileParameters.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def quadkeys(self):
        """Gets the quadkeys of this GetVectorTileParameters.  # noqa: E501


        :return: The quadkeys of this GetVectorTileParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._quadkeys

    @quadkeys.setter
    def quadkeys(self, quadkeys):
        """Sets the quadkeys of this GetVectorTileParameters.


        :param quadkeys: The quadkeys of this GetVectorTileParameters.  # noqa: E501
        :type: list[str]
        """

        self._quadkeys = quadkeys

    @property
    def column_ids(self):
        """Gets the column_ids of this GetVectorTileParameters.  # noqa: E501


        :return: The column_ids of this GetVectorTileParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._column_ids

    @column_ids.setter
    def column_ids(self, column_ids):
        """Sets the column_ids of this GetVectorTileParameters.


        :param column_ids: The column_ids of this GetVectorTileParameters.  # noqa: E501
        :type: list[str]
        """

        self._column_ids = column_ids

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
        if issubclass(GetVectorTileParameters, dict):
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
        if not isinstance(other, GetVectorTileParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
