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

This request requires the identifier of the user to which the API key will be linked.   * The identifier can be retrieved with the GET request `/{tenantUrlCode}/api/v2/users`, which returns all users in the tenant. The relevant field is `securityIdentifier`.    The request also requires a list of IP addresses to be whitelisted for the API key.    Optional notes can be added to describe the purpose of the API key.    For example, the request `/tenantName/api/v2/User/00000000-0000-0000-0000-000000000001/ApiKey` with the following body:   ```json {  \"ipWhitelisting\": [   \"X.X.X.X\"  ],  \"notes\": \"Example API\" } ``` will create an API key for the user 00000000-0000-0000-0000-000000000001, valid only for requests originating from the IP address X.X.X.X.

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

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

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

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_generate_secret_key**
> str api_key_generate_secret_key(id, tenant_url_code)

Generates a secret key for additional security on the access key.

Once a secret key is generated for an API key, it cannot be removed.   If an API key has both an IP whitelist and a secret key, requests must satisfy both conditions.   To use only the secret key, the IP whitelist can be cleared by sending a request to `/{tenantUrlCode}/api/v2/ApiKey` with `\"ipWhitelisting\": []` in the body.

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

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

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

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_update_access_key**
> api_key_update_access_key(body, tenant_url_code)

Updates the access key.

Updating an access key requires its identifier as well as the properties to be modified. These are provided in the request body. The available fields are:    - **accessKey** (required): The identifier of the access key to update.     The identifier can be retrieved from `/{tenantUrlCode}/api/v2/User/{UserIdentifier}/ApiKey`, where `{UserIdentifier}` corresponds to the user that owns the access key.     If the user identifier is not known, it can be obtained from `/{tenantUrlCode}/api/v2/users`. The `securityIdentifier` field represents the user identifier.    - **enabled** (required): A boolean (`true` or `false`) indicating whether the access key is active.    - **ipWhitelisted** (required): A list of IP addresses from which requests can be made using the access key. An empty list removes all IPs from the access key.    - **notes** (required): A free-text field to describe the purpose or usage of the access key.    For example, the request `tenantName/api/v2/ApiKey` with the body:   ```json {   \"accessKey\": \"00000000-0000-0000-0000-000000000001\",   \"enabled\": false,   \"ipWhitelisted\": [],   \"notes\": \"\" } ``` will disable the access key 00000000-0000-0000-0000-000000000001 as well as removing the notes and all whitelisted IP addresses from it.

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
api_instance = cartovista_cloud_clients.ApiKeyApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateAccessKeyDTO() # UpdateAccessKeyDTO | 
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
 **body** | [**UpdateAccessKeyDTO**](UpdateAccessKeyDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


