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

class ThematicAnalysisSettings(object):
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
        'range_calculation_method': 'str',
        'range_palette': 'str',
        'range_overlay_palette': 'str',
        'fill_pattern_color': 'str',
        'not_available_color': 'str'
    }

    attribute_map = {
        'range_calculation_method': 'rangeCalculationMethod',
        'range_palette': 'rangePalette',
        'range_overlay_palette': 'rangeOverlayPalette',
        'fill_pattern_color': 'fillPatternColor',
        'not_available_color': 'notAvailableColor'
    }

    def __init__(self, range_calculation_method=None, range_palette=None, range_overlay_palette=None, fill_pattern_color=None, not_available_color=None):  # noqa: E501
        """ThematicAnalysisSettings - a model defined in Swagger"""  # noqa: E501
        self._range_calculation_method = None
        self._range_palette = None
        self._range_overlay_palette = None
        self._fill_pattern_color = None
        self._not_available_color = None
        self.discriminator = None
        if range_calculation_method is not None:
            self.range_calculation_method = range_calculation_method
        if range_palette is not None:
            self.range_palette = range_palette
        if range_overlay_palette is not None:
            self.range_overlay_palette = range_overlay_palette
        if fill_pattern_color is not None:
            self.fill_pattern_color = fill_pattern_color
        if not_available_color is not None:
            self.not_available_color = not_available_color

    @property
    def range_calculation_method(self):
        """Gets the range_calculation_method of this ThematicAnalysisSettings.  # noqa: E501


        :return: The range_calculation_method of this ThematicAnalysisSettings.  # noqa: E501
        :rtype: str
        """
        return self._range_calculation_method

    @range_calculation_method.setter
    def range_calculation_method(self, range_calculation_method):
        """Sets the range_calculation_method of this ThematicAnalysisSettings.


        :param range_calculation_method: The range_calculation_method of this ThematicAnalysisSettings.  # noqa: E501
        :type: str
        """

        self._range_calculation_method = range_calculation_method

    @property
    def range_palette(self):
        """Gets the range_palette of this ThematicAnalysisSettings.  # noqa: E501


        :return: The range_palette of this ThematicAnalysisSettings.  # noqa: E501
        :rtype: str
        """
        return self._range_palette

    @range_palette.setter
    def range_palette(self, range_palette):
        """Sets the range_palette of this ThematicAnalysisSettings.


        :param range_palette: The range_palette of this ThematicAnalysisSettings.  # noqa: E501
        :type: str
        """

        self._range_palette = range_palette

    @property
    def range_overlay_palette(self):
        """Gets the range_overlay_palette of this ThematicAnalysisSettings.  # noqa: E501


        :return: The range_overlay_palette of this ThematicAnalysisSettings.  # noqa: E501
        :rtype: str
        """
        return self._range_overlay_palette

    @range_overlay_palette.setter
    def range_overlay_palette(self, range_overlay_palette):
        """Sets the range_overlay_palette of this ThematicAnalysisSettings.


        :param range_overlay_palette: The range_overlay_palette of this ThematicAnalysisSettings.  # noqa: E501
        :type: str
        """

        self._range_overlay_palette = range_overlay_palette

    @property
    def fill_pattern_color(self):
        """Gets the fill_pattern_color of this ThematicAnalysisSettings.  # noqa: E501


        :return: The fill_pattern_color of this ThematicAnalysisSettings.  # noqa: E501
        :rtype: str
        """
        return self._fill_pattern_color

    @fill_pattern_color.setter
    def fill_pattern_color(self, fill_pattern_color):
        """Sets the fill_pattern_color of this ThematicAnalysisSettings.


        :param fill_pattern_color: The fill_pattern_color of this ThematicAnalysisSettings.  # noqa: E501
        :type: str
        """

        self._fill_pattern_color = fill_pattern_color

    @property
    def not_available_color(self):
        """Gets the not_available_color of this ThematicAnalysisSettings.  # noqa: E501


        :return: The not_available_color of this ThematicAnalysisSettings.  # noqa: E501
        :rtype: str
        """
        return self._not_available_color

    @not_available_color.setter
    def not_available_color(self, not_available_color):
        """Sets the not_available_color of this ThematicAnalysisSettings.


        :param not_available_color: The not_available_color of this ThematicAnalysisSettings.  # noqa: E501
        :type: str
        """

        self._not_available_color = not_available_color

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
        if issubclass(ThematicAnalysisSettings, dict):
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
        if not isinstance(other, ThematicAnalysisSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other