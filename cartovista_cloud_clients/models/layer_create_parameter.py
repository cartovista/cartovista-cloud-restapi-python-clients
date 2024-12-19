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

class LayerCreateParameter(object):
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
        'identifier': 'str',
        'proj4': 'str',
        'name': 'str',
        'metadata': 'str',
        'geometry_type': 'str',
        'description': 'str',
        'vector_tiling': 'bool',
        'live': 'bool',
        'system_identifier': 'str',
        'data_table_system_identifier': 'str',
        'feature_id_column_system_identifier': 'str',
        'folder_id': 'str'
    }

    attribute_map = {
        'identifier': 'identifier',
        'proj4': 'proj4',
        'name': 'name',
        'metadata': 'metadata',
        'geometry_type': 'geometryType',
        'description': 'description',
        'vector_tiling': 'vectorTiling',
        'live': 'live',
        'system_identifier': 'systemIdentifier',
        'data_table_system_identifier': 'dataTableSystemIdentifier',
        'feature_id_column_system_identifier': 'featureIdColumnSystemIdentifier',
        'folder_id': 'folderId'
    }

    def __init__(self, identifier=None, proj4=None, name=None, metadata=None, geometry_type=None, description=None, vector_tiling=None, live=None, system_identifier=None, data_table_system_identifier=None, feature_id_column_system_identifier=None, folder_id=None):  # noqa: E501
        """LayerCreateParameter - a model defined in Swagger"""  # noqa: E501
        self._identifier = None
        self._proj4 = None
        self._name = None
        self._metadata = None
        self._geometry_type = None
        self._description = None
        self._vector_tiling = None
        self._live = None
        self._system_identifier = None
        self._data_table_system_identifier = None
        self._feature_id_column_system_identifier = None
        self._folder_id = None
        self.discriminator = None
        if identifier is not None:
            self.identifier = identifier
        if proj4 is not None:
            self.proj4 = proj4
        if name is not None:
            self.name = name
        if metadata is not None:
            self.metadata = metadata
        if geometry_type is not None:
            self.geometry_type = geometry_type
        if description is not None:
            self.description = description
        if vector_tiling is not None:
            self.vector_tiling = vector_tiling
        if live is not None:
            self.live = live
        if system_identifier is not None:
            self.system_identifier = system_identifier
        if data_table_system_identifier is not None:
            self.data_table_system_identifier = data_table_system_identifier
        if feature_id_column_system_identifier is not None:
            self.feature_id_column_system_identifier = feature_id_column_system_identifier
        if folder_id is not None:
            self.folder_id = folder_id

    @property
    def identifier(self):
        """Gets the identifier of this LayerCreateParameter.  # noqa: E501


        :return: The identifier of this LayerCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this LayerCreateParameter.


        :param identifier: The identifier of this LayerCreateParameter.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def proj4(self):
        """Gets the proj4 of this LayerCreateParameter.  # noqa: E501


        :return: The proj4 of this LayerCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._proj4

    @proj4.setter
    def proj4(self, proj4):
        """Sets the proj4 of this LayerCreateParameter.


        :param proj4: The proj4 of this LayerCreateParameter.  # noqa: E501
        :type: str
        """

        self._proj4 = proj4

    @property
    def name(self):
        """Gets the name of this LayerCreateParameter.  # noqa: E501


        :return: The name of this LayerCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LayerCreateParameter.


        :param name: The name of this LayerCreateParameter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this LayerCreateParameter.  # noqa: E501


        :return: The metadata of this LayerCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this LayerCreateParameter.


        :param metadata: The metadata of this LayerCreateParameter.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def geometry_type(self):
        """Gets the geometry_type of this LayerCreateParameter.  # noqa: E501


        :return: The geometry_type of this LayerCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._geometry_type

    @geometry_type.setter
    def geometry_type(self, geometry_type):
        """Sets the geometry_type of this LayerCreateParameter.


        :param geometry_type: The geometry_type of this LayerCreateParameter.  # noqa: E501
        :type: str
        """

        self._geometry_type = geometry_type

    @property
    def description(self):
        """Gets the description of this LayerCreateParameter.  # noqa: E501


        :return: The description of this LayerCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LayerCreateParameter.


        :param description: The description of this LayerCreateParameter.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def vector_tiling(self):
        """Gets the vector_tiling of this LayerCreateParameter.  # noqa: E501


        :return: The vector_tiling of this LayerCreateParameter.  # noqa: E501
        :rtype: bool
        """
        return self._vector_tiling

    @vector_tiling.setter
    def vector_tiling(self, vector_tiling):
        """Sets the vector_tiling of this LayerCreateParameter.


        :param vector_tiling: The vector_tiling of this LayerCreateParameter.  # noqa: E501
        :type: bool
        """

        self._vector_tiling = vector_tiling

    @property
    def live(self):
        """Gets the live of this LayerCreateParameter.  # noqa: E501


        :return: The live of this LayerCreateParameter.  # noqa: E501
        :rtype: bool
        """
        return self._live

    @live.setter
    def live(self, live):
        """Sets the live of this LayerCreateParameter.


        :param live: The live of this LayerCreateParameter.  # noqa: E501
        :type: bool
        """

        self._live = live

    @property
    def system_identifier(self):
        """Gets the system_identifier of this LayerCreateParameter.  # noqa: E501


        :return: The system_identifier of this LayerCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._system_identifier

    @system_identifier.setter
    def system_identifier(self, system_identifier):
        """Sets the system_identifier of this LayerCreateParameter.


        :param system_identifier: The system_identifier of this LayerCreateParameter.  # noqa: E501
        :type: str
        """

        self._system_identifier = system_identifier

    @property
    def data_table_system_identifier(self):
        """Gets the data_table_system_identifier of this LayerCreateParameter.  # noqa: E501


        :return: The data_table_system_identifier of this LayerCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._data_table_system_identifier

    @data_table_system_identifier.setter
    def data_table_system_identifier(self, data_table_system_identifier):
        """Sets the data_table_system_identifier of this LayerCreateParameter.


        :param data_table_system_identifier: The data_table_system_identifier of this LayerCreateParameter.  # noqa: E501
        :type: str
        """

        self._data_table_system_identifier = data_table_system_identifier

    @property
    def feature_id_column_system_identifier(self):
        """Gets the feature_id_column_system_identifier of this LayerCreateParameter.  # noqa: E501


        :return: The feature_id_column_system_identifier of this LayerCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._feature_id_column_system_identifier

    @feature_id_column_system_identifier.setter
    def feature_id_column_system_identifier(self, feature_id_column_system_identifier):
        """Sets the feature_id_column_system_identifier of this LayerCreateParameter.


        :param feature_id_column_system_identifier: The feature_id_column_system_identifier of this LayerCreateParameter.  # noqa: E501
        :type: str
        """

        self._feature_id_column_system_identifier = feature_id_column_system_identifier

    @property
    def folder_id(self):
        """Gets the folder_id of this LayerCreateParameter.  # noqa: E501


        :return: The folder_id of this LayerCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this LayerCreateParameter.


        :param folder_id: The folder_id of this LayerCreateParameter.  # noqa: E501
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
        if issubclass(LayerCreateParameter, dict):
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
        if not isinstance(other, LayerCreateParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
