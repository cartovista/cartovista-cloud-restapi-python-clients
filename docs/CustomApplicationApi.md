# cartovista_cloud_clients.CustomApplicationApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_application_get_custom_application_settings**](CustomApplicationApi.md#custom_application_get_custom_application_settings) | **GET** /{tenantUrlCode}/api/v2/map/{mapId}/custom-application/{urlCode}/settings | 
[**custom_application_toggle_custom_application**](CustomApplicationApi.md#custom_application_toggle_custom_application) | **PATCH** /{tenantUrlCode}/api/v2/map/{mapId}/custom-application/{urlCode}/toggle | 
[**custom_application_update_custom_application_settings**](CustomApplicationApi.md#custom_application_update_custom_application_settings) | **PATCH** /{tenantUrlCode}/api/v2/map/{mapId}/custom-application/{urlCode}/settings | 

# **custom_application_get_custom_application_settings**
> object custom_application_get_custom_application_settings(map_id, url_code, tenant_url_code)



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
# Configure API key authorization: secretKey
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.CustomApplicationApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | 
url_code = 'url_code_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.custom_application_get_custom_application_settings(map_id, url_code, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomApplicationApi->custom_application_get_custom_application_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **url_code** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_application_toggle_custom_application**
> list[CustomApplicationMapSettings] custom_application_toggle_custom_application(body, map_id, url_code, tenant_url_code)



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
# Configure API key authorization: secretKey
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.CustomApplicationApi(cartovista_cloud_clients.ApiClient(configuration))
body = True # bool | 
map_id = 'map_id_example' # str | 
url_code = 'url_code_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.custom_application_toggle_custom_application(body, map_id, url_code, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomApplicationApi->custom_application_toggle_custom_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**bool**](bool.md)|  | 
 **map_id** | **str**|  | 
 **url_code** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[CustomApplicationMapSettings]**](CustomApplicationMapSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_application_update_custom_application_settings**
> object custom_application_update_custom_application_settings(body, map_id, url_code, tenant_url_code)



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
# Configure API key authorization: secretKey
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.CustomApplicationApi(cartovista_cloud_clients.ApiClient(configuration))
body = NULL # object | 
map_id = 'map_id_example' # str | 
url_code = 'url_code_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.custom_application_update_custom_application_settings(body, map_id, url_code, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomApplicationApi->custom_application_update_custom_application_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **map_id** | **str**|  | 
 **url_code** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


