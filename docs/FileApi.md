# cartovista_cloud_clients.FileApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_download_file**](FileApi.md#file_download_file) | **POST** /{tenantUrlCode}/api/v2/DownloadFile/download | Downloads the data.
[**file_download_grid_source**](FileApi.md#file_download_grid_source) | **GET** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId}/GridSource/{gridSourceId}/download | Downloads the grid source in the given grid layer.
[**file_export_feedback**](FileApi.md#file_export_feedback) | **GET** /{tenantUrlCode}/api/v2/feedback/{mapId} | Exports the map&#x27;s feedback in MapInfo format.
[**file_get_data**](FileApi.md#file_get_data) | **GET** /{tenantUrlCode}/api/v2/GridLayer/{gridLayerId}/GridSource/{gridSourceId}/getData | Gets a chunk of the grid layer&#x27;s data.
[**file_get_raster**](FileApi.md#file_get_raster) | **GET** /{tenantUrlCode}/api/v2/wms/{identifier}/raster | Generates a WMS raster in PNG format.
[**file_get_symbol_file**](FileApi.md#file_get_symbol_file) | **GET** /{tenantUrlCode}/api/v2/symbols/{id}/file | Downloads the symbol&#x27;s file.

# **file_download_file**
> GenericWebPortalResponse file_download_file(body, tenant_url_code)

Downloads the data.

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
api_instance = cartovista_cloud_clients.FileApi(cartovista_cloud_clients.ApiClient(configuration))
body = 'body_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Downloads the data.
    api_response = api_instance.file_download_file(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->file_download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GenericWebPortalResponse**](GenericWebPortalResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_download_grid_source**
> str file_download_grid_source(grid_layer_id, grid_source_id, tenant_url_code, original_file=original_file)

Downloads the grid source in the given grid layer.

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
api_instance = cartovista_cloud_clients.FileApi(cartovista_cloud_clients.ApiClient(configuration))
grid_layer_id = 'grid_layer_id_example' # str | 
grid_source_id = 'grid_source_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 
original_file = true # bool | Optional (optional) (default to true)

try:
    # Downloads the grid source in the given grid layer.
    api_response = api_instance.file_download_grid_source(grid_layer_id, grid_source_id, tenant_url_code, original_file=original_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->file_download_grid_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_layer_id** | **str**|  | 
 **grid_source_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 
 **original_file** | **bool**| Optional | [optional] [default to true]

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_export_feedback**
> str file_export_feedback(map_id, tenant_url_code)

Exports the map's feedback in MapInfo format.

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
api_instance = cartovista_cloud_clients.FileApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Exports the map's feedback in MapInfo format.
    api_response = api_instance.file_export_feedback(map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->file_export_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_get_data**
> str file_get_data(grid_layer_id, grid_source_id, tenant_url_code)

Gets a chunk of the grid layer's data.

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
api_instance = cartovista_cloud_clients.FileApi(cartovista_cloud_clients.ApiClient(configuration))
grid_layer_id = 'grid_layer_id_example' # str | 
grid_source_id = 'grid_source_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a chunk of the grid layer's data.
    api_response = api_instance.file_get_data(grid_layer_id, grid_source_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->file_get_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_layer_id** | **str**|  | 
 **grid_source_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_get_raster**
> str file_get_raster(identifier, bbox, width, height, tenant_url_code)

Generates a WMS raster in PNG format.

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
api_instance = cartovista_cloud_clients.FileApi(cartovista_cloud_clients.ApiClient(configuration))
identifier = 'identifier_example' # str | 
bbox = 'bbox_example' # str | 
width = 'width_example' # str | 
height = 'height_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Generates a WMS raster in PNG format.
    api_response = api_instance.file_get_raster(identifier, bbox, width, height, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->file_get_raster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **bbox** | **str**|  | 
 **width** | **str**|  | 
 **height** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_get_symbol_file**
> str file_get_symbol_file(id, tenant_url_code)

Downloads the symbol's file.

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
api_instance = cartovista_cloud_clients.FileApi(cartovista_cloud_clients.ApiClient(configuration))
id = 'id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Downloads the symbol's file.
    api_response = api_instance.file_get_symbol_file(id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->file_get_symbol_file: %s\n" % e)
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
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

