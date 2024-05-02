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

class SpatialFilterDTO(object):
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
        'wkts': 'list[str]',
        'zoom_level': 'int',
        'is_clustering_activated': 'bool'
    }

    attribute_map = {
        'wkts': 'wkts',
        'zoom_level': 'zoomLevel',
        'is_clustering_activated': 'isClusteringActivated'
    }

    def __init__(self, wkts=None, zoom_level=None, is_clustering_activated=None):  # noqa: E501
        """SpatialFilterDTO - a model defined in Swagger"""  # noqa: E501
        self._wkts = None
        self._zoom_level = None
        self._is_clustering_activated = None
        self.discriminator = None
        if wkts is not None:
            self.wkts = wkts
        if zoom_level is not None:
            self.zoom_level = zoom_level
        if is_clustering_activated is not None:
            self.is_clustering_activated = is_clustering_activated

    @property
    def wkts(self):
        """Gets the wkts of this SpatialFilterDTO.  # noqa: E501


        :return: The wkts of this SpatialFilterDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._wkts

    @wkts.setter
    def wkts(self, wkts):
        """Sets the wkts of this SpatialFilterDTO.


        :param wkts: The wkts of this SpatialFilterDTO.  # noqa: E501
        :type: list[str]
        """

        self._wkts = wkts

    @property
    def zoom_level(self):
        """Gets the zoom_level of this SpatialFilterDTO.  # noqa: E501


        :return: The zoom_level of this SpatialFilterDTO.  # noqa: E501
        :rtype: int
        """
        return self._zoom_level

    @zoom_level.setter
    def zoom_level(self, zoom_level):
        """Sets the zoom_level of this SpatialFilterDTO.


        :param zoom_level: The zoom_level of this SpatialFilterDTO.  # noqa: E501
        :type: int
        """

        self._zoom_level = zoom_level

    @property
    def is_clustering_activated(self):
        """Gets the is_clustering_activated of this SpatialFilterDTO.  # noqa: E501


        :return: The is_clustering_activated of this SpatialFilterDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_clustering_activated

    @is_clustering_activated.setter
    def is_clustering_activated(self, is_clustering_activated):
        """Sets the is_clustering_activated of this SpatialFilterDTO.


        :param is_clustering_activated: The is_clustering_activated of this SpatialFilterDTO.  # noqa: E501
        :type: bool
        """

        self._is_clustering_activated = is_clustering_activated

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
        if issubclass(SpatialFilterDTO, dict):
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
        if not isinstance(other, SpatialFilterDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other