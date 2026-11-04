# cartovista_cloud_clients.PMTApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p_mt_create_pmt_layer**](PMTApi.md#p_mt_create_pmt_layer) | **POST** /{tenantUrlCode}/api/v2/pmt | Creates a new PM Tile layer.
[**p_mt_delete_pmt_layer**](PMTApi.md#p_mt_delete_pmt_layer) | **DELETE** /{tenantUrlCode}/api/v2/pmt/{identifier} | Deletes the PM Tile layer.
[**p_mt_get_pmt_layer**](PMTApi.md#p_mt_get_pmt_layer) | **GET** /{tenantUrlCode}/api/v2/pmt/{identifier} | Gets a specific PM Tile layer.
[**p_mt_get_pmt_layer_details**](PMTApi.md#p_mt_get_pmt_layer_details) | **GET** /{tenantUrlCode}/api/v2/pmt/{identifier}/details | Gets the PM Tile layer and its related maps.
[**p_mt_get_pmt_layers**](PMTApi.md#p_mt_get_pmt_layers) | **GET** /{tenantUrlCode}/api/v2/pmt | Gets all the PM Tile layers the user has access to.
[**p_mt_update_pmt_layer**](PMTApi.md#p_mt_update_pmt_layer) | **PATCH** /{tenantUrlCode}/api/v2/pmt/{identifier} | Updates the PM Tile layer&#x27;s properties.
[**p_mt_update_pmt_layer_permissions**](PMTApi.md#p_mt_update_pmt_layer_permissions) | **PATCH** /{tenantUrlCode}/api/v2/pmt/{identifier}/permissions | Updates the PM Tile layer&#x27;s permissions.

# **p_mt_create_pmt_layer**
> PMTLayer p_mt_create_pmt_layer(body, tenant_url_code)

Creates a new PM Tile layer.

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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PMTApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreatePMTLayer() # CreatePMTLayer | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a new PM Tile layer.
    api_response = api_instance.p_mt_create_pmt_layer(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PMTApi->p_mt_create_pmt_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePMTLayer**](CreatePMTLayer.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**PMTLayer**](PMTLayer.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_mt_delete_pmt_layer**
> DeletePMTLayerResponse p_mt_delete_pmt_layer(identifier, tenant_url_code)

Deletes the PM Tile layer.

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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PMTApi(cartovista_cloud_clients.ApiClient(configuration))
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes the PM Tile layer.
    api_response = api_instance.p_mt_delete_pmt_layer(identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PMTApi->p_mt_delete_pmt_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DeletePMTLayerResponse**](DeletePMTLayerResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_mt_get_pmt_layer**
> PMTLayer p_mt_get_pmt_layer(identifier, tenant_url_code)

Gets a specific PM Tile layer.

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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PMTApi(cartovista_cloud_clients.ApiClient(configuration))
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific PM Tile layer.
    api_response = api_instance.p_mt_get_pmt_layer(identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PMTApi->p_mt_get_pmt_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**PMTLayer**](PMTLayer.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_mt_get_pmt_layer_details**
> PMTLayerWithDetails p_mt_get_pmt_layer_details(identifier, tenant_url_code)

Gets the PM Tile layer and its related maps.

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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PMTApi(cartovista_cloud_clients.ApiClient(configuration))
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the PM Tile layer and its related maps.
    api_response = api_instance.p_mt_get_pmt_layer_details(identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PMTApi->p_mt_get_pmt_layer_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**PMTLayerWithDetails**](PMTLayerWithDetails.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_mt_get_pmt_layers**
> list[PMTLayer] p_mt_get_pmt_layers(tenant_url_code)

Gets all the PM Tile layers the user has access to.

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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PMTApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the PM Tile layers the user has access to.
    api_response = api_instance.p_mt_get_pmt_layers(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PMTApi->p_mt_get_pmt_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**list[PMTLayer]**](PMTLayer.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_mt_update_pmt_layer**
> PMTLayer p_mt_update_pmt_layer(body, identifier, tenant_url_code)

Updates the PM Tile layer's properties.

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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PMTApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdatePMTLayerParameter() # UpdatePMTLayerParameter | 
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the PM Tile layer's properties.
    api_response = api_instance.p_mt_update_pmt_layer(body, identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PMTApi->p_mt_update_pmt_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePMTLayerParameter**](UpdatePMTLayerParameter.md)|  | 
 **identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**PMTLayer**](PMTLayer.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_mt_update_pmt_layer_permissions**
> list[PermissionPairComplexDTO] p_mt_update_pmt_layer_permissions(body, identifier, tenant_url_code)

Updates the PM Tile layer's permissions.

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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PMTApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ApplyGenericPermissionsParameter() # ApplyGenericPermissionsParameter | 
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the PM Tile layer's permissions.
    api_response = api_instance.p_mt_update_pmt_layer_permissions(body, identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PMTApi->p_mt_update_pmt_layer_permissions: %s\n" % e)
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

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


