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

class FileSheet(object):
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
        'sheet_name': 'str',
        'columns': 'list[FileColumn]'
    }

    attribute_map = {
        'sheet_name': 'sheetName',
        'columns': 'columns'
    }

    def __init__(self, sheet_name=None, columns=None):  # noqa: E501
        """FileSheet - a model defined in Swagger"""  # noqa: E501
        self._sheet_name = None
        self._columns = None
        self.discriminator = None
        if sheet_name is not None:
            self.sheet_name = sheet_name
        if columns is not None:
            self.columns = columns

    @property
    def sheet_name(self):
        """Gets the sheet_name of this FileSheet.  # noqa: E501


        :return: The sheet_name of this FileSheet.  # noqa: E501
        :rtype: str
        """
        return self._sheet_name

    @sheet_name.setter
    def sheet_name(self, sheet_name):
        """Sets the sheet_name of this FileSheet.


        :param sheet_name: The sheet_name of this FileSheet.  # noqa: E501
        :type: str
        """

        self._sheet_name = sheet_name

    @property
    def columns(self):
        """Gets the columns of this FileSheet.  # noqa: E501


        :return: The columns of this FileSheet.  # noqa: E501
        :rtype: list[FileColumn]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this FileSheet.


        :param columns: The columns of this FileSheet.  # noqa: E501
        :type: list[FileColumn]
        """

        self._columns = columns

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
        if issubclass(FileSheet, dict):
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
        if not isinstance(other, FileSheet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
