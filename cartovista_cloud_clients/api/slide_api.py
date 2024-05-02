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


class SlideApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def slide_delete_slide(self, slide_id, tenant_url_code, **kwargs):  # noqa: E501
        """Deletes the slide.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_delete_slide(slide_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slide_id: (required)
        :param str tenant_url_code: (required)
        :return: list[Slide]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slide_delete_slide_with_http_info(slide_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.slide_delete_slide_with_http_info(slide_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def slide_delete_slide_with_http_info(self, slide_id, tenant_url_code, **kwargs):  # noqa: E501
        """Deletes the slide.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_delete_slide_with_http_info(slide_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slide_id: (required)
        :param str tenant_url_code: (required)
        :return: list[Slide]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slide_id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method slide_delete_slide" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slide_id' is set
        if ('slide_id' not in params or
                params['slide_id'] is None):
            raise ValueError("Missing the required parameter `slide_id` when calling `slide_delete_slide`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `slide_delete_slide`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slide_id' in params:
            path_params['slideId'] = params['slide_id']  # noqa: E501
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
            '/{tenantUrlCode}/api/v2/slides/{slideId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Slide]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def slide_delete_slide_analysis(self, slide_id, analysis_id, tenant_url_code, **kwargs):  # noqa: E501
        """Deletes the analysis from the slide.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_delete_slide_analysis(slide_id, analysis_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slide_id: (required)
        :param str analysis_id: (required)
        :param str tenant_url_code: (required)
        :return: Slide
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slide_delete_slide_analysis_with_http_info(slide_id, analysis_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.slide_delete_slide_analysis_with_http_info(slide_id, analysis_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def slide_delete_slide_analysis_with_http_info(self, slide_id, analysis_id, tenant_url_code, **kwargs):  # noqa: E501
        """Deletes the analysis from the slide.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_delete_slide_analysis_with_http_info(slide_id, analysis_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slide_id: (required)
        :param str analysis_id: (required)
        :param str tenant_url_code: (required)
        :return: Slide
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slide_id', 'analysis_id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method slide_delete_slide_analysis" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slide_id' is set
        if ('slide_id' not in params or
                params['slide_id'] is None):
            raise ValueError("Missing the required parameter `slide_id` when calling `slide_delete_slide_analysis`")  # noqa: E501
        # verify the required parameter 'analysis_id' is set
        if ('analysis_id' not in params or
                params['analysis_id'] is None):
            raise ValueError("Missing the required parameter `analysis_id` when calling `slide_delete_slide_analysis`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `slide_delete_slide_analysis`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slide_id' in params:
            path_params['slideId'] = params['slide_id']  # noqa: E501
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
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/slides/{slideId}/analysis/{analysisId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Slide',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def slide_get_slide(self, slide_id, tenant_url_code, **kwargs):  # noqa: E501
        """Gets a specific slide.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_get_slide(slide_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slide_id: (required)
        :param str tenant_url_code: (required)
        :return: Slide
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slide_get_slide_with_http_info(slide_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.slide_get_slide_with_http_info(slide_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def slide_get_slide_with_http_info(self, slide_id, tenant_url_code, **kwargs):  # noqa: E501
        """Gets a specific slide.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_get_slide_with_http_info(slide_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slide_id: (required)
        :param str tenant_url_code: (required)
        :return: Slide
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slide_id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method slide_get_slide" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slide_id' is set
        if ('slide_id' not in params or
                params['slide_id'] is None):
            raise ValueError("Missing the required parameter `slide_id` when calling `slide_get_slide`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `slide_get_slide`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slide_id' in params:
            path_params['slideId'] = params['slide_id']  # noqa: E501
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
            '/{tenantUrlCode}/api/v2/slides/{slideId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Slide',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def slide_reorder_slides(self, body, map_id, tenant_url_code, **kwargs):  # noqa: E501
        """Changes the order of a slide in the slide details view. The order will be the same in the slide ids list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_reorder_slides(body, map_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: (required)
        :param str map_id: (required)
        :param str tenant_url_code: (required)
        :return: list[Slide]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slide_reorder_slides_with_http_info(body, map_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.slide_reorder_slides_with_http_info(body, map_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def slide_reorder_slides_with_http_info(self, body, map_id, tenant_url_code, **kwargs):  # noqa: E501
        """Changes the order of a slide in the slide details view. The order will be the same in the slide ids list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_reorder_slides_with_http_info(body, map_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: (required)
        :param str map_id: (required)
        :param str tenant_url_code: (required)
        :return: list[Slide]
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
                    " to method slide_reorder_slides" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `slide_reorder_slides`")  # noqa: E501
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `slide_reorder_slides`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `slide_reorder_slides`")  # noqa: E501

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
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/slides/{mapId}/reorderSlides', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Slide]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def slide_update_default_slide_thumbnail(self, body, map_id, tenant_url_code, **kwargs):  # noqa: E501
        """Updates the map's default slide's thumbnail.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_update_default_slide_thumbnail(body, map_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str map_id: (required)
        :param str tenant_url_code: (required)
        :return: DefaultSlideThumbnailUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slide_update_default_slide_thumbnail_with_http_info(body, map_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.slide_update_default_slide_thumbnail_with_http_info(body, map_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def slide_update_default_slide_thumbnail_with_http_info(self, body, map_id, tenant_url_code, **kwargs):  # noqa: E501
        """Updates the map's default slide's thumbnail.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_update_default_slide_thumbnail_with_http_info(body, map_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str map_id: (required)
        :param str tenant_url_code: (required)
        :return: DefaultSlideThumbnailUpdateResponse
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
                    " to method slide_update_default_slide_thumbnail" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `slide_update_default_slide_thumbnail`")  # noqa: E501
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `slide_update_default_slide_thumbnail`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `slide_update_default_slide_thumbnail`")  # noqa: E501

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
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/api/v2/maps/{mapId}/default-slide-thumbnail', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DefaultSlideThumbnailUpdateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def slide_update_slide(self, body, slide_id, tenant_url_code, **kwargs):  # noqa: E501
        """Updates the slide.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_update_slide(body, slide_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SlideCreateUpdate body: (required)
        :param str slide_id: (required)
        :param str tenant_url_code: (required)
        :return: Slide
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slide_update_slide_with_http_info(body, slide_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.slide_update_slide_with_http_info(body, slide_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def slide_update_slide_with_http_info(self, body, slide_id, tenant_url_code, **kwargs):  # noqa: E501
        """Updates the slide.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_update_slide_with_http_info(body, slide_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SlideCreateUpdate body: (required)
        :param str slide_id: (required)
        :param str tenant_url_code: (required)
        :return: Slide
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'slide_id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method slide_update_slide" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `slide_update_slide`")  # noqa: E501
        # verify the required parameter 'slide_id' is set
        if ('slide_id' not in params or
                params['slide_id'] is None):
            raise ValueError("Missing the required parameter `slide_id` when calling `slide_update_slide`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `slide_update_slide`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slide_id' in params:
            path_params['slideId'] = params['slide_id']  # noqa: E501
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
            '/{tenantUrlCode}/api/v2/slides/{slideId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Slide',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def slide_update_slide_extent_from_layers(self, body, slide_id, tenant_url_code, **kwargs):  # noqa: E501
        """Updates the slide's extent by combining the layers' extents.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_update_slide_extent_from_layers(body, slide_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: (required)
        :param str slide_id: (required)
        :param str tenant_url_code: (required)
        :return: Slide
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slide_update_slide_extent_from_layers_with_http_info(body, slide_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.slide_update_slide_extent_from_layers_with_http_info(body, slide_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def slide_update_slide_extent_from_layers_with_http_info(self, body, slide_id, tenant_url_code, **kwargs):  # noqa: E501
        """Updates the slide's extent by combining the layers' extents.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_update_slide_extent_from_layers_with_http_info(body, slide_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: (required)
        :param str slide_id: (required)
        :param str tenant_url_code: (required)
        :return: Slide
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'slide_id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method slide_update_slide_extent_from_layers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `slide_update_slide_extent_from_layers`")  # noqa: E501
        # verify the required parameter 'slide_id' is set
        if ('slide_id' not in params or
                params['slide_id'] is None):
            raise ValueError("Missing the required parameter `slide_id` when calling `slide_update_slide_extent_from_layers`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `slide_update_slide_extent_from_layers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slide_id' in params:
            path_params['slideId'] = params['slide_id']  # noqa: E501
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
            '/{tenantUrlCode}/api/v2/slides/{slideId}/extent-from-layers', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Slide',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def slide_update_slide_theme_set(self, body, slide_id, tenant_url_code, **kwargs):  # noqa: E501
        """Updates the slide's theme set.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_update_slide_theme_set(body, slide_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str slide_id: (required)
        :param str tenant_url_code: (required)
        :return: Slide
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slide_update_slide_theme_set_with_http_info(body, slide_id, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.slide_update_slide_theme_set_with_http_info(body, slide_id, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def slide_update_slide_theme_set_with_http_info(self, body, slide_id, tenant_url_code, **kwargs):  # noqa: E501
        """Updates the slide's theme set.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slide_update_slide_theme_set_with_http_info(body, slide_id, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str slide_id: (required)
        :param str tenant_url_code: (required)
        :return: Slide
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'slide_id', 'tenant_url_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method slide_update_slide_theme_set" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `slide_update_slide_theme_set`")  # noqa: E501
        # verify the required parameter 'slide_id' is set
        if ('slide_id' not in params or
                params['slide_id'] is None):
            raise ValueError("Missing the required parameter `slide_id` when calling `slide_update_slide_theme_set`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `slide_update_slide_theme_set`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slide_id' in params:
            path_params['slideId'] = params['slide_id']  # noqa: E501
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
            '/{tenantUrlCode}/api/v2/slides/{slideId}/themeset', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Slide',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)