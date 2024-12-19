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


class PoiAnalysisApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def poi_analysis_create_custom_poi_analysis(self, body, map_id, tenant_url_code, **kwargs):  # noqa: E501
        """Creates a new custom analysis.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_create_custom_poi_analysis(body, map_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateCustomPoiAnalysisParameter body: (required)
        :param str map_id: (required)
        :param str tenant_url_code: (required)
        :return: CustomPoiAnalysisWithNewId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.poi_analysis_create_custom_poi_analysis_with_http_info(body, map_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.poi_analysis_create_custom_poi_analysis_with_http_info(body, map_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def poi_analysis_create_custom_poi_analysis_with_http_info(self, body, map_id, tenant_url_code, **kwargs):  # noqa: E501
        """Creates a new custom analysis.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_create_custom_poi_analysis_with_http_info(body, map_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateCustomPoiAnalysisParameter body: (required)
        :param str map_id: (required)
        :param str tenant_url_code: (required)
        :return: CustomPoiAnalysisWithNewId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'map_id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method poi_analysis_create_custom_poi_analysis" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `poi_analysis_create_custom_poi_analysis`")  # noqa: E501
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `poi_analysis_create_custom_poi_analysis`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `poi_analysis_create_custom_poi_analysis`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['mapId'] = params['map_id']  # noqa: E501
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
            '/{tenantUrlCode}/api/v2/poi-analysis/{mapId}/analysis', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomPoiAnalysisWithNewId',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def poi_analysis_create_poi_analysis(self, body, map_id, tenant_url_code, **kwargs):  # noqa: E501
        """Creates a POI analysis for the map.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_create_poi_analysis(body, map_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePoiAnalysisParameter body: (required)
        :param str map_id: (required)
        :param str tenant_url_code: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.poi_analysis_create_poi_analysis_with_http_info(body, map_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.poi_analysis_create_poi_analysis_with_http_info(body, map_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def poi_analysis_create_poi_analysis_with_http_info(self, body, map_id, tenant_url_code, **kwargs):  # noqa: E501
        """Creates a POI analysis for the map.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_create_poi_analysis_with_http_info(body, map_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePoiAnalysisParameter body: (required)
        :param str map_id: (required)
        :param str tenant_url_code: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'map_id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method poi_analysis_create_poi_analysis" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `poi_analysis_create_poi_analysis`")  # noqa: E501
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `poi_analysis_create_poi_analysis`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `poi_analysis_create_poi_analysis`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['mapId'] = params['map_id']  # noqa: E501
        if 'tenant_url_code' in params:
            path_params['tenantUrlCode'] = params['tenant_url_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'secretKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/poi-analysis/{mapId}', 'POST',
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

    def poi_analysis_delete_custom_poi_analysis(self, map_id, analysis_id, tenant_url_code, **kwargs):  # noqa: E501
        """Deletes a custom analysis.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_delete_custom_poi_analysis(map_id, analysis_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str map_id: (required)
        :param str analysis_id: (required)
        :param str tenant_url_code: (required)
        :return: list[CustomPoiAnalysis]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.poi_analysis_delete_custom_poi_analysis_with_http_info(map_id, analysis_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.poi_analysis_delete_custom_poi_analysis_with_http_info(map_id, analysis_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def poi_analysis_delete_custom_poi_analysis_with_http_info(self, map_id, analysis_id, tenant_url_code, **kwargs):  # noqa: E501
        """Deletes a custom analysis.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_delete_custom_poi_analysis_with_http_info(map_id, analysis_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str map_id: (required)
        :param str analysis_id: (required)
        :param str tenant_url_code: (required)
        :return: list[CustomPoiAnalysis]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['map_id', 'analysis_id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method poi_analysis_delete_custom_poi_analysis" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `poi_analysis_delete_custom_poi_analysis`")  # noqa: E501
        # verify the required parameter 'analysis_id' is set
        if ('analysis_id' not in params or
                params['analysis_id'] is None):
            raise ValueError("Missing the required parameter `analysis_id` when calling `poi_analysis_delete_custom_poi_analysis`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `poi_analysis_delete_custom_poi_analysis`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['mapId'] = params['map_id']  # noqa: E501
        if 'analysis_id' in params:
            path_params['analysisId'] = params['analysis_id']  # noqa: E501
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
            '/{tenantUrlCode}/api/v2/poi-analysis/{mapId}/analysis/{analysisId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CustomPoiAnalysis]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def poi_analysis_get_poi_analysis(self, map_id, tenant_url_code, **kwargs):  # noqa: E501
        """Gets the POI analysis used by the map.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_get_poi_analysis(map_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str map_id: (required)
        :param str tenant_url_code: (required)
        :return: PoiAnalysis
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.poi_analysis_get_poi_analysis_with_http_info(map_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.poi_analysis_get_poi_analysis_with_http_info(map_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def poi_analysis_get_poi_analysis_with_http_info(self, map_id, tenant_url_code, **kwargs):  # noqa: E501
        """Gets the POI analysis used by the map.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_get_poi_analysis_with_http_info(map_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str map_id: (required)
        :param str tenant_url_code: (required)
        :return: PoiAnalysis
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['map_id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method poi_analysis_get_poi_analysis" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `poi_analysis_get_poi_analysis`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `poi_analysis_get_poi_analysis`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['mapId'] = params['map_id']  # noqa: E501
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
            '/{tenantUrlCode}/api/v2/poi-analysis/{mapId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PoiAnalysis',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def poi_analysis_get_poi_analysis_data(self, map_id, analysis_id, tenant_url_code, **kwargs):  # noqa: E501
        """Gets the data computed for the custom analysis.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_get_poi_analysis_data(map_id, analysis_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str map_id: (required)
        :param str analysis_id: (required)
        :param str tenant_url_code: (required)
        :return: list[PoiAnalysisData]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.poi_analysis_get_poi_analysis_data_with_http_info(map_id, analysis_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.poi_analysis_get_poi_analysis_data_with_http_info(map_id, analysis_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def poi_analysis_get_poi_analysis_data_with_http_info(self, map_id, analysis_id, tenant_url_code, **kwargs):  # noqa: E501
        """Gets the data computed for the custom analysis.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_get_poi_analysis_data_with_http_info(map_id, analysis_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str map_id: (required)
        :param str analysis_id: (required)
        :param str tenant_url_code: (required)
        :return: list[PoiAnalysisData]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['map_id', 'analysis_id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method poi_analysis_get_poi_analysis_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `poi_analysis_get_poi_analysis_data`")  # noqa: E501
        # verify the required parameter 'analysis_id' is set
        if ('analysis_id' not in params or
                params['analysis_id'] is None):
            raise ValueError("Missing the required parameter `analysis_id` when calling `poi_analysis_get_poi_analysis_data`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `poi_analysis_get_poi_analysis_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['mapId'] = params['map_id']  # noqa: E501
        if 'analysis_id' in params:
            path_params['analysisId'] = params['analysis_id']  # noqa: E501
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
            '/{tenantUrlCode}/api/v2/poi-analysis/{mapId}/analysis/{analysisId}/data', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PoiAnalysisData]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def poi_analysis_get_poi_analysis_settings(self, tenant_url_code, **kwargs):  # noqa: E501
        """Gets the usable options to create a new POI analysis.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_get_poi_analysis_settings(tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_url_code: (required)
        :return: PoiAnalysisSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.poi_analysis_get_poi_analysis_settings_with_http_info(tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.poi_analysis_get_poi_analysis_settings_with_http_info(tenant_url_code, **kwargs)  # noqa: E501
            return data

    def poi_analysis_get_poi_analysis_settings_with_http_info(self, tenant_url_code, **kwargs):  # noqa: E501
        """Gets the usable options to create a new POI analysis.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_get_poi_analysis_settings_with_http_info(tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_url_code: (required)
        :return: PoiAnalysisSettings
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
                    " to method poi_analysis_get_poi_analysis_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `poi_analysis_get_poi_analysis_settings`")  # noqa: E501

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
        auth_settings = ['apiKey', 'secretKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/poi-analysis/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PoiAnalysisSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def poi_analysis_pregenerate_rasters(self, map_id, tenant_url_code, **kwargs):  # noqa: E501
        """Generates all the missing raster for each scenario, year and kV level.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_pregenerate_rasters(map_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str map_id: (required)
        :param str tenant_url_code: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.poi_analysis_pregenerate_rasters_with_http_info(map_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.poi_analysis_pregenerate_rasters_with_http_info(map_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def poi_analysis_pregenerate_rasters_with_http_info(self, map_id, tenant_url_code, **kwargs):  # noqa: E501
        """Generates all the missing raster for each scenario, year and kV level.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_pregenerate_rasters_with_http_info(map_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str map_id: (required)
        :param str tenant_url_code: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['map_id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method poi_analysis_pregenerate_rasters" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `poi_analysis_pregenerate_rasters`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `poi_analysis_pregenerate_rasters`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['mapId'] = params['map_id']  # noqa: E501
        if 'tenant_url_code' in params:
            path_params['tenantUrlCode'] = params['tenant_url_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey', 'secretKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/poi-analysis/{mapId}/pregenerate', 'GET',
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

    def poi_analysis_toggle_default_analysis(self, body, map_id, analysis_id, tenant_url_code, **kwargs):  # noqa: E501
        """Toggles the default value of the custom analysis.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_toggle_default_analysis(body, map_id, analysis_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool body: (required)
        :param str map_id: (required)
        :param str analysis_id: (required)
        :param str tenant_url_code: (required)
        :return: list[CustomPoiAnalysis]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.poi_analysis_toggle_default_analysis_with_http_info(body, map_id, analysis_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.poi_analysis_toggle_default_analysis_with_http_info(body, map_id, analysis_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def poi_analysis_toggle_default_analysis_with_http_info(self, body, map_id, analysis_id, tenant_url_code, **kwargs):  # noqa: E501
        """Toggles the default value of the custom analysis.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_analysis_toggle_default_analysis_with_http_info(body, map_id, analysis_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool body: (required)
        :param str map_id: (required)
        :param str analysis_id: (required)
        :param str tenant_url_code: (required)
        :return: list[CustomPoiAnalysis]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'map_id', 'analysis_id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method poi_analysis_toggle_default_analysis" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `poi_analysis_toggle_default_analysis`")  # noqa: E501
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `poi_analysis_toggle_default_analysis`")  # noqa: E501
        # verify the required parameter 'analysis_id' is set
        if ('analysis_id' not in params or
                params['analysis_id'] is None):
            raise ValueError("Missing the required parameter `analysis_id` when calling `poi_analysis_toggle_default_analysis`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `poi_analysis_toggle_default_analysis`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['mapId'] = params['map_id']  # noqa: E501
        if 'analysis_id' in params:
            path_params['analysisId'] = params['analysis_id']  # noqa: E501
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
            '/{tenantUrlCode}/api/v2/poi-analysis/{mapId}/analysis/{analysisId}/default', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CustomPoiAnalysis]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
