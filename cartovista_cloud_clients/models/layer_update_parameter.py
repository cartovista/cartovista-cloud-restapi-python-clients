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

class LayerUpdateParameter(object):
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
        'metadata': 'str',
        'description': 'str',
        'vector_tiling': 'bool',
        'precision': 'int',
        'is_live': 'bool',
        'external_service_live_feed': 'bool',
        'vector_quality_type': 'VectorQualityTypeEnum',
        'data_columns': 'list[DataColumnUpdateParameterExtended]'
    }

    attribute_map = {
        'name': 'name',
        'metadata': 'metadata',
        'description': 'description',
        'vector_tiling': 'vectorTiling',
        'precision': 'precision',
        'is_live': 'isLive',
        'external_service_live_feed': 'externalServiceLiveFeed',
        'vector_quality_type': 'vectorQualityType',
        'data_columns': 'dataColumns'
    }

    def __init__(self, name=None, metadata=None, description=None, vector_tiling=None, precision=None, is_live=None, external_service_live_feed=None, vector_quality_type=None, data_columns=None):  # noqa: E501
        """LayerUpdateParameter - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._metadata = None
        self._description = None
        self._vector_tiling = None
        self._precision = None
        self._is_live = None
        self._external_service_live_feed = None
        self._vector_quality_type = None
        self._data_columns = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if metadata is not None:
            self.metadata = metadata
        if description is not None:
            self.description = description
        if vector_tiling is not None:
            self.vector_tiling = vector_tiling
        if precision is not None:
            self.precision = precision
        if is_live is not None:
            self.is_live = is_live
        if external_service_live_feed is not None:
            self.external_service_live_feed = external_service_live_feed
        if vector_quality_type is not None:
            self.vector_quality_type = vector_quality_type
        if data_columns is not None:
            self.data_columns = data_columns

    @property
    def name(self):
        """Gets the name of this LayerUpdateParameter.  # noqa: E501


        :return: The name of this LayerUpdateParameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LayerUpdateParameter.


        :param name: The name of this LayerUpdateParameter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this LayerUpdateParameter.  # noqa: E501


        :return: The metadata of this LayerUpdateParameter.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this LayerUpdateParameter.


        :param metadata: The metadata of this LayerUpdateParameter.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def description(self):
        """Gets the description of this LayerUpdateParameter.  # noqa: E501


        :return: The description of this LayerUpdateParameter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LayerUpdateParameter.


        :param description: The description of this LayerUpdateParameter.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def vector_tiling(self):
        """Gets the vector_tiling of this LayerUpdateParameter.  # noqa: E501


        :return: The vector_tiling of this LayerUpdateParameter.  # noqa: E501
        :rtype: bool
        """
        return self._vector_tiling

    @vector_tiling.setter
    def vector_tiling(self, vector_tiling):
        """Sets the vector_tiling of this LayerUpdateParameter.


        :param vector_tiling: The vector_tiling of this LayerUpdateParameter.  # noqa: E501
        :type: bool
        """

        self._vector_tiling = vector_tiling

    @property
    def precision(self):
        """Gets the precision of this LayerUpdateParameter.  # noqa: E501


        :return: The precision of this LayerUpdateParameter.  # noqa: E501
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this LayerUpdateParameter.


        :param precision: The precision of this LayerUpdateParameter.  # noqa: E501
        :type: int
        """

        self._precision = precision

    @property
    def is_live(self):
        """Gets the is_live of this LayerUpdateParameter.  # noqa: E501


        :return: The is_live of this LayerUpdateParameter.  # noqa: E501
        :rtype: bool
        """
        return self._is_live

    @is_live.setter
    def is_live(self, is_live):
        """Sets the is_live of this LayerUpdateParameter.


        :param is_live: The is_live of this LayerUpdateParameter.  # noqa: E501
        :type: bool
        """

        self._is_live = is_live

    @property
    def external_service_live_feed(self):
        """Gets the external_service_live_feed of this LayerUpdateParameter.  # noqa: E501


        :return: The external_service_live_feed of this LayerUpdateParameter.  # noqa: E501
        :rtype: bool
        """
        return self._external_service_live_feed

    @external_service_live_feed.setter
    def external_service_live_feed(self, external_service_live_feed):
        """Sets the external_service_live_feed of this LayerUpdateParameter.


        :param external_service_live_feed: The external_service_live_feed of this LayerUpdateParameter.  # noqa: E501
        :type: bool
        """

        self._external_service_live_feed = external_service_live_feed

    @property
    def vector_quality_type(self):
        """Gets the vector_quality_type of this LayerUpdateParameter.  # noqa: E501


        :return: The vector_quality_type of this LayerUpdateParameter.  # noqa: E501
        :rtype: VectorQualityTypeEnum
        """
        return self._vector_quality_type

    @vector_quality_type.setter
    def vector_quality_type(self, vector_quality_type):
        """Sets the vector_quality_type of this LayerUpdateParameter.


        :param vector_quality_type: The vector_quality_type of this LayerUpdateParameter.  # noqa: E501
        :type: VectorQualityTypeEnum
        """

        self._vector_quality_type = vector_quality_type

    @property
    def data_columns(self):
        """Gets the data_columns of this LayerUpdateParameter.  # noqa: E501


        :return: The data_columns of this LayerUpdateParameter.  # noqa: E501
        :rtype: list[DataColumnUpdateParameterExtended]
        """
        return self._data_columns

    @data_columns.setter
    def data_columns(self, data_columns):
        """Sets the data_columns of this LayerUpdateParameter.


        :param data_columns: The data_columns of this LayerUpdateParameter.  # noqa: E501
        :type: list[DataColumnUpdateParameterExtended]
        """

        self._data_columns = data_columns

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
        if issubclass(LayerUpdateParameter, dict):
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
        if not isinstance(other, LayerUpdateParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other