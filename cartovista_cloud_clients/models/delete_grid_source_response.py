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

class DeleteGridSourceResponse(object):
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
        'grid_layer_id': 'str',
        'name': 'str',
        'type': 'GridLayerTypeEnum',
        'did_delete': 'bool',
        'used_in_maps': 'list[SimpleMap]'
    }

    attribute_map = {
        'id': 'id',
        'grid_layer_id': 'gridLayerId',
        'name': 'name',
        'type': 'type',
        'did_delete': 'didDelete',
        'used_in_maps': 'usedInMaps'
    }

    def __init__(self, id=None, grid_layer_id=None, name=None, type=None, did_delete=None, used_in_maps=None):  # noqa: E501
        """DeleteGridSourceResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._grid_layer_id = None
        self._name = None
        self._type = None
        self._did_delete = None
        self._used_in_maps = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if grid_layer_id is not None:
            self.grid_layer_id = grid_layer_id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if did_delete is not None:
            self.did_delete = did_delete
        if used_in_maps is not None:
            self.used_in_maps = used_in_maps

    @property
    def id(self):
        """Gets the id of this DeleteGridSourceResponse.  # noqa: E501


        :return: The id of this DeleteGridSourceResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteGridSourceResponse.


        :param id: The id of this DeleteGridSourceResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def grid_layer_id(self):
        """Gets the grid_layer_id of this DeleteGridSourceResponse.  # noqa: E501


        :return: The grid_layer_id of this DeleteGridSourceResponse.  # noqa: E501
        :rtype: str
        """
        return self._grid_layer_id

    @grid_layer_id.setter
    def grid_layer_id(self, grid_layer_id):
        """Sets the grid_layer_id of this DeleteGridSourceResponse.


        :param grid_layer_id: The grid_layer_id of this DeleteGridSourceResponse.  # noqa: E501
        :type: str
        """

        self._grid_layer_id = grid_layer_id

    @property
    def name(self):
        """Gets the name of this DeleteGridSourceResponse.  # noqa: E501


        :return: The name of this DeleteGridSourceResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeleteGridSourceResponse.


        :param name: The name of this DeleteGridSourceResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this DeleteGridSourceResponse.  # noqa: E501


        :return: The type of this DeleteGridSourceResponse.  # noqa: E501
        :rtype: GridLayerTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeleteGridSourceResponse.


        :param type: The type of this DeleteGridSourceResponse.  # noqa: E501
        :type: GridLayerTypeEnum
        """

        self._type = type

    @property
    def did_delete(self):
        """Gets the did_delete of this DeleteGridSourceResponse.  # noqa: E501


        :return: The did_delete of this DeleteGridSourceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._did_delete

    @did_delete.setter
    def did_delete(self, did_delete):
        """Sets the did_delete of this DeleteGridSourceResponse.


        :param did_delete: The did_delete of this DeleteGridSourceResponse.  # noqa: E501
        :type: bool
        """

        self._did_delete = did_delete

    @property
    def used_in_maps(self):
        """Gets the used_in_maps of this DeleteGridSourceResponse.  # noqa: E501


        :return: The used_in_maps of this DeleteGridSourceResponse.  # noqa: E501
        :rtype: list[SimpleMap]
        """
        return self._used_in_maps

    @used_in_maps.setter
    def used_in_maps(self, used_in_maps):
        """Sets the used_in_maps of this DeleteGridSourceResponse.


        :param used_in_maps: The used_in_maps of this DeleteGridSourceResponse.  # noqa: E501
        :type: list[SimpleMap]
        """

        self._used_in_maps = used_in_maps

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
        if issubclass(DeleteGridSourceResponse, dict):
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
        if not isinstance(other, DeleteGridSourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
