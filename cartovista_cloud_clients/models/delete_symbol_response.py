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

class DeleteSymbolResponse(object):
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
        'did_delete': 'bool',
        'used_in_maps': 'list[str]',
        'used_in_layers': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'did_delete': 'didDelete',
        'used_in_maps': 'usedInMaps',
        'used_in_layers': 'usedInLayers'
    }

    def __init__(self, id=None, did_delete=None, used_in_maps=None, used_in_layers=None):  # noqa: E501
        """DeleteSymbolResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._did_delete = None
        self._used_in_maps = None
        self._used_in_layers = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if did_delete is not None:
            self.did_delete = did_delete
        if used_in_maps is not None:
            self.used_in_maps = used_in_maps
        if used_in_layers is not None:
            self.used_in_layers = used_in_layers

    @property
    def id(self):
        """Gets the id of this DeleteSymbolResponse.  # noqa: E501


        :return: The id of this DeleteSymbolResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteSymbolResponse.


        :param id: The id of this DeleteSymbolResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def did_delete(self):
        """Gets the did_delete of this DeleteSymbolResponse.  # noqa: E501


        :return: The did_delete of this DeleteSymbolResponse.  # noqa: E501
        :rtype: bool
        """
        return self._did_delete

    @did_delete.setter
    def did_delete(self, did_delete):
        """Sets the did_delete of this DeleteSymbolResponse.


        :param did_delete: The did_delete of this DeleteSymbolResponse.  # noqa: E501
        :type: bool
        """

        self._did_delete = did_delete

    @property
    def used_in_maps(self):
        """Gets the used_in_maps of this DeleteSymbolResponse.  # noqa: E501


        :return: The used_in_maps of this DeleteSymbolResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._used_in_maps

    @used_in_maps.setter
    def used_in_maps(self, used_in_maps):
        """Sets the used_in_maps of this DeleteSymbolResponse.


        :param used_in_maps: The used_in_maps of this DeleteSymbolResponse.  # noqa: E501
        :type: list[str]
        """

        self._used_in_maps = used_in_maps

    @property
    def used_in_layers(self):
        """Gets the used_in_layers of this DeleteSymbolResponse.  # noqa: E501


        :return: The used_in_layers of this DeleteSymbolResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._used_in_layers

    @used_in_layers.setter
    def used_in_layers(self, used_in_layers):
        """Sets the used_in_layers of this DeleteSymbolResponse.


        :param used_in_layers: The used_in_layers of this DeleteSymbolResponse.  # noqa: E501
        :type: list[str]
        """

        self._used_in_layers = used_in_layers

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
        if issubclass(DeleteSymbolResponse, dict):
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
        if not isinstance(other, DeleteSymbolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
