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

class User(object):
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
        'security_identifier': 'str',
        'security_provider_identity': 'str',
        'email_address': 'str',
        'user_name': 'str',
        'display_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'notes': 'str',
        'roles': 'list[PermissionDTO]',
        'enabled': 'bool',
        'last_login_time': 'datetime',
        'last_visit': 'datetime',
        'creation_time': 'datetime',
        'modification_time': 'datetime',
        'security_provider': 'str',
        'provider_status': 'str',
        'provider_name': 'str',
        'app_name': 'str',
        'access_failed_count': 'int',
        'lockout_reason': 'str',
        'lockout_start_time': 'datetime',
        'thumbnail_url': 'str',
        'can_dismiss_subscription_banner': 'bool',
        'did_dimiss_schedule_notice': 'bool',
        'groups': 'list[Group]',
        'disclaimer_accepted_time': 'datetime'
    }

    attribute_map = {
        'security_identifier': 'securityIdentifier',
        'security_provider_identity': 'securityProviderIdentity',
        'email_address': 'emailAddress',
        'user_name': 'userName',
        'display_name': 'displayName',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'notes': 'notes',
        'roles': 'roles',
        'enabled': 'enabled',
        'last_login_time': 'lastLoginTime',
        'last_visit': 'lastVisit',
        'creation_time': 'creationTime',
        'modification_time': 'modificationTime',
        'security_provider': 'securityProvider',
        'provider_status': 'providerStatus',
        'provider_name': 'providerName',
        'app_name': 'appName',
        'access_failed_count': 'accessFailedCount',
        'lockout_reason': 'lockoutReason',
        'lockout_start_time': 'lockoutStartTime',
        'thumbnail_url': 'thumbnailUrl',
        'can_dismiss_subscription_banner': 'canDismissSubscriptionBanner',
        'did_dimiss_schedule_notice': 'didDimissScheduleNotice',
        'groups': 'groups',
        'disclaimer_accepted_time': 'disclaimerAcceptedTime'
    }

    def __init__(self, security_identifier=None, security_provider_identity=None, email_address=None, user_name=None, display_name=None, first_name=None, last_name=None, notes=None, roles=None, enabled=None, last_login_time=None, last_visit=None, creation_time=None, modification_time=None, security_provider=None, provider_status=None, provider_name=None, app_name=None, access_failed_count=None, lockout_reason=None, lockout_start_time=None, thumbnail_url=None, can_dismiss_subscription_banner=None, did_dimiss_schedule_notice=None, groups=None, disclaimer_accepted_time=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._security_identifier = None
        self._security_provider_identity = None
        self._email_address = None
        self._user_name = None
        self._display_name = None
        self._first_name = None
        self._last_name = None
        self._notes = None
        self._roles = None
        self._enabled = None
        self._last_login_time = None
        self._last_visit = None
        self._creation_time = None
        self._modification_time = None
        self._security_provider = None
        self._provider_status = None
        self._provider_name = None
        self._app_name = None
        self._access_failed_count = None
        self._lockout_reason = None
        self._lockout_start_time = None
        self._thumbnail_url = None
        self._can_dismiss_subscription_banner = None
        self._did_dimiss_schedule_notice = None
        self._groups = None
        self._disclaimer_accepted_time = None
        self.discriminator = None
        if security_identifier is not None:
            self.security_identifier = security_identifier
        if security_provider_identity is not None:
            self.security_provider_identity = security_provider_identity
        if email_address is not None:
            self.email_address = email_address
        if user_name is not None:
            self.user_name = user_name
        if display_name is not None:
            self.display_name = display_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if notes is not None:
            self.notes = notes
        if roles is not None:
            self.roles = roles
        if enabled is not None:
            self.enabled = enabled
        if last_login_time is not None:
            self.last_login_time = last_login_time
        if last_visit is not None:
            self.last_visit = last_visit
        if creation_time is not None:
            self.creation_time = creation_time
        if modification_time is not None:
            self.modification_time = modification_time
        if security_provider is not None:
            self.security_provider = security_provider
        if provider_status is not None:
            self.provider_status = provider_status
        if provider_name is not None:
            self.provider_name = provider_name
        if app_name is not None:
            self.app_name = app_name
        if access_failed_count is not None:
            self.access_failed_count = access_failed_count
        if lockout_reason is not None:
            self.lockout_reason = lockout_reason
        if lockout_start_time is not None:
            self.lockout_start_time = lockout_start_time
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        if can_dismiss_subscription_banner is not None:
            self.can_dismiss_subscription_banner = can_dismiss_subscription_banner
        if did_dimiss_schedule_notice is not None:
            self.did_dimiss_schedule_notice = did_dimiss_schedule_notice
        if groups is not None:
            self.groups = groups
        if disclaimer_accepted_time is not None:
            self.disclaimer_accepted_time = disclaimer_accepted_time

    @property
    def security_identifier(self):
        """Gets the security_identifier of this User.  # noqa: E501


        :return: The security_identifier of this User.  # noqa: E501
        :rtype: str
        """
        return self._security_identifier

    @security_identifier.setter
    def security_identifier(self, security_identifier):
        """Sets the security_identifier of this User.


        :param security_identifier: The security_identifier of this User.  # noqa: E501
        :type: str
        """

        self._security_identifier = security_identifier

    @property
    def security_provider_identity(self):
        """Gets the security_provider_identity of this User.  # noqa: E501


        :return: The security_provider_identity of this User.  # noqa: E501
        :rtype: str
        """
        return self._security_provider_identity

    @security_provider_identity.setter
    def security_provider_identity(self, security_provider_identity):
        """Sets the security_provider_identity of this User.


        :param security_provider_identity: The security_provider_identity of this User.  # noqa: E501
        :type: str
        """

        self._security_provider_identity = security_provider_identity

    @property
    def email_address(self):
        """Gets the email_address of this User.  # noqa: E501


        :return: The email_address of this User.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this User.


        :param email_address: The email_address of this User.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def user_name(self):
        """Gets the user_name of this User.  # noqa: E501


        :return: The user_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this User.


        :param user_name: The user_name of this User.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def display_name(self):
        """Gets the display_name of this User.  # noqa: E501


        :return: The display_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this User.


        :param display_name: The display_name of this User.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501


        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501


        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def notes(self):
        """Gets the notes of this User.  # noqa: E501


        :return: The notes of this User.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this User.


        :param notes: The notes of this User.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def roles(self):
        """Gets the roles of this User.  # noqa: E501


        :return: The roles of this User.  # noqa: E501
        :rtype: list[PermissionDTO]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this User.


        :param roles: The roles of this User.  # noqa: E501
        :type: list[PermissionDTO]
        """

        self._roles = roles

    @property
    def enabled(self):
        """Gets the enabled of this User.  # noqa: E501


        :return: The enabled of this User.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this User.


        :param enabled: The enabled of this User.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def last_login_time(self):
        """Gets the last_login_time of this User.  # noqa: E501


        :return: The last_login_time of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """Sets the last_login_time of this User.


        :param last_login_time: The last_login_time of this User.  # noqa: E501
        :type: datetime
        """

        self._last_login_time = last_login_time

    @property
    def last_visit(self):
        """Gets the last_visit of this User.  # noqa: E501


        :return: The last_visit of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._last_visit

    @last_visit.setter
    def last_visit(self, last_visit):
        """Sets the last_visit of this User.


        :param last_visit: The last_visit of this User.  # noqa: E501
        :type: datetime
        """

        self._last_visit = last_visit

    @property
    def creation_time(self):
        """Gets the creation_time of this User.  # noqa: E501


        :return: The creation_time of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this User.


        :param creation_time: The creation_time of this User.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def modification_time(self):
        """Gets the modification_time of this User.  # noqa: E501


        :return: The modification_time of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._modification_time

    @modification_time.setter
    def modification_time(self, modification_time):
        """Sets the modification_time of this User.


        :param modification_time: The modification_time of this User.  # noqa: E501
        :type: datetime
        """

        self._modification_time = modification_time

    @property
    def security_provider(self):
        """Gets the security_provider of this User.  # noqa: E501


        :return: The security_provider of this User.  # noqa: E501
        :rtype: str
        """
        return self._security_provider

    @security_provider.setter
    def security_provider(self, security_provider):
        """Sets the security_provider of this User.


        :param security_provider: The security_provider of this User.  # noqa: E501
        :type: str
        """

        self._security_provider = security_provider

    @property
    def provider_status(self):
        """Gets the provider_status of this User.  # noqa: E501


        :return: The provider_status of this User.  # noqa: E501
        :rtype: str
        """
        return self._provider_status

    @provider_status.setter
    def provider_status(self, provider_status):
        """Sets the provider_status of this User.


        :param provider_status: The provider_status of this User.  # noqa: E501
        :type: str
        """

        self._provider_status = provider_status

    @property
    def provider_name(self):
        """Gets the provider_name of this User.  # noqa: E501


        :return: The provider_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this User.


        :param provider_name: The provider_name of this User.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def app_name(self):
        """Gets the app_name of this User.  # noqa: E501


        :return: The app_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this User.


        :param app_name: The app_name of this User.  # noqa: E501
        :type: str
        """

        self._app_name = app_name

    @property
    def access_failed_count(self):
        """Gets the access_failed_count of this User.  # noqa: E501


        :return: The access_failed_count of this User.  # noqa: E501
        :rtype: int
        """
        return self._access_failed_count

    @access_failed_count.setter
    def access_failed_count(self, access_failed_count):
        """Sets the access_failed_count of this User.


        :param access_failed_count: The access_failed_count of this User.  # noqa: E501
        :type: int
        """

        self._access_failed_count = access_failed_count

    @property
    def lockout_reason(self):
        """Gets the lockout_reason of this User.  # noqa: E501


        :return: The lockout_reason of this User.  # noqa: E501
        :rtype: str
        """
        return self._lockout_reason

    @lockout_reason.setter
    def lockout_reason(self, lockout_reason):
        """Sets the lockout_reason of this User.


        :param lockout_reason: The lockout_reason of this User.  # noqa: E501
        :type: str
        """

        self._lockout_reason = lockout_reason

    @property
    def lockout_start_time(self):
        """Gets the lockout_start_time of this User.  # noqa: E501


        :return: The lockout_start_time of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._lockout_start_time

    @lockout_start_time.setter
    def lockout_start_time(self, lockout_start_time):
        """Sets the lockout_start_time of this User.


        :param lockout_start_time: The lockout_start_time of this User.  # noqa: E501
        :type: datetime
        """

        self._lockout_start_time = lockout_start_time

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this User.  # noqa: E501


        :return: The thumbnail_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this User.


        :param thumbnail_url: The thumbnail_url of this User.  # noqa: E501
        :type: str
        """

        self._thumbnail_url = thumbnail_url

    @property
    def can_dismiss_subscription_banner(self):
        """Gets the can_dismiss_subscription_banner of this User.  # noqa: E501


        :return: The can_dismiss_subscription_banner of this User.  # noqa: E501
        :rtype: bool
        """
        return self._can_dismiss_subscription_banner

    @can_dismiss_subscription_banner.setter
    def can_dismiss_subscription_banner(self, can_dismiss_subscription_banner):
        """Sets the can_dismiss_subscription_banner of this User.


        :param can_dismiss_subscription_banner: The can_dismiss_subscription_banner of this User.  # noqa: E501
        :type: bool
        """

        self._can_dismiss_subscription_banner = can_dismiss_subscription_banner

    @property
    def did_dimiss_schedule_notice(self):
        """Gets the did_dimiss_schedule_notice of this User.  # noqa: E501


        :return: The did_dimiss_schedule_notice of this User.  # noqa: E501
        :rtype: bool
        """
        return self._did_dimiss_schedule_notice

    @did_dimiss_schedule_notice.setter
    def did_dimiss_schedule_notice(self, did_dimiss_schedule_notice):
        """Sets the did_dimiss_schedule_notice of this User.


        :param did_dimiss_schedule_notice: The did_dimiss_schedule_notice of this User.  # noqa: E501
        :type: bool
        """

        self._did_dimiss_schedule_notice = did_dimiss_schedule_notice

    @property
    def groups(self):
        """Gets the groups of this User.  # noqa: E501


        :return: The groups of this User.  # noqa: E501
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this User.


        :param groups: The groups of this User.  # noqa: E501
        :type: list[Group]
        """

        self._groups = groups

    @property
    def disclaimer_accepted_time(self):
        """Gets the disclaimer_accepted_time of this User.  # noqa: E501


        :return: The disclaimer_accepted_time of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._disclaimer_accepted_time

    @disclaimer_accepted_time.setter
    def disclaimer_accepted_time(self, disclaimer_accepted_time):
        """Sets the disclaimer_accepted_time of this User.


        :param disclaimer_accepted_time: The disclaimer_accepted_time of this User.  # noqa: E501
        :type: datetime
        """

        self._disclaimer_accepted_time = disclaimer_accepted_time

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
