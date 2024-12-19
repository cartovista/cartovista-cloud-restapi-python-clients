# cartovista_cloud_clients.WmsApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wms_create_wms_layer**](WmsApi.md#wms_create_wms_layer) | **POST** /{tenantUrlCode}/api/v2/wms | Creates a new WMS layer.
[**wms_delete_wms_layer**](WmsApi.md#wms_delete_wms_layer) | **DELETE** /{tenantUrlCode}/api/v2/wms/{identifier} | Deletes the WMS layer.
[**wms_get_wms_extents**](WmsApi.md#wms_get_wms_extents) | **POST** /{tenantUrlCode}/api/v2/wms/GetExtents | Gets the extents of one or more WMS layers. NOTE: Some services may not have extents defined.
[**wms_get_wms_layer**](WmsApi.md#wms_get_wms_layer) | **GET** /{tenantUrlCode}/api/v2/wms/{identifier} | Gets a specific WMS layer.
[**wms_get_wms_layer_details**](WmsApi.md#wms_get_wms_layer_details) | **GET** /{tenantUrlCode}/api/v2/wms/{identifier}/details | Gets the WMS layer and its related maps.
[**wms_get_wms_layers**](WmsApi.md#wms_get_wms_layers) | **GET** /{tenantUrlCode}/api/v2/wms | Gets all the WMS layers the user has access to.
[**wms_update_wms_layer**](WmsApi.md#wms_update_wms_layer) | **PATCH** /{tenantUrlCode}/api/v2/wms/{identifier} | Updates the WMS layer
[**wms_update_wms_layer_permissions**](WmsApi.md#wms_update_wms_layer_permissions) | **PATCH** /{tenantUrlCode}/api/v2/wms/{identifier}/permissions | Updates the WMS layer permissions.

# **wms_create_wms_layer**
> WmsLayer wms_create_wms_layer(body, tenant_url_code)

Creates a new WMS layer.

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
api_instance = cartovista_cloud_clients.WmsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreateWmsLayer() # CreateWmsLayer | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a new WMS layer.
    api_response = api_instance.wms_create_wms_layer(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmsApi->wms_create_wms_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWmsLayer**](CreateWmsLayer.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**WmsLayer**](WmsLayer.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wms_delete_wms_layer**
> DeleteWmsLayerResponse wms_delete_wms_layer(identifier, tenant_url_code)

Deletes the WMS layer.

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
api_instance = cartovista_cloud_clients.WmsApi(cartovista_cloud_clients.ApiClient(configuration))
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes the WMS layer.
    api_response = api_instance.wms_delete_wms_layer(identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmsApi->wms_delete_wms_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DeleteWmsLayerResponse**](DeleteWmsLayerResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wms_get_wms_extents**
> list[ExtentDTO] wms_get_wms_extents(body, tenant_url_code)

Gets the extents of one or more WMS layers. NOTE: Some services may not have extents defined.

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
api_instance = cartovista_cloud_clients.WmsApi(cartovista_cloud_clients.ApiClient(configuration))
body = ['body_example'] # list[str] | The layer identifiers.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the extents of one or more WMS layers. NOTE: Some services may not have extents defined.
    api_response = api_instance.wms_get_wms_extents(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmsApi->wms_get_wms_extents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The layer identifiers. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[ExtentDTO]**](ExtentDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wms_get_wms_layer**
> WmsLayer wms_get_wms_layer(identifier, tenant_url_code)

Gets a specific WMS layer.

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
api_instance = cartovista_cloud_clients.WmsApi(cartovista_cloud_clients.ApiClient(configuration))
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific WMS layer.
    api_response = api_instance.wms_get_wms_layer(identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmsApi->wms_get_wms_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**WmsLayer**](WmsLayer.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wms_get_wms_layer_details**
> WmsLayerWithDetails wms_get_wms_layer_details(identifier, tenant_url_code)

Gets the WMS layer and its related maps.

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
api_instance = cartovista_cloud_clients.WmsApi(cartovista_cloud_clients.ApiClient(configuration))
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the WMS layer and its related maps.
    api_response = api_instance.wms_get_wms_layer_details(identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmsApi->wms_get_wms_layer_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**WmsLayerWithDetails**](WmsLayerWithDetails.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wms_get_wms_layers**
> list[WmsLayer] wms_get_wms_layers(tenant_url_code)

Gets all the WMS layers the user has access to.

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
api_instance = cartovista_cloud_clients.WmsApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the WMS layers the user has access to.
    api_response = api_instance.wms_get_wms_layers(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmsApi->wms_get_wms_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**list[WmsLayer]**](WmsLayer.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wms_update_wms_layer**
> WmsLayer wms_update_wms_layer(body, identifier, tenant_url_code)

Updates the WMS layer

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
api_instance = cartovista_cloud_clients.WmsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateWmsLayerParameter() # UpdateWmsLayerParameter | 
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the WMS layer
    api_response = api_instance.wms_update_wms_layer(body, identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmsApi->wms_update_wms_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWmsLayerParameter**](UpdateWmsLayerParameter.md)|  | 
 **identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**WmsLayer**](WmsLayer.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wms_update_wms_layer_permissions**
> list[PermissionPairComplexDTO] wms_update_wms_layer_permissions(body, identifier, tenant_url_code)

Updates the WMS layer permissions.

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
api_instance = cartovista_cloud_clients.WmsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ApplyGenericPermissionsParameter() # ApplyGenericPermissionsParameter | 
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the WMS layer permissions.
    api_response = api_instance.wms_update_wms_layer_permissions(body, identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmsApi->wms_update_wms_layer_permissions: %s\n" % e)
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


