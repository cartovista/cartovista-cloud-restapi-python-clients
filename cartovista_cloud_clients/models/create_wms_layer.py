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

class CreateWmsLayer(object):
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
        'layer_names': 'list[str]',
        'extent': 'OneOfCreateWmsLayerExtent',
        'get_legend_url': 'str',
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'url': 'url',
        'add_to_map_id': 'addToMapId',
        'folder_id': 'folderId',
        'set_public_access': 'setPublicAccess',
        'layer_names': 'layerNames',
        'extent': 'extent',
        'get_legend_url': 'getLegendUrl',
        'version': 'version'
    }

    def __init__(self, name=None, url=None, add_to_map_id=None, folder_id=None, set_public_access=None, layer_names=None, extent=None, get_legend_url=None, version=None):  # noqa: E501
        """CreateWmsLayer - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._url = None
        self._add_to_map_id = None
        self._folder_id = None
        self._set_public_access = None
        self._layer_names = None
        self._extent = None
        self._get_legend_url = None
        self._version = None
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
        if layer_names is not None:
            self.layer_names = layer_names
        if extent is not None:
            self.extent = extent
        if get_legend_url is not None:
            self.get_legend_url = get_legend_url
        if version is not None:
            self.version = version

    @property
    def name(self):
        """Gets the name of this CreateWmsLayer.  # noqa: E501


        :return: The name of this CreateWmsLayer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateWmsLayer.


        :param name: The name of this CreateWmsLayer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this CreateWmsLayer.  # noqa: E501


        :return: The url of this CreateWmsLayer.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateWmsLayer.


        :param url: The url of this CreateWmsLayer.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def add_to_map_id(self):
        """Gets the add_to_map_id of this CreateWmsLayer.  # noqa: E501


        :return: The add_to_map_id of this CreateWmsLayer.  # noqa: E501
        :rtype: str
        """
        return self._add_to_map_id

    @add_to_map_id.setter
    def add_to_map_id(self, add_to_map_id):
        """Sets the add_to_map_id of this CreateWmsLayer.


        :param add_to_map_id: The add_to_map_id of this CreateWmsLayer.  # noqa: E501
        :type: str
        """

        self._add_to_map_id = add_to_map_id

    @property
    def folder_id(self):
        """Gets the folder_id of this CreateWmsLayer.  # noqa: E501


        :return: The folder_id of this CreateWmsLayer.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this CreateWmsLayer.


        :param folder_id: The folder_id of this CreateWmsLayer.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def set_public_access(self):
        """Gets the set_public_access of this CreateWmsLayer.  # noqa: E501


        :return: The set_public_access of this CreateWmsLayer.  # noqa: E501
        :rtype: bool
        """
        return self._set_public_access

    @set_public_access.setter
    def set_public_access(self, set_public_access):
        """Sets the set_public_access of this CreateWmsLayer.


        :param set_public_access: The set_public_access of this CreateWmsLayer.  # noqa: E501
        :type: bool
        """

        self._set_public_access = set_public_access

    @property
    def layer_names(self):
        """Gets the layer_names of this CreateWmsLayer.  # noqa: E501


        :return: The layer_names of this CreateWmsLayer.  # noqa: E501
        :rtype: list[str]
        """
        return self._layer_names

    @layer_names.setter
    def layer_names(self, layer_names):
        """Sets the layer_names of this CreateWmsLayer.


        :param layer_names: The layer_names of this CreateWmsLayer.  # noqa: E501
        :type: list[str]
        """

        self._layer_names = layer_names

    @property
    def extent(self):
        """Gets the extent of this CreateWmsLayer.  # noqa: E501


        :return: The extent of this CreateWmsLayer.  # noqa: E501
        :rtype: OneOfCreateWmsLayerExtent
        """
        return self._extent

    @extent.setter
    def extent(self, extent):
        """Sets the extent of this CreateWmsLayer.


        :param extent: The extent of this CreateWmsLayer.  # noqa: E501
        :type: OneOfCreateWmsLayerExtent
        """

        self._extent = extent

    @property
    def get_legend_url(self):
        """Gets the get_legend_url of this CreateWmsLayer.  # noqa: E501


        :return: The get_legend_url of this CreateWmsLayer.  # noqa: E501
        :rtype: str
        """
        return self._get_legend_url

    @get_legend_url.setter
    def get_legend_url(self, get_legend_url):
        """Sets the get_legend_url of this CreateWmsLayer.


        :param get_legend_url: The get_legend_url of this CreateWmsLayer.  # noqa: E501
        :type: str
        """

        self._get_legend_url = get_legend_url

    @property
    def version(self):
        """Gets the version of this CreateWmsLayer.  # noqa: E501


        :return: The version of this CreateWmsLayer.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateWmsLayer.


        :param version: The version of this CreateWmsLayer.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(CreateWmsLayer, dict):
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
        if not isinstance(other, CreateWmsLayer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
