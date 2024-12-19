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

class Map(object):
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
        'title': 'str',
        'unique_identifier': 'str',
        'description': 'str',
        'language': 'LanguageEnum',
        'type': 'MapTypeEnum',
        'is_territory_manager': 'bool',
        'editable': 'bool',
        'seo_title': 'str',
        'seo_description': 'str',
        'seo_custom_html': 'str',
        'thumbnail_url': 'str',
        'thumbnail_url_expiry': 'datetime',
        'creation_date': 'datetime',
        'last_update': 'datetime',
        'owner_name': 'str',
        'keywords': 'list[KeywordDTO]',
        'can_edit': 'bool',
        'public_access': 'bool',
        'vanity_url': 'str',
        'has_onboarding': 'bool',
        'is_locked': 'bool',
        'can_add_layers': 'bool',
        'has_custom_thumbnail': 'bool',
        'is_poi_analysis': 'bool',
        'folder_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'unique_identifier': 'uniqueIdentifier',
        'description': 'description',
        'language': 'language',
        'type': 'type',
        'is_territory_manager': 'isTerritoryManager',
        'editable': 'editable',
        'seo_title': 'seoTitle',
        'seo_description': 'seoDescription',
        'seo_custom_html': 'seoCustomHTML',
        'thumbnail_url': 'thumbnailUrl',
        'thumbnail_url_expiry': 'thumbnailUrlExpiry',
        'creation_date': 'creationDate',
        'last_update': 'lastUpdate',
        'owner_name': 'ownerName',
        'keywords': 'keywords',
        'can_edit': 'canEdit',
        'public_access': 'publicAccess',
        'vanity_url': 'vanityUrl',
        'has_onboarding': 'hasOnboarding',
        'is_locked': 'isLocked',
        'can_add_layers': 'canAddLayers',
        'has_custom_thumbnail': 'hasCustomThumbnail',
        'is_poi_analysis': 'isPoiAnalysis',
        'folder_id': 'folderId'
    }

    def __init__(self, id=None, title=None, unique_identifier=None, description=None, language=None, type=None, is_territory_manager=None, editable=None, seo_title=None, seo_description=None, seo_custom_html=None, thumbnail_url=None, thumbnail_url_expiry=None, creation_date=None, last_update=None, owner_name=None, keywords=None, can_edit=None, public_access=None, vanity_url=None, has_onboarding=None, is_locked=None, can_add_layers=None, has_custom_thumbnail=None, is_poi_analysis=None, folder_id=None):  # noqa: E501
        """Map - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._unique_identifier = None
        self._description = None
        self._language = None
        self._type = None
        self._is_territory_manager = None
        self._editable = None
        self._seo_title = None
        self._seo_description = None
        self._seo_custom_html = None
        self._thumbnail_url = None
        self._thumbnail_url_expiry = None
        self._creation_date = None
        self._last_update = None
        self._owner_name = None
        self._keywords = None
        self._can_edit = None
        self._public_access = None
        self._vanity_url = None
        self._has_onboarding = None
        self._is_locked = None
        self._can_add_layers = None
        self._has_custom_thumbnail = None
        self._is_poi_analysis = None
        self._folder_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if unique_identifier is not None:
            self.unique_identifier = unique_identifier
        if description is not None:
            self.description = description
        if language is not None:
            self.language = language
        if type is not None:
            self.type = type
        if is_territory_manager is not None:
            self.is_territory_manager = is_territory_manager
        if editable is not None:
            self.editable = editable
        if seo_title is not None:
            self.seo_title = seo_title
        if seo_description is not None:
            self.seo_description = seo_description
        if seo_custom_html is not None:
            self.seo_custom_html = seo_custom_html
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        if thumbnail_url_expiry is not None:
            self.thumbnail_url_expiry = thumbnail_url_expiry
        if creation_date is not None:
            self.creation_date = creation_date
        if last_update is not None:
            self.last_update = last_update
        if owner_name is not None:
            self.owner_name = owner_name
        if keywords is not None:
            self.keywords = keywords
        if can_edit is not None:
            self.can_edit = can_edit
        if public_access is not None:
            self.public_access = public_access
        if vanity_url is not None:
            self.vanity_url = vanity_url
        if has_onboarding is not None:
            self.has_onboarding = has_onboarding
        if is_locked is not None:
            self.is_locked = is_locked
        if can_add_layers is not None:
            self.can_add_layers = can_add_layers
        if has_custom_thumbnail is not None:
            self.has_custom_thumbnail = has_custom_thumbnail
        if is_poi_analysis is not None:
            self.is_poi_analysis = is_poi_analysis
        if folder_id is not None:
            self.folder_id = folder_id

    @property
    def id(self):
        """Gets the id of this Map.  # noqa: E501


        :return: The id of this Map.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Map.


        :param id: The id of this Map.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this Map.  # noqa: E501


        :return: The title of this Map.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Map.


        :param title: The title of this Map.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this Map.  # noqa: E501


        :return: The unique_identifier of this Map.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this Map.


        :param unique_identifier: The unique_identifier of this Map.  # noqa: E501
        :type: str
        """

        self._unique_identifier = unique_identifier

    @property
    def description(self):
        """Gets the description of this Map.  # noqa: E501


        :return: The description of this Map.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Map.


        :param description: The description of this Map.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def language(self):
        """Gets the language of this Map.  # noqa: E501


        :return: The language of this Map.  # noqa: E501
        :rtype: LanguageEnum
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Map.


        :param language: The language of this Map.  # noqa: E501
        :type: LanguageEnum
        """

        self._language = language

    @property
    def type(self):
        """Gets the type of this Map.  # noqa: E501


        :return: The type of this Map.  # noqa: E501
        :rtype: MapTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Map.


        :param type: The type of this Map.  # noqa: E501
        :type: MapTypeEnum
        """

        self._type = type

    @property
    def is_territory_manager(self):
        """Gets the is_territory_manager of this Map.  # noqa: E501


        :return: The is_territory_manager of this Map.  # noqa: E501
        :rtype: bool
        """
        return self._is_territory_manager

    @is_territory_manager.setter
    def is_territory_manager(self, is_territory_manager):
        """Sets the is_territory_manager of this Map.


        :param is_territory_manager: The is_territory_manager of this Map.  # noqa: E501
        :type: bool
        """

        self._is_territory_manager = is_territory_manager

    @property
    def editable(self):
        """Gets the editable of this Map.  # noqa: E501


        :return: The editable of this Map.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this Map.


        :param editable: The editable of this Map.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def seo_title(self):
        """Gets the seo_title of this Map.  # noqa: E501


        :return: The seo_title of this Map.  # noqa: E501
        :rtype: str
        """
        return self._seo_title

    @seo_title.setter
    def seo_title(self, seo_title):
        """Sets the seo_title of this Map.


        :param seo_title: The seo_title of this Map.  # noqa: E501
        :type: str
        """

        self._seo_title = seo_title

    @property
    def seo_description(self):
        """Gets the seo_description of this Map.  # noqa: E501


        :return: The seo_description of this Map.  # noqa: E501
        :rtype: str
        """
        return self._seo_description

    @seo_description.setter
    def seo_description(self, seo_description):
        """Sets the seo_description of this Map.


        :param seo_description: The seo_description of this Map.  # noqa: E501
        :type: str
        """

        self._seo_description = seo_description

    @property
    def seo_custom_html(self):
        """Gets the seo_custom_html of this Map.  # noqa: E501


        :return: The seo_custom_html of this Map.  # noqa: E501
        :rtype: str
        """
        return self._seo_custom_html

    @seo_custom_html.setter
    def seo_custom_html(self, seo_custom_html):
        """Sets the seo_custom_html of this Map.


        :param seo_custom_html: The seo_custom_html of this Map.  # noqa: E501
        :type: str
        """

        self._seo_custom_html = seo_custom_html

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this Map.  # noqa: E501


        :return: The thumbnail_url of this Map.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this Map.


        :param thumbnail_url: The thumbnail_url of this Map.  # noqa: E501
        :type: str
        """

        self._thumbnail_url = thumbnail_url

    @property
    def thumbnail_url_expiry(self):
        """Gets the thumbnail_url_expiry of this Map.  # noqa: E501


        :return: The thumbnail_url_expiry of this Map.  # noqa: E501
        :rtype: datetime
        """
        return self._thumbnail_url_expiry

    @thumbnail_url_expiry.setter
    def thumbnail_url_expiry(self, thumbnail_url_expiry):
        """Sets the thumbnail_url_expiry of this Map.


        :param thumbnail_url_expiry: The thumbnail_url_expiry of this Map.  # noqa: E501
        :type: datetime
        """

        self._thumbnail_url_expiry = thumbnail_url_expiry

    @property
    def creation_date(self):
        """Gets the creation_date of this Map.  # noqa: E501


        :return: The creation_date of this Map.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Map.


        :param creation_date: The creation_date of this Map.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def last_update(self):
        """Gets the last_update of this Map.  # noqa: E501


        :return: The last_update of this Map.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this Map.


        :param last_update: The last_update of this Map.  # noqa: E501
        :type: datetime
        """

        self._last_update = last_update

    @property
    def owner_name(self):
        """Gets the owner_name of this Map.  # noqa: E501


        :return: The owner_name of this Map.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this Map.


        :param owner_name: The owner_name of this Map.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def keywords(self):
        """Gets the keywords of this Map.  # noqa: E501


        :return: The keywords of this Map.  # noqa: E501
        :rtype: list[KeywordDTO]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this Map.


        :param keywords: The keywords of this Map.  # noqa: E501
        :type: list[KeywordDTO]
        """

        self._keywords = keywords

    @property
    def can_edit(self):
        """Gets the can_edit of this Map.  # noqa: E501


        :return: The can_edit of this Map.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        """Sets the can_edit of this Map.


        :param can_edit: The can_edit of this Map.  # noqa: E501
        :type: bool
        """

        self._can_edit = can_edit

    @property
    def public_access(self):
        """Gets the public_access of this Map.  # noqa: E501


        :return: The public_access of this Map.  # noqa: E501
        :rtype: bool
        """
        return self._public_access

    @public_access.setter
    def public_access(self, public_access):
        """Sets the public_access of this Map.


        :param public_access: The public_access of this Map.  # noqa: E501
        :type: bool
        """

        self._public_access = public_access

    @property
    def vanity_url(self):
        """Gets the vanity_url of this Map.  # noqa: E501


        :return: The vanity_url of this Map.  # noqa: E501
        :rtype: str
        """
        return self._vanity_url

    @vanity_url.setter
    def vanity_url(self, vanity_url):
        """Sets the vanity_url of this Map.


        :param vanity_url: The vanity_url of this Map.  # noqa: E501
        :type: str
        """

        self._vanity_url = vanity_url

    @property
    def has_onboarding(self):
        """Gets the has_onboarding of this Map.  # noqa: E501


        :return: The has_onboarding of this Map.  # noqa: E501
        :rtype: bool
        """
        return self._has_onboarding

    @has_onboarding.setter
    def has_onboarding(self, has_onboarding):
        """Sets the has_onboarding of this Map.


        :param has_onboarding: The has_onboarding of this Map.  # noqa: E501
        :type: bool
        """

        self._has_onboarding = has_onboarding

    @property
    def is_locked(self):
        """Gets the is_locked of this Map.  # noqa: E501


        :return: The is_locked of this Map.  # noqa: E501
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this Map.


        :param is_locked: The is_locked of this Map.  # noqa: E501
        :type: bool
        """

        self._is_locked = is_locked

    @property
    def can_add_layers(self):
        """Gets the can_add_layers of this Map.  # noqa: E501


        :return: The can_add_layers of this Map.  # noqa: E501
        :rtype: bool
        """
        return self._can_add_layers

    @can_add_layers.setter
    def can_add_layers(self, can_add_layers):
        """Sets the can_add_layers of this Map.


        :param can_add_layers: The can_add_layers of this Map.  # noqa: E501
        :type: bool
        """

        self._can_add_layers = can_add_layers

    @property
    def has_custom_thumbnail(self):
        """Gets the has_custom_thumbnail of this Map.  # noqa: E501


        :return: The has_custom_thumbnail of this Map.  # noqa: E501
        :rtype: bool
        """
        return self._has_custom_thumbnail

    @has_custom_thumbnail.setter
    def has_custom_thumbnail(self, has_custom_thumbnail):
        """Sets the has_custom_thumbnail of this Map.


        :param has_custom_thumbnail: The has_custom_thumbnail of this Map.  # noqa: E501
        :type: bool
        """

        self._has_custom_thumbnail = has_custom_thumbnail

    @property
    def is_poi_analysis(self):
        """Gets the is_poi_analysis of this Map.  # noqa: E501


        :return: The is_poi_analysis of this Map.  # noqa: E501
        :rtype: bool
        """
        return self._is_poi_analysis

    @is_poi_analysis.setter
    def is_poi_analysis(self, is_poi_analysis):
        """Sets the is_poi_analysis of this Map.


        :param is_poi_analysis: The is_poi_analysis of this Map.  # noqa: E501
        :type: bool
        """

        self._is_poi_analysis = is_poi_analysis

    @property
    def folder_id(self):
        """Gets the folder_id of this Map.  # noqa: E501


        :return: The folder_id of this Map.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this Map.


        :param folder_id: The folder_id of this Map.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

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
        if issubclass(Map, dict):
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
        if not isinstance(other, Map):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
