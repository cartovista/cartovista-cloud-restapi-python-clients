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

class PoiAnalysisScenarioAndYear(object):
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
        'scenario': 'str',
        'year': 'float',
        'is_pregenerated': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'scenario': 'scenario',
        'year': 'year',
        'is_pregenerated': 'isPregenerated'
    }

    def __init__(self, id=None, scenario=None, year=None, is_pregenerated=None):  # noqa: E501
        """PoiAnalysisScenarioAndYear - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._scenario = None
        self._year = None
        self._is_pregenerated = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if scenario is not None:
            self.scenario = scenario
        if year is not None:
            self.year = year
        if is_pregenerated is not None:
            self.is_pregenerated = is_pregenerated

    @property
    def id(self):
        """Gets the id of this PoiAnalysisScenarioAndYear.  # noqa: E501


        :return: The id of this PoiAnalysisScenarioAndYear.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PoiAnalysisScenarioAndYear.


        :param id: The id of this PoiAnalysisScenarioAndYear.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def scenario(self):
        """Gets the scenario of this PoiAnalysisScenarioAndYear.  # noqa: E501


        :return: The scenario of this PoiAnalysisScenarioAndYear.  # noqa: E501
        :rtype: str
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        """Sets the scenario of this PoiAnalysisScenarioAndYear.


        :param scenario: The scenario of this PoiAnalysisScenarioAndYear.  # noqa: E501
        :type: str
        """

        self._scenario = scenario

    @property
    def year(self):
        """Gets the year of this PoiAnalysisScenarioAndYear.  # noqa: E501


        :return: The year of this PoiAnalysisScenarioAndYear.  # noqa: E501
        :rtype: float
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this PoiAnalysisScenarioAndYear.


        :param year: The year of this PoiAnalysisScenarioAndYear.  # noqa: E501
        :type: float
        """

        self._year = year

    @property
    def is_pregenerated(self):
        """Gets the is_pregenerated of this PoiAnalysisScenarioAndYear.  # noqa: E501


        :return: The is_pregenerated of this PoiAnalysisScenarioAndYear.  # noqa: E501
        :rtype: bool
        """
        return self._is_pregenerated

    @is_pregenerated.setter
    def is_pregenerated(self, is_pregenerated):
        """Sets the is_pregenerated of this PoiAnalysisScenarioAndYear.


        :param is_pregenerated: The is_pregenerated of this PoiAnalysisScenarioAndYear.  # noqa: E501
        :type: bool
        """

        self._is_pregenerated = is_pregenerated

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
        if issubclass(PoiAnalysisScenarioAndYear, dict):
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
        if not isinstance(other, PoiAnalysisScenarioAndYear):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
