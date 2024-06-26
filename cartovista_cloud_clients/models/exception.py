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

class Exception(object):
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
        'message': 'str',
        'inner_exception': 'OneOfExceptionInnerException',
        'source': 'str',
        'stack_trace': 'str'
    }

    attribute_map = {
        'message': 'Message',
        'inner_exception': 'InnerException',
        'source': 'Source',
        'stack_trace': 'StackTrace'
    }

    def __init__(self, message=None, inner_exception=None, source=None, stack_trace=None):  # noqa: E501
        """Exception - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._inner_exception = None
        self._source = None
        self._stack_trace = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if inner_exception is not None:
            self.inner_exception = inner_exception
        if source is not None:
            self.source = source
        if stack_trace is not None:
            self.stack_trace = stack_trace

    @property
    def message(self):
        """Gets the message of this Exception.  # noqa: E501


        :return: The message of this Exception.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Exception.


        :param message: The message of this Exception.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def inner_exception(self):
        """Gets the inner_exception of this Exception.  # noqa: E501


        :return: The inner_exception of this Exception.  # noqa: E501
        :rtype: OneOfExceptionInnerException
        """
        return self._inner_exception

    @inner_exception.setter
    def inner_exception(self, inner_exception):
        """Sets the inner_exception of this Exception.


        :param inner_exception: The inner_exception of this Exception.  # noqa: E501
        :type: OneOfExceptionInnerException
        """

        self._inner_exception = inner_exception

    @property
    def source(self):
        """Gets the source of this Exception.  # noqa: E501


        :return: The source of this Exception.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Exception.


        :param source: The source of this Exception.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def stack_trace(self):
        """Gets the stack_trace of this Exception.  # noqa: E501


        :return: The stack_trace of this Exception.  # noqa: E501
        :rtype: str
        """
        return self._stack_trace

    @stack_trace.setter
    def stack_trace(self, stack_trace):
        """Sets the stack_trace of this Exception.


        :param stack_trace: The stack_trace of this Exception.  # noqa: E501
        :type: str
        """

        self._stack_trace = stack_trace

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
        if issubclass(Exception, dict):
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
        if not isinstance(other, Exception):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
