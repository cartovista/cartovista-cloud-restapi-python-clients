# cartovista_cloud_clients.OAuthApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_auth_authorize_redirect_uri**](OAuthApi.md#o_auth_authorize_redirect_uri) | **POST** /api/v2/oauth2/authorizeRedirectUri | 
[**o_auth_get_o_auth_client**](OAuthApi.md#o_auth_get_o_auth_client) | **GET** /api/v2/oauth2/client | 
[**o_auth_token**](OAuthApi.md#o_auth_token) | **POST** /api/v2/oauth2/token | 

# **o_auth_authorize_redirect_uri**
> str o_auth_authorize_redirect_uri(body)



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
# Configure API key authorization: bearer
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.OAuthApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.OAuthAuthorizeParams() # OAuthAuthorizeParams | 

try:
    api_response = api_instance.o_auth_authorize_redirect_uri(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->o_auth_authorize_redirect_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OAuthAuthorizeParams**](OAuthAuthorizeParams.md)|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_auth_get_o_auth_client**
> OAuthRegisteredClient o_auth_get_o_auth_client(client_id)



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
# Configure API key authorization: bearer
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.OAuthApi(cartovista_cloud_clients.ApiClient(configuration))
client_id = 'client_id_example' # str | 

try:
    api_response = api_instance.o_auth_get_o_auth_client(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->o_auth_get_o_auth_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

[**OAuthRegisteredClient**](OAuthRegisteredClient.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_auth_token**
> str o_auth_token(grant_type=grant_type, code=code, redirect_uri=redirect_uri, client_id=client_id, code_verifier=code_verifier, refresh_token=refresh_token)



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
# Configure API key authorization: bearer
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.OAuthApi(cartovista_cloud_clients.ApiClient(configuration))
grant_type = 'grant_type_example' # str |  (optional)
code = 'code_example' # str |  (optional)
redirect_uri = 'redirect_uri_example' # str |  (optional)
client_id = 'client_id_example' # str |  (optional)
code_verifier = 'code_verifier_example' # str |  (optional)
refresh_token = 'refresh_token_example' # str |  (optional)

try:
    api_response = api_instance.o_auth_token(grant_type=grant_type, code=code, redirect_uri=redirect_uri, client_id=client_id, code_verifier=code_verifier, refresh_token=refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->o_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  | [optional] 
 **code** | **str**|  | [optional] 
 **redirect_uri** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **code_verifier** | **str**|  | [optional] 
 **refresh_token** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


