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

class Layer(object):
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
        'unique_identifier': 'str',
        'name': 'str',
        'creation_time': 'datetime',
        'modified_time': 'datetime',
        'data_table_unique_identifier': 'str',
        'description': 'str',
        'geometry_type': 'GeometryTypeEnum',
        'metadata': 'str',
        'owner_name': 'str',
        'proj4': 'str',
        'row_count': 'int',
        'data_usage': 'int',
        'system_identifier': 'str',
        'unique_id_data_column': 'str',
        'precision': 'int',
        'public_access': 'bool',
        'thumbnail_url': 'str',
        'thumbnail_url_expiry': 'datetime',
        'icon': 'str',
        'cluster_status': 'ClusterStatusEnum',
        'is_clusterable': 'bool',
        'vector_tiling': 'bool',
        'vector_tiling_forced': 'bool',
        'vector_quality_type': 'VectorQualityTypeEnum',
        'can_edit': 'bool',
        'related_maps': 'list[Map]',
        'is_locked': 'bool',
        'is_demo_source': 'bool',
        'is_heatmap_source': 'bool',
        'optimization_status': 'ClickHouseStatus',
        'is_view': 'bool',
        'is_external': 'bool',
        'is_live': 'bool',
        'external_service_live_feed': 'bool',
        'external_service_type': 'OneOfLayerExternalServiceType',
        'folder_id': 'str'
    }

    attribute_map = {
        'unique_identifier': 'uniqueIdentifier',
        'name': 'name',
        'creation_time': 'creationTime',
        'modified_time': 'modifiedTime',
        'data_table_unique_identifier': 'dataTableUniqueIdentifier',
        'description': 'description',
        'geometry_type': 'geometryType',
        'metadata': 'metadata',
        'owner_name': 'ownerName',
        'proj4': 'proj4',
        'row_count': 'rowCount',
        'data_usage': 'dataUsage',
        'system_identifier': 'systemIdentifier',
        'unique_id_data_column': 'uniqueIdDataColumn',
        'precision': 'precision',
        'public_access': 'publicAccess',
        'thumbnail_url': 'thumbnailUrl',
        'thumbnail_url_expiry': 'thumbnailUrlExpiry',
        'icon': 'icon',
        'cluster_status': 'clusterStatus',
        'is_clusterable': 'isClusterable',
        'vector_tiling': 'vectorTiling',
        'vector_tiling_forced': 'vectorTilingForced',
        'vector_quality_type': 'vectorQualityType',
        'can_edit': 'canEdit',
        'related_maps': 'relatedMaps',
        'is_locked': 'isLocked',
        'is_demo_source': 'isDemoSource',
        'is_heatmap_source': 'isHeatmapSource',
        'optimization_status': 'optimizationStatus',
        'is_view': 'isView',
        'is_external': 'isExternal',
        'is_live': 'isLive',
        'external_service_live_feed': 'externalServiceLiveFeed',
        'external_service_type': 'externalServiceType',
        'folder_id': 'folderId'
    }

    def __init__(self, unique_identifier=None, name=None, creation_time=None, modified_time=None, data_table_unique_identifier=None, description=None, geometry_type=None, metadata=None, owner_name=None, proj4=None, row_count=None, data_usage=None, system_identifier=None, unique_id_data_column=None, precision=None, public_access=None, thumbnail_url=None, thumbnail_url_expiry=None, icon=None, cluster_status=None, is_clusterable=None, vector_tiling=None, vector_tiling_forced=None, vector_quality_type=None, can_edit=None, related_maps=None, is_locked=None, is_demo_source=None, is_heatmap_source=None, optimization_status=None, is_view=None, is_external=None, is_live=None, external_service_live_feed=None, external_service_type=None, folder_id=None):  # noqa: E501
        """Layer - a model defined in Swagger"""  # noqa: E501
        self._unique_identifier = None
        self._name = None
        self._creation_time = None
        self._modified_time = None
        self._data_table_unique_identifier = None
        self._description = None
        self._geometry_type = None
        self._metadata = None
        self._owner_name = None
        self._proj4 = None
        self._row_count = None
        self._data_usage = None
        self._system_identifier = None
        self._unique_id_data_column = None
        self._precision = None
        self._public_access = None
        self._thumbnail_url = None
        self._thumbnail_url_expiry = None
        self._icon = None
        self._cluster_status = None
        self._is_clusterable = None
        self._vector_tiling = None
        self._vector_tiling_forced = None
        self._vector_quality_type = None
        self._can_edit = None
        self._related_maps = None
        self._is_locked = None
        self._is_demo_source = None
        self._is_heatmap_source = None
        self._optimization_status = None
        self._is_view = None
        self._is_external = None
        self._is_live = None
        self._external_service_live_feed = None
        self._external_service_type = None
        self._folder_id = None
        self.discriminator = None
        if unique_identifier is not None:
            self.unique_identifier = unique_identifier
        if name is not None:
            self.name = name
        if creation_time is not None:
            self.creation_time = creation_time
        if modified_time is not None:
            self.modified_time = modified_time
        if data_table_unique_identifier is not None:
            self.data_table_unique_identifier = data_table_unique_identifier
        if description is not None:
            self.description = description
        if geometry_type is not None:
            self.geometry_type = geometry_type
        if metadata is not None:
            self.metadata = metadata
        if owner_name is not None:
            self.owner_name = owner_name
        if proj4 is not None:
            self.proj4 = proj4
        if row_count is not None:
            self.row_count = row_count
        if data_usage is not None:
            self.data_usage = data_usage
        if system_identifier is not None:
            self.system_identifier = system_identifier
        if unique_id_data_column is not None:
            self.unique_id_data_column = unique_id_data_column
        if precision is not None:
            self.precision = precision
        if public_access is not None:
            self.public_access = public_access
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        if thumbnail_url_expiry is not None:
            self.thumbnail_url_expiry = thumbnail_url_expiry
        if icon is not None:
            self.icon = icon
        if cluster_status is not None:
            self.cluster_status = cluster_status
        if is_clusterable is not None:
            self.is_clusterable = is_clusterable
        if vector_tiling is not None:
            self.vector_tiling = vector_tiling
        if vector_tiling_forced is not None:
            self.vector_tiling_forced = vector_tiling_forced
        if vector_quality_type is not None:
            self.vector_quality_type = vector_quality_type
        if can_edit is not None:
            self.can_edit = can_edit
        if related_maps is not None:
            self.related_maps = related_maps
        if is_locked is not None:
            self.is_locked = is_locked
        if is_demo_source is not None:
            self.is_demo_source = is_demo_source
        if is_heatmap_source is not None:
            self.is_heatmap_source = is_heatmap_source
        if optimization_status is not None:
            self.optimization_status = optimization_status
        if is_view is not None:
            self.is_view = is_view
        if is_external is not None:
            self.is_external = is_external
        if is_live is not None:
            self.is_live = is_live
        if external_service_live_feed is not None:
            self.external_service_live_feed = external_service_live_feed
        if external_service_type is not None:
            self.external_service_type = external_service_type
        if folder_id is not None:
            self.folder_id = folder_id

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this Layer.  # noqa: E501


        :return: The unique_identifier of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this Layer.


        :param unique_identifier: The unique_identifier of this Layer.  # noqa: E501
        :type: str
        """

        self._unique_identifier = unique_identifier

    @property
    def name(self):
        """Gets the name of this Layer.  # noqa: E501


        :return: The name of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Layer.


        :param name: The name of this Layer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def creation_time(self):
        """Gets the creation_time of this Layer.  # noqa: E501


        :return: The creation_time of this Layer.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Layer.


        :param creation_time: The creation_time of this Layer.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def modified_time(self):
        """Gets the modified_time of this Layer.  # noqa: E501


        :return: The modified_time of this Layer.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this Layer.


        :param modified_time: The modified_time of this Layer.  # noqa: E501
        :type: datetime
        """

        self._modified_time = modified_time

    @property
    def data_table_unique_identifier(self):
        """Gets the data_table_unique_identifier of this Layer.  # noqa: E501


        :return: The data_table_unique_identifier of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._data_table_unique_identifier

    @data_table_unique_identifier.setter
    def data_table_unique_identifier(self, data_table_unique_identifier):
        """Sets the data_table_unique_identifier of this Layer.


        :param data_table_unique_identifier: The data_table_unique_identifier of this Layer.  # noqa: E501
        :type: str
        """

        self._data_table_unique_identifier = data_table_unique_identifier

    @property
    def description(self):
        """Gets the description of this Layer.  # noqa: E501


        :return: The description of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Layer.


        :param description: The description of this Layer.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def geometry_type(self):
        """Gets the geometry_type of this Layer.  # noqa: E501


        :return: The geometry_type of this Layer.  # noqa: E501
        :rtype: GeometryTypeEnum
        """
        return self._geometry_type

    @geometry_type.setter
    def geometry_type(self, geometry_type):
        """Sets the geometry_type of this Layer.


        :param geometry_type: The geometry_type of this Layer.  # noqa: E501
        :type: GeometryTypeEnum
        """

        self._geometry_type = geometry_type

    @property
    def metadata(self):
        """Gets the metadata of this Layer.  # noqa: E501


        :return: The metadata of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Layer.


        :param metadata: The metadata of this Layer.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def owner_name(self):
        """Gets the owner_name of this Layer.  # noqa: E501


        :return: The owner_name of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this Layer.


        :param owner_name: The owner_name of this Layer.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def proj4(self):
        """Gets the proj4 of this Layer.  # noqa: E501


        :return: The proj4 of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._proj4

    @proj4.setter
    def proj4(self, proj4):
        """Sets the proj4 of this Layer.


        :param proj4: The proj4 of this Layer.  # noqa: E501
        :type: str
        """

        self._proj4 = proj4

    @property
    def row_count(self):
        """Gets the row_count of this Layer.  # noqa: E501


        :return: The row_count of this Layer.  # noqa: E501
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this Layer.


        :param row_count: The row_count of this Layer.  # noqa: E501
        :type: int
        """

        self._row_count = row_count

    @property
    def data_usage(self):
        """Gets the data_usage of this Layer.  # noqa: E501


        :return: The data_usage of this Layer.  # noqa: E501
        :rtype: int
        """
        return self._data_usage

    @data_usage.setter
    def data_usage(self, data_usage):
        """Sets the data_usage of this Layer.


        :param data_usage: The data_usage of this Layer.  # noqa: E501
        :type: int
        """

        self._data_usage = data_usage

    @property
    def system_identifier(self):
        """Gets the system_identifier of this Layer.  # noqa: E501


        :return: The system_identifier of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._system_identifier

    @system_identifier.setter
    def system_identifier(self, system_identifier):
        """Sets the system_identifier of this Layer.


        :param system_identifier: The system_identifier of this Layer.  # noqa: E501
        :type: str
        """

        self._system_identifier = system_identifier

    @property
    def unique_id_data_column(self):
        """Gets the unique_id_data_column of this Layer.  # noqa: E501


        :return: The unique_id_data_column of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._unique_id_data_column

    @unique_id_data_column.setter
    def unique_id_data_column(self, unique_id_data_column):
        """Sets the unique_id_data_column of this Layer.


        :param unique_id_data_column: The unique_id_data_column of this Layer.  # noqa: E501
        :type: str
        """

        self._unique_id_data_column = unique_id_data_column

    @property
    def precision(self):
        """Gets the precision of this Layer.  # noqa: E501


        :return: The precision of this Layer.  # noqa: E501
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this Layer.


        :param precision: The precision of this Layer.  # noqa: E501
        :type: int
        """

        self._precision = precision

    @property
    def public_access(self):
        """Gets the public_access of this Layer.  # noqa: E501


        :return: The public_access of this Layer.  # noqa: E501
        :rtype: bool
        """
        return self._public_access

    @public_access.setter
    def public_access(self, public_access):
        """Sets the public_access of this Layer.


        :param public_access: The public_access of this Layer.  # noqa: E501
        :type: bool
        """

        self._public_access = public_access

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this Layer.  # noqa: E501


        :return: The thumbnail_url of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this Layer.


        :param thumbnail_url: The thumbnail_url of this Layer.  # noqa: E501
        :type: str
        """

        self._thumbnail_url = thumbnail_url

    @property
    def thumbnail_url_expiry(self):
        """Gets the thumbnail_url_expiry of this Layer.  # noqa: E501


        :return: The thumbnail_url_expiry of this Layer.  # noqa: E501
        :rtype: datetime
        """
        return self._thumbnail_url_expiry

    @thumbnail_url_expiry.setter
    def thumbnail_url_expiry(self, thumbnail_url_expiry):
        """Sets the thumbnail_url_expiry of this Layer.


        :param thumbnail_url_expiry: The thumbnail_url_expiry of this Layer.  # noqa: E501
        :type: datetime
        """

        self._thumbnail_url_expiry = thumbnail_url_expiry

    @property
    def icon(self):
        """Gets the icon of this Layer.  # noqa: E501


        :return: The icon of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this Layer.


        :param icon: The icon of this Layer.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def cluster_status(self):
        """Gets the cluster_status of this Layer.  # noqa: E501


        :return: The cluster_status of this Layer.  # noqa: E501
        :rtype: ClusterStatusEnum
        """
        return self._cluster_status

    @cluster_status.setter
    def cluster_status(self, cluster_status):
        """Sets the cluster_status of this Layer.


        :param cluster_status: The cluster_status of this Layer.  # noqa: E501
        :type: ClusterStatusEnum
        """

        self._cluster_status = cluster_status

    @property
    def is_clusterable(self):
        """Gets the is_clusterable of this Layer.  # noqa: E501


        :return: The is_clusterable of this Layer.  # noqa: E501
        :rtype: bool
        """
        return self._is_clusterable

    @is_clusterable.setter
    def is_clusterable(self, is_clusterable):
        """Sets the is_clusterable of this Layer.


        :param is_clusterable: The is_clusterable of this Layer.  # noqa: E501
        :type: bool
        """

        self._is_clusterable = is_clusterable

    @property
    def vector_tiling(self):
        """Gets the vector_tiling of this Layer.  # noqa: E501


        :return: The vector_tiling of this Layer.  # noqa: E501
        :rtype: bool
        """
        return self._vector_tiling

    @vector_tiling.setter
    def vector_tiling(self, vector_tiling):
        """Sets the vector_tiling of this Layer.


        :param vector_tiling: The vector_tiling of this Layer.  # noqa: E501
        :type: bool
        """

        self._vector_tiling = vector_tiling

    @property
    def vector_tiling_forced(self):
        """Gets the vector_tiling_forced of this Layer.  # noqa: E501


        :return: The vector_tiling_forced of this Layer.  # noqa: E501
        :rtype: bool
        """
        return self._vector_tiling_forced

    @vector_tiling_forced.setter
    def vector_tiling_forced(self, vector_tiling_forced):
        """Sets the vector_tiling_forced of this Layer.


        :param vector_tiling_forced: The vector_tiling_forced of this Layer.  # noqa: E501
        :type: bool
        """

        self._vector_tiling_forced = vector_tiling_forced

    @property
    def vector_quality_type(self):
        """Gets the vector_quality_type of this Layer.  # noqa: E501


        :return: The vector_quality_type of this Layer.  # noqa: E501
        :rtype: VectorQualityTypeEnum
        """
        return self._vector_quality_type

    @vector_quality_type.setter
    def vector_quality_type(self, vector_quality_type):
        """Sets the vector_quality_type of this Layer.


        :param vector_quality_type: The vector_quality_type of this Layer.  # noqa: E501
        :type: VectorQualityTypeEnum
        """

        self._vector_quality_type = vector_quality_type

    @property
    def can_edit(self):
        """Gets the can_edit of this Layer.  # noqa: E501


        :return: The can_edit of this Layer.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        """Sets the can_edit of this Layer.


        :param can_edit: The can_edit of this Layer.  # noqa: E501
        :type: bool
        """

        self._can_edit = can_edit

    @property
    def related_maps(self):
        """Gets the related_maps of this Layer.  # noqa: E501


        :return: The related_maps of this Layer.  # noqa: E501
        :rtype: list[Map]
        """
        return self._related_maps

    @related_maps.setter
    def related_maps(self, related_maps):
        """Sets the related_maps of this Layer.


        :param related_maps: The related_maps of this Layer.  # noqa: E501
        :type: list[Map]
        """

        self._related_maps = related_maps

    @property
    def is_locked(self):
        """Gets the is_locked of this Layer.  # noqa: E501


        :return: The is_locked of this Layer.  # noqa: E501
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this Layer.


        :param is_locked: The is_locked of this Layer.  # noqa: E501
        :type: bool
        """

        self._is_locked = is_locked

    @property
    def is_demo_source(self):
        """Gets the is_demo_source of this Layer.  # noqa: E501


        :return: The is_demo_source of this Layer.  # noqa: E501
        :rtype: bool
        """
        return self._is_demo_source

    @is_demo_source.setter
    def is_demo_source(self, is_demo_source):
        """Sets the is_demo_source of this Layer.


        :param is_demo_source: The is_demo_source of this Layer.  # noqa: E501
        :type: bool
        """

        self._is_demo_source = is_demo_source

    @property
    def is_heatmap_source(self):
        """Gets the is_heatmap_source of this Layer.  # noqa: E501


        :return: The is_heatmap_source of this Layer.  # noqa: E501
        :rtype: bool
        """
        return self._is_heatmap_source

    @is_heatmap_source.setter
    def is_heatmap_source(self, is_heatmap_source):
        """Sets the is_heatmap_source of this Layer.


        :param is_heatmap_source: The is_heatmap_source of this Layer.  # noqa: E501
        :type: bool
        """

        self._is_heatmap_source = is_heatmap_source

    @property
    def optimization_status(self):
        """Gets the optimization_status of this Layer.  # noqa: E501


        :return: The optimization_status of this Layer.  # noqa: E501
        :rtype: ClickHouseStatus
        """
        return self._optimization_status

    @optimization_status.setter
    def optimization_status(self, optimization_status):
        """Sets the optimization_status of this Layer.


        :param optimization_status: The optimization_status of this Layer.  # noqa: E501
        :type: ClickHouseStatus
        """

        self._optimization_status = optimization_status

    @property
    def is_view(self):
        """Gets the is_view of this Layer.  # noqa: E501


        :return: The is_view of this Layer.  # noqa: E501
        :rtype: bool
        """
        return self._is_view

    @is_view.setter
    def is_view(self, is_view):
        """Sets the is_view of this Layer.


        :param is_view: The is_view of this Layer.  # noqa: E501
        :type: bool
        """

        self._is_view = is_view

    @property
    def is_external(self):
        """Gets the is_external of this Layer.  # noqa: E501


        :return: The is_external of this Layer.  # noqa: E501
        :rtype: bool
        """
        return self._is_external

    @is_external.setter
    def is_external(self, is_external):
        """Sets the is_external of this Layer.


        :param is_external: The is_external of this Layer.  # noqa: E501
        :type: bool
        """

        self._is_external = is_external

    @property
    def is_live(self):
        """Gets the is_live of this Layer.  # noqa: E501


        :return: The is_live of this Layer.  # noqa: E501
        :rtype: bool
        """
        return self._is_live

    @is_live.setter
    def is_live(self, is_live):
        """Sets the is_live of this Layer.


        :param is_live: The is_live of this Layer.  # noqa: E501
        :type: bool
        """

        self._is_live = is_live

    @property
    def external_service_live_feed(self):
        """Gets the external_service_live_feed of this Layer.  # noqa: E501


        :return: The external_service_live_feed of this Layer.  # noqa: E501
        :rtype: bool
        """
        return self._external_service_live_feed

    @external_service_live_feed.setter
    def external_service_live_feed(self, external_service_live_feed):
        """Sets the external_service_live_feed of this Layer.


        :param external_service_live_feed: The external_service_live_feed of this Layer.  # noqa: E501
        :type: bool
        """

        self._external_service_live_feed = external_service_live_feed

    @property
    def external_service_type(self):
        """Gets the external_service_type of this Layer.  # noqa: E501


        :return: The external_service_type of this Layer.  # noqa: E501
        :rtype: OneOfLayerExternalServiceType
        """
        return self._external_service_type

    @external_service_type.setter
    def external_service_type(self, external_service_type):
        """Sets the external_service_type of this Layer.


        :param external_service_type: The external_service_type of this Layer.  # noqa: E501
        :type: OneOfLayerExternalServiceType
        """

        self._external_service_type = external_service_type

    @property
    def folder_id(self):
        """Gets the folder_id of this Layer.  # noqa: E501


        :return: The folder_id of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this Layer.


        :param folder_id: The folder_id of this Layer.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

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
        if issubclass(Layer, dict):
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
        if not isinstance(other, Layer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other