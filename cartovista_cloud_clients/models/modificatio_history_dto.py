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

class ModificatioHistoryDTO(object):
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
        'object_id': 'str',
        'modification_time': 'datetime',
        'modification_type': 'str',
        'full_name': 'str',
        'additional_information': 'str',
        'object_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'object_id': 'objectId',
        'modification_time': 'modificationTime',
        'modification_type': 'modificationType',
        'full_name': 'fullName',
        'additional_information': 'additionalInformation',
        'object_name': 'objectName'
    }

    def __init__(self, id=None, object_id=None, modification_time=None, modification_type=None, full_name=None, additional_information=None, object_name=None):  # noqa: E501
        """ModificatioHistoryDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._object_id = None
        self._modification_time = None
        self._modification_type = None
        self._full_name = None
        self._additional_information = None
        self._object_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if object_id is not None:
            self.object_id = object_id
        if modification_time is not None:
            self.modification_time = modification_time
        if modification_type is not None:
            self.modification_type = modification_type
        if full_name is not None:
            self.full_name = full_name
        if additional_information is not None:
            self.additional_information = additional_information
        if object_name is not None:
            self.object_name = object_name

    @property
    def id(self):
        """Gets the id of this ModificatioHistoryDTO.  # noqa: E501


        :return: The id of this ModificatioHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModificatioHistoryDTO.


        :param id: The id of this ModificatioHistoryDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def object_id(self):
        """Gets the object_id of this ModificatioHistoryDTO.  # noqa: E501


        :return: The object_id of this ModificatioHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this ModificatioHistoryDTO.


        :param object_id: The object_id of this ModificatioHistoryDTO.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def modification_time(self):
        """Gets the modification_time of this ModificatioHistoryDTO.  # noqa: E501


        :return: The modification_time of this ModificatioHistoryDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._modification_time

    @modification_time.setter
    def modification_time(self, modification_time):
        """Sets the modification_time of this ModificatioHistoryDTO.


        :param modification_time: The modification_time of this ModificatioHistoryDTO.  # noqa: E501
        :type: datetime
        """

        self._modification_time = modification_time

    @property
    def modification_type(self):
        """Gets the modification_type of this ModificatioHistoryDTO.  # noqa: E501


        :return: The modification_type of this ModificatioHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._modification_type

    @modification_type.setter
    def modification_type(self, modification_type):
        """Sets the modification_type of this ModificatioHistoryDTO.


        :param modification_type: The modification_type of this ModificatioHistoryDTO.  # noqa: E501
        :type: str
        """

        self._modification_type = modification_type

    @property
    def full_name(self):
        """Gets the full_name of this ModificatioHistoryDTO.  # noqa: E501


        :return: The full_name of this ModificatioHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this ModificatioHistoryDTO.


        :param full_name: The full_name of this ModificatioHistoryDTO.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def additional_information(self):
        """Gets the additional_information of this ModificatioHistoryDTO.  # noqa: E501


        :return: The additional_information of this ModificatioHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """Sets the additional_information of this ModificatioHistoryDTO.


        :param additional_information: The additional_information of this ModificatioHistoryDTO.  # noqa: E501
        :type: str
        """

        self._additional_information = additional_information

    @property
    def object_name(self):
        """Gets the object_name of this ModificatioHistoryDTO.  # noqa: E501


        :return: The object_name of this ModificatioHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this ModificatioHistoryDTO.


        :param object_name: The object_name of this ModificatioHistoryDTO.  # noqa: E501
        :type: str
        """

        self._object_name = object_name

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
        if issubclass(ModificatioHistoryDTO, dict):
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
        if not isinstance(other, ModificatioHistoryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other