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

class VariableWithUpdatedWeightsDTO(object):
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
        'variable': 'VariableDTO',
        'updated_weights': 'list[PairVariableIdWeightDTO]'
    }

    attribute_map = {
        'variable': 'variable',
        'updated_weights': 'updatedWeights'
    }

    def __init__(self, variable=None, updated_weights=None):  # noqa: E501
        """VariableWithUpdatedWeightsDTO - a model defined in Swagger"""  # noqa: E501
        self._variable = None
        self._updated_weights = None
        self.discriminator = None
        if variable is not None:
            self.variable = variable
        if updated_weights is not None:
            self.updated_weights = updated_weights

    @property
    def variable(self):
        """Gets the variable of this VariableWithUpdatedWeightsDTO.  # noqa: E501


        :return: The variable of this VariableWithUpdatedWeightsDTO.  # noqa: E501
        :rtype: VariableDTO
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this VariableWithUpdatedWeightsDTO.


        :param variable: The variable of this VariableWithUpdatedWeightsDTO.  # noqa: E501
        :type: VariableDTO
        """

        self._variable = variable

    @property
    def updated_weights(self):
        """Gets the updated_weights of this VariableWithUpdatedWeightsDTO.  # noqa: E501


        :return: The updated_weights of this VariableWithUpdatedWeightsDTO.  # noqa: E501
        :rtype: list[PairVariableIdWeightDTO]
        """
        return self._updated_weights

    @updated_weights.setter
    def updated_weights(self, updated_weights):
        """Sets the updated_weights of this VariableWithUpdatedWeightsDTO.


        :param updated_weights: The updated_weights of this VariableWithUpdatedWeightsDTO.  # noqa: E501
        :type: list[PairVariableIdWeightDTO]
        """

        self._updated_weights = updated_weights

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
        if issubclass(VariableWithUpdatedWeightsDTO, dict):
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
        if not isinstance(other, VariableWithUpdatedWeightsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
