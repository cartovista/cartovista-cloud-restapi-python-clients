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

class AnalysisDataTableDTO(object):
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
        'src': 'str',
        'join_column_id': 'str',
        'source_id': 'str',
        'layer_source_id': 'str',
        'data_table_join_id': 'str',
        'server_cache_enabled': 'bool',
        'data_column': 'DataTableColumnDTO'
    }

    attribute_map = {
        'id': 'id',
        'src': 'src',
        'join_column_id': 'joinColumnId',
        'source_id': 'sourceId',
        'layer_source_id': 'layerSourceId',
        'data_table_join_id': 'dataTableJoinId',
        'server_cache_enabled': 'serverCacheEnabled',
        'data_column': 'dataColumn'
    }

    def __init__(self, id=None, src=None, join_column_id=None, source_id=None, layer_source_id=None, data_table_join_id=None, server_cache_enabled=None, data_column=None):  # noqa: E501
        """AnalysisDataTableDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._src = None
        self._join_column_id = None
        self._source_id = None
        self._layer_source_id = None
        self._data_table_join_id = None
        self._server_cache_enabled = None
        self._data_column = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if src is not None:
            self.src = src
        if join_column_id is not None:
            self.join_column_id = join_column_id
        if source_id is not None:
            self.source_id = source_id
        if layer_source_id is not None:
            self.layer_source_id = layer_source_id
        if data_table_join_id is not None:
            self.data_table_join_id = data_table_join_id
        if server_cache_enabled is not None:
            self.server_cache_enabled = server_cache_enabled
        if data_column is not None:
            self.data_column = data_column

    @property
    def id(self):
        """Gets the id of this AnalysisDataTableDTO.  # noqa: E501


        :return: The id of this AnalysisDataTableDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnalysisDataTableDTO.


        :param id: The id of this AnalysisDataTableDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def src(self):
        """Gets the src of this AnalysisDataTableDTO.  # noqa: E501


        :return: The src of this AnalysisDataTableDTO.  # noqa: E501
        :rtype: str
        """
        return self._src

    @src.setter
    def src(self, src):
        """Sets the src of this AnalysisDataTableDTO.


        :param src: The src of this AnalysisDataTableDTO.  # noqa: E501
        :type: str
        """

        self._src = src

    @property
    def join_column_id(self):
        """Gets the join_column_id of this AnalysisDataTableDTO.  # noqa: E501


        :return: The join_column_id of this AnalysisDataTableDTO.  # noqa: E501
        :rtype: str
        """
        return self._join_column_id

    @join_column_id.setter
    def join_column_id(self, join_column_id):
        """Sets the join_column_id of this AnalysisDataTableDTO.


        :param join_column_id: The join_column_id of this AnalysisDataTableDTO.  # noqa: E501
        :type: str
        """

        self._join_column_id = join_column_id

    @property
    def source_id(self):
        """Gets the source_id of this AnalysisDataTableDTO.  # noqa: E501


        :return: The source_id of this AnalysisDataTableDTO.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this AnalysisDataTableDTO.


        :param source_id: The source_id of this AnalysisDataTableDTO.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def layer_source_id(self):
        """Gets the layer_source_id of this AnalysisDataTableDTO.  # noqa: E501


        :return: The layer_source_id of this AnalysisDataTableDTO.  # noqa: E501
        :rtype: str
        """
        return self._layer_source_id

    @layer_source_id.setter
    def layer_source_id(self, layer_source_id):
        """Sets the layer_source_id of this AnalysisDataTableDTO.


        :param layer_source_id: The layer_source_id of this AnalysisDataTableDTO.  # noqa: E501
        :type: str
        """

        self._layer_source_id = layer_source_id

    @property
    def data_table_join_id(self):
        """Gets the data_table_join_id of this AnalysisDataTableDTO.  # noqa: E501


        :return: The data_table_join_id of this AnalysisDataTableDTO.  # noqa: E501
        :rtype: str
        """
        return self._data_table_join_id

    @data_table_join_id.setter
    def data_table_join_id(self, data_table_join_id):
        """Sets the data_table_join_id of this AnalysisDataTableDTO.


        :param data_table_join_id: The data_table_join_id of this AnalysisDataTableDTO.  # noqa: E501
        :type: str
        """

        self._data_table_join_id = data_table_join_id

    @property
    def server_cache_enabled(self):
        """Gets the server_cache_enabled of this AnalysisDataTableDTO.  # noqa: E501


        :return: The server_cache_enabled of this AnalysisDataTableDTO.  # noqa: E501
        :rtype: bool
        """
        return self._server_cache_enabled

    @server_cache_enabled.setter
    def server_cache_enabled(self, server_cache_enabled):
        """Sets the server_cache_enabled of this AnalysisDataTableDTO.


        :param server_cache_enabled: The server_cache_enabled of this AnalysisDataTableDTO.  # noqa: E501
        :type: bool
        """

        self._server_cache_enabled = server_cache_enabled

    @property
    def data_column(self):
        """Gets the data_column of this AnalysisDataTableDTO.  # noqa: E501


        :return: The data_column of this AnalysisDataTableDTO.  # noqa: E501
        :rtype: DataTableColumnDTO
        """
        return self._data_column

    @data_column.setter
    def data_column(self, data_column):
        """Sets the data_column of this AnalysisDataTableDTO.


        :param data_column: The data_column of this AnalysisDataTableDTO.  # noqa: E501
        :type: DataTableColumnDTO
        """

        self._data_column = data_column

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
        if issubclass(AnalysisDataTableDTO, dict):
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
        if not isinstance(other, AnalysisDataTableDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
