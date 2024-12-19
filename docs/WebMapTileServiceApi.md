# cartovista_cloud_clients.WebMapTileServiceApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**web_map_tile_service_get_tile_set_tile**](WebMapTileServiceApi.md#web_map_tile_service_get_tile_set_tile) | **GET** /{tenantUrlCode}/api/v2/wmts/{basemapId}/{zoomLevel}/{row}/{col} | 

# **web_map_tile_service_get_tile_set_tile**
> str web_map_tile_service_get_tile_set_tile(basemap_id, zoom_level, row, col, tenant_url_code)



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
api_instance = cartovista_cloud_clients.WebMapTileServiceApi(cartovista_cloud_clients.ApiClient(configuration))
basemap_id = 'basemap_id_example' # str | 
zoom_level = 56 # int | 
row = 56 # int | 
col = 56 # int | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.web_map_tile_service_get_tile_set_tile(basemap_id, zoom_level, row, col, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebMapTileServiceApi->web_map_tile_service_get_tile_set_tile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basemap_id** | **str**|  | 
 **zoom_level** | **int**|  | 
 **row** | **int**|  | 
 **col** | **int**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


