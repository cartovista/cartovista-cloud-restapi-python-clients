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


class StyleThemeServicesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def style_theme_services_get_style_sheet_viewer(self, tenant_url_code, **kwargs):  # noqa: E501
        """style_theme_services_get_style_sheet_viewer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.style_theme_services_get_style_sheet_viewer(tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_url_code: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.style_theme_services_get_style_sheet_viewer_with_http_info(tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.style_theme_services_get_style_sheet_viewer_with_http_info(tenant_url_code, **kwargs)  # noqa: E501
            return data

    def style_theme_services_get_style_sheet_viewer_with_http_info(self, tenant_url_code, **kwargs):  # noqa: E501
        """style_theme_services_get_style_sheet_viewer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.style_theme_services_get_style_sheet_viewer_with_http_info(tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_url_code: (required)
        :return: str
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
                    " to method style_theme_services_get_style_sheet_viewer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `style_theme_services_get_style_sheet_viewer`")  # noqa: E501

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
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/StyleThemeServices/GetStyleSheetViewer', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def style_theme_services_get_style_sheet_viewer2(self, tenant_url_code, **kwargs):  # noqa: E501
        """style_theme_services_get_style_sheet_viewer2  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.style_theme_services_get_style_sheet_viewer2(tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_url_code: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.style_theme_services_get_style_sheet_viewer2_with_http_info(tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.style_theme_services_get_style_sheet_viewer2_with_http_info(tenant_url_code, **kwargs)  # noqa: E501
            return data

    def style_theme_services_get_style_sheet_viewer2_with_http_info(self, tenant_url_code, **kwargs):  # noqa: E501
        """style_theme_services_get_style_sheet_viewer2  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.style_theme_services_get_style_sheet_viewer2_with_http_info(tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_url_code: (required)
        :return: str
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
                    " to method style_theme_services_get_style_sheet_viewer2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `style_theme_services_get_style_sheet_viewer2`")  # noqa: E501

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
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/WebPortalServices/StyleThemeServices/GetStyleSheetViewer', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)