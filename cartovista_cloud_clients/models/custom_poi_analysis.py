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

class CustomPoiAnalysis(object):
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
        'id': 'str',
        'poi_analysis_id': 'str',
        'scenario_and_year_id': 'str',
        'feature_id': 'str',
        'value': 'int',
        'scenario': 'str',
        'year': 'float',
        'kv_levels': 'list[float]',
        'is_default': 'bool',
        'is_overloaded': 'bool',
        'x': 'float',
        'y': 'float',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'poi_analysis_id': 'poiAnalysisId',
        'scenario_and_year_id': 'scenarioAndYearId',
        'feature_id': 'featureId',
        'value': 'value',
        'scenario': 'scenario',
        'year': 'year',
        'kv_levels': 'kvLevels',
        'is_default': 'isDefault',
        'is_overloaded': 'isOverloaded',
        'x': 'x',
        'y': 'y',
        'name': 'name'
    }

    def __init__(self, id=None, poi_analysis_id=None, scenario_and_year_id=None, feature_id=None, value=None, scenario=None, year=None, kv_levels=None, is_default=None, is_overloaded=None, x=None, y=None, name=None):  # noqa: E501
        """CustomPoiAnalysis - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._poi_analysis_id = None
        self._scenario_and_year_id = None
        self._feature_id = None
        self._value = None
        self._scenario = None
        self._year = None
        self._kv_levels = None
        self._is_default = None
        self._is_overloaded = None
        self._x = None
        self._y = None
        self._name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if poi_analysis_id is not None:
            self.poi_analysis_id = poi_analysis_id
        if scenario_and_year_id is not None:
            self.scenario_and_year_id = scenario_and_year_id
        if feature_id is not None:
            self.feature_id = feature_id
        if value is not None:
            self.value = value
        if scenario is not None:
            self.scenario = scenario
        if year is not None:
            self.year = year
        if kv_levels is not None:
            self.kv_levels = kv_levels
        if is_default is not None:
            self.is_default = is_default
        if is_overloaded is not None:
            self.is_overloaded = is_overloaded
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this CustomPoiAnalysis.  # noqa: E501


        :return: The id of this CustomPoiAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomPoiAnalysis.


        :param id: The id of this CustomPoiAnalysis.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def poi_analysis_id(self):
        """Gets the poi_analysis_id of this CustomPoiAnalysis.  # noqa: E501


        :return: The poi_analysis_id of this CustomPoiAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._poi_analysis_id

    @poi_analysis_id.setter
    def poi_analysis_id(self, poi_analysis_id):
        """Sets the poi_analysis_id of this CustomPoiAnalysis.


        :param poi_analysis_id: The poi_analysis_id of this CustomPoiAnalysis.  # noqa: E501
        :type: str
        """

        self._poi_analysis_id = poi_analysis_id

    @property
    def scenario_and_year_id(self):
        """Gets the scenario_and_year_id of this CustomPoiAnalysis.  # noqa: E501


        :return: The scenario_and_year_id of this CustomPoiAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._scenario_and_year_id

    @scenario_and_year_id.setter
    def scenario_and_year_id(self, scenario_and_year_id):
        """Sets the scenario_and_year_id of this CustomPoiAnalysis.


        :param scenario_and_year_id: The scenario_and_year_id of this CustomPoiAnalysis.  # noqa: E501
        :type: str
        """

        self._scenario_and_year_id = scenario_and_year_id

    @property
    def feature_id(self):
        """Gets the feature_id of this CustomPoiAnalysis.  # noqa: E501


        :return: The feature_id of this CustomPoiAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """Sets the feature_id of this CustomPoiAnalysis.


        :param feature_id: The feature_id of this CustomPoiAnalysis.  # noqa: E501
        :type: str
        """

        self._feature_id = feature_id

    @property
    def value(self):
        """Gets the value of this CustomPoiAnalysis.  # noqa: E501


        :return: The value of this CustomPoiAnalysis.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomPoiAnalysis.


        :param value: The value of this CustomPoiAnalysis.  # noqa: E501
        :type: int
        """

        self._value = value

    @property
    def scenario(self):
        """Gets the scenario of this CustomPoiAnalysis.  # noqa: E501


        :return: The scenario of this CustomPoiAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        """Sets the scenario of this CustomPoiAnalysis.


        :param scenario: The scenario of this CustomPoiAnalysis.  # noqa: E501
        :type: str
        """

        self._scenario = scenario

    @property
    def year(self):
        """Gets the year of this CustomPoiAnalysis.  # noqa: E501


        :return: The year of this CustomPoiAnalysis.  # noqa: E501
        :rtype: float
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this CustomPoiAnalysis.


        :param year: The year of this CustomPoiAnalysis.  # noqa: E501
        :type: float
        """

        self._year = year

    @property
    def kv_levels(self):
        """Gets the kv_levels of this CustomPoiAnalysis.  # noqa: E501


        :return: The kv_levels of this CustomPoiAnalysis.  # noqa: E501
        :rtype: list[float]
        """
        return self._kv_levels

    @kv_levels.setter
    def kv_levels(self, kv_levels):
        """Sets the kv_levels of this CustomPoiAnalysis.


        :param kv_levels: The kv_levels of this CustomPoiAnalysis.  # noqa: E501
        :type: list[float]
        """

        self._kv_levels = kv_levels

    @property
    def is_default(self):
        """Gets the is_default of this CustomPoiAnalysis.  # noqa: E501


        :return: The is_default of this CustomPoiAnalysis.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this CustomPoiAnalysis.


        :param is_default: The is_default of this CustomPoiAnalysis.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def is_overloaded(self):
        """Gets the is_overloaded of this CustomPoiAnalysis.  # noqa: E501


        :return: The is_overloaded of this CustomPoiAnalysis.  # noqa: E501
        :rtype: bool
        """
        return self._is_overloaded

    @is_overloaded.setter
    def is_overloaded(self, is_overloaded):
        """Sets the is_overloaded of this CustomPoiAnalysis.


        :param is_overloaded: The is_overloaded of this CustomPoiAnalysis.  # noqa: E501
        :type: bool
        """

        self._is_overloaded = is_overloaded

    @property
    def x(self):
        """Gets the x of this CustomPoiAnalysis.  # noqa: E501


        :return: The x of this CustomPoiAnalysis.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this CustomPoiAnalysis.


        :param x: The x of this CustomPoiAnalysis.  # noqa: E501
        :type: float
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this CustomPoiAnalysis.  # noqa: E501


        :return: The y of this CustomPoiAnalysis.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this CustomPoiAnalysis.


        :param y: The y of this CustomPoiAnalysis.  # noqa: E501
        :type: float
        """

        self._y = y

    @property
    def name(self):
        """Gets the name of this CustomPoiAnalysis.  # noqa: E501


        :return: The name of this CustomPoiAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomPoiAnalysis.


        :param name: The name of this CustomPoiAnalysis.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(CustomPoiAnalysis, dict):
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
        if not isinstance(other, CustomPoiAnalysis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other