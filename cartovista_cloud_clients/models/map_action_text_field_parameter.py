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

class MapActionTextFieldParameter(object):
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
        'hint': 'str',
        'placeholder': 'str',
        'spatial_autofill_returns_id': 'str',
        'disabled': 'bool',
        'returns': 'list[MapActionParameterReturnOfTextFieldReturnsEnum]',
        'type': 'MapActionParameterType'
    }

    attribute_map = {
        'name': 'name',
        'hint': 'hint',
        'placeholder': 'placeholder',
        'spatial_autofill_returns_id': 'spatialAutofillReturnsId',
        'disabled': 'disabled',
        'returns': 'returns',
        'type': 'type'
    }

    def __init__(self, name=None, hint=None, placeholder=None, spatial_autofill_returns_id=None, disabled=None, returns=None, type=None):  # noqa: E501
        """MapActionTextFieldParameter - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._hint = None
        self._placeholder = None
        self._spatial_autofill_returns_id = None
        self._disabled = None
        self._returns = None
        self._type = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if hint is not None:
            self.hint = hint
        if placeholder is not None:
            self.placeholder = placeholder
        if spatial_autofill_returns_id is not None:
            self.spatial_autofill_returns_id = spatial_autofill_returns_id
        if disabled is not None:
            self.disabled = disabled
        if returns is not None:
            self.returns = returns
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this MapActionTextFieldParameter.  # noqa: E501


        :return: The name of this MapActionTextFieldParameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MapActionTextFieldParameter.


        :param name: The name of this MapActionTextFieldParameter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def hint(self):
        """Gets the hint of this MapActionTextFieldParameter.  # noqa: E501


        :return: The hint of this MapActionTextFieldParameter.  # noqa: E501
        :rtype: str
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        """Sets the hint of this MapActionTextFieldParameter.


        :param hint: The hint of this MapActionTextFieldParameter.  # noqa: E501
        :type: str
        """

        self._hint = hint

    @property
    def placeholder(self):
        """Gets the placeholder of this MapActionTextFieldParameter.  # noqa: E501


        :return: The placeholder of this MapActionTextFieldParameter.  # noqa: E501
        :rtype: str
        """
        return self._placeholder

    @placeholder.setter
    def placeholder(self, placeholder):
        """Sets the placeholder of this MapActionTextFieldParameter.


        :param placeholder: The placeholder of this MapActionTextFieldParameter.  # noqa: E501
        :type: str
        """

        self._placeholder = placeholder

    @property
    def spatial_autofill_returns_id(self):
        """Gets the spatial_autofill_returns_id of this MapActionTextFieldParameter.  # noqa: E501


        :return: The spatial_autofill_returns_id of this MapActionTextFieldParameter.  # noqa: E501
        :rtype: str
        """
        return self._spatial_autofill_returns_id

    @spatial_autofill_returns_id.setter
    def spatial_autofill_returns_id(self, spatial_autofill_returns_id):
        """Sets the spatial_autofill_returns_id of this MapActionTextFieldParameter.


        :param spatial_autofill_returns_id: The spatial_autofill_returns_id of this MapActionTextFieldParameter.  # noqa: E501
        :type: str
        """

        self._spatial_autofill_returns_id = spatial_autofill_returns_id

    @property
    def disabled(self):
        """Gets the disabled of this MapActionTextFieldParameter.  # noqa: E501


        :return: The disabled of this MapActionTextFieldParameter.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this MapActionTextFieldParameter.


        :param disabled: The disabled of this MapActionTextFieldParameter.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def returns(self):
        """Gets the returns of this MapActionTextFieldParameter.  # noqa: E501


        :return: The returns of this MapActionTextFieldParameter.  # noqa: E501
        :rtype: list[MapActionParameterReturnOfTextFieldReturnsEnum]
        """
        return self._returns

    @returns.setter
    def returns(self, returns):
        """Sets the returns of this MapActionTextFieldParameter.


        :param returns: The returns of this MapActionTextFieldParameter.  # noqa: E501
        :type: list[MapActionParameterReturnOfTextFieldReturnsEnum]
        """

        self._returns = returns

    @property
    def type(self):
        """Gets the type of this MapActionTextFieldParameter.  # noqa: E501


        :return: The type of this MapActionTextFieldParameter.  # noqa: E501
        :rtype: MapActionParameterType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MapActionTextFieldParameter.


        :param type: The type of this MapActionTextFieldParameter.  # noqa: E501
        :type: MapActionParameterType
        """

        self._type = type

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
        if issubclass(MapActionTextFieldParameter, dict):
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
        if not isinstance(other, MapActionTextFieldParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
