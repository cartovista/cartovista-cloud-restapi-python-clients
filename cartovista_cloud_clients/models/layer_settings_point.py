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

class LayerSettingsPoint(object):
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
        'color': 'str',
        'size': 'int',
        'shape': 'str',
        'has_halo': 'bool',
        'halo_color': 'str',
        'has_background': 'bool',
        'background_color': 'str',
        'background_shape': 'str',
        'font_name': 'str',
        'background_font_name': 'str',
        'is_custom_symbol': 'bool'
    }

    attribute_map = {
        'color': 'color',
        'size': 'size',
        'shape': 'shape',
        'has_halo': 'hasHalo',
        'halo_color': 'haloColor',
        'has_background': 'hasBackground',
        'background_color': 'backgroundColor',
        'background_shape': 'backgroundShape',
        'font_name': 'fontName',
        'background_font_name': 'backgroundFontName',
        'is_custom_symbol': 'isCustomSymbol'
    }

    def __init__(self, color=None, size=None, shape=None, has_halo=None, halo_color=None, has_background=None, background_color=None, background_shape=None, font_name=None, background_font_name=None, is_custom_symbol=None):  # noqa: E501
        """LayerSettingsPoint - a model defined in Swagger"""  # noqa: E501
        self._color = None
        self._size = None
        self._shape = None
        self._has_halo = None
        self._halo_color = None
        self._has_background = None
        self._background_color = None
        self._background_shape = None
        self._font_name = None
        self._background_font_name = None
        self._is_custom_symbol = None
        self.discriminator = None
        if color is not None:
            self.color = color
        if size is not None:
            self.size = size
        if shape is not None:
            self.shape = shape
        if has_halo is not None:
            self.has_halo = has_halo
        if halo_color is not None:
            self.halo_color = halo_color
        if has_background is not None:
            self.has_background = has_background
        if background_color is not None:
            self.background_color = background_color
        if background_shape is not None:
            self.background_shape = background_shape
        if font_name is not None:
            self.font_name = font_name
        if background_font_name is not None:
            self.background_font_name = background_font_name
        if is_custom_symbol is not None:
            self.is_custom_symbol = is_custom_symbol

    @property
    def color(self):
        """Gets the color of this LayerSettingsPoint.  # noqa: E501


        :return: The color of this LayerSettingsPoint.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this LayerSettingsPoint.


        :param color: The color of this LayerSettingsPoint.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def size(self):
        """Gets the size of this LayerSettingsPoint.  # noqa: E501


        :return: The size of this LayerSettingsPoint.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LayerSettingsPoint.


        :param size: The size of this LayerSettingsPoint.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def shape(self):
        """Gets the shape of this LayerSettingsPoint.  # noqa: E501


        :return: The shape of this LayerSettingsPoint.  # noqa: E501
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this LayerSettingsPoint.


        :param shape: The shape of this LayerSettingsPoint.  # noqa: E501
        :type: str
        """

        self._shape = shape

    @property
    def has_halo(self):
        """Gets the has_halo of this LayerSettingsPoint.  # noqa: E501


        :return: The has_halo of this LayerSettingsPoint.  # noqa: E501
        :rtype: bool
        """
        return self._has_halo

    @has_halo.setter
    def has_halo(self, has_halo):
        """Sets the has_halo of this LayerSettingsPoint.


        :param has_halo: The has_halo of this LayerSettingsPoint.  # noqa: E501
        :type: bool
        """

        self._has_halo = has_halo

    @property
    def halo_color(self):
        """Gets the halo_color of this LayerSettingsPoint.  # noqa: E501


        :return: The halo_color of this LayerSettingsPoint.  # noqa: E501
        :rtype: str
        """
        return self._halo_color

    @halo_color.setter
    def halo_color(self, halo_color):
        """Sets the halo_color of this LayerSettingsPoint.


        :param halo_color: The halo_color of this LayerSettingsPoint.  # noqa: E501
        :type: str
        """

        self._halo_color = halo_color

    @property
    def has_background(self):
        """Gets the has_background of this LayerSettingsPoint.  # noqa: E501


        :return: The has_background of this LayerSettingsPoint.  # noqa: E501
        :rtype: bool
        """
        return self._has_background

    @has_background.setter
    def has_background(self, has_background):
        """Sets the has_background of this LayerSettingsPoint.


        :param has_background: The has_background of this LayerSettingsPoint.  # noqa: E501
        :type: bool
        """

        self._has_background = has_background

    @property
    def background_color(self):
        """Gets the background_color of this LayerSettingsPoint.  # noqa: E501


        :return: The background_color of this LayerSettingsPoint.  # noqa: E501
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this LayerSettingsPoint.


        :param background_color: The background_color of this LayerSettingsPoint.  # noqa: E501
        :type: str
        """

        self._background_color = background_color

    @property
    def background_shape(self):
        """Gets the background_shape of this LayerSettingsPoint.  # noqa: E501


        :return: The background_shape of this LayerSettingsPoint.  # noqa: E501
        :rtype: str
        """
        return self._background_shape

    @background_shape.setter
    def background_shape(self, background_shape):
        """Sets the background_shape of this LayerSettingsPoint.


        :param background_shape: The background_shape of this LayerSettingsPoint.  # noqa: E501
        :type: str
        """

        self._background_shape = background_shape

    @property
    def font_name(self):
        """Gets the font_name of this LayerSettingsPoint.  # noqa: E501


        :return: The font_name of this LayerSettingsPoint.  # noqa: E501
        :rtype: str
        """
        return self._font_name

    @font_name.setter
    def font_name(self, font_name):
        """Sets the font_name of this LayerSettingsPoint.


        :param font_name: The font_name of this LayerSettingsPoint.  # noqa: E501
        :type: str
        """

        self._font_name = font_name

    @property
    def background_font_name(self):
        """Gets the background_font_name of this LayerSettingsPoint.  # noqa: E501


        :return: The background_font_name of this LayerSettingsPoint.  # noqa: E501
        :rtype: str
        """
        return self._background_font_name

    @background_font_name.setter
    def background_font_name(self, background_font_name):
        """Sets the background_font_name of this LayerSettingsPoint.


        :param background_font_name: The background_font_name of this LayerSettingsPoint.  # noqa: E501
        :type: str
        """

        self._background_font_name = background_font_name

    @property
    def is_custom_symbol(self):
        """Gets the is_custom_symbol of this LayerSettingsPoint.  # noqa: E501


        :return: The is_custom_symbol of this LayerSettingsPoint.  # noqa: E501
        :rtype: bool
        """
        return self._is_custom_symbol

    @is_custom_symbol.setter
    def is_custom_symbol(self, is_custom_symbol):
        """Sets the is_custom_symbol of this LayerSettingsPoint.


        :param is_custom_symbol: The is_custom_symbol of this LayerSettingsPoint.  # noqa: E501
        :type: bool
        """

        self._is_custom_symbol = is_custom_symbol

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
        if issubclass(LayerSettingsPoint, dict):
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
        if not isinstance(other, LayerSettingsPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
