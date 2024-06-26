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

class DistanceToPosDTO(object):
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
        'block_id': 'str',
        'drive_time': 'int',
        'drive_distance': 'int',
        'distance': 'float'
    }

    attribute_map = {
        'block_id': 'blockId',
        'drive_time': 'driveTime',
        'drive_distance': 'driveDistance',
        'distance': 'distance'
    }

    def __init__(self, block_id=None, drive_time=None, drive_distance=None, distance=None):  # noqa: E501
        """DistanceToPosDTO - a model defined in Swagger"""  # noqa: E501
        self._block_id = None
        self._drive_time = None
        self._drive_distance = None
        self._distance = None
        self.discriminator = None
        if block_id is not None:
            self.block_id = block_id
        if drive_time is not None:
            self.drive_time = drive_time
        if drive_distance is not None:
            self.drive_distance = drive_distance
        if distance is not None:
            self.distance = distance

    @property
    def block_id(self):
        """Gets the block_id of this DistanceToPosDTO.  # noqa: E501


        :return: The block_id of this DistanceToPosDTO.  # noqa: E501
        :rtype: str
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        """Sets the block_id of this DistanceToPosDTO.


        :param block_id: The block_id of this DistanceToPosDTO.  # noqa: E501
        :type: str
        """

        self._block_id = block_id

    @property
    def drive_time(self):
        """Gets the drive_time of this DistanceToPosDTO.  # noqa: E501


        :return: The drive_time of this DistanceToPosDTO.  # noqa: E501
        :rtype: int
        """
        return self._drive_time

    @drive_time.setter
    def drive_time(self, drive_time):
        """Sets the drive_time of this DistanceToPosDTO.


        :param drive_time: The drive_time of this DistanceToPosDTO.  # noqa: E501
        :type: int
        """

        self._drive_time = drive_time

    @property
    def drive_distance(self):
        """Gets the drive_distance of this DistanceToPosDTO.  # noqa: E501


        :return: The drive_distance of this DistanceToPosDTO.  # noqa: E501
        :rtype: int
        """
        return self._drive_distance

    @drive_distance.setter
    def drive_distance(self, drive_distance):
        """Sets the drive_distance of this DistanceToPosDTO.


        :param drive_distance: The drive_distance of this DistanceToPosDTO.  # noqa: E501
        :type: int
        """

        self._drive_distance = drive_distance

    @property
    def distance(self):
        """Gets the distance of this DistanceToPosDTO.  # noqa: E501


        :return: The distance of this DistanceToPosDTO.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this DistanceToPosDTO.


        :param distance: The distance of this DistanceToPosDTO.  # noqa: E501
        :type: float
        """

        self._distance = distance

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
        if issubclass(DistanceToPosDTO, dict):
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
        if not isinstance(other, DistanceToPosDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
