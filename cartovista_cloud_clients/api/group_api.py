# coding: utf-8

"""
    CartoVista REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cartovista_cloud_clients.api_client import ApiClient


class GroupApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def group_add_users_to_group(self, body, group_id_or_identifier, tenant_url_code, **kwargs):  # noqa: E501
        """Adds a collection of users to the group using their id and/or usernames.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_add_users_to_group(body, group_id_or_identifier, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: (required)
        :param str group_id_or_identifier: (required)
        :param str tenant_url_code: (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.group_add_users_to_group_with_http_info(body, group_id_or_identifier, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.group_add_users_to_group_with_http_info(body, group_id_or_identifier, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def group_add_users_to_group_with_http_info(self, body, group_id_or_identifier, tenant_url_code, **kwargs):  # noqa: E501
        """Adds a collection of users to the group using their id and/or usernames.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_add_users_to_group_with_http_info(body, group_id_or_identifier, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: (required)
        :param str group_id_or_identifier: (required)
        :param str tenant_url_code: (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'group_id_or_identifier', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_add_users_to_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `group_add_users_to_group`")  # noqa: E501
        # verify the required parameter 'group_id_or_identifier' is set
        if ('group_id_or_identifier' not in params or
                params['group_id_or_identifier'] is None):
            raise ValueError("Missing the required parameter `group_id_or_identifier` when calling `group_add_users_to_group`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `group_add_users_to_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id_or_identifier' in params:
            path_params['groupIdOrIdentifier'] = params['group_id_or_identifier']  # noqa: E501
        if 'tenant_url_code' in params:
            path_params['tenantUrlCode'] = params['tenant_url_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/Groups/{groupIdOrIdentifier}/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Group',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def group_create_group(self, body, tenant_url_code, **kwargs):  # noqa: E501
        """Creates a group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_create_group(body, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateGroupParameter body: (required)
        :param str tenant_url_code: (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.group_create_group_with_http_info(body, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.group_create_group_with_http_info(body, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def group_create_group_with_http_info(self, body, tenant_url_code, **kwargs):  # noqa: E501
        """Creates a group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_create_group_with_http_info(body, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateGroupParameter body: (required)
        :param str tenant_url_code: (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_create_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `group_create_group`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `group_create_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_url_code' in params:
            path_params['tenantUrlCode'] = params['tenant_url_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/Groups/Groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Group',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def group_delete_group(self, group_id_or_identifier, tenant_url_code, **kwargs):  # noqa: E501
        """Deletes a specific group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_delete_group(group_id_or_identifier, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id_or_identifier: (required)
        :param str tenant_url_code: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.group_delete_group_with_http_info(group_id_or_identifier, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.group_delete_group_with_http_info(group_id_or_identifier, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def group_delete_group_with_http_info(self, group_id_or_identifier, tenant_url_code, **kwargs):  # noqa: E501
        """Deletes a specific group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_delete_group_with_http_info(group_id_or_identifier, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id_or_identifier: (required)
        :param str tenant_url_code: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id_or_identifier', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_delete_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id_or_identifier' is set
        if ('group_id_or_identifier' not in params or
                params['group_id_or_identifier'] is None):
            raise ValueError("Missing the required parameter `group_id_or_identifier` when calling `group_delete_group`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `group_delete_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id_or_identifier' in params:
            path_params['groupIdOrIdentifier'] = params['group_id_or_identifier']  # noqa: E501
        if 'tenant_url_code' in params:
            path_params['tenantUrlCode'] = params['tenant_url_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/Groups/{groupIdOrIdentifier}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def group_get_group(self, group_id_or_identifier, tenant_url_code, **kwargs):  # noqa: E501
        """Gets a specific group by id or identifier.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_get_group(group_id_or_identifier, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id_or_identifier: (required)
        :param str tenant_url_code: (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.group_get_group_with_http_info(group_id_or_identifier, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.group_get_group_with_http_info(group_id_or_identifier, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def group_get_group_with_http_info(self, group_id_or_identifier, tenant_url_code, **kwargs):  # noqa: E501
        """Gets a specific group by id or identifier.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_get_group_with_http_info(group_id_or_identifier, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id_or_identifier: (required)
        :param str tenant_url_code: (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id_or_identifier', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_get_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id_or_identifier' is set
        if ('group_id_or_identifier' not in params or
                params['group_id_or_identifier'] is None):
            raise ValueError("Missing the required parameter `group_id_or_identifier` when calling `group_get_group`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `group_get_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id_or_identifier' in params:
            path_params['groupIdOrIdentifier'] = params['group_id_or_identifier']  # noqa: E501
        if 'tenant_url_code' in params:
            path_params['tenantUrlCode'] = params['tenant_url_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/Groups/{groupIdOrIdentifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Group',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def group_get_groups(self, tenant_url_code, **kwargs):  # noqa: E501
        """Gets all the groups.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_get_groups(tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_url_code: (required)
        :return: list[Group]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.group_get_groups_with_http_info(tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.group_get_groups_with_http_info(tenant_url_code, **kwargs)  # noqa: E501
            return data

    def group_get_groups_with_http_info(self, tenant_url_code, **kwargs):  # noqa: E501
        """Gets all the groups.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_get_groups_with_http_info(tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_url_code: (required)
        :return: list[Group]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_get_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `group_get_groups`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_url_code' in params:
            path_params['tenantUrlCode'] = params['tenant_url_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/Groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Group]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def group_remove_users_from_group(self, body, group_id_or_identifier, tenant_url_code, **kwargs):  # noqa: E501
        """Removes a collection of users to the group using their id and/or usernames.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_remove_users_from_group(body, group_id_or_identifier, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: (required)
        :param str group_id_or_identifier: (required)
        :param str tenant_url_code: (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.group_remove_users_from_group_with_http_info(body, group_id_or_identifier, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.group_remove_users_from_group_with_http_info(body, group_id_or_identifier, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def group_remove_users_from_group_with_http_info(self, body, group_id_or_identifier, tenant_url_code, **kwargs):  # noqa: E501
        """Removes a collection of users to the group using their id and/or usernames.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_remove_users_from_group_with_http_info(body, group_id_or_identifier, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: (required)
        :param str group_id_or_identifier: (required)
        :param str tenant_url_code: (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'group_id_or_identifier', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_remove_users_from_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `group_remove_users_from_group`")  # noqa: E501
        # verify the required parameter 'group_id_or_identifier' is set
        if ('group_id_or_identifier' not in params or
                params['group_id_or_identifier'] is None):
            raise ValueError("Missing the required parameter `group_id_or_identifier` when calling `group_remove_users_from_group`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `group_remove_users_from_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id_or_identifier' in params:
            path_params['groupIdOrIdentifier'] = params['group_id_or_identifier']  # noqa: E501
        if 'tenant_url_code' in params:
            path_params['tenantUrlCode'] = params['tenant_url_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/Groups/{groupIdOrIdentifier}/users', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Group',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def group_update_group(self, body, group_id_or_identifier, tenant_url_code, **kwargs):  # noqa: E501
        """Updates a group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_update_group(body, group_id_or_identifier, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateGroupParameter body: (required)
        :param str group_id_or_identifier: (required)
        :param str tenant_url_code: (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.group_update_group_with_http_info(body, group_id_or_identifier, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.group_update_group_with_http_info(body, group_id_or_identifier, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def group_update_group_with_http_info(self, body, group_id_or_identifier, tenant_url_code, **kwargs):  # noqa: E501
        """Updates a group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_update_group_with_http_info(body, group_id_or_identifier, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateGroupParameter body: (required)
        :param str group_id_or_identifier: (required)
        :param str tenant_url_code: (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'group_id_or_identifier', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_update_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `group_update_group`")  # noqa: E501
        # verify the required parameter 'group_id_or_identifier' is set
        if ('group_id_or_identifier' not in params or
                params['group_id_or_identifier'] is None):
            raise ValueError("Missing the required parameter `group_id_or_identifier` when calling `group_update_group`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `group_update_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id_or_identifier' in params:
            path_params['groupIdOrIdentifier'] = params['group_id_or_identifier']  # noqa: E501
        if 'tenant_url_code' in params:
            path_params['tenantUrlCode'] = params['tenant_url_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/Groups/{groupIdOrIdentifier}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Group',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)