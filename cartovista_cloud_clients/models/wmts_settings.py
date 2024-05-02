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

class WmtsSettings(object):
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
        'wmts_id': 'str',
        'map_id': 'str',
        'alias': 'str',
        'rendering': 'LayerSettingsRendering',
        'visibility_ranges': 'WmtsSettingsVisibilityRanges',
        'id': 'str'
    }

    attribute_map = {
        'wmts_id': 'wmtsId',
        'map_id': 'mapId',
        'alias': 'alias',
        'rendering': 'rendering',
        'visibility_ranges': 'visibilityRanges',
        'id': 'id'
    }

    def __init__(self, wmts_id=None, map_id=None, alias=None, rendering=None, visibility_ranges=None, id=None):  # noqa: E501
        """WmtsSettings - a model defined in Swagger"""  # noqa: E501
        self._wmts_id = None
        self._map_id = None
        self._alias = None
        self._rendering = None
        self._visibility_ranges = None
        self._id = None
        self.discriminator = None
        if wmts_id is not None:
            self.wmts_id = wmts_id
        if map_id is not None:
            self.map_id = map_id
        if alias is not None:
            self.alias = alias
        if rendering is not None:
            self.rendering = rendering
        if visibility_ranges is not None:
            self.visibility_ranges = visibility_ranges
        if id is not None:
            self.id = id

    @property
    def wmts_id(self):
        """Gets the wmts_id of this WmtsSettings.  # noqa: E501


        :return: The wmts_id of this WmtsSettings.  # noqa: E501
        :rtype: str
        """
        return self._wmts_id

    @wmts_id.setter
    def wmts_id(self, wmts_id):
        """Sets the wmts_id of this WmtsSettings.


        :param wmts_id: The wmts_id of this WmtsSettings.  # noqa: E501
        :type: str
        """

        self._wmts_id = wmts_id

    @property
    def map_id(self):
        """Gets the map_id of this WmtsSettings.  # noqa: E501


        :return: The map_id of this WmtsSettings.  # noqa: E501
        :rtype: str
        """
        return self._map_id

    @map_id.setter
    def map_id(self, map_id):
        """Sets the map_id of this WmtsSettings.


        :param map_id: The map_id of this WmtsSettings.  # noqa: E501
        :type: str
        """

        self._map_id = map_id

    @property
    def alias(self):
        """Gets the alias of this WmtsSettings.  # noqa: E501


        :return: The alias of this WmtsSettings.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this WmtsSettings.


        :param alias: The alias of this WmtsSettings.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def rendering(self):
        """Gets the rendering of this WmtsSettings.  # noqa: E501


        :return: The rendering of this WmtsSettings.  # noqa: E501
        :rtype: LayerSettingsRendering
        """
        return self._rendering

    @rendering.setter
    def rendering(self, rendering):
        """Sets the rendering of this WmtsSettings.


        :param rendering: The rendering of this WmtsSettings.  # noqa: E501
        :type: LayerSettingsRendering
        """

        self._rendering = rendering

    @property
    def visibility_ranges(self):
        """Gets the visibility_ranges of this WmtsSettings.  # noqa: E501


        :return: The visibility_ranges of this WmtsSettings.  # noqa: E501
        :rtype: WmtsSettingsVisibilityRanges
        """
        return self._visibility_ranges

    @visibility_ranges.setter
    def visibility_ranges(self, visibility_ranges):
        """Sets the visibility_ranges of this WmtsSettings.


        :param visibility_ranges: The visibility_ranges of this WmtsSettings.  # noqa: E501
        :type: WmtsSettingsVisibilityRanges
        """

        self._visibility_ranges = visibility_ranges

    @property
    def id(self):
        """Gets the id of this WmtsSettings.  # noqa: E501


        :return: The id of this WmtsSettings.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WmtsSettings.


        :param id: The id of this WmtsSettings.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(WmtsSettings, dict):
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
        if not isinstance(other, WmtsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other