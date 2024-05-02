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

class GridLayer(object):
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
        'system_identifier': 'str',
        'unique_identifier': 'str',
        'description': 'str',
        'metadata': 'str',
        'proj4': 'str',
        'units': 'str',
        'precision': 'int',
        'icon': 'str',
        'grid_source_count': 'int',
        'name': 'str',
        'creation_time': 'datetime',
        'modified_time': 'datetime',
        'map_use_count': 'int',
        'grid_layer_type': 'GridLayerTypeEnum',
        'disabled': 'bool',
        'owner_name': 'str',
        'can_edit': 'bool',
        'public_access': 'bool',
        'thumbnail_url': 'str',
        'thumbnail_url_expiry': 'datetime',
        'folder_id': 'str',
        'is_heatmap': 'bool'
    }

    attribute_map = {
        'system_identifier': 'systemIdentifier',
        'unique_identifier': 'uniqueIdentifier',
        'description': 'description',
        'metadata': 'metadata',
        'proj4': 'proj4',
        'units': 'units',
        'precision': 'precision',
        'icon': 'icon',
        'grid_source_count': 'gridSourceCount',
        'name': 'name',
        'creation_time': 'creationTime',
        'modified_time': 'modifiedTime',
        'map_use_count': 'mapUseCount',
        'grid_layer_type': 'gridLayerType',
        'disabled': 'disabled',
        'owner_name': 'ownerName',
        'can_edit': 'canEdit',
        'public_access': 'publicAccess',
        'thumbnail_url': 'thumbnailUrl',
        'thumbnail_url_expiry': 'thumbnailUrlExpiry',
        'folder_id': 'folderId',
        'is_heatmap': 'isHeatmap'
    }

    def __init__(self, system_identifier=None, unique_identifier=None, description=None, metadata=None, proj4=None, units=None, precision=None, icon=None, grid_source_count=None, name=None, creation_time=None, modified_time=None, map_use_count=None, grid_layer_type=None, disabled=None, owner_name=None, can_edit=None, public_access=None, thumbnail_url=None, thumbnail_url_expiry=None, folder_id=None, is_heatmap=None):  # noqa: E501
        """GridLayer - a model defined in Swagger"""  # noqa: E501
        self._system_identifier = None
        self._unique_identifier = None
        self._description = None
        self._metadata = None
        self._proj4 = None
        self._units = None
        self._precision = None
        self._icon = None
        self._grid_source_count = None
        self._name = None
        self._creation_time = None
        self._modified_time = None
        self._map_use_count = None
        self._grid_layer_type = None
        self._disabled = None
        self._owner_name = None
        self._can_edit = None
        self._public_access = None
        self._thumbnail_url = None
        self._thumbnail_url_expiry = None
        self._folder_id = None
        self._is_heatmap = None
        self.discriminator = None
        if system_identifier is not None:
            self.system_identifier = system_identifier
        if unique_identifier is not None:
            self.unique_identifier = unique_identifier
        if description is not None:
            self.description = description
        if metadata is not None:
            self.metadata = metadata
        if proj4 is not None:
            self.proj4 = proj4
        if units is not None:
            self.units = units
        if precision is not None:
            self.precision = precision
        if icon is not None:
            self.icon = icon
        if grid_source_count is not None:
            self.grid_source_count = grid_source_count
        if name is not None:
            self.name = name
        if creation_time is not None:
            self.creation_time = creation_time
        if modified_time is not None:
            self.modified_time = modified_time
        if map_use_count is not None:
            self.map_use_count = map_use_count
        if grid_layer_type is not None:
            self.grid_layer_type = grid_layer_type
        if disabled is not None:
            self.disabled = disabled
        if owner_name is not None:
            self.owner_name = owner_name
        if can_edit is not None:
            self.can_edit = can_edit
        if public_access is not None:
            self.public_access = public_access
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        if thumbnail_url_expiry is not None:
            self.thumbnail_url_expiry = thumbnail_url_expiry
        if folder_id is not None:
            self.folder_id = folder_id
        if is_heatmap is not None:
            self.is_heatmap = is_heatmap

    @property
    def system_identifier(self):
        """Gets the system_identifier of this GridLayer.  # noqa: E501


        :return: The system_identifier of this GridLayer.  # noqa: E501
        :rtype: str
        """
        return self._system_identifier

    @system_identifier.setter
    def system_identifier(self, system_identifier):
        """Sets the system_identifier of this GridLayer.


        :param system_identifier: The system_identifier of this GridLayer.  # noqa: E501
        :type: str
        """

        self._system_identifier = system_identifier

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this GridLayer.  # noqa: E501


        :return: The unique_identifier of this GridLayer.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this GridLayer.


        :param unique_identifier: The unique_identifier of this GridLayer.  # noqa: E501
        :type: str
        """

        self._unique_identifier = unique_identifier

    @property
    def description(self):
        """Gets the description of this GridLayer.  # noqa: E501


        :return: The description of this GridLayer.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GridLayer.


        :param description: The description of this GridLayer.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def metadata(self):
        """Gets the metadata of this GridLayer.  # noqa: E501


        :return: The metadata of this GridLayer.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this GridLayer.


        :param metadata: The metadata of this GridLayer.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def proj4(self):
        """Gets the proj4 of this GridLayer.  # noqa: E501


        :return: The proj4 of this GridLayer.  # noqa: E501
        :rtype: str
        """
        return self._proj4

    @proj4.setter
    def proj4(self, proj4):
        """Sets the proj4 of this GridLayer.


        :param proj4: The proj4 of this GridLayer.  # noqa: E501
        :type: str
        """

        self._proj4 = proj4

    @property
    def units(self):
        """Gets the units of this GridLayer.  # noqa: E501


        :return: The units of this GridLayer.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this GridLayer.


        :param units: The units of this GridLayer.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def precision(self):
        """Gets the precision of this GridLayer.  # noqa: E501


        :return: The precision of this GridLayer.  # noqa: E501
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this GridLayer.


        :param precision: The precision of this GridLayer.  # noqa: E501
        :type: int
        """

        self._precision = precision

    @property
    def icon(self):
        """Gets the icon of this GridLayer.  # noqa: E501


        :return: The icon of this GridLayer.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this GridLayer.


        :param icon: The icon of this GridLayer.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def grid_source_count(self):
        """Gets the grid_source_count of this GridLayer.  # noqa: E501


        :return: The grid_source_count of this GridLayer.  # noqa: E501
        :rtype: int
        """
        return self._grid_source_count

    @grid_source_count.setter
    def grid_source_count(self, grid_source_count):
        """Sets the grid_source_count of this GridLayer.


        :param grid_source_count: The grid_source_count of this GridLayer.  # noqa: E501
        :type: int
        """

        self._grid_source_count = grid_source_count

    @property
    def name(self):
        """Gets the name of this GridLayer.  # noqa: E501


        :return: The name of this GridLayer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GridLayer.


        :param name: The name of this GridLayer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def creation_time(self):
        """Gets the creation_time of this GridLayer.  # noqa: E501


        :return: The creation_time of this GridLayer.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this GridLayer.


        :param creation_time: The creation_time of this GridLayer.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def modified_time(self):
        """Gets the modified_time of this GridLayer.  # noqa: E501


        :return: The modified_time of this GridLayer.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this GridLayer.


        :param modified_time: The modified_time of this GridLayer.  # noqa: E501
        :type: datetime
        """

        self._modified_time = modified_time

    @property
    def map_use_count(self):
        """Gets the map_use_count of this GridLayer.  # noqa: E501


        :return: The map_use_count of this GridLayer.  # noqa: E501
        :rtype: int
        """
        return self._map_use_count

    @map_use_count.setter
    def map_use_count(self, map_use_count):
        """Sets the map_use_count of this GridLayer.


        :param map_use_count: The map_use_count of this GridLayer.  # noqa: E501
        :type: int
        """

        self._map_use_count = map_use_count

    @property
    def grid_layer_type(self):
        """Gets the grid_layer_type of this GridLayer.  # noqa: E501


        :return: The grid_layer_type of this GridLayer.  # noqa: E501
        :rtype: GridLayerTypeEnum
        """
        return self._grid_layer_type

    @grid_layer_type.setter
    def grid_layer_type(self, grid_layer_type):
        """Sets the grid_layer_type of this GridLayer.


        :param grid_layer_type: The grid_layer_type of this GridLayer.  # noqa: E501
        :type: GridLayerTypeEnum
        """

        self._grid_layer_type = grid_layer_type

    @property
    def disabled(self):
        """Gets the disabled of this GridLayer.  # noqa: E501


        :return: The disabled of this GridLayer.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this GridLayer.


        :param disabled: The disabled of this GridLayer.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def owner_name(self):
        """Gets the owner_name of this GridLayer.  # noqa: E501


        :return: The owner_name of this GridLayer.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this GridLayer.


        :param owner_name: The owner_name of this GridLayer.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def can_edit(self):
        """Gets the can_edit of this GridLayer.  # noqa: E501


        :return: The can_edit of this GridLayer.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        """Sets the can_edit of this GridLayer.


        :param can_edit: The can_edit of this GridLayer.  # noqa: E501
        :type: bool
        """

        self._can_edit = can_edit

    @property
    def public_access(self):
        """Gets the public_access of this GridLayer.  # noqa: E501


        :return: The public_access of this GridLayer.  # noqa: E501
        :rtype: bool
        """
        return self._public_access

    @public_access.setter
    def public_access(self, public_access):
        """Sets the public_access of this GridLayer.


        :param public_access: The public_access of this GridLayer.  # noqa: E501
        :type: bool
        """

        self._public_access = public_access

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this GridLayer.  # noqa: E501


        :return: The thumbnail_url of this GridLayer.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this GridLayer.


        :param thumbnail_url: The thumbnail_url of this GridLayer.  # noqa: E501
        :type: str
        """

        self._thumbnail_url = thumbnail_url

    @property
    def thumbnail_url_expiry(self):
        """Gets the thumbnail_url_expiry of this GridLayer.  # noqa: E501


        :return: The thumbnail_url_expiry of this GridLayer.  # noqa: E501
        :rtype: datetime
        """
        return self._thumbnail_url_expiry

    @thumbnail_url_expiry.setter
    def thumbnail_url_expiry(self, thumbnail_url_expiry):
        """Sets the thumbnail_url_expiry of this GridLayer.


        :param thumbnail_url_expiry: The thumbnail_url_expiry of this GridLayer.  # noqa: E501
        :type: datetime
        """

        self._thumbnail_url_expiry = thumbnail_url_expiry

    @property
    def folder_id(self):
        """Gets the folder_id of this GridLayer.  # noqa: E501


        :return: The folder_id of this GridLayer.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this GridLayer.


        :param folder_id: The folder_id of this GridLayer.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def is_heatmap(self):
        """Gets the is_heatmap of this GridLayer.  # noqa: E501


        :return: The is_heatmap of this GridLayer.  # noqa: E501
        :rtype: bool
        """
        return self._is_heatmap

    @is_heatmap.setter
    def is_heatmap(self, is_heatmap):
        """Sets the is_heatmap of this GridLayer.


        :param is_heatmap: The is_heatmap of this GridLayer.  # noqa: E501
        :type: bool
        """

        self._is_heatmap = is_heatmap

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
        if issubclass(GridLayer, dict):
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
        if not isinstance(other, GridLayer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other