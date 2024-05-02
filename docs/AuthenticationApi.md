# cartovista_cloud_clients.AuthenticationApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_global_login**](AuthenticationApi.md#authentication_global_login) | **POST** /authentication/login | 
[**authentication_logout**](AuthenticationApi.md#authentication_logout) | **POST** /authentication/logout | 
[**authentication_request_new_token**](AuthenticationApi.md#authentication_request_new_token) | **POST** /authentication/refresh-token | 
[**authentication_request_password_reset**](AuthenticationApi.md#authentication_request_password_reset) | **POST** /authentication/reset-password | 
[**authentication_reset_password**](AuthenticationApi.md#authentication_reset_password) | **POST** /authentication/reset-password/{userId}/{resetCode} | 
[**authentication_set_external_provider**](AuthenticationApi.md#authentication_set_external_provider) | **POST** /authentication/provider/{userId}/{resetCode} | 
[**authentication_tenant_login**](AuthenticationApi.md#authentication_tenant_login) | **POST** /{tenantUrlCode}/authentication/tenant-login | 
[**authentication_validate_reset_code**](AuthenticationApi.md#authentication_validate_reset_code) | **GET** /authentication/reset-password/{userId}/{resetCode}/validate | 

# **authentication_global_login**
> str authentication_global_login(body)



### Example
```python
from __future__ import print_function
import time
import cartovista_cloud_clients
from cartovista_cloud_clients.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.AuthenticationApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.LoginCredentialDTO() # LoginCredentialDTO | 

try:
    api_response = api_instance.authentication_global_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_global_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginCredentialDTO**](LoginCredentialDTO.md)|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_logout**
> str authentication_logout()



### Example
```python
from __future__ import print_function
import time
import cartovista_cloud_clients
from cartovista_cloud_clients.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.AuthenticationApi(cartovista_cloud_clients.ApiClient(configuration))

try:
    api_response = api_instance.authentication_logout()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_request_new_token**
> str authentication_request_new_token(body)



### Example
```python
from __future__ import print_function
import time
import cartovista_cloud_clients
from cartovista_cloud_clients.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.AuthenticationApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.RefreshParam() # RefreshParam | 

try:
    api_response = api_instance.authentication_request_new_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_request_new_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RefreshParam**](RefreshParam.md)|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_request_password_reset**
> authentication_request_password_reset(body)



### Example
```python
from __future__ import print_function
import time
import cartovista_cloud_clients
from cartovista_cloud_clients.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.AuthenticationApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.RequestResetPasswordParameter() # RequestResetPasswordParameter | 

try:
    api_instance.authentication_request_password_reset(body)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_request_password_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestResetPasswordParameter**](RequestResetPasswordParameter.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_reset_password**
> InlineResponse200 authentication_reset_password(body, user_id, reset_code)



### Example
```python
from __future__ import print_function
import time
import cartovista_cloud_clients
from cartovista_cloud_clients.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.AuthenticationApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ResetPasswordWithCodeParameters() # ResetPasswordWithCodeParameters | 
user_id = 'user_id_example' # str | 
reset_code = 'reset_code_example' # str | 

try:
    api_response = api_instance.authentication_reset_password(body, user_id, reset_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetPasswordWithCodeParameters**](ResetPasswordWithCodeParameters.md)|  | 
 **user_id** | **str**|  | 
 **reset_code** | **str**|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_set_external_provider**
> authentication_set_external_provider(body, user_id, reset_code)



### Example
```python
from __future__ import print_function
import time
import cartovista_cloud_clients
from cartovista_cloud_clients.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.AuthenticationApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.SetProviderParameter() # SetProviderParameter | 
user_id = 'user_id_example' # str | 
reset_code = 'reset_code_example' # str | 

try:
    api_instance.authentication_set_external_provider(body, user_id, reset_code)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_set_external_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetProviderParameter**](SetProviderParameter.md)|  | 
 **user_id** | **str**|  | 
 **reset_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_tenant_login**
> str authentication_tenant_login(body, tenant_url_code)



### Example
```python
from __future__ import print_function
import time
import cartovista_cloud_clients
from cartovista_cloud_clients.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.AuthenticationApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.LoginCredentialDTO() # LoginCredentialDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.authentication_tenant_login(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_tenant_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginCredentialDTO**](LoginCredentialDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_validate_reset_code**
> UserReset authentication_validate_reset_code(user_id, reset_code)



### Example
```python
from __future__ import print_function
import time
import cartovista_cloud_clients
from cartovista_cloud_clients.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.AuthenticationApi(cartovista_cloud_clients.ApiClient(configuration))
user_id = 'user_id_example' # str | 
reset_code = 'reset_code_example' # str | 

try:
    api_response = api_instance.authentication_validate_reset_code(user_id, reset_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_validate_reset_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **reset_code** | **str**|  | 

### Return type

[**UserReset**](UserReset.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

