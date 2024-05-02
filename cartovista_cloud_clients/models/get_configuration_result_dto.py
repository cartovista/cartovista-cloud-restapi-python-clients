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

class GetConfigurationResultDTO(object):
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
        'version': 'str',
        'extent': 'ExtentDto',
        'geometry_type': 'str',
        'srid': 'int',
        'tiled': 'bool',
        'vector_quality_type': 'VectorQualityTypeEnum',
        'data_query_max_count': 'int',
        'editable': 'bool',
        'quad_tree_configuration': 'QuadTreeConfigurationDTO',
        'editable_tm': 'bool',
        'maximum_cluster_zoom_level': 'int'
    }

    attribute_map = {
        'version': 'version',
        'extent': 'extent',
        'geometry_type': 'geometryType',
        'srid': 'srid',
        'tiled': 'tiled',
        'vector_quality_type': 'vectorQualityType',
        'data_query_max_count': 'dataQueryMaxCount',
        'editable': 'editable',
        'quad_tree_configuration': 'quadTreeConfiguration',
        'editable_tm': 'editableTM',
        'maximum_cluster_zoom_level': 'maximumClusterZoomLevel'
    }

    def __init__(self, version=None, extent=None, geometry_type=None, srid=None, tiled=None, vector_quality_type=None, data_query_max_count=None, editable=None, quad_tree_configuration=None, editable_tm=None, maximum_cluster_zoom_level=None):  # noqa: E501
        """GetConfigurationResultDTO - a model defined in Swagger"""  # noqa: E501
        self._version = None
        self._extent = None
        self._geometry_type = None
        self._srid = None
        self._tiled = None
        self._vector_quality_type = None
        self._data_query_max_count = None
        self._editable = None
        self._quad_tree_configuration = None
        self._editable_tm = None
        self._maximum_cluster_zoom_level = None
        self.discriminator = None
        if version is not None:
            self.version = version
        if extent is not None:
            self.extent = extent
        if geometry_type is not None:
            self.geometry_type = geometry_type
        if srid is not None:
            self.srid = srid
        if tiled is not None:
            self.tiled = tiled
        if vector_quality_type is not None:
            self.vector_quality_type = vector_quality_type
        if data_query_max_count is not None:
            self.data_query_max_count = data_query_max_count
        if editable is not None:
            self.editable = editable
        if quad_tree_configuration is not None:
            self.quad_tree_configuration = quad_tree_configuration
        if editable_tm is not None:
            self.editable_tm = editable_tm
        if maximum_cluster_zoom_level is not None:
            self.maximum_cluster_zoom_level = maximum_cluster_zoom_level

    @property
    def version(self):
        """Gets the version of this GetConfigurationResultDTO.  # noqa: E501


        :return: The version of this GetConfigurationResultDTO.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GetConfigurationResultDTO.


        :param version: The version of this GetConfigurationResultDTO.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def extent(self):
        """Gets the extent of this GetConfigurationResultDTO.  # noqa: E501


        :return: The extent of this GetConfigurationResultDTO.  # noqa: E501
        :rtype: ExtentDto
        """
        return self._extent

    @extent.setter
    def extent(self, extent):
        """Sets the extent of this GetConfigurationResultDTO.


        :param extent: The extent of this GetConfigurationResultDTO.  # noqa: E501
        :type: ExtentDto
        """

        self._extent = extent

    @property
    def geometry_type(self):
        """Gets the geometry_type of this GetConfigurationResultDTO.  # noqa: E501


        :return: The geometry_type of this GetConfigurationResultDTO.  # noqa: E501
        :rtype: str
        """
        return self._geometry_type

    @geometry_type.setter
    def geometry_type(self, geometry_type):
        """Sets the geometry_type of this GetConfigurationResultDTO.


        :param geometry_type: The geometry_type of this GetConfigurationResultDTO.  # noqa: E501
        :type: str
        """

        self._geometry_type = geometry_type

    @property
    def srid(self):
        """Gets the srid of this GetConfigurationResultDTO.  # noqa: E501


        :return: The srid of this GetConfigurationResultDTO.  # noqa: E501
        :rtype: int
        """
        return self._srid

    @srid.setter
    def srid(self, srid):
        """Sets the srid of this GetConfigurationResultDTO.


        :param srid: The srid of this GetConfigurationResultDTO.  # noqa: E501
        :type: int
        """

        self._srid = srid

    @property
    def tiled(self):
        """Gets the tiled of this GetConfigurationResultDTO.  # noqa: E501


        :return: The tiled of this GetConfigurationResultDTO.  # noqa: E501
        :rtype: bool
        """
        return self._tiled

    @tiled.setter
    def tiled(self, tiled):
        """Sets the tiled of this GetConfigurationResultDTO.


        :param tiled: The tiled of this GetConfigurationResultDTO.  # noqa: E501
        :type: bool
        """

        self._tiled = tiled

    @property
    def vector_quality_type(self):
        """Gets the vector_quality_type of this GetConfigurationResultDTO.  # noqa: E501


        :return: The vector_quality_type of this GetConfigurationResultDTO.  # noqa: E501
        :rtype: VectorQualityTypeEnum
        """
        return self._vector_quality_type

    @vector_quality_type.setter
    def vector_quality_type(self, vector_quality_type):
        """Sets the vector_quality_type of this GetConfigurationResultDTO.


        :param vector_quality_type: The vector_quality_type of this GetConfigurationResultDTO.  # noqa: E501
        :type: VectorQualityTypeEnum
        """

        self._vector_quality_type = vector_quality_type

    @property
    def data_query_max_count(self):
        """Gets the data_query_max_count of this GetConfigurationResultDTO.  # noqa: E501


        :return: The data_query_max_count of this GetConfigurationResultDTO.  # noqa: E501
        :rtype: int
        """
        return self._data_query_max_count

    @data_query_max_count.setter
    def data_query_max_count(self, data_query_max_count):
        """Sets the data_query_max_count of this GetConfigurationResultDTO.


        :param data_query_max_count: The data_query_max_count of this GetConfigurationResultDTO.  # noqa: E501
        :type: int
        """

        self._data_query_max_count = data_query_max_count

    @property
    def editable(self):
        """Gets the editable of this GetConfigurationResultDTO.  # noqa: E501


        :return: The editable of this GetConfigurationResultDTO.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this GetConfigurationResultDTO.


        :param editable: The editable of this GetConfigurationResultDTO.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def quad_tree_configuration(self):
        """Gets the quad_tree_configuration of this GetConfigurationResultDTO.  # noqa: E501


        :return: The quad_tree_configuration of this GetConfigurationResultDTO.  # noqa: E501
        :rtype: QuadTreeConfigurationDTO
        """
        return self._quad_tree_configuration

    @quad_tree_configuration.setter
    def quad_tree_configuration(self, quad_tree_configuration):
        """Sets the quad_tree_configuration of this GetConfigurationResultDTO.


        :param quad_tree_configuration: The quad_tree_configuration of this GetConfigurationResultDTO.  # noqa: E501
        :type: QuadTreeConfigurationDTO
        """

        self._quad_tree_configuration = quad_tree_configuration

    @property
    def editable_tm(self):
        """Gets the editable_tm of this GetConfigurationResultDTO.  # noqa: E501


        :return: The editable_tm of this GetConfigurationResultDTO.  # noqa: E501
        :rtype: bool
        """
        return self._editable_tm

    @editable_tm.setter
    def editable_tm(self, editable_tm):
        """Sets the editable_tm of this GetConfigurationResultDTO.


        :param editable_tm: The editable_tm of this GetConfigurationResultDTO.  # noqa: E501
        :type: bool
        """

        self._editable_tm = editable_tm

    @property
    def maximum_cluster_zoom_level(self):
        """Gets the maximum_cluster_zoom_level of this GetConfigurationResultDTO.  # noqa: E501


        :return: The maximum_cluster_zoom_level of this GetConfigurationResultDTO.  # noqa: E501
        :rtype: int
        """
        return self._maximum_cluster_zoom_level

    @maximum_cluster_zoom_level.setter
    def maximum_cluster_zoom_level(self, maximum_cluster_zoom_level):
        """Sets the maximum_cluster_zoom_level of this GetConfigurationResultDTO.


        :param maximum_cluster_zoom_level: The maximum_cluster_zoom_level of this GetConfigurationResultDTO.  # noqa: E501
        :type: int
        """

        self._maximum_cluster_zoom_level = maximum_cluster_zoom_level

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
        if issubclass(GetConfigurationResultDTO, dict):
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
        if not isinstance(other, GetConfigurationResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
