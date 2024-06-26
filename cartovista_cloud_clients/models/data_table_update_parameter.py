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

class DataTableUpdateParameter(object):
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
        'data_columns': 'list[DataColumnUpdateParameterExtended]'
    }

    attribute_map = {
        'name': 'name',
        'metadata': 'metadata',
        'description': 'description',
        'data_columns': 'dataColumns'
    }

    def __init__(self, name=None, metadata=None, description=None, data_columns=None):  # noqa: E501
        """DataTableUpdateParameter - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._metadata = None
        self._description = None
        self._data_columns = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if metadata is not None:
            self.metadata = metadata
        if description is not None:
            self.description = description
        if data_columns is not None:
            self.data_columns = data_columns

    @property
    def name(self):
        """Gets the name of this DataTableUpdateParameter.  # noqa: E501


        :return: The name of this DataTableUpdateParameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataTableUpdateParameter.


        :param name: The name of this DataTableUpdateParameter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this DataTableUpdateParameter.  # noqa: E501


        :return: The metadata of this DataTableUpdateParameter.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DataTableUpdateParameter.


        :param metadata: The metadata of this DataTableUpdateParameter.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def description(self):
        """Gets the description of this DataTableUpdateParameter.  # noqa: E501


        :return: The description of this DataTableUpdateParameter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataTableUpdateParameter.


        :param description: The description of this DataTableUpdateParameter.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def data_columns(self):
        """Gets the data_columns of this DataTableUpdateParameter.  # noqa: E501


        :return: The data_columns of this DataTableUpdateParameter.  # noqa: E501
        :rtype: list[DataColumnUpdateParameterExtended]
        """
        return self._data_columns

    @data_columns.setter
    def data_columns(self, data_columns):
        """Sets the data_columns of this DataTableUpdateParameter.


        :param data_columns: The data_columns of this DataTableUpdateParameter.  # noqa: E501
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
        if issubclass(DataTableUpdateParameter, dict):
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
        if not isinstance(other, DataTableUpdateParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
