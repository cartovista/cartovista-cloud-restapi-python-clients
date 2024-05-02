# cartovista_cloud_clients.GridLayerApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_layer_add_grid_source**](GridLayerApi.md#grid_layer_add_grid_source) | **POST** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId}/GridSources | Add a grid source to an existing grid layer.
[**grid_layer_add_grid_sources**](GridLayerApi.md#grid_layer_add_grid_sources) | **POST** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId}/GridSources/all | Add all the bands from a tif file to an existing grid layer.
[**grid_layer_create_grid_layer**](GridLayerApi.md#grid_layer_create_grid_layer) | **POST** /{tenantUrlCode}/api/v2/GridLayer | Create a grid layer with the specified parameters.
[**grid_layer_delete_grid_layer**](GridLayerApi.md#grid_layer_delete_grid_layer) | **DELETE** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId} | Delete an existing grid layer.
[**grid_layer_delete_grid_source**](GridLayerApi.md#grid_layer_delete_grid_source) | **DELETE** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId}/GridSources/{gridSourceId} | Delete an existing grid source.
[**grid_layer_export_grid_source_subset**](GridLayerApi.md#grid_layer_export_grid_source_subset) | **POST** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId}/GridSources/{gridSourceId}/subset | Exports a subset of the grid source. The file can be downloaded with &#x60;DownloadFile/download&#x60;.
[**grid_layer_get_first_grid_source_extents**](GridLayerApi.md#grid_layer_get_first_grid_source_extents) | **POST** /{tenantUrlCode}/api/v2/GridLayer/firstGridSourceExtents | Gets the extents of the first grid source of each layer.
[**grid_layer_get_grid_layer_by_id**](GridLayerApi.md#grid_layer_get_grid_layer_by_id) | **GET** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId} | Get a grid layer by identifier.
[**grid_layer_get_grid_layer_details**](GridLayerApi.md#grid_layer_get_grid_layer_details) | **GET** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId}/details | Gets the grid layer, its grid sources, related maps and settings.
[**grid_layer_get_grid_layers**](GridLayerApi.md#grid_layer_get_grid_layers) | **GET** /{tenantUrlCode}/api/v2/GridLayers | Get the list of all grid layers.
[**grid_layer_get_grid_source**](GridLayerApi.md#grid_layer_get_grid_source) | **GET** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId}/GridSources/{gridSourceId} | Get a grid source by identifier.
[**grid_layer_get_grid_sources_for_grid_layer**](GridLayerApi.md#grid_layer_get_grid_sources_for_grid_layer) | **GET** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId}/GridSources | Get all the grid sources associated with the grid layer.
[**grid_layer_get_maps_by_grid_layer**](GridLayerApi.md#grid_layer_get_maps_by_grid_layer) | **GET** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId}/maps | Gets all the maps that use the grid layer.
[**grid_layer_update_grid_layer**](GridLayerApi.md#grid_layer_update_grid_layer) | **PATCH** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId} | Update the properties of an existing grid layer.
[**grid_layer_update_grid_layer_permissions**](GridLayerApi.md#grid_layer_update_grid_layer_permissions) | **PATCH** /{tenantUrlCode}/api/v2/GridLayer/{identifier}/permissions | Updates the grid layer&#x27;s permissions.
[**grid_layer_update_grid_source**](GridLayerApi.md#grid_layer_update_grid_source) | **PATCH** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId}/GridSources/{gridSourceId} | Update the properties of an existing grid source.
[**grid_layer_update_grid_source_geotiff**](GridLayerApi.md#grid_layer_update_grid_source_geotiff) | **POST** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId}/GridSources/{gridSourceId}/updateGeotiff | Update the geoTIFF of an existing grid source.

# **grid_layer_add_grid_source**
> GridSource grid_layer_add_grid_source(body, grid_layer_id, tenant_url_code)

Add a grid source to an existing grid layer.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.FlatFileGridLayerDefinitionDTO() # FlatFileGridLayerDefinitionDTO | 
grid_layer_id = 'grid_layer_id_example' # str | The grid layer system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Add a grid source to an existing grid layer.
    api_response = api_instance.grid_layer_add_grid_source(body, grid_layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_add_grid_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FlatFileGridLayerDefinitionDTO**](FlatFileGridLayerDefinitionDTO.md)|  | 
 **grid_layer_id** | **str**| The grid layer system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GridSource**](GridSource.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_add_grid_sources**
> list[GridSource] grid_layer_add_grid_sources(grid_layer_id, tenant_url_code, file=file)

Add all the bands from a tif file to an existing grid layer.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
grid_layer_id = 'grid_layer_id_example' # str | The grid layer system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Add all the bands from a tif file to an existing grid layer.
    api_response = api_instance.grid_layer_add_grid_sources(grid_layer_id, tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_add_grid_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_layer_id** | **str**| The grid layer system identifier. | 
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**list[GridSource]**](GridSource.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_create_grid_layer**
> GridLayer grid_layer_create_grid_layer(body, tenant_url_code)

Create a grid layer with the specified parameters.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GridLayerCreateParameters() # GridLayerCreateParameters | The parameters used to create the grid layer.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Create a grid layer with the specified parameters.
    api_response = api_instance.grid_layer_create_grid_layer(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_create_grid_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GridLayerCreateParameters**](GridLayerCreateParameters.md)| The parameters used to create the grid layer. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GridLayer**](GridLayer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_delete_grid_layer**
> DeleteGridLayerResponse grid_layer_delete_grid_layer(grid_layer_id, tenant_url_code)

Delete an existing grid layer.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
grid_layer_id = 'grid_layer_id_example' # str | The grid layer system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Delete an existing grid layer.
    api_response = api_instance.grid_layer_delete_grid_layer(grid_layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_delete_grid_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_layer_id** | **str**| The grid layer system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DeleteGridLayerResponse**](DeleteGridLayerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_delete_grid_source**
> DeleteGridSourceResponse grid_layer_delete_grid_source(grid_layer_id, grid_source_id, tenant_url_code)

Delete an existing grid source.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
grid_layer_id = 'grid_layer_id_example' # str | The grid layer system identifier.
grid_source_id = 'grid_source_id_example' # str | The grid source system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Delete an existing grid source.
    api_response = api_instance.grid_layer_delete_grid_source(grid_layer_id, grid_source_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_delete_grid_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_layer_id** | **str**| The grid layer system identifier. | 
 **grid_source_id** | **str**| The grid source system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DeleteGridSourceResponse**](DeleteGridSourceResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_export_grid_source_subset**
> str grid_layer_export_grid_source_subset(body, grid_layer_id, grid_source_id, tenant_url_code)

Exports a subset of the grid source. The file can be downloaded with `DownloadFile/download`.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = 'body_example' # str | 
grid_layer_id = 'grid_layer_id_example' # str | 
grid_source_id = 'grid_source_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Exports a subset of the grid source. The file can be downloaded with `DownloadFile/download`.
    api_response = api_instance.grid_layer_export_grid_source_subset(body, grid_layer_id, grid_source_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_export_grid_source_subset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **grid_layer_id** | **str**|  | 
 **grid_source_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_get_first_grid_source_extents**
> list[ExtentDTO] grid_layer_get_first_grid_source_extents(body, tenant_url_code)

Gets the extents of the first grid source of each layer.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = ['body_example'] # list[str] | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the extents of the first grid source of each layer.
    api_response = api_instance.grid_layer_get_first_grid_source_extents(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_get_first_grid_source_extents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[ExtentDTO]**](ExtentDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_get_grid_layer_by_id**
> GridLayer grid_layer_get_grid_layer_by_id(grid_layer_id, tenant_url_code)

Get a grid layer by identifier.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
grid_layer_id = 'grid_layer_id_example' # str | The grid layer system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Get a grid layer by identifier.
    api_response = api_instance.grid_layer_get_grid_layer_by_id(grid_layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_get_grid_layer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_layer_id** | **str**| The grid layer system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GridLayer**](GridLayer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_get_grid_layer_details**
> GridLayerWithDetails grid_layer_get_grid_layer_details(grid_layer_id, tenant_url_code)

Gets the grid layer, its grid sources, related maps and settings.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
grid_layer_id = 'grid_layer_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the grid layer, its grid sources, related maps and settings.
    api_response = api_instance.grid_layer_get_grid_layer_details(grid_layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_get_grid_layer_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_layer_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GridLayerWithDetails**](GridLayerWithDetails.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_get_grid_layers**
> list[GridLayer] grid_layer_get_grid_layers(tenant_url_code)

Get the list of all grid layers.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Get the list of all grid layers.
    api_response = api_instance.grid_layer_get_grid_layers(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_get_grid_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**list[GridLayer]**](GridLayer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_get_grid_source**
> GridSource grid_layer_get_grid_source(grid_layer_id, grid_source_id, tenant_url_code)

Get a grid source by identifier.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
grid_layer_id = 'grid_layer_id_example' # str | The grid layer system identifier.
grid_source_id = 'grid_source_id_example' # str | The grid source system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Get a grid source by identifier.
    api_response = api_instance.grid_layer_get_grid_source(grid_layer_id, grid_source_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_get_grid_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_layer_id** | **str**| The grid layer system identifier. | 
 **grid_source_id** | **str**| The grid source system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GridSource**](GridSource.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_get_grid_sources_for_grid_layer**
> list[GridSource] grid_layer_get_grid_sources_for_grid_layer(grid_layer_id, tenant_url_code)

Get all the grid sources associated with the grid layer.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
grid_layer_id = 'grid_layer_id_example' # str | The grid layer system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Get all the grid sources associated with the grid layer.
    api_response = api_instance.grid_layer_get_grid_sources_for_grid_layer(grid_layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_get_grid_sources_for_grid_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_layer_id** | **str**| The grid layer system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[GridSource]**](GridSource.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_get_maps_by_grid_layer**
> list[Map] grid_layer_get_maps_by_grid_layer(grid_layer_id, tenant_url_code)

Gets all the maps that use the grid layer.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
grid_layer_id = 'grid_layer_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the maps that use the grid layer.
    api_response = api_instance.grid_layer_get_maps_by_grid_layer(grid_layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_get_maps_by_grid_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_layer_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Map]**](Map.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_update_grid_layer**
> GridLayer grid_layer_update_grid_layer(body, grid_layer_id, tenant_url_code)

Update the properties of an existing grid layer.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GridLayerUpdateParameters() # GridLayerUpdateParameters | The parameters to update.
grid_layer_id = 'grid_layer_id_example' # str | The grid layer system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Update the properties of an existing grid layer.
    api_response = api_instance.grid_layer_update_grid_layer(body, grid_layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_update_grid_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GridLayerUpdateParameters**](GridLayerUpdateParameters.md)| The parameters to update. | 
 **grid_layer_id** | **str**| The grid layer system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GridLayer**](GridLayer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_update_grid_layer_permissions**
> list[PermissionPairComplexDTO] grid_layer_update_grid_layer_permissions(body, identifier, tenant_url_code)

Updates the grid layer's permissions.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ApplyGenericPermissionsParameter() # ApplyGenericPermissionsParameter | 
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the grid layer's permissions.
    api_response = api_instance.grid_layer_update_grid_layer_permissions(body, identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_update_grid_layer_permissions: %s\n" % e)
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

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_update_grid_source**
> GridSource grid_layer_update_grid_source(body, grid_layer_id, grid_source_id, tenant_url_code)

Update the properties of an existing grid source.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GridSourceUpdateParameters() # GridSourceUpdateParameters | The parameters to update.
grid_layer_id = 'grid_layer_id_example' # str | The grid layer system identifier.
grid_source_id = 'grid_source_id_example' # str | The grid source system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Update the properties of an existing grid source.
    api_response = api_instance.grid_layer_update_grid_source(body, grid_layer_id, grid_source_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_update_grid_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GridSourceUpdateParameters**](GridSourceUpdateParameters.md)| The parameters to update. | 
 **grid_layer_id** | **str**| The grid layer system identifier. | 
 **grid_source_id** | **str**| The grid source system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GridSource**](GridSource.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_update_grid_source_geotiff**
> GridSource grid_layer_update_grid_source_geotiff(body, grid_layer_id, grid_source_id, tenant_url_code)

Update the geoTIFF of an existing grid source.

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
api_instance = cartovista_cloud_clients.GridLayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.FlatFileGridLayerDefinitionDTO() # FlatFileGridLayerDefinitionDTO | 
grid_layer_id = 'grid_layer_id_example' # str | The grid layer system identifier.
grid_source_id = 'grid_source_id_example' # str | The grid source system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Update the geoTIFF of an existing grid source.
    api_response = api_instance.grid_layer_update_grid_source_geotiff(body, grid_layer_id, grid_source_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerApi->grid_layer_update_grid_source_geotiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FlatFileGridLayerDefinitionDTO**](FlatFileGridLayerDefinitionDTO.md)|  | 
 **grid_layer_id** | **str**| The grid layer system identifier. | 
 **grid_source_id** | **str**| The grid source system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GridSource**](GridSource.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

