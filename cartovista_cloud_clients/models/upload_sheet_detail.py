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

class UploadSheetDetail(object):
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
        'columns_tokeep': 'list[FinalizeColumnUploadParameters]',
        'lat_long_columns': 'OneOfUploadSheetDetailLatLongColumns',
        'address_columns': 'OneOfUploadSheetDetailAddressColumns'
    }

    attribute_map = {
        'sheet_name': 'sheetName',
        'columns_tokeep': 'columnsTokeep',
        'lat_long_columns': 'latLongColumns',
        'address_columns': 'addressColumns'
    }

    def __init__(self, sheet_name=None, columns_tokeep=None, lat_long_columns=None, address_columns=None):  # noqa: E501
        """UploadSheetDetail - a model defined in Swagger"""  # noqa: E501
        self._sheet_name = None
        self._columns_tokeep = None
        self._lat_long_columns = None
        self._address_columns = None
        self.discriminator = None
        if sheet_name is not None:
            self.sheet_name = sheet_name
        if columns_tokeep is not None:
            self.columns_tokeep = columns_tokeep
        if lat_long_columns is not None:
            self.lat_long_columns = lat_long_columns
        if address_columns is not None:
            self.address_columns = address_columns

    @property
    def sheet_name(self):
        """Gets the sheet_name of this UploadSheetDetail.  # noqa: E501


        :return: The sheet_name of this UploadSheetDetail.  # noqa: E501
        :rtype: str
        """
        return self._sheet_name

    @sheet_name.setter
    def sheet_name(self, sheet_name):
        """Sets the sheet_name of this UploadSheetDetail.


        :param sheet_name: The sheet_name of this UploadSheetDetail.  # noqa: E501
        :type: str
        """

        self._sheet_name = sheet_name

    @property
    def columns_tokeep(self):
        """Gets the columns_tokeep of this UploadSheetDetail.  # noqa: E501


        :return: The columns_tokeep of this UploadSheetDetail.  # noqa: E501
        :rtype: list[FinalizeColumnUploadParameters]
        """
        return self._columns_tokeep

    @columns_tokeep.setter
    def columns_tokeep(self, columns_tokeep):
        """Sets the columns_tokeep of this UploadSheetDetail.


        :param columns_tokeep: The columns_tokeep of this UploadSheetDetail.  # noqa: E501
        :type: list[FinalizeColumnUploadParameters]
        """

        self._columns_tokeep = columns_tokeep

    @property
    def lat_long_columns(self):
        """Gets the lat_long_columns of this UploadSheetDetail.  # noqa: E501


        :return: The lat_long_columns of this UploadSheetDetail.  # noqa: E501
        :rtype: OneOfUploadSheetDetailLatLongColumns
        """
        return self._lat_long_columns

    @lat_long_columns.setter
    def lat_long_columns(self, lat_long_columns):
        """Sets the lat_long_columns of this UploadSheetDetail.


        :param lat_long_columns: The lat_long_columns of this UploadSheetDetail.  # noqa: E501
        :type: OneOfUploadSheetDetailLatLongColumns
        """

        self._lat_long_columns = lat_long_columns

    @property
    def address_columns(self):
        """Gets the address_columns of this UploadSheetDetail.  # noqa: E501


        :return: The address_columns of this UploadSheetDetail.  # noqa: E501
        :rtype: OneOfUploadSheetDetailAddressColumns
        """
        return self._address_columns

    @address_columns.setter
    def address_columns(self, address_columns):
        """Sets the address_columns of this UploadSheetDetail.


        :param address_columns: The address_columns of this UploadSheetDetail.  # noqa: E501
        :type: OneOfUploadSheetDetailAddressColumns
        """

        self._address_columns = address_columns

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
        if issubclass(UploadSheetDetail, dict):
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
        if not isinstance(other, UploadSheetDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other