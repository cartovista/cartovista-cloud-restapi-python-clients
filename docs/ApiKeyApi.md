# cartovista_cloud_clients.ApiKeyApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_create_access_key**](ApiKeyApi.md#api_key_create_access_key) | **POST** /{tenantUrlCode}/api/v2/User/{UserIdentifier}/ApiKey | Generates an access key for a specific user.
[**api_key_delete_api_key**](ApiKeyApi.md#api_key_delete_api_key) | **DELETE** /{tenantUrlCode}/api/v2/ApiKey/{id} | Deletes an API key.
[**api_key_generate_secret_key**](ApiKeyApi.md#api_key_generate_secret_key) | **POST** /{tenantUrlCode}/api/v2/ApiKey/{id}/generateSecret | Generates a secret key for additional security on the access key.
[**api_key_get_access_keys**](ApiKeyApi.md#api_key_get_access_keys) | **GET** /{tenantUrlCode}/api/v2/User/{UserIdentifier}/ApiKey | Gets all the access keys created for a specific user.
[**api_key_update_access_key**](ApiKeyApi.md#api_key_update_access_key) | **POST** /{tenantUrlCode}/api/v2/ApiKey | Updates the access key.

# **api_key_create_access_key**
> AccessKeyDTO api_key_create_access_key(body, user_identifier, tenant_url_code)

Generates an access key for a specific user.

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
api_instance = cartovista_cloud_clients.ApiKeyApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreateApiKeyParameter() # CreateApiKeyParameter | 
user_identifier = 'user_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Generates an access key for a specific user.
    api_response = api_instance.api_key_create_access_key(body, user_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeyApi->api_key_create_access_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateApiKeyParameter**](CreateApiKeyParameter.md)|  | 
 **user_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**AccessKeyDTO**](AccessKeyDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_delete_api_key**
> api_key_delete_api_key(id, tenant_url_code)

Deletes an API key.

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
api_instance = cartovista_cloud_clients.ApiKeyApi(cartovista_cloud_clients.ApiClient(configuration))
id = 'id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes an API key.
    api_instance.api_key_delete_api_key(id, tenant_url_code)
except ApiException as e:
    print("Exception when calling ApiKeyApi->api_key_delete_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_generate_secret_key**
> str api_key_generate_secret_key(id, tenant_url_code)

Generates a secret key for additional security on the access key.

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
api_instance = cartovista_cloud_clients.ApiKeyApi(cartovista_cloud_clients.ApiClient(configuration))
id = 'id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Generates a secret key for additional security on the access key.
    api_response = api_instance.api_key_generate_secret_key(id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeyApi->api_key_generate_secret_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_get_access_keys**
> list[AccessKeyDTO] api_key_get_access_keys(user_identifier, tenant_url_code)

Gets all the access keys created for a specific user.

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
api_instance = cartovista_cloud_clients.ApiKeyApi(cartovista_cloud_clients.ApiClient(configuration))
user_identifier = 'user_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the access keys created for a specific user.
    api_response = api_instance.api_key_get_access_keys(user_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeyApi->api_key_get_access_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[AccessKeyDTO]**](AccessKeyDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_update_access_key**
> api_key_update_access_key(body, tenant_url_code)

Updates the access key.

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
api_instance = cartovista_cloud_clients.ApiKeyApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.AccessKeyDTO() # AccessKeyDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the access key.
    api_instance.api_key_update_access_key(body, tenant_url_code)
except ApiException as e:
    print("Exception when calling ApiKeyApi->api_key_update_access_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessKeyDTO**](AccessKeyDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

