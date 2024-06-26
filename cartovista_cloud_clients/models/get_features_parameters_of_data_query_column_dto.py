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

class GetFeaturesParametersOfDataQueryColumnDTO(object):
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
        'feature_type': 'str',
        'attributes': 'list[str]',
        'format': 'str',
        'extent': 'OneOfGetFeaturesParametersOfDataQueryColumnDTOExtent',
        'width': 'int',
        'height': 'int',
        'filter_data_columns': 'list[DataQueryColumnDTO]',
        'spatial_filter': 'OneOfGetFeaturesParametersOfDataQueryColumnDTOSpatialFilter',
        'zoom_level': 'int',
        'proj4': 'str',
        'use_compression': 'bool',
        'fid': 'str',
        'feature_ids': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'feature_type': 'featureType',
        'attributes': 'attributes',
        'format': 'format',
        'extent': 'extent',
        'width': 'width',
        'height': 'height',
        'filter_data_columns': 'filterDataColumns',
        'spatial_filter': 'spatialFilter',
        'zoom_level': 'zoomLevel',
        'proj4': 'proj4',
        'use_compression': 'useCompression',
        'fid': 'fid',
        'feature_ids': 'featureIds'
    }

    def __init__(self, id=None, feature_type=None, attributes=None, format=None, extent=None, width=None, height=None, filter_data_columns=None, spatial_filter=None, zoom_level=None, proj4=None, use_compression=None, fid=None, feature_ids=None):  # noqa: E501
        """GetFeaturesParametersOfDataQueryColumnDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._feature_type = None
        self._attributes = None
        self._format = None
        self._extent = None
        self._width = None
        self._height = None
        self._filter_data_columns = None
        self._spatial_filter = None
        self._zoom_level = None
        self._proj4 = None
        self._use_compression = None
        self._fid = None
        self._feature_ids = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if feature_type is not None:
            self.feature_type = feature_type
        if attributes is not None:
            self.attributes = attributes
        if format is not None:
            self.format = format
        if extent is not None:
            self.extent = extent
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if filter_data_columns is not None:
            self.filter_data_columns = filter_data_columns
        if spatial_filter is not None:
            self.spatial_filter = spatial_filter
        if zoom_level is not None:
            self.zoom_level = zoom_level
        if proj4 is not None:
            self.proj4 = proj4
        if use_compression is not None:
            self.use_compression = use_compression
        if fid is not None:
            self.fid = fid
        if feature_ids is not None:
            self.feature_ids = feature_ids

    @property
    def id(self):
        """Gets the id of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501


        :return: The id of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetFeaturesParametersOfDataQueryColumnDTO.


        :param id: The id of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def feature_type(self):
        """Gets the feature_type of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501


        :return: The feature_type of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._feature_type

    @feature_type.setter
    def feature_type(self, feature_type):
        """Sets the feature_type of this GetFeaturesParametersOfDataQueryColumnDTO.


        :param feature_type: The feature_type of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._feature_type = feature_type

    @property
    def attributes(self):
        """Gets the attributes of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501


        :return: The attributes of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this GetFeaturesParametersOfDataQueryColumnDTO.


        :param attributes: The attributes of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :type: list[str]
        """

        self._attributes = attributes

    @property
    def format(self):
        """Gets the format of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501


        :return: The format of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this GetFeaturesParametersOfDataQueryColumnDTO.


        :param format: The format of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def extent(self):
        """Gets the extent of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501


        :return: The extent of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :rtype: OneOfGetFeaturesParametersOfDataQueryColumnDTOExtent
        """
        return self._extent

    @extent.setter
    def extent(self, extent):
        """Sets the extent of this GetFeaturesParametersOfDataQueryColumnDTO.


        :param extent: The extent of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :type: OneOfGetFeaturesParametersOfDataQueryColumnDTOExtent
        """

        self._extent = extent

    @property
    def width(self):
        """Gets the width of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501


        :return: The width of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this GetFeaturesParametersOfDataQueryColumnDTO.


        :param width: The width of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501


        :return: The height of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this GetFeaturesParametersOfDataQueryColumnDTO.


        :param height: The height of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def filter_data_columns(self):
        """Gets the filter_data_columns of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501


        :return: The filter_data_columns of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :rtype: list[DataQueryColumnDTO]
        """
        return self._filter_data_columns

    @filter_data_columns.setter
    def filter_data_columns(self, filter_data_columns):
        """Sets the filter_data_columns of this GetFeaturesParametersOfDataQueryColumnDTO.


        :param filter_data_columns: The filter_data_columns of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :type: list[DataQueryColumnDTO]
        """

        self._filter_data_columns = filter_data_columns

    @property
    def spatial_filter(self):
        """Gets the spatial_filter of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501


        :return: The spatial_filter of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :rtype: OneOfGetFeaturesParametersOfDataQueryColumnDTOSpatialFilter
        """
        return self._spatial_filter

    @spatial_filter.setter
    def spatial_filter(self, spatial_filter):
        """Sets the spatial_filter of this GetFeaturesParametersOfDataQueryColumnDTO.


        :param spatial_filter: The spatial_filter of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :type: OneOfGetFeaturesParametersOfDataQueryColumnDTOSpatialFilter
        """

        self._spatial_filter = spatial_filter

    @property
    def zoom_level(self):
        """Gets the zoom_level of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501


        :return: The zoom_level of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :rtype: int
        """
        return self._zoom_level

    @zoom_level.setter
    def zoom_level(self, zoom_level):
        """Sets the zoom_level of this GetFeaturesParametersOfDataQueryColumnDTO.


        :param zoom_level: The zoom_level of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :type: int
        """

        self._zoom_level = zoom_level

    @property
    def proj4(self):
        """Gets the proj4 of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501


        :return: The proj4 of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._proj4

    @proj4.setter
    def proj4(self, proj4):
        """Sets the proj4 of this GetFeaturesParametersOfDataQueryColumnDTO.


        :param proj4: The proj4 of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._proj4 = proj4

    @property
    def use_compression(self):
        """Gets the use_compression of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501


        :return: The use_compression of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :rtype: bool
        """
        return self._use_compression

    @use_compression.setter
    def use_compression(self, use_compression):
        """Sets the use_compression of this GetFeaturesParametersOfDataQueryColumnDTO.


        :param use_compression: The use_compression of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :type: bool
        """

        self._use_compression = use_compression

    @property
    def fid(self):
        """Gets the fid of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501


        :return: The fid of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._fid

    @fid.setter
    def fid(self, fid):
        """Sets the fid of this GetFeaturesParametersOfDataQueryColumnDTO.


        :param fid: The fid of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._fid = fid

    @property
    def feature_ids(self):
        """Gets the feature_ids of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501


        :return: The feature_ids of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._feature_ids

    @feature_ids.setter
    def feature_ids(self, feature_ids):
        """Sets the feature_ids of this GetFeaturesParametersOfDataQueryColumnDTO.


        :param feature_ids: The feature_ids of this GetFeaturesParametersOfDataQueryColumnDTO.  # noqa: E501
        :type: list[str]
        """

        self._feature_ids = feature_ids

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
        if issubclass(GetFeaturesParametersOfDataQueryColumnDTO, dict):
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
        if not isinstance(other, GetFeaturesParametersOfDataQueryColumnDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
