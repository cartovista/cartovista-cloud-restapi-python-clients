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


class FileApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def file_download_file(self, body, tenant_url_code, **kwargs):  # noqa: E501
        """Downloads the data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_download_file(body, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str tenant_url_code: (required)
        :return: GenericWebPortalResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.file_download_file_with_http_info(body, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.file_download_file_with_http_info(body, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def file_download_file_with_http_info(self, body, tenant_url_code, **kwargs):  # noqa: E501
        """Downloads the data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_download_file_with_http_info(body, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str tenant_url_code: (required)
        :return: GenericWebPortalResponse
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
                    " to method file_download_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `file_download_file`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `file_download_file`")  # noqa: E501

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
            '/{tenantUrlCode}/api/v2/DownloadFile/download', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GenericWebPortalResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def file_download_grid_source(self, grid_layer_id, grid_source_id, tenant_url_code, **kwargs):  # noqa: E501
        """Downloads the grid source in the given grid layer.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_download_grid_source(grid_layer_id, grid_source_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str grid_layer_id: (required)
        :param str grid_source_id: (required)
        :param str tenant_url_code: (required)
        :param bool original_file: Optional
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.file_download_grid_source_with_http_info(grid_layer_id, grid_source_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.file_download_grid_source_with_http_info(grid_layer_id, grid_source_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def file_download_grid_source_with_http_info(self, grid_layer_id, grid_source_id, tenant_url_code, **kwargs):  # noqa: E501
        """Downloads the grid source in the given grid layer.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_download_grid_source_with_http_info(grid_layer_id, grid_source_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str grid_layer_id: (required)
        :param str grid_source_id: (required)
        :param str tenant_url_code: (required)
        :param bool original_file: Optional
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['grid_layer_id', 'grid_source_id', 'tenant_url_code', 'original_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method file_download_grid_source" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'grid_layer_id' is set
        if ('grid_layer_id' not in params or
                params['grid_layer_id'] is None):
            raise ValueError("Missing the required parameter `grid_layer_id` when calling `file_download_grid_source`")  # noqa: E501
        # verify the required parameter 'grid_source_id' is set
        if ('grid_source_id' not in params or
                params['grid_source_id'] is None):
            raise ValueError("Missing the required parameter `grid_source_id` when calling `file_download_grid_source`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `file_download_grid_source`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'grid_layer_id' in params:
            path_params['gridLayerId'] = params['grid_layer_id']  # noqa: E501
        if 'grid_source_id' in params:
            path_params['gridSourceId'] = params['grid_source_id']  # noqa: E501
        if 'tenant_url_code' in params:
            path_params['tenantUrlCode'] = params['tenant_url_code']  # noqa: E501

        query_params = []
        if 'original_file' in params:
            query_params.append(('originalFile', params['original_file']))  # noqa: E501

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
            '/{tenantUrlCode}/api/v2/GridLayer/{gridLayerId}/GridSource/{gridSourceId}/download', 'GET',
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

    def file_export_feedback(self, map_id, tenant_url_code, **kwargs):  # noqa: E501
        """Exports the map's feedback in MapInfo format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_export_feedback(map_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str map_id: (required)
        :param str tenant_url_code: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.file_export_feedback_with_http_info(map_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.file_export_feedback_with_http_info(map_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def file_export_feedback_with_http_info(self, map_id, tenant_url_code, **kwargs):  # noqa: E501
        """Exports the map's feedback in MapInfo format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_export_feedback_with_http_info(map_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str map_id: (required)
        :param str tenant_url_code: (required)
        :return: str
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
                    " to method file_export_feedback" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `file_export_feedback`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `file_export_feedback`")  # noqa: E501

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
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/feedback/{mapId}', 'GET',
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

    def file_get_data(self, grid_layer_id, grid_source_id, tenant_url_code, **kwargs):  # noqa: E501
        """Gets a chunk of the grid layer's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_get_data(grid_layer_id, grid_source_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str grid_layer_id: (required)
        :param str grid_source_id: (required)
        :param str tenant_url_code: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.file_get_data_with_http_info(grid_layer_id, grid_source_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.file_get_data_with_http_info(grid_layer_id, grid_source_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def file_get_data_with_http_info(self, grid_layer_id, grid_source_id, tenant_url_code, **kwargs):  # noqa: E501
        """Gets a chunk of the grid layer's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_get_data_with_http_info(grid_layer_id, grid_source_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str grid_layer_id: (required)
        :param str grid_source_id: (required)
        :param str tenant_url_code: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['grid_layer_id', 'grid_source_id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method file_get_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'grid_layer_id' is set
        if ('grid_layer_id' not in params or
                params['grid_layer_id'] is None):
            raise ValueError("Missing the required parameter `grid_layer_id` when calling `file_get_data`")  # noqa: E501
        # verify the required parameter 'grid_source_id' is set
        if ('grid_source_id' not in params or
                params['grid_source_id'] is None):
            raise ValueError("Missing the required parameter `grid_source_id` when calling `file_get_data`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `file_get_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'grid_layer_id' in params:
            path_params['gridLayerId'] = params['grid_layer_id']  # noqa: E501
        if 'grid_source_id' in params:
            path_params['gridSourceId'] = params['grid_source_id']  # noqa: E501
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
            '/{tenantUrlCode}/api/v2/GridLayer/{gridLayerId}/GridSource/{gridSourceId}/getData', 'GET',
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

    def file_get_raster(self, identifier, bbox, width, height, tenant_url_code, **kwargs):  # noqa: E501
        """Generates a WMS raster in PNG format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_get_raster(identifier, bbox, width, height, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: (required)
        :param str bbox: (required)
        :param str width: (required)
        :param str height: (required)
        :param str tenant_url_code: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.file_get_raster_with_http_info(identifier, bbox, width, height, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.file_get_raster_with_http_info(identifier, bbox, width, height, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def file_get_raster_with_http_info(self, identifier, bbox, width, height, tenant_url_code, **kwargs):  # noqa: E501
        """Generates a WMS raster in PNG format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_get_raster_with_http_info(identifier, bbox, width, height, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: (required)
        :param str bbox: (required)
        :param str width: (required)
        :param str height: (required)
        :param str tenant_url_code: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'bbox', 'width', 'height', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method file_get_raster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `file_get_raster`")  # noqa: E501
        # verify the required parameter 'bbox' is set
        if ('bbox' not in params or
                params['bbox'] is None):
            raise ValueError("Missing the required parameter `bbox` when calling `file_get_raster`")  # noqa: E501
        # verify the required parameter 'width' is set
        if ('width' not in params or
                params['width'] is None):
            raise ValueError("Missing the required parameter `width` when calling `file_get_raster`")  # noqa: E501
        # verify the required parameter 'height' is set
        if ('height' not in params or
                params['height'] is None):
            raise ValueError("Missing the required parameter `height` when calling `file_get_raster`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `file_get_raster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'tenant_url_code' in params:
            path_params['tenantUrlCode'] = params['tenant_url_code']  # noqa: E501

        query_params = []
        if 'bbox' in params:
            query_params.append(('Bbox', params['bbox']))  # noqa: E501
        if 'width' in params:
            query_params.append(('Width', params['width']))  # noqa: E501
        if 'height' in params:
            query_params.append(('Height', params['height']))  # noqa: E501

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
            '/{tenantUrlCode}/api/v2/wms/{identifier}/raster', 'GET',
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

    def file_get_symbol_file(self, id, tenant_url_code, **kwargs):  # noqa: E501
        """Downloads the symbol's file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_get_symbol_file(id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str tenant_url_code: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.file_get_symbol_file_with_http_info(id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.file_get_symbol_file_with_http_info(id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def file_get_symbol_file_with_http_info(self, id, tenant_url_code, **kwargs):  # noqa: E501
        """Downloads the symbol's file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_get_symbol_file_with_http_info(id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str tenant_url_code: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method file_get_symbol_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `file_get_symbol_file`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `file_get_symbol_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
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
            '/{tenantUrlCode}/api/v2/symbols/{id}/file', 'GET',
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
