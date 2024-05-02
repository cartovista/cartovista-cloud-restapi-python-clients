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

class FeedbackContent(object):
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
        'annotations': 'list[FeedbackAnnotation]',
        'geometries_wkt': 'list[str]'
    }

    attribute_map = {
        'annotations': 'annotations',
        'geometries_wkt': 'geometriesWKT'
    }

    def __init__(self, annotations=None, geometries_wkt=None):  # noqa: E501
        """FeedbackContent - a model defined in Swagger"""  # noqa: E501
        self._annotations = None
        self._geometries_wkt = None
        self.discriminator = None
        if annotations is not None:
            self.annotations = annotations
        if geometries_wkt is not None:
            self.geometries_wkt = geometries_wkt

    @property
    def annotations(self):
        """Gets the annotations of this FeedbackContent.  # noqa: E501


        :return: The annotations of this FeedbackContent.  # noqa: E501
        :rtype: list[FeedbackAnnotation]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this FeedbackContent.


        :param annotations: The annotations of this FeedbackContent.  # noqa: E501
        :type: list[FeedbackAnnotation]
        """

        self._annotations = annotations

    @property
    def geometries_wkt(self):
        """Gets the geometries_wkt of this FeedbackContent.  # noqa: E501


        :return: The geometries_wkt of this FeedbackContent.  # noqa: E501
        :rtype: list[str]
        """
        return self._geometries_wkt

    @geometries_wkt.setter
    def geometries_wkt(self, geometries_wkt):
        """Sets the geometries_wkt of this FeedbackContent.


        :param geometries_wkt: The geometries_wkt of this FeedbackContent.  # noqa: E501
        :type: list[str]
        """

        self._geometries_wkt = geometries_wkt

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
        if issubclass(FeedbackContent, dict):
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
        if not isinstance(other, FeedbackContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other