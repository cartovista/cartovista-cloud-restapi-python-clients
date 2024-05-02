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

class PropertiesOfBoolean(object):
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
        'map': 'bool',
        'layers': 'bool',
        'info': 'bool',
        'data': 'bool',
        'legend': 'bool',
        'chart': 'bool',
        'story': 'bool',
        'routing': 'bool',
        'profile': 'bool',
        'time_view': 'bool',
        'time_animation_controller': 'bool'
    }

    attribute_map = {
        'map': 'map',
        'layers': 'layers',
        'info': 'info',
        'data': 'data',
        'legend': 'legend',
        'chart': 'chart',
        'story': 'story',
        'routing': 'routing',
        'profile': 'profile',
        'time_view': 'timeView',
        'time_animation_controller': 'timeAnimationController'
    }

    def __init__(self, map=None, layers=None, info=None, data=None, legend=None, chart=None, story=None, routing=None, profile=None, time_view=None, time_animation_controller=None):  # noqa: E501
        """PropertiesOfBoolean - a model defined in Swagger"""  # noqa: E501
        self._map = None
        self._layers = None
        self._info = None
        self._data = None
        self._legend = None
        self._chart = None
        self._story = None
        self._routing = None
        self._profile = None
        self._time_view = None
        self._time_animation_controller = None
        self.discriminator = None
        if map is not None:
            self.map = map
        if layers is not None:
            self.layers = layers
        if info is not None:
            self.info = info
        if data is not None:
            self.data = data
        if legend is not None:
            self.legend = legend
        if chart is not None:
            self.chart = chart
        if story is not None:
            self.story = story
        if routing is not None:
            self.routing = routing
        if profile is not None:
            self.profile = profile
        if time_view is not None:
            self.time_view = time_view
        if time_animation_controller is not None:
            self.time_animation_controller = time_animation_controller

    @property
    def map(self):
        """Gets the map of this PropertiesOfBoolean.  # noqa: E501


        :return: The map of this PropertiesOfBoolean.  # noqa: E501
        :rtype: bool
        """
        return self._map

    @map.setter
    def map(self, map):
        """Sets the map of this PropertiesOfBoolean.


        :param map: The map of this PropertiesOfBoolean.  # noqa: E501
        :type: bool
        """

        self._map = map

    @property
    def layers(self):
        """Gets the layers of this PropertiesOfBoolean.  # noqa: E501


        :return: The layers of this PropertiesOfBoolean.  # noqa: E501
        :rtype: bool
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """Sets the layers of this PropertiesOfBoolean.


        :param layers: The layers of this PropertiesOfBoolean.  # noqa: E501
        :type: bool
        """

        self._layers = layers

    @property
    def info(self):
        """Gets the info of this PropertiesOfBoolean.  # noqa: E501


        :return: The info of this PropertiesOfBoolean.  # noqa: E501
        :rtype: bool
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this PropertiesOfBoolean.


        :param info: The info of this PropertiesOfBoolean.  # noqa: E501
        :type: bool
        """

        self._info = info

    @property
    def data(self):
        """Gets the data of this PropertiesOfBoolean.  # noqa: E501


        :return: The data of this PropertiesOfBoolean.  # noqa: E501
        :rtype: bool
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PropertiesOfBoolean.


        :param data: The data of this PropertiesOfBoolean.  # noqa: E501
        :type: bool
        """

        self._data = data

    @property
    def legend(self):
        """Gets the legend of this PropertiesOfBoolean.  # noqa: E501


        :return: The legend of this PropertiesOfBoolean.  # noqa: E501
        :rtype: bool
        """
        return self._legend

    @legend.setter
    def legend(self, legend):
        """Sets the legend of this PropertiesOfBoolean.


        :param legend: The legend of this PropertiesOfBoolean.  # noqa: E501
        :type: bool
        """

        self._legend = legend

    @property
    def chart(self):
        """Gets the chart of this PropertiesOfBoolean.  # noqa: E501


        :return: The chart of this PropertiesOfBoolean.  # noqa: E501
        :rtype: bool
        """
        return self._chart

    @chart.setter
    def chart(self, chart):
        """Sets the chart of this PropertiesOfBoolean.


        :param chart: The chart of this PropertiesOfBoolean.  # noqa: E501
        :type: bool
        """

        self._chart = chart

    @property
    def story(self):
        """Gets the story of this PropertiesOfBoolean.  # noqa: E501


        :return: The story of this PropertiesOfBoolean.  # noqa: E501
        :rtype: bool
        """
        return self._story

    @story.setter
    def story(self, story):
        """Sets the story of this PropertiesOfBoolean.


        :param story: The story of this PropertiesOfBoolean.  # noqa: E501
        :type: bool
        """

        self._story = story

    @property
    def routing(self):
        """Gets the routing of this PropertiesOfBoolean.  # noqa: E501


        :return: The routing of this PropertiesOfBoolean.  # noqa: E501
        :rtype: bool
        """
        return self._routing

    @routing.setter
    def routing(self, routing):
        """Sets the routing of this PropertiesOfBoolean.


        :param routing: The routing of this PropertiesOfBoolean.  # noqa: E501
        :type: bool
        """

        self._routing = routing

    @property
    def profile(self):
        """Gets the profile of this PropertiesOfBoolean.  # noqa: E501


        :return: The profile of this PropertiesOfBoolean.  # noqa: E501
        :rtype: bool
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this PropertiesOfBoolean.


        :param profile: The profile of this PropertiesOfBoolean.  # noqa: E501
        :type: bool
        """

        self._profile = profile

    @property
    def time_view(self):
        """Gets the time_view of this PropertiesOfBoolean.  # noqa: E501


        :return: The time_view of this PropertiesOfBoolean.  # noqa: E501
        :rtype: bool
        """
        return self._time_view

    @time_view.setter
    def time_view(self, time_view):
        """Sets the time_view of this PropertiesOfBoolean.


        :param time_view: The time_view of this PropertiesOfBoolean.  # noqa: E501
        :type: bool
        """

        self._time_view = time_view

    @property
    def time_animation_controller(self):
        """Gets the time_animation_controller of this PropertiesOfBoolean.  # noqa: E501


        :return: The time_animation_controller of this PropertiesOfBoolean.  # noqa: E501
        :rtype: bool
        """
        return self._time_animation_controller

    @time_animation_controller.setter
    def time_animation_controller(self, time_animation_controller):
        """Sets the time_animation_controller of this PropertiesOfBoolean.


        :param time_animation_controller: The time_animation_controller of this PropertiesOfBoolean.  # noqa: E501
        :type: bool
        """

        self._time_animation_controller = time_animation_controller

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
        if issubclass(PropertiesOfBoolean, dict):
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
        if not isinstance(other, PropertiesOfBoolean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
