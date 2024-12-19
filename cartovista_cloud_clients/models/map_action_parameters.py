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

class MapActionParameters(object):
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
        'spatial_parameters': 'list[MapActionSpatialParameter]',
        'parameters': 'list[MapActionParameter]'
    }

    attribute_map = {
        'spatial_parameters': 'spatialParameters',
        'parameters': 'parameters'
    }

    def __init__(self, spatial_parameters=None, parameters=None):  # noqa: E501
        """MapActionParameters - a model defined in Swagger"""  # noqa: E501
        self._spatial_parameters = None
        self._parameters = None
        self.discriminator = None
        if spatial_parameters is not None:
            self.spatial_parameters = spatial_parameters
        if parameters is not None:
            self.parameters = parameters

    @property
    def spatial_parameters(self):
        """Gets the spatial_parameters of this MapActionParameters.  # noqa: E501


        :return: The spatial_parameters of this MapActionParameters.  # noqa: E501
        :rtype: list[MapActionSpatialParameter]
        """
        return self._spatial_parameters

    @spatial_parameters.setter
    def spatial_parameters(self, spatial_parameters):
        """Sets the spatial_parameters of this MapActionParameters.


        :param spatial_parameters: The spatial_parameters of this MapActionParameters.  # noqa: E501
        :type: list[MapActionSpatialParameter]
        """

        self._spatial_parameters = spatial_parameters

    @property
    def parameters(self):
        """Gets the parameters of this MapActionParameters.  # noqa: E501


        :return: The parameters of this MapActionParameters.  # noqa: E501
        :rtype: list[MapActionParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this MapActionParameters.


        :param parameters: The parameters of this MapActionParameters.  # noqa: E501
        :type: list[MapActionParameter]
        """

        self._parameters = parameters

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
        if issubclass(MapActionParameters, dict):
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
        if not isinstance(other, MapActionParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
