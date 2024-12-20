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

class SubscriptionAndUser(object):
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
        'current_user': 'OneOfSubscriptionAndUserCurrentUser',
        'subscription': 'OneOfSubscriptionAndUserSubscription',
        'subscription_summary': 'OneOfSubscriptionAndUserSubscriptionSummary',
        'maximum_number_of_users': 'int',
        'public_maps': 'bool',
        'rest_api': 'bool',
        'live_layers': 'bool',
        'content_count': 'OneOfSubscriptionAndUserContentCount',
        'query_optimizer': 'bool',
        'heatmap_generation': 'bool',
        'grace_period_end_date': 'datetime',
        'license_expired': 'bool',
        'composite_scoring': 'bool',
        'poi_analysis': 'bool'
    }

    attribute_map = {
        'current_user': 'currentUser',
        'subscription': 'subscription',
        'subscription_summary': 'subscriptionSummary',
        'maximum_number_of_users': 'maximumNumberOfUsers',
        'public_maps': 'publicMaps',
        'rest_api': 'restApi',
        'live_layers': 'liveLayers',
        'content_count': 'contentCount',
        'query_optimizer': 'queryOptimizer',
        'heatmap_generation': 'heatmapGeneration',
        'grace_period_end_date': 'gracePeriodEndDate',
        'license_expired': 'licenseExpired',
        'composite_scoring': 'compositeScoring',
        'poi_analysis': 'poiAnalysis'
    }

    def __init__(self, current_user=None, subscription=None, subscription_summary=None, maximum_number_of_users=None, public_maps=None, rest_api=None, live_layers=None, content_count=None, query_optimizer=None, heatmap_generation=None, grace_period_end_date=None, license_expired=None, composite_scoring=None, poi_analysis=None):  # noqa: E501
        """SubscriptionAndUser - a model defined in Swagger"""  # noqa: E501
        self._current_user = None
        self._subscription = None
        self._subscription_summary = None
        self._maximum_number_of_users = None
        self._public_maps = None
        self._rest_api = None
        self._live_layers = None
        self._content_count = None
        self._query_optimizer = None
        self._heatmap_generation = None
        self._grace_period_end_date = None
        self._license_expired = None
        self._composite_scoring = None
        self._poi_analysis = None
        self.discriminator = None
        if current_user is not None:
            self.current_user = current_user
        if subscription is not None:
            self.subscription = subscription
        if subscription_summary is not None:
            self.subscription_summary = subscription_summary
        if maximum_number_of_users is not None:
            self.maximum_number_of_users = maximum_number_of_users
        if public_maps is not None:
            self.public_maps = public_maps
        if rest_api is not None:
            self.rest_api = rest_api
        if live_layers is not None:
            self.live_layers = live_layers
        if content_count is not None:
            self.content_count = content_count
        if query_optimizer is not None:
            self.query_optimizer = query_optimizer
        if heatmap_generation is not None:
            self.heatmap_generation = heatmap_generation
        if grace_period_end_date is not None:
            self.grace_period_end_date = grace_period_end_date
        if license_expired is not None:
            self.license_expired = license_expired
        if composite_scoring is not None:
            self.composite_scoring = composite_scoring
        if poi_analysis is not None:
            self.poi_analysis = poi_analysis

    @property
    def current_user(self):
        """Gets the current_user of this SubscriptionAndUser.  # noqa: E501


        :return: The current_user of this SubscriptionAndUser.  # noqa: E501
        :rtype: OneOfSubscriptionAndUserCurrentUser
        """
        return self._current_user

    @current_user.setter
    def current_user(self, current_user):
        """Sets the current_user of this SubscriptionAndUser.


        :param current_user: The current_user of this SubscriptionAndUser.  # noqa: E501
        :type: OneOfSubscriptionAndUserCurrentUser
        """

        self._current_user = current_user

    @property
    def subscription(self):
        """Gets the subscription of this SubscriptionAndUser.  # noqa: E501


        :return: The subscription of this SubscriptionAndUser.  # noqa: E501
        :rtype: OneOfSubscriptionAndUserSubscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this SubscriptionAndUser.


        :param subscription: The subscription of this SubscriptionAndUser.  # noqa: E501
        :type: OneOfSubscriptionAndUserSubscription
        """

        self._subscription = subscription

    @property
    def subscription_summary(self):
        """Gets the subscription_summary of this SubscriptionAndUser.  # noqa: E501


        :return: The subscription_summary of this SubscriptionAndUser.  # noqa: E501
        :rtype: OneOfSubscriptionAndUserSubscriptionSummary
        """
        return self._subscription_summary

    @subscription_summary.setter
    def subscription_summary(self, subscription_summary):
        """Sets the subscription_summary of this SubscriptionAndUser.


        :param subscription_summary: The subscription_summary of this SubscriptionAndUser.  # noqa: E501
        :type: OneOfSubscriptionAndUserSubscriptionSummary
        """

        self._subscription_summary = subscription_summary

    @property
    def maximum_number_of_users(self):
        """Gets the maximum_number_of_users of this SubscriptionAndUser.  # noqa: E501


        :return: The maximum_number_of_users of this SubscriptionAndUser.  # noqa: E501
        :rtype: int
        """
        return self._maximum_number_of_users

    @maximum_number_of_users.setter
    def maximum_number_of_users(self, maximum_number_of_users):
        """Sets the maximum_number_of_users of this SubscriptionAndUser.


        :param maximum_number_of_users: The maximum_number_of_users of this SubscriptionAndUser.  # noqa: E501
        :type: int
        """

        self._maximum_number_of_users = maximum_number_of_users

    @property
    def public_maps(self):
        """Gets the public_maps of this SubscriptionAndUser.  # noqa: E501


        :return: The public_maps of this SubscriptionAndUser.  # noqa: E501
        :rtype: bool
        """
        return self._public_maps

    @public_maps.setter
    def public_maps(self, public_maps):
        """Sets the public_maps of this SubscriptionAndUser.


        :param public_maps: The public_maps of this SubscriptionAndUser.  # noqa: E501
        :type: bool
        """

        self._public_maps = public_maps

    @property
    def rest_api(self):
        """Gets the rest_api of this SubscriptionAndUser.  # noqa: E501


        :return: The rest_api of this SubscriptionAndUser.  # noqa: E501
        :rtype: bool
        """
        return self._rest_api

    @rest_api.setter
    def rest_api(self, rest_api):
        """Sets the rest_api of this SubscriptionAndUser.


        :param rest_api: The rest_api of this SubscriptionAndUser.  # noqa: E501
        :type: bool
        """

        self._rest_api = rest_api

    @property
    def live_layers(self):
        """Gets the live_layers of this SubscriptionAndUser.  # noqa: E501


        :return: The live_layers of this SubscriptionAndUser.  # noqa: E501
        :rtype: bool
        """
        return self._live_layers

    @live_layers.setter
    def live_layers(self, live_layers):
        """Sets the live_layers of this SubscriptionAndUser.


        :param live_layers: The live_layers of this SubscriptionAndUser.  # noqa: E501
        :type: bool
        """

        self._live_layers = live_layers

    @property
    def content_count(self):
        """Gets the content_count of this SubscriptionAndUser.  # noqa: E501


        :return: The content_count of this SubscriptionAndUser.  # noqa: E501
        :rtype: OneOfSubscriptionAndUserContentCount
        """
        return self._content_count

    @content_count.setter
    def content_count(self, content_count):
        """Sets the content_count of this SubscriptionAndUser.


        :param content_count: The content_count of this SubscriptionAndUser.  # noqa: E501
        :type: OneOfSubscriptionAndUserContentCount
        """

        self._content_count = content_count

    @property
    def query_optimizer(self):
        """Gets the query_optimizer of this SubscriptionAndUser.  # noqa: E501


        :return: The query_optimizer of this SubscriptionAndUser.  # noqa: E501
        :rtype: bool
        """
        return self._query_optimizer

    @query_optimizer.setter
    def query_optimizer(self, query_optimizer):
        """Sets the query_optimizer of this SubscriptionAndUser.


        :param query_optimizer: The query_optimizer of this SubscriptionAndUser.  # noqa: E501
        :type: bool
        """

        self._query_optimizer = query_optimizer

    @property
    def heatmap_generation(self):
        """Gets the heatmap_generation of this SubscriptionAndUser.  # noqa: E501


        :return: The heatmap_generation of this SubscriptionAndUser.  # noqa: E501
        :rtype: bool
        """
        return self._heatmap_generation

    @heatmap_generation.setter
    def heatmap_generation(self, heatmap_generation):
        """Sets the heatmap_generation of this SubscriptionAndUser.


        :param heatmap_generation: The heatmap_generation of this SubscriptionAndUser.  # noqa: E501
        :type: bool
        """

        self._heatmap_generation = heatmap_generation

    @property
    def grace_period_end_date(self):
        """Gets the grace_period_end_date of this SubscriptionAndUser.  # noqa: E501


        :return: The grace_period_end_date of this SubscriptionAndUser.  # noqa: E501
        :rtype: datetime
        """
        return self._grace_period_end_date

    @grace_period_end_date.setter
    def grace_period_end_date(self, grace_period_end_date):
        """Sets the grace_period_end_date of this SubscriptionAndUser.


        :param grace_period_end_date: The grace_period_end_date of this SubscriptionAndUser.  # noqa: E501
        :type: datetime
        """

        self._grace_period_end_date = grace_period_end_date

    @property
    def license_expired(self):
        """Gets the license_expired of this SubscriptionAndUser.  # noqa: E501


        :return: The license_expired of this SubscriptionAndUser.  # noqa: E501
        :rtype: bool
        """
        return self._license_expired

    @license_expired.setter
    def license_expired(self, license_expired):
        """Sets the license_expired of this SubscriptionAndUser.


        :param license_expired: The license_expired of this SubscriptionAndUser.  # noqa: E501
        :type: bool
        """

        self._license_expired = license_expired

    @property
    def composite_scoring(self):
        """Gets the composite_scoring of this SubscriptionAndUser.  # noqa: E501


        :return: The composite_scoring of this SubscriptionAndUser.  # noqa: E501
        :rtype: bool
        """
        return self._composite_scoring

    @composite_scoring.setter
    def composite_scoring(self, composite_scoring):
        """Sets the composite_scoring of this SubscriptionAndUser.


        :param composite_scoring: The composite_scoring of this SubscriptionAndUser.  # noqa: E501
        :type: bool
        """

        self._composite_scoring = composite_scoring

    @property
    def poi_analysis(self):
        """Gets the poi_analysis of this SubscriptionAndUser.  # noqa: E501


        :return: The poi_analysis of this SubscriptionAndUser.  # noqa: E501
        :rtype: bool
        """
        return self._poi_analysis

    @poi_analysis.setter
    def poi_analysis(self, poi_analysis):
        """Sets the poi_analysis of this SubscriptionAndUser.


        :param poi_analysis: The poi_analysis of this SubscriptionAndUser.  # noqa: E501
        :type: bool
        """

        self._poi_analysis = poi_analysis

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
        if issubclass(SubscriptionAndUser, dict):
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
        if not isinstance(other, SubscriptionAndUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
