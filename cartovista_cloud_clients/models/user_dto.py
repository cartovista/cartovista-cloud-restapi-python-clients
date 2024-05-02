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

class UserDTO(object):
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
        'is_anonymous': 'bool',
        'display_name': 'str',
        'name': 'str',
        'id': 'str',
        'is_group': 'bool',
        'last_modification_time': 'datetime',
        'creation_time': 'datetime',
        'tenant_id': 'str',
        'provider': 'SecurityProvider',
        'provider_name': 'str',
        'identifier': 'str',
        'provider_status': 'ProviderStatus',
        'path': 'str',
        'secure_object_permissions': 'list[PermissionPairDTO]',
        'first_name': 'str',
        'last_name': 'str',
        'username': 'str',
        'email_address': 'str',
        'notes': 'str',
        'last_login_time': 'datetime',
        'login_count': 'int',
        'access_failed_count': 'int',
        'folder_id': 'str',
        'paid_products': 'list[ProductUserDTO]',
        'app_name': 'str',
        'is_locked': 'bool',
        'password_reset_code': 'str',
        'thumbnail_url': 'str',
        'lockout_reason': 'str',
        'lockout_start_time': 'datetime',
        'groups': 'list[GroupDTO]',
        'last_visit': 'datetime',
        'can_dismiss_subscription_banner': 'bool',
        'did_dimiss_schedule_notice': 'bool',
        'company_role': 'str',
        'phone': 'str',
        'disclaimer_accepted_time': 'datetime'
    }

    attribute_map = {
        'is_anonymous': 'isAnonymous',
        'display_name': 'displayName',
        'name': 'name',
        'id': 'id',
        'is_group': 'isGroup',
        'last_modification_time': 'lastModificationTime',
        'creation_time': 'creationTime',
        'tenant_id': 'tenantId',
        'provider': 'provider',
        'provider_name': 'providerName',
        'identifier': 'identifier',
        'provider_status': 'providerStatus',
        'path': 'path',
        'secure_object_permissions': 'secureObjectPermissions',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'username': 'username',
        'email_address': 'emailAddress',
        'notes': 'notes',
        'last_login_time': 'lastLoginTime',
        'login_count': 'loginCount',
        'access_failed_count': 'accessFailedCount',
        'folder_id': 'folderId',
        'paid_products': 'paidProducts',
        'app_name': 'appName',
        'is_locked': 'isLocked',
        'password_reset_code': 'passwordResetCode',
        'thumbnail_url': 'thumbnailURL',
        'lockout_reason': 'lockoutReason',
        'lockout_start_time': 'lockoutStartTime',
        'groups': 'groups',
        'last_visit': 'lastVisit',
        'can_dismiss_subscription_banner': 'canDismissSubscriptionBanner',
        'did_dimiss_schedule_notice': 'didDimissScheduleNotice',
        'company_role': 'companyRole',
        'phone': 'phone',
        'disclaimer_accepted_time': 'disclaimerAcceptedTime'
    }

    def __init__(self, is_anonymous=None, display_name=None, name=None, id=None, is_group=None, last_modification_time=None, creation_time=None, tenant_id=None, provider=None, provider_name=None, identifier=None, provider_status=None, path=None, secure_object_permissions=None, first_name=None, last_name=None, username=None, email_address=None, notes=None, last_login_time=None, login_count=None, access_failed_count=None, folder_id=None, paid_products=None, app_name=None, is_locked=None, password_reset_code=None, thumbnail_url=None, lockout_reason=None, lockout_start_time=None, groups=None, last_visit=None, can_dismiss_subscription_banner=None, did_dimiss_schedule_notice=None, company_role=None, phone=None, disclaimer_accepted_time=None):  # noqa: E501
        """UserDTO - a model defined in Swagger"""  # noqa: E501
        self._is_anonymous = None
        self._display_name = None
        self._name = None
        self._id = None
        self._is_group = None
        self._last_modification_time = None
        self._creation_time = None
        self._tenant_id = None
        self._provider = None
        self._provider_name = None
        self._identifier = None
        self._provider_status = None
        self._path = None
        self._secure_object_permissions = None
        self._first_name = None
        self._last_name = None
        self._username = None
        self._email_address = None
        self._notes = None
        self._last_login_time = None
        self._login_count = None
        self._access_failed_count = None
        self._folder_id = None
        self._paid_products = None
        self._app_name = None
        self._is_locked = None
        self._password_reset_code = None
        self._thumbnail_url = None
        self._lockout_reason = None
        self._lockout_start_time = None
        self._groups = None
        self._last_visit = None
        self._can_dismiss_subscription_banner = None
        self._did_dimiss_schedule_notice = None
        self._company_role = None
        self._phone = None
        self._disclaimer_accepted_time = None
        self.discriminator = None
        if is_anonymous is not None:
            self.is_anonymous = is_anonymous
        if display_name is not None:
            self.display_name = display_name
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if is_group is not None:
            self.is_group = is_group
        if last_modification_time is not None:
            self.last_modification_time = last_modification_time
        if creation_time is not None:
            self.creation_time = creation_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if provider is not None:
            self.provider = provider
        if provider_name is not None:
            self.provider_name = provider_name
        if identifier is not None:
            self.identifier = identifier
        if provider_status is not None:
            self.provider_status = provider_status
        if path is not None:
            self.path = path
        if secure_object_permissions is not None:
            self.secure_object_permissions = secure_object_permissions
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if username is not None:
            self.username = username
        if email_address is not None:
            self.email_address = email_address
        if notes is not None:
            self.notes = notes
        if last_login_time is not None:
            self.last_login_time = last_login_time
        if login_count is not None:
            self.login_count = login_count
        if access_failed_count is not None:
            self.access_failed_count = access_failed_count
        if folder_id is not None:
            self.folder_id = folder_id
        if paid_products is not None:
            self.paid_products = paid_products
        if app_name is not None:
            self.app_name = app_name
        if is_locked is not None:
            self.is_locked = is_locked
        if password_reset_code is not None:
            self.password_reset_code = password_reset_code
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        if lockout_reason is not None:
            self.lockout_reason = lockout_reason
        if lockout_start_time is not None:
            self.lockout_start_time = lockout_start_time
        if groups is not None:
            self.groups = groups
        if last_visit is not None:
            self.last_visit = last_visit
        if can_dismiss_subscription_banner is not None:
            self.can_dismiss_subscription_banner = can_dismiss_subscription_banner
        if did_dimiss_schedule_notice is not None:
            self.did_dimiss_schedule_notice = did_dimiss_schedule_notice
        if company_role is not None:
            self.company_role = company_role
        if phone is not None:
            self.phone = phone
        if disclaimer_accepted_time is not None:
            self.disclaimer_accepted_time = disclaimer_accepted_time

    @property
    def is_anonymous(self):
        """Gets the is_anonymous of this UserDTO.  # noqa: E501


        :return: The is_anonymous of this UserDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_anonymous

    @is_anonymous.setter
    def is_anonymous(self, is_anonymous):
        """Sets the is_anonymous of this UserDTO.


        :param is_anonymous: The is_anonymous of this UserDTO.  # noqa: E501
        :type: bool
        """

        self._is_anonymous = is_anonymous

    @property
    def display_name(self):
        """Gets the display_name of this UserDTO.  # noqa: E501


        :return: The display_name of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UserDTO.


        :param display_name: The display_name of this UserDTO.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def name(self):
        """Gets the name of this UserDTO.  # noqa: E501


        :return: The name of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserDTO.


        :param name: The name of this UserDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this UserDTO.  # noqa: E501


        :return: The id of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDTO.


        :param id: The id of this UserDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_group(self):
        """Gets the is_group of this UserDTO.  # noqa: E501


        :return: The is_group of this UserDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_group

    @is_group.setter
    def is_group(self, is_group):
        """Sets the is_group of this UserDTO.


        :param is_group: The is_group of this UserDTO.  # noqa: E501
        :type: bool
        """

        self._is_group = is_group

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this UserDTO.  # noqa: E501


        :return: The last_modification_time of this UserDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this UserDTO.


        :param last_modification_time: The last_modification_time of this UserDTO.  # noqa: E501
        :type: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def creation_time(self):
        """Gets the creation_time of this UserDTO.  # noqa: E501


        :return: The creation_time of this UserDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this UserDTO.


        :param creation_time: The creation_time of this UserDTO.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this UserDTO.  # noqa: E501


        :return: The tenant_id of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this UserDTO.


        :param tenant_id: The tenant_id of this UserDTO.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def provider(self):
        """Gets the provider of this UserDTO.  # noqa: E501


        :return: The provider of this UserDTO.  # noqa: E501
        :rtype: SecurityProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this UserDTO.


        :param provider: The provider of this UserDTO.  # noqa: E501
        :type: SecurityProvider
        """

        self._provider = provider

    @property
    def provider_name(self):
        """Gets the provider_name of this UserDTO.  # noqa: E501


        :return: The provider_name of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this UserDTO.


        :param provider_name: The provider_name of this UserDTO.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def identifier(self):
        """Gets the identifier of this UserDTO.  # noqa: E501


        :return: The identifier of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this UserDTO.


        :param identifier: The identifier of this UserDTO.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def provider_status(self):
        """Gets the provider_status of this UserDTO.  # noqa: E501


        :return: The provider_status of this UserDTO.  # noqa: E501
        :rtype: ProviderStatus
        """
        return self._provider_status

    @provider_status.setter
    def provider_status(self, provider_status):
        """Sets the provider_status of this UserDTO.


        :param provider_status: The provider_status of this UserDTO.  # noqa: E501
        :type: ProviderStatus
        """

        self._provider_status = provider_status

    @property
    def path(self):
        """Gets the path of this UserDTO.  # noqa: E501


        :return: The path of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this UserDTO.


        :param path: The path of this UserDTO.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def secure_object_permissions(self):
        """Gets the secure_object_permissions of this UserDTO.  # noqa: E501


        :return: The secure_object_permissions of this UserDTO.  # noqa: E501
        :rtype: list[PermissionPairDTO]
        """
        return self._secure_object_permissions

    @secure_object_permissions.setter
    def secure_object_permissions(self, secure_object_permissions):
        """Sets the secure_object_permissions of this UserDTO.


        :param secure_object_permissions: The secure_object_permissions of this UserDTO.  # noqa: E501
        :type: list[PermissionPairDTO]
        """

        self._secure_object_permissions = secure_object_permissions

    @property
    def first_name(self):
        """Gets the first_name of this UserDTO.  # noqa: E501


        :return: The first_name of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserDTO.


        :param first_name: The first_name of this UserDTO.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserDTO.  # noqa: E501


        :return: The last_name of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserDTO.


        :param last_name: The last_name of this UserDTO.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def username(self):
        """Gets the username of this UserDTO.  # noqa: E501


        :return: The username of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserDTO.


        :param username: The username of this UserDTO.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def email_address(self):
        """Gets the email_address of this UserDTO.  # noqa: E501


        :return: The email_address of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UserDTO.


        :param email_address: The email_address of this UserDTO.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def notes(self):
        """Gets the notes of this UserDTO.  # noqa: E501


        :return: The notes of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this UserDTO.


        :param notes: The notes of this UserDTO.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def last_login_time(self):
        """Gets the last_login_time of this UserDTO.  # noqa: E501


        :return: The last_login_time of this UserDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """Sets the last_login_time of this UserDTO.


        :param last_login_time: The last_login_time of this UserDTO.  # noqa: E501
        :type: datetime
        """

        self._last_login_time = last_login_time

    @property
    def login_count(self):
        """Gets the login_count of this UserDTO.  # noqa: E501


        :return: The login_count of this UserDTO.  # noqa: E501
        :rtype: int
        """
        return self._login_count

    @login_count.setter
    def login_count(self, login_count):
        """Sets the login_count of this UserDTO.


        :param login_count: The login_count of this UserDTO.  # noqa: E501
        :type: int
        """

        self._login_count = login_count

    @property
    def access_failed_count(self):
        """Gets the access_failed_count of this UserDTO.  # noqa: E501


        :return: The access_failed_count of this UserDTO.  # noqa: E501
        :rtype: int
        """
        return self._access_failed_count

    @access_failed_count.setter
    def access_failed_count(self, access_failed_count):
        """Sets the access_failed_count of this UserDTO.


        :param access_failed_count: The access_failed_count of this UserDTO.  # noqa: E501
        :type: int
        """

        self._access_failed_count = access_failed_count

    @property
    def folder_id(self):
        """Gets the folder_id of this UserDTO.  # noqa: E501


        :return: The folder_id of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this UserDTO.


        :param folder_id: The folder_id of this UserDTO.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def paid_products(self):
        """Gets the paid_products of this UserDTO.  # noqa: E501


        :return: The paid_products of this UserDTO.  # noqa: E501
        :rtype: list[ProductUserDTO]
        """
        return self._paid_products

    @paid_products.setter
    def paid_products(self, paid_products):
        """Sets the paid_products of this UserDTO.


        :param paid_products: The paid_products of this UserDTO.  # noqa: E501
        :type: list[ProductUserDTO]
        """

        self._paid_products = paid_products

    @property
    def app_name(self):
        """Gets the app_name of this UserDTO.  # noqa: E501


        :return: The app_name of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this UserDTO.


        :param app_name: The app_name of this UserDTO.  # noqa: E501
        :type: str
        """

        self._app_name = app_name

    @property
    def is_locked(self):
        """Gets the is_locked of this UserDTO.  # noqa: E501


        :return: The is_locked of this UserDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this UserDTO.


        :param is_locked: The is_locked of this UserDTO.  # noqa: E501
        :type: bool
        """

        self._is_locked = is_locked

    @property
    def password_reset_code(self):
        """Gets the password_reset_code of this UserDTO.  # noqa: E501


        :return: The password_reset_code of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._password_reset_code

    @password_reset_code.setter
    def password_reset_code(self, password_reset_code):
        """Sets the password_reset_code of this UserDTO.


        :param password_reset_code: The password_reset_code of this UserDTO.  # noqa: E501
        :type: str
        """

        self._password_reset_code = password_reset_code

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this UserDTO.  # noqa: E501


        :return: The thumbnail_url of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this UserDTO.


        :param thumbnail_url: The thumbnail_url of this UserDTO.  # noqa: E501
        :type: str
        """

        self._thumbnail_url = thumbnail_url

    @property
    def lockout_reason(self):
        """Gets the lockout_reason of this UserDTO.  # noqa: E501


        :return: The lockout_reason of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._lockout_reason

    @lockout_reason.setter
    def lockout_reason(self, lockout_reason):
        """Sets the lockout_reason of this UserDTO.


        :param lockout_reason: The lockout_reason of this UserDTO.  # noqa: E501
        :type: str
        """

        self._lockout_reason = lockout_reason

    @property
    def lockout_start_time(self):
        """Gets the lockout_start_time of this UserDTO.  # noqa: E501


        :return: The lockout_start_time of this UserDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._lockout_start_time

    @lockout_start_time.setter
    def lockout_start_time(self, lockout_start_time):
        """Sets the lockout_start_time of this UserDTO.


        :param lockout_start_time: The lockout_start_time of this UserDTO.  # noqa: E501
        :type: datetime
        """

        self._lockout_start_time = lockout_start_time

    @property
    def groups(self):
        """Gets the groups of this UserDTO.  # noqa: E501


        :return: The groups of this UserDTO.  # noqa: E501
        :rtype: list[GroupDTO]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserDTO.


        :param groups: The groups of this UserDTO.  # noqa: E501
        :type: list[GroupDTO]
        """

        self._groups = groups

    @property
    def last_visit(self):
        """Gets the last_visit of this UserDTO.  # noqa: E501


        :return: The last_visit of this UserDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_visit

    @last_visit.setter
    def last_visit(self, last_visit):
        """Sets the last_visit of this UserDTO.


        :param last_visit: The last_visit of this UserDTO.  # noqa: E501
        :type: datetime
        """

        self._last_visit = last_visit

    @property
    def can_dismiss_subscription_banner(self):
        """Gets the can_dismiss_subscription_banner of this UserDTO.  # noqa: E501


        :return: The can_dismiss_subscription_banner of this UserDTO.  # noqa: E501
        :rtype: bool
        """
        return self._can_dismiss_subscription_banner

    @can_dismiss_subscription_banner.setter
    def can_dismiss_subscription_banner(self, can_dismiss_subscription_banner):
        """Sets the can_dismiss_subscription_banner of this UserDTO.


        :param can_dismiss_subscription_banner: The can_dismiss_subscription_banner of this UserDTO.  # noqa: E501
        :type: bool
        """

        self._can_dismiss_subscription_banner = can_dismiss_subscription_banner

    @property
    def did_dimiss_schedule_notice(self):
        """Gets the did_dimiss_schedule_notice of this UserDTO.  # noqa: E501


        :return: The did_dimiss_schedule_notice of this UserDTO.  # noqa: E501
        :rtype: bool
        """
        return self._did_dimiss_schedule_notice

    @did_dimiss_schedule_notice.setter
    def did_dimiss_schedule_notice(self, did_dimiss_schedule_notice):
        """Sets the did_dimiss_schedule_notice of this UserDTO.


        :param did_dimiss_schedule_notice: The did_dimiss_schedule_notice of this UserDTO.  # noqa: E501
        :type: bool
        """

        self._did_dimiss_schedule_notice = did_dimiss_schedule_notice

    @property
    def company_role(self):
        """Gets the company_role of this UserDTO.  # noqa: E501


        :return: The company_role of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._company_role

    @company_role.setter
    def company_role(self, company_role):
        """Sets the company_role of this UserDTO.


        :param company_role: The company_role of this UserDTO.  # noqa: E501
        :type: str
        """

        self._company_role = company_role

    @property
    def phone(self):
        """Gets the phone of this UserDTO.  # noqa: E501


        :return: The phone of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UserDTO.


        :param phone: The phone of this UserDTO.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def disclaimer_accepted_time(self):
        """Gets the disclaimer_accepted_time of this UserDTO.  # noqa: E501


        :return: The disclaimer_accepted_time of this UserDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._disclaimer_accepted_time

    @disclaimer_accepted_time.setter
    def disclaimer_accepted_time(self, disclaimer_accepted_time):
        """Sets the disclaimer_accepted_time of this UserDTO.


        :param disclaimer_accepted_time: The disclaimer_accepted_time of this UserDTO.  # noqa: E501
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
        if issubclass(UserDTO, dict):
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
        if not isinstance(other, UserDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
