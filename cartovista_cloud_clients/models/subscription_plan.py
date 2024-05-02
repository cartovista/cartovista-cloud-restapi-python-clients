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

class SubscriptionPlan(object):
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
        'package': 'SubscriptionPackage',
        'storage': 'int',
        'is_gb': 'bool',
        'maps': 'int',
        'layers_per_map': 'int',
        'features_per_layer': 'int',
        'rest_api': 'bool',
        'monthly': 'OneOfSubscriptionPlanMonthly',
        'yearly': 'OneOfSubscriptionPlanYearly'
    }

    attribute_map = {
        'package': 'package',
        'storage': 'storage',
        'is_gb': 'isGB',
        'maps': 'maps',
        'layers_per_map': 'layersPerMap',
        'features_per_layer': 'featuresPerLayer',
        'rest_api': 'restApi',
        'monthly': 'monthly',
        'yearly': 'yearly'
    }

    def __init__(self, package=None, storage=None, is_gb=None, maps=None, layers_per_map=None, features_per_layer=None, rest_api=None, monthly=None, yearly=None):  # noqa: E501
        """SubscriptionPlan - a model defined in Swagger"""  # noqa: E501
        self._package = None
        self._storage = None
        self._is_gb = None
        self._maps = None
        self._layers_per_map = None
        self._features_per_layer = None
        self._rest_api = None
        self._monthly = None
        self._yearly = None
        self.discriminator = None
        if package is not None:
            self.package = package
        if storage is not None:
            self.storage = storage
        if is_gb is not None:
            self.is_gb = is_gb
        if maps is not None:
            self.maps = maps
        if layers_per_map is not None:
            self.layers_per_map = layers_per_map
        if features_per_layer is not None:
            self.features_per_layer = features_per_layer
        if rest_api is not None:
            self.rest_api = rest_api
        if monthly is not None:
            self.monthly = monthly
        if yearly is not None:
            self.yearly = yearly

    @property
    def package(self):
        """Gets the package of this SubscriptionPlan.  # noqa: E501


        :return: The package of this SubscriptionPlan.  # noqa: E501
        :rtype: SubscriptionPackage
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this SubscriptionPlan.


        :param package: The package of this SubscriptionPlan.  # noqa: E501
        :type: SubscriptionPackage
        """

        self._package = package

    @property
    def storage(self):
        """Gets the storage of this SubscriptionPlan.  # noqa: E501


        :return: The storage of this SubscriptionPlan.  # noqa: E501
        :rtype: int
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this SubscriptionPlan.


        :param storage: The storage of this SubscriptionPlan.  # noqa: E501
        :type: int
        """

        self._storage = storage

    @property
    def is_gb(self):
        """Gets the is_gb of this SubscriptionPlan.  # noqa: E501


        :return: The is_gb of this SubscriptionPlan.  # noqa: E501
        :rtype: bool
        """
        return self._is_gb

    @is_gb.setter
    def is_gb(self, is_gb):
        """Sets the is_gb of this SubscriptionPlan.


        :param is_gb: The is_gb of this SubscriptionPlan.  # noqa: E501
        :type: bool
        """

        self._is_gb = is_gb

    @property
    def maps(self):
        """Gets the maps of this SubscriptionPlan.  # noqa: E501


        :return: The maps of this SubscriptionPlan.  # noqa: E501
        :rtype: int
        """
        return self._maps

    @maps.setter
    def maps(self, maps):
        """Sets the maps of this SubscriptionPlan.


        :param maps: The maps of this SubscriptionPlan.  # noqa: E501
        :type: int
        """

        self._maps = maps

    @property
    def layers_per_map(self):
        """Gets the layers_per_map of this SubscriptionPlan.  # noqa: E501


        :return: The layers_per_map of this SubscriptionPlan.  # noqa: E501
        :rtype: int
        """
        return self._layers_per_map

    @layers_per_map.setter
    def layers_per_map(self, layers_per_map):
        """Sets the layers_per_map of this SubscriptionPlan.


        :param layers_per_map: The layers_per_map of this SubscriptionPlan.  # noqa: E501
        :type: int
        """

        self._layers_per_map = layers_per_map

    @property
    def features_per_layer(self):
        """Gets the features_per_layer of this SubscriptionPlan.  # noqa: E501


        :return: The features_per_layer of this SubscriptionPlan.  # noqa: E501
        :rtype: int
        """
        return self._features_per_layer

    @features_per_layer.setter
    def features_per_layer(self, features_per_layer):
        """Sets the features_per_layer of this SubscriptionPlan.


        :param features_per_layer: The features_per_layer of this SubscriptionPlan.  # noqa: E501
        :type: int
        """

        self._features_per_layer = features_per_layer

    @property
    def rest_api(self):
        """Gets the rest_api of this SubscriptionPlan.  # noqa: E501


        :return: The rest_api of this SubscriptionPlan.  # noqa: E501
        :rtype: bool
        """
        return self._rest_api

    @rest_api.setter
    def rest_api(self, rest_api):
        """Sets the rest_api of this SubscriptionPlan.


        :param rest_api: The rest_api of this SubscriptionPlan.  # noqa: E501
        :type: bool
        """

        self._rest_api = rest_api

    @property
    def monthly(self):
        """Gets the monthly of this SubscriptionPlan.  # noqa: E501


        :return: The monthly of this SubscriptionPlan.  # noqa: E501
        :rtype: OneOfSubscriptionPlanMonthly
        """
        return self._monthly

    @monthly.setter
    def monthly(self, monthly):
        """Sets the monthly of this SubscriptionPlan.


        :param monthly: The monthly of this SubscriptionPlan.  # noqa: E501
        :type: OneOfSubscriptionPlanMonthly
        """

        self._monthly = monthly

    @property
    def yearly(self):
        """Gets the yearly of this SubscriptionPlan.  # noqa: E501


        :return: The yearly of this SubscriptionPlan.  # noqa: E501
        :rtype: OneOfSubscriptionPlanYearly
        """
        return self._yearly

    @yearly.setter
    def yearly(self, yearly):
        """Sets the yearly of this SubscriptionPlan.


        :param yearly: The yearly of this SubscriptionPlan.  # noqa: E501
        :type: OneOfSubscriptionPlanYearly
        """

        self._yearly = yearly

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
        if issubclass(SubscriptionPlan, dict):
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
        if not isinstance(other, SubscriptionPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
