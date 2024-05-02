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

class GenerateHeatmapParameter(object):
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
        'column_id': 'str',
        'power': 'float',
        'smoothing': 'float',
        'radius': 'float',
        'pixel_size': 'int',
        'name': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'column_id': 'columnId',
        'power': 'power',
        'smoothing': 'smoothing',
        'radius': 'radius',
        'pixel_size': 'pixelSize',
        'name': 'name',
        'unit': 'unit'
    }

    def __init__(self, column_id=None, power=None, smoothing=None, radius=None, pixel_size=None, name=None, unit=None):  # noqa: E501
        """GenerateHeatmapParameter - a model defined in Swagger"""  # noqa: E501
        self._column_id = None
        self._power = None
        self._smoothing = None
        self._radius = None
        self._pixel_size = None
        self._name = None
        self._unit = None
        self.discriminator = None
        if column_id is not None:
            self.column_id = column_id
        if power is not None:
            self.power = power
        if smoothing is not None:
            self.smoothing = smoothing
        if radius is not None:
            self.radius = radius
        if pixel_size is not None:
            self.pixel_size = pixel_size
        if name is not None:
            self.name = name
        if unit is not None:
            self.unit = unit

    @property
    def column_id(self):
        """Gets the column_id of this GenerateHeatmapParameter.  # noqa: E501


        :return: The column_id of this GenerateHeatmapParameter.  # noqa: E501
        :rtype: str
        """
        return self._column_id

    @column_id.setter
    def column_id(self, column_id):
        """Sets the column_id of this GenerateHeatmapParameter.


        :param column_id: The column_id of this GenerateHeatmapParameter.  # noqa: E501
        :type: str
        """

        self._column_id = column_id

    @property
    def power(self):
        """Gets the power of this GenerateHeatmapParameter.  # noqa: E501


        :return: The power of this GenerateHeatmapParameter.  # noqa: E501
        :rtype: float
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this GenerateHeatmapParameter.


        :param power: The power of this GenerateHeatmapParameter.  # noqa: E501
        :type: float
        """

        self._power = power

    @property
    def smoothing(self):
        """Gets the smoothing of this GenerateHeatmapParameter.  # noqa: E501


        :return: The smoothing of this GenerateHeatmapParameter.  # noqa: E501
        :rtype: float
        """
        return self._smoothing

    @smoothing.setter
    def smoothing(self, smoothing):
        """Sets the smoothing of this GenerateHeatmapParameter.


        :param smoothing: The smoothing of this GenerateHeatmapParameter.  # noqa: E501
        :type: float
        """

        self._smoothing = smoothing

    @property
    def radius(self):
        """Gets the radius of this GenerateHeatmapParameter.  # noqa: E501


        :return: The radius of this GenerateHeatmapParameter.  # noqa: E501
        :rtype: float
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Sets the radius of this GenerateHeatmapParameter.


        :param radius: The radius of this GenerateHeatmapParameter.  # noqa: E501
        :type: float
        """

        self._radius = radius

    @property
    def pixel_size(self):
        """Gets the pixel_size of this GenerateHeatmapParameter.  # noqa: E501


        :return: The pixel_size of this GenerateHeatmapParameter.  # noqa: E501
        :rtype: int
        """
        return self._pixel_size

    @pixel_size.setter
    def pixel_size(self, pixel_size):
        """Sets the pixel_size of this GenerateHeatmapParameter.


        :param pixel_size: The pixel_size of this GenerateHeatmapParameter.  # noqa: E501
        :type: int
        """

        self._pixel_size = pixel_size

    @property
    def name(self):
        """Gets the name of this GenerateHeatmapParameter.  # noqa: E501


        :return: The name of this GenerateHeatmapParameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GenerateHeatmapParameter.


        :param name: The name of this GenerateHeatmapParameter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def unit(self):
        """Gets the unit of this GenerateHeatmapParameter.  # noqa: E501


        :return: The unit of this GenerateHeatmapParameter.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this GenerateHeatmapParameter.


        :param unit: The unit of this GenerateHeatmapParameter.  # noqa: E501
        :type: str
        """

        self._unit = unit

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
        if issubclass(GenerateHeatmapParameter, dict):
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
        if not isinstance(other, GenerateHeatmapParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
