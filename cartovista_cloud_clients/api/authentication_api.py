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


class AuthenticationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def authentication_global_login(self, body, **kwargs):  # noqa: E501
        """authentication_global_login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_global_login(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginCredentialDTO body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_global_login_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_global_login_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def authentication_global_login_with_http_info(self, body, **kwargs):  # noqa: E501
        """authentication_global_login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_global_login_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginCredentialDTO body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_global_login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `authentication_global_login`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/authentication/login', 'POST',
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

    def authentication_logout(self, **kwargs):  # noqa: E501
        """authentication_logout  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_logout(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_logout_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.authentication_logout_with_http_info(**kwargs)  # noqa: E501
            return data

    def authentication_logout_with_http_info(self, **kwargs):  # noqa: E501
        """authentication_logout  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_logout_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_logout" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'secretKey']  # noqa: E501

        return self.api_client.call_api(
            '/authentication/logout', 'POST',
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

    def authentication_request_new_token(self, body, **kwargs):  # noqa: E501
        """authentication_request_new_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_request_new_token(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RefreshParam body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_request_new_token_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_request_new_token_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def authentication_request_new_token_with_http_info(self, body, **kwargs):  # noqa: E501
        """authentication_request_new_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_request_new_token_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RefreshParam body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_request_new_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `authentication_request_new_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/authentication/refresh-token', 'POST',
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

    def authentication_request_password_reset(self, body, **kwargs):  # noqa: E501
        """authentication_request_password_reset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_request_password_reset(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestResetPasswordParameter body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_request_password_reset_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_request_password_reset_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def authentication_request_password_reset_with_http_info(self, body, **kwargs):  # noqa: E501
        """authentication_request_password_reset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_request_password_reset_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestResetPasswordParameter body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_request_password_reset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `authentication_request_password_reset`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/authentication/reset-password', 'POST',
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

    def authentication_reset_password(self, body, user_id, reset_code, **kwargs):  # noqa: E501
        """authentication_reset_password  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_reset_password(body, user_id, reset_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResetPasswordWithCodeParameters body: (required)
        :param str user_id: (required)
        :param str reset_code: (required)
        :return: UserDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_reset_password_with_http_info(body, user_id, reset_code, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_reset_password_with_http_info(body, user_id, reset_code, **kwargs)  # noqa: E501
            return data

    def authentication_reset_password_with_http_info(self, body, user_id, reset_code, **kwargs):  # noqa: E501
        """authentication_reset_password  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_reset_password_with_http_info(body, user_id, reset_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResetPasswordWithCodeParameters body: (required)
        :param str user_id: (required)
        :param str reset_code: (required)
        :return: UserDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'user_id', 'reset_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_reset_password" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `authentication_reset_password`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `authentication_reset_password`")  # noqa: E501
        # verify the required parameter 'reset_code' is set
        if ('reset_code' not in params or
                params['reset_code'] is None):
            raise ValueError("Missing the required parameter `reset_code` when calling `authentication_reset_password`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501
        if 'reset_code' in params:
            path_params['resetCode'] = params['reset_code']  # noqa: E501

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
            '/authentication/reset-password/{userId}/{resetCode}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def authentication_set_external_provider(self, body, user_id, reset_code, **kwargs):  # noqa: E501
        """authentication_set_external_provider  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_set_external_provider(body, user_id, reset_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SetProviderParameter body: (required)
        :param str user_id: (required)
        :param str reset_code: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_set_external_provider_with_http_info(body, user_id, reset_code, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_set_external_provider_with_http_info(body, user_id, reset_code, **kwargs)  # noqa: E501
            return data

    def authentication_set_external_provider_with_http_info(self, body, user_id, reset_code, **kwargs):  # noqa: E501
        """authentication_set_external_provider  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_set_external_provider_with_http_info(body, user_id, reset_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SetProviderParameter body: (required)
        :param str user_id: (required)
        :param str reset_code: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'user_id', 'reset_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_set_external_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `authentication_set_external_provider`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `authentication_set_external_provider`")  # noqa: E501
        # verify the required parameter 'reset_code' is set
        if ('reset_code' not in params or
                params['reset_code'] is None):
            raise ValueError("Missing the required parameter `reset_code` when calling `authentication_set_external_provider`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501
        if 'reset_code' in params:
            path_params['resetCode'] = params['reset_code']  # noqa: E501

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
            '/authentication/provider/{userId}/{resetCode}', 'POST',
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

    def authentication_tenant_login(self, body, tenant_url_code, **kwargs):  # noqa: E501
        """authentication_tenant_login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_tenant_login(body, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginCredentialDTO body: (required)
        :param str tenant_url_code: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_tenant_login_with_http_info(body, tenant_url_code, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_tenant_login_with_http_info(body, tenant_url_code, **kwargs)  # noqa: E501
            return data

    def authentication_tenant_login_with_http_info(self, body, tenant_url_code, **kwargs):  # noqa: E501
        """authentication_tenant_login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_tenant_login_with_http_info(body, tenant_url_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginCredentialDTO body: (required)
        :param str tenant_url_code: (required)
        :return: str
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
                    " to method authentication_tenant_login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `authentication_tenant_login`")  # noqa: E501
        # verify the required parameter 'tenant_url_code' is set
        if ('tenant_url_code' not in params or
                params['tenant_url_code'] is None):
            raise ValueError("Missing the required parameter `tenant_url_code` when calling `authentication_tenant_login`")  # noqa: E501

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
        auth_settings = ['apiKey', 'secretKey']  # noqa: E501

        return self.api_client.call_api(
            '/{tenantUrlCode}/authentication/tenant-login', 'POST',
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

    def authentication_validate_reset_code(self, user_id, reset_code, **kwargs):  # noqa: E501
        """authentication_validate_reset_code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_validate_reset_code(user_id, reset_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str reset_code: (required)
        :return: UserReset
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_validate_reset_code_with_http_info(user_id, reset_code, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_validate_reset_code_with_http_info(user_id, reset_code, **kwargs)  # noqa: E501
            return data

    def authentication_validate_reset_code_with_http_info(self, user_id, reset_code, **kwargs):  # noqa: E501
        """authentication_validate_reset_code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_validate_reset_code_with_http_info(user_id, reset_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str reset_code: (required)
        :return: UserReset
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'reset_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_validate_reset_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `authentication_validate_reset_code`")  # noqa: E501
        # verify the required parameter 'reset_code' is set
        if ('reset_code' not in params or
                params['reset_code'] is None):
            raise ValueError("Missing the required parameter `reset_code` when calling `authentication_validate_reset_code`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501
        if 'reset_code' in params:
            path_params['resetCode'] = params['reset_code']  # noqa: E501

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
            '/authentication/reset-password/{userId}/{resetCode}/validate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserReset',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
