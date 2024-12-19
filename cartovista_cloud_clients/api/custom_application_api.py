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


class CustomApplicationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def custom_application_get_custom_application_settings(self, map_id, url_code, tenant_url_code, **kwargs):  # noqa: E501
        """custom_application_get_custom_application_settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_application_get_custom_application_settings(map_id, url_code, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str map_id: (required)
        :param str url_code: (required)
        :param str tenant_url_code: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.custom_application_get_custom_application_settings_with_http_info(map_id, url_code, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.custom_application_get_custom_application_settings_with_http_info(map_id, url_code, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def custom_application_get_custom_application_settings_with_http_info(self, map_id, url_code, tenant_url_code, **kwargs):  # noqa: E501
        """custom_application_get_custom_application_settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_application_get_custom_application_settings_with_http_info(map_id, url_code, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str map_id: (required)
        :param str url_code: (required)
        :param str tenant_url_code: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['map_id', 'url_code', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method custom_application_get_custom_application_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `custom_application_get_custom_application_settings`")  # noqa: E501
        # verify the required parameter 'url_code' is set
        if ('url_code' not in params or
                params['url_code'] is None):
            raise ValueError("Missing the required parameter `url_code` when calling `custom_application_get_custom_application_settings`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `custom_application_get_custom_application_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['mapId'] = params['map_id']  # noqa: E501
        if 'url_code' in params:
            path_params['urlCode'] = params['url_code']  # noqa: E501
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
        auth_settings = ['apiKey', 'secretKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/map/{mapId}/custom-application/{urlCode}/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def custom_application_toggle_custom_application(self, body, map_id, url_code, tenant_url_code, **kwargs):  # noqa: E501
        """custom_application_toggle_custom_application  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_application_toggle_custom_application(body, map_id, url_code, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool body: (required)
        :param str map_id: (required)
        :param str url_code: (required)
        :param str tenant_url_code: (required)
        :return: list[CustomApplicationMapSettings]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.custom_application_toggle_custom_application_with_http_info(body, map_id, url_code, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.custom_application_toggle_custom_application_with_http_info(body, map_id, url_code, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def custom_application_toggle_custom_application_with_http_info(self, body, map_id, url_code, tenant_url_code, **kwargs):  # noqa: E501
        """custom_application_toggle_custom_application  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_application_toggle_custom_application_with_http_info(body, map_id, url_code, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool body: (required)
        :param str map_id: (required)
        :param str url_code: (required)
        :param str tenant_url_code: (required)
        :return: list[CustomApplicationMapSettings]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'map_id', 'url_code', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method custom_application_toggle_custom_application" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `custom_application_toggle_custom_application`")  # noqa: E501
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `custom_application_toggle_custom_application`")  # noqa: E501
        # verify the required parameter 'url_code' is set
        if ('url_code' not in params or
                params['url_code'] is None):
            raise ValueError("Missing the required parameter `url_code` when calling `custom_application_toggle_custom_application`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `custom_application_toggle_custom_application`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['mapId'] = params['map_id']  # noqa: E501
        if 'url_code' in params:
            path_params['urlCode'] = params['url_code']  # noqa: E501
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
        auth_settings = ['apiKey', 'secretKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/map/{mapId}/custom-application/{urlCode}/toggle', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CustomApplicationMapSettings]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def custom_application_update_custom_application_settings(self, body, map_id, url_code, tenant_url_code, **kwargs):  # noqa: E501
        """custom_application_update_custom_application_settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_application_update_custom_application_settings(body, map_id, url_code, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param str map_id: (required)
        :param str url_code: (required)
        :param str tenant_url_code: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.custom_application_update_custom_application_settings_with_http_info(body, map_id, url_code, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.custom_application_update_custom_application_settings_with_http_info(body, map_id, url_code, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def custom_application_update_custom_application_settings_with_http_info(self, body, map_id, url_code, tenant_url_code, **kwargs):  # noqa: E501
        """custom_application_update_custom_application_settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_application_update_custom_application_settings_with_http_info(body, map_id, url_code, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param str map_id: (required)
        :param str url_code: (required)
        :param str tenant_url_code: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'map_id', 'url_code', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method custom_application_update_custom_application_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `custom_application_update_custom_application_settings`")  # noqa: E501
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `custom_application_update_custom_application_settings`")  # noqa: E501
        # verify the required parameter 'url_code' is set
        if ('url_code' not in params or
                params['url_code'] is None):
            raise ValueError("Missing the required parameter `url_code` when calling `custom_application_update_custom_application_settings`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `custom_application_update_custom_application_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['mapId'] = params['map_id']  # noqa: E501
        if 'url_code' in params:
            path_params['urlCode'] = params['url_code']  # noqa: E501
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
        auth_settings = ['apiKey', 'secretKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/map/{mapId}/custom-application/{urlCode}/settings', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
