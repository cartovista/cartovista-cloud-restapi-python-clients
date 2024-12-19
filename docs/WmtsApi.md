# cartovista_cloud_clients.WmtsApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wmts_create_wmts_layer**](WmtsApi.md#wmts_create_wmts_layer) | **POST** /{tenantUrlCode}/api/v2/wmts | Creates a new WMTS layer.
[**wmts_delete_wmts_layer**](WmtsApi.md#wmts_delete_wmts_layer) | **DELETE** /{tenantUrlCode}/api/v2/wmts/{identifier} | Deletes the WMTS layer.
[**wmts_get_wmts_layer**](WmtsApi.md#wmts_get_wmts_layer) | **GET** /{tenantUrlCode}/api/v2/wmts/{identifier} | Gets a specific WMTs layer.
[**wmts_get_wmts_layer_details**](WmtsApi.md#wmts_get_wmts_layer_details) | **GET** /{tenantUrlCode}/api/v2/wmts/{identifier}/details | Gets the WMTS layer and its related maps.
[**wmts_get_wmts_layers**](WmtsApi.md#wmts_get_wmts_layers) | **GET** /{tenantUrlCode}/api/v2/wmts | Gets all the WMTS layers the user has access to.
[**wmts_update_wmts_layer**](WmtsApi.md#wmts_update_wmts_layer) | **PATCH** /{tenantUrlCode}/api/v2/wmts/{identifier} | Updates the WMTS layer&#x27;s properties.
[**wmts_update_wmts_layer_permissions**](WmtsApi.md#wmts_update_wmts_layer_permissions) | **PATCH** /{tenantUrlCode}/api/v2/wmts/{identifier}/permissions | Updates the WMTS layer&#x27;s permissions.

# **wmts_create_wmts_layer**
> WmtsLayer wmts_create_wmts_layer(body, tenant_url_code)

Creates a new WMTS layer.

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
api_instance = cartovista_cloud_clients.WmtsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreateWmtsLayer() # CreateWmtsLayer | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a new WMTS layer.
    api_response = api_instance.wmts_create_wmts_layer(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmtsApi->wmts_create_wmts_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWmtsLayer**](CreateWmtsLayer.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**WmtsLayer**](WmtsLayer.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wmts_delete_wmts_layer**
> DeleteWmtsLayerResponse wmts_delete_wmts_layer(identifier, tenant_url_code)

Deletes the WMTS layer.

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
api_instance = cartovista_cloud_clients.WmtsApi(cartovista_cloud_clients.ApiClient(configuration))
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes the WMTS layer.
    api_response = api_instance.wmts_delete_wmts_layer(identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmtsApi->wmts_delete_wmts_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DeleteWmtsLayerResponse**](DeleteWmtsLayerResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wmts_get_wmts_layer**
> WmtsLayer wmts_get_wmts_layer(identifier, tenant_url_code)

Gets a specific WMTs layer.

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
api_instance = cartovista_cloud_clients.WmtsApi(cartovista_cloud_clients.ApiClient(configuration))
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific WMTs layer.
    api_response = api_instance.wmts_get_wmts_layer(identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmtsApi->wmts_get_wmts_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**WmtsLayer**](WmtsLayer.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wmts_get_wmts_layer_details**
> WmtsLayerWithDetails wmts_get_wmts_layer_details(identifier, tenant_url_code)

Gets the WMTS layer and its related maps.

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
api_instance = cartovista_cloud_clients.WmtsApi(cartovista_cloud_clients.ApiClient(configuration))
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the WMTS layer and its related maps.
    api_response = api_instance.wmts_get_wmts_layer_details(identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmtsApi->wmts_get_wmts_layer_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**WmtsLayerWithDetails**](WmtsLayerWithDetails.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wmts_get_wmts_layers**
> list[WmtsLayer] wmts_get_wmts_layers(tenant_url_code)

Gets all the WMTS layers the user has access to.

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
api_instance = cartovista_cloud_clients.WmtsApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the WMTS layers the user has access to.
    api_response = api_instance.wmts_get_wmts_layers(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmtsApi->wmts_get_wmts_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**list[WmtsLayer]**](WmtsLayer.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wmts_update_wmts_layer**
> WmtsLayer wmts_update_wmts_layer(body, identifier, tenant_url_code)

Updates the WMTS layer's properties.

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
api_instance = cartovista_cloud_clients.WmtsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateWmtsLayerParameter() # UpdateWmtsLayerParameter | 
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the WMTS layer's properties.
    api_response = api_instance.wmts_update_wmts_layer(body, identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmtsApi->wmts_update_wmts_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWmtsLayerParameter**](UpdateWmtsLayerParameter.md)|  | 
 **identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**WmtsLayer**](WmtsLayer.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wmts_update_wmts_layer_permissions**
> list[PermissionPairComplexDTO] wmts_update_wmts_layer_permissions(body, identifier, tenant_url_code)

Updates the WMTS layer's permissions.

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
api_instance = cartovista_cloud_clients.WmtsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ApplyGenericPermissionsParameter() # ApplyGenericPermissionsParameter | 
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the WMTS layer's permissions.
    api_response = api_instance.wmts_update_wmts_layer_permissions(body, identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmtsApi->wmts_update_wmts_layer_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyGenericPermissionsParameter**](ApplyGenericPermissionsParameter.md)|  | 
 **identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[PermissionPairComplexDTO]**](PermissionPairComplexDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


