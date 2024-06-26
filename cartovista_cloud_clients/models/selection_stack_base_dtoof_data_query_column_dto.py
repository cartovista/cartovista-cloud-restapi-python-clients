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

class SelectionStackBaseDTOOfDataQueryColumnDTO(object):
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
        'stack_id': 'str',
        'intersect': 'bool',
        'stack_type': 'SelectionStackEnum'
    }

    attribute_map = {
        'stack_id': 'stackId',
        'intersect': 'intersect',
        'stack_type': 'stackType'
    }

    def __init__(self, stack_id=None, intersect=None, stack_type=None):  # noqa: E501
        """SelectionStackBaseDTOOfDataQueryColumnDTO - a model defined in Swagger"""  # noqa: E501
        self._stack_id = None
        self._intersect = None
        self._stack_type = None
        self.discriminator = None
        if stack_id is not None:
            self.stack_id = stack_id
        if intersect is not None:
            self.intersect = intersect
        if stack_type is not None:
            self.stack_type = stack_type

    @property
    def stack_id(self):
        """Gets the stack_id of this SelectionStackBaseDTOOfDataQueryColumnDTO.  # noqa: E501


        :return: The stack_id of this SelectionStackBaseDTOOfDataQueryColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this SelectionStackBaseDTOOfDataQueryColumnDTO.


        :param stack_id: The stack_id of this SelectionStackBaseDTOOfDataQueryColumnDTO.  # noqa: E501
        :type: str
        """

        self._stack_id = stack_id

    @property
    def intersect(self):
        """Gets the intersect of this SelectionStackBaseDTOOfDataQueryColumnDTO.  # noqa: E501


        :return: The intersect of this SelectionStackBaseDTOOfDataQueryColumnDTO.  # noqa: E501
        :rtype: bool
        """
        return self._intersect

    @intersect.setter
    def intersect(self, intersect):
        """Sets the intersect of this SelectionStackBaseDTOOfDataQueryColumnDTO.


        :param intersect: The intersect of this SelectionStackBaseDTOOfDataQueryColumnDTO.  # noqa: E501
        :type: bool
        """

        self._intersect = intersect

    @property
    def stack_type(self):
        """Gets the stack_type of this SelectionStackBaseDTOOfDataQueryColumnDTO.  # noqa: E501


        :return: The stack_type of this SelectionStackBaseDTOOfDataQueryColumnDTO.  # noqa: E501
        :rtype: SelectionStackEnum
        """
        return self._stack_type

    @stack_type.setter
    def stack_type(self, stack_type):
        """Sets the stack_type of this SelectionStackBaseDTOOfDataQueryColumnDTO.


        :param stack_type: The stack_type of this SelectionStackBaseDTOOfDataQueryColumnDTO.  # noqa: E501
        :type: SelectionStackEnum
        """

        self._stack_type = stack_type

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
        if issubclass(SelectionStackBaseDTOOfDataQueryColumnDTO, dict):
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
        if not isinstance(other, SelectionStackBaseDTOOfDataQueryColumnDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
