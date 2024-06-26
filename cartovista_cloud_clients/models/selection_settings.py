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

class SelectionSettings(object):
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
        'stroke_color': 'str',
        'stroke_size': 'int',
        'fill_color': 'str',
        'fill_opacity': 'float',
        'fill_enabled': 'bool',
        'hide_non_visible_layers': 'bool',
        'append_mode': 'bool',
        'spatial_selection_enabled': 'bool'
    }

    attribute_map = {
        'stroke_color': 'strokeColor',
        'stroke_size': 'strokeSize',
        'fill_color': 'fillColor',
        'fill_opacity': 'fillOpacity',
        'fill_enabled': 'fillEnabled',
        'hide_non_visible_layers': 'hideNonVisibleLayers',
        'append_mode': 'appendMode',
        'spatial_selection_enabled': 'spatialSelectionEnabled'
    }

    def __init__(self, stroke_color=None, stroke_size=None, fill_color=None, fill_opacity=None, fill_enabled=None, hide_non_visible_layers=None, append_mode=None, spatial_selection_enabled=None):  # noqa: E501
        """SelectionSettings - a model defined in Swagger"""  # noqa: E501
        self._stroke_color = None
        self._stroke_size = None
        self._fill_color = None
        self._fill_opacity = None
        self._fill_enabled = None
        self._hide_non_visible_layers = None
        self._append_mode = None
        self._spatial_selection_enabled = None
        self.discriminator = None
        if stroke_color is not None:
            self.stroke_color = stroke_color
        if stroke_size is not None:
            self.stroke_size = stroke_size
        if fill_color is not None:
            self.fill_color = fill_color
        if fill_opacity is not None:
            self.fill_opacity = fill_opacity
        if fill_enabled is not None:
            self.fill_enabled = fill_enabled
        if hide_non_visible_layers is not None:
            self.hide_non_visible_layers = hide_non_visible_layers
        if append_mode is not None:
            self.append_mode = append_mode
        if spatial_selection_enabled is not None:
            self.spatial_selection_enabled = spatial_selection_enabled

    @property
    def stroke_color(self):
        """Gets the stroke_color of this SelectionSettings.  # noqa: E501


        :return: The stroke_color of this SelectionSettings.  # noqa: E501
        :rtype: str
        """
        return self._stroke_color

    @stroke_color.setter
    def stroke_color(self, stroke_color):
        """Sets the stroke_color of this SelectionSettings.


        :param stroke_color: The stroke_color of this SelectionSettings.  # noqa: E501
        :type: str
        """

        self._stroke_color = stroke_color

    @property
    def stroke_size(self):
        """Gets the stroke_size of this SelectionSettings.  # noqa: E501


        :return: The stroke_size of this SelectionSettings.  # noqa: E501
        :rtype: int
        """
        return self._stroke_size

    @stroke_size.setter
    def stroke_size(self, stroke_size):
        """Sets the stroke_size of this SelectionSettings.


        :param stroke_size: The stroke_size of this SelectionSettings.  # noqa: E501
        :type: int
        """

        self._stroke_size = stroke_size

    @property
    def fill_color(self):
        """Gets the fill_color of this SelectionSettings.  # noqa: E501


        :return: The fill_color of this SelectionSettings.  # noqa: E501
        :rtype: str
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, fill_color):
        """Sets the fill_color of this SelectionSettings.


        :param fill_color: The fill_color of this SelectionSettings.  # noqa: E501
        :type: str
        """

        self._fill_color = fill_color

    @property
    def fill_opacity(self):
        """Gets the fill_opacity of this SelectionSettings.  # noqa: E501


        :return: The fill_opacity of this SelectionSettings.  # noqa: E501
        :rtype: float
        """
        return self._fill_opacity

    @fill_opacity.setter
    def fill_opacity(self, fill_opacity):
        """Sets the fill_opacity of this SelectionSettings.


        :param fill_opacity: The fill_opacity of this SelectionSettings.  # noqa: E501
        :type: float
        """

        self._fill_opacity = fill_opacity

    @property
    def fill_enabled(self):
        """Gets the fill_enabled of this SelectionSettings.  # noqa: E501


        :return: The fill_enabled of this SelectionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._fill_enabled

    @fill_enabled.setter
    def fill_enabled(self, fill_enabled):
        """Sets the fill_enabled of this SelectionSettings.


        :param fill_enabled: The fill_enabled of this SelectionSettings.  # noqa: E501
        :type: bool
        """

        self._fill_enabled = fill_enabled

    @property
    def hide_non_visible_layers(self):
        """Gets the hide_non_visible_layers of this SelectionSettings.  # noqa: E501


        :return: The hide_non_visible_layers of this SelectionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._hide_non_visible_layers

    @hide_non_visible_layers.setter
    def hide_non_visible_layers(self, hide_non_visible_layers):
        """Sets the hide_non_visible_layers of this SelectionSettings.


        :param hide_non_visible_layers: The hide_non_visible_layers of this SelectionSettings.  # noqa: E501
        :type: bool
        """

        self._hide_non_visible_layers = hide_non_visible_layers

    @property
    def append_mode(self):
        """Gets the append_mode of this SelectionSettings.  # noqa: E501


        :return: The append_mode of this SelectionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._append_mode

    @append_mode.setter
    def append_mode(self, append_mode):
        """Sets the append_mode of this SelectionSettings.


        :param append_mode: The append_mode of this SelectionSettings.  # noqa: E501
        :type: bool
        """

        self._append_mode = append_mode

    @property
    def spatial_selection_enabled(self):
        """Gets the spatial_selection_enabled of this SelectionSettings.  # noqa: E501


        :return: The spatial_selection_enabled of this SelectionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._spatial_selection_enabled

    @spatial_selection_enabled.setter
    def spatial_selection_enabled(self, spatial_selection_enabled):
        """Sets the spatial_selection_enabled of this SelectionSettings.


        :param spatial_selection_enabled: The spatial_selection_enabled of this SelectionSettings.  # noqa: E501
        :type: bool
        """

        self._spatial_selection_enabled = spatial_selection_enabled

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
        if issubclass(SelectionSettings, dict):
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
        if not isinstance(other, SelectionSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
