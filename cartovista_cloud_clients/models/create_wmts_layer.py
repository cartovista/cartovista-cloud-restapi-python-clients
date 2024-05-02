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

class CreateWmtsLayer(object):
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
        'name': 'str',
        'url': 'str',
        'add_to_map_id': 'str',
        'folder_id': 'str',
        'set_public_access': 'bool',
        'extent': 'OneOfCreateWmtsLayerExtent'
    }

    attribute_map = {
        'name': 'name',
        'url': 'url',
        'add_to_map_id': 'addToMapId',
        'folder_id': 'folderId',
        'set_public_access': 'setPublicAccess',
        'extent': 'extent'
    }

    def __init__(self, name=None, url=None, add_to_map_id=None, folder_id=None, set_public_access=None, extent=None):  # noqa: E501
        """CreateWmtsLayer - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._url = None
        self._add_to_map_id = None
        self._folder_id = None
        self._set_public_access = None
        self._extent = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if add_to_map_id is not None:
            self.add_to_map_id = add_to_map_id
        if folder_id is not None:
            self.folder_id = folder_id
        if set_public_access is not None:
            self.set_public_access = set_public_access
        if extent is not None:
            self.extent = extent

    @property
    def name(self):
        """Gets the name of this CreateWmtsLayer.  # noqa: E501


        :return: The name of this CreateWmtsLayer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateWmtsLayer.


        :param name: The name of this CreateWmtsLayer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this CreateWmtsLayer.  # noqa: E501


        :return: The url of this CreateWmtsLayer.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateWmtsLayer.


        :param url: The url of this CreateWmtsLayer.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def add_to_map_id(self):
        """Gets the add_to_map_id of this CreateWmtsLayer.  # noqa: E501


        :return: The add_to_map_id of this CreateWmtsLayer.  # noqa: E501
        :rtype: str
        """
        return self._add_to_map_id

    @add_to_map_id.setter
    def add_to_map_id(self, add_to_map_id):
        """Sets the add_to_map_id of this CreateWmtsLayer.


        :param add_to_map_id: The add_to_map_id of this CreateWmtsLayer.  # noqa: E501
        :type: str
        """

        self._add_to_map_id = add_to_map_id

    @property
    def folder_id(self):
        """Gets the folder_id of this CreateWmtsLayer.  # noqa: E501


        :return: The folder_id of this CreateWmtsLayer.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this CreateWmtsLayer.


        :param folder_id: The folder_id of this CreateWmtsLayer.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def set_public_access(self):
        """Gets the set_public_access of this CreateWmtsLayer.  # noqa: E501


        :return: The set_public_access of this CreateWmtsLayer.  # noqa: E501
        :rtype: bool
        """
        return self._set_public_access

    @set_public_access.setter
    def set_public_access(self, set_public_access):
        """Sets the set_public_access of this CreateWmtsLayer.


        :param set_public_access: The set_public_access of this CreateWmtsLayer.  # noqa: E501
        :type: bool
        """

        self._set_public_access = set_public_access

    @property
    def extent(self):
        """Gets the extent of this CreateWmtsLayer.  # noqa: E501


        :return: The extent of this CreateWmtsLayer.  # noqa: E501
        :rtype: OneOfCreateWmtsLayerExtent
        """
        return self._extent

    @extent.setter
    def extent(self, extent):
        """Sets the extent of this CreateWmtsLayer.


        :param extent: The extent of this CreateWmtsLayer.  # noqa: E501
        :type: OneOfCreateWmtsLayerExtent
        """

        self._extent = extent

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
        if issubclass(CreateWmtsLayer, dict):
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
        if not isinstance(other, CreateWmtsLayer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
