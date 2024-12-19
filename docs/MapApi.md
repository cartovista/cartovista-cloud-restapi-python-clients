# cartovista_cloud_clients.MapApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**map_add_layers_to_map**](MapApi.md#map_add_layers_to_map) | **POST** /{tenantUrlCode}/api/v2/maps/{mapId}/layers | Add layers to a dynamic map. The operation adds new layers only, the existing layers are not removed.
[**map_clone_map**](MapApi.md#map_clone_map) | **POST** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/clone | Clones the map.
[**map_create_map**](MapApi.md#map_create_map) | **POST** /{tenantUrlCode}/api/v2/maps | Create a map based on the provided parameters.
[**map_create_slide**](MapApi.md#map_create_slide) | **POST** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/slides | Creates a new slide.
[**map_delete_map**](MapApi.md#map_delete_map) | **DELETE** /{tenantUrlCode}/api/v2/maps/{mapId} | Deletes a map.
[**map_delete_map_grid_layer**](MapApi.md#map_delete_map_grid_layer) | **DELETE** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/grid/{gridLayerIdentifier} | Removes the grid layer from the map.
[**map_delete_map_layer**](MapApi.md#map_delete_map_layer) | **DELETE** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/layers/{layerIdentifier} | Removes the layer from the map.
[**map_delete_map_wms_layer**](MapApi.md#map_delete_map_wms_layer) | **DELETE** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/wms/{wmsLayerIdentifier} | Removes the WMS layer from the map.
[**map_delete_map_wmts_layer**](MapApi.md#map_delete_map_wmts_layer) | **DELETE** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/wmts/{wmtsLayerIdentifier} | Removes the WMTS layer from the map.
[**map_export_map_data_by_extent**](MapApi.md#map_export_map_data_by_extent) | **POST** /{tenantUrlCode}/api/v2/maps/export-data-extent | Exports some or all the map&#x27;s layers data within an extent in Excel format. The file can be downloaded with &#x60;DownloadFile/download&#x60;.
[**map_export_map_data_by_selection**](MapApi.md#map_export_map_data_by_selection) | **POST** /{tenantUrlCode}/api/v2/maps/export-data-selection | Exports the map&#x27;s selection in Excel format. The file can be downloaded with &#x60;DownloadFile/download&#x60;.
[**map_export_map_elements**](MapApi.md#map_export_map_elements) | **POST** /{tenantUrlCode}/api/v2/maps/ExportMapElements | Exports an Excel sheet of all the maps. The file can be downloaded with &#x60;DownloadFile/download&#x60;. The language is used to localized the sheet&#x27;s name and columns.
[**map_get_data_tables_by_map**](MapApi.md#map_get_data_tables_by_map) | **GET** /{tenantUrlCode}/api/v2/maps/{mapId}/dataTables | Gets the tables used by this map.
[**map_get_grid_layers_by_map**](MapApi.md#map_get_grid_layers_by_map) | **GET** /{tenantUrlCode}/api/v2/maps/{mapId}/gridLayers | Gets the list of grid layers used in a map.
[**map_get_keywords**](MapApi.md#map_get_keywords) | **GET** /{tenantUrlCode}/api/v2/maps/keywords | Gets the map&#x27;s keywords.
[**map_get_layers_by_map**](MapApi.md#map_get_layers_by_map) | **GET** /{tenantUrlCode}/api/v2/maps/{mapId}/layers | Gets the list of Layers used in a map.
[**map_get_map**](MapApi.md#map_get_map) | **GET** /{tenantUrlCode}/api/v2/maps/{mapId} | Get a map based on the map id or a friendly identifier.
[**map_get_map_advanced_settings**](MapApi.md#map_get_map_advanced_settings) | **GET** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/advancedSettings | Gets the map&#x27;s advanced settings.
[**map_get_map_for_viewer**](MapApi.md#map_get_map_for_viewer) | **GET** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/viewer | Gets all the data required to open a map.
[**map_get_map_toolbar**](MapApi.md#map_get_map_toolbar) | **GET** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/toolbar | Gets the map&#x27;s toolbar settings.
[**map_get_map_with_details**](MapApi.md#map_get_map_with_details) | **GET** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/details | Gets the map, its tables and its layers.
[**map_get_maps**](MapApi.md#map_get_maps) | **GET** /{tenantUrlCode}/api/v2/maps/maps | Get all maps the requesting user has access to.
[**map_get_maps_content**](MapApi.md#map_get_maps_content) | **POST** /{tenantUrlCode}/api/v2/maps/elements | Gets all the maps and folders the user has access to in a specific folder. If the folder id is omitted, the root folder is used.
[**map_get_slides**](MapApi.md#map_get_slides) | **GET** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/slides | Gets the map&#x27;s slides.
[**map_move_map_layer**](MapApi.md#map_move_map_layer) | **PATCH** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/layer-order | Reorders the map&#x27;s layers.
[**map_run_map_action**](MapApi.md#map_run_map_action) | **POST** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/action | Runs a map action.
[**map_save_default_map_print_layout**](MapApi.md#map_save_default_map_print_layout) | **POST** /{tenantUrlCode}/api/v2/maps/save-default-layout | Updates the default print layout.
[**map_save_map_print_layout**](MapApi.md#map_save_map_print_layout) | **POST** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/save-layout | Updates the map&#x27;s print layout.
[**map_search_map**](MapApi.md#map_search_map) | **POST** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/search | Searches for a match in the searchable columns of the map&#x27;s layers and geocoded addresses.
[**map_search_map_layer**](MapApi.md#map_search_map_layer) | **POST** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/layer/{layerIdentifier}/search | Searches for a match in the searchable columns of the map&#x27;s layers.
[**map_share_map**](MapApi.md#map_share_map) | **POST** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/share | Shares the map with internal users.
[**map_share_map_external**](MapApi.md#map_share_map_external) | **POST** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/share-external | Shares the map with external users. The map is set to public.
[**map_update_map**](MapApi.md#map_update_map) | **PATCH** /{tenantUrlCode}/api/v2/maps/{mapId} | Updates a map properties based on the given parameters.
[**map_update_map_advanced_settings**](MapApi.md#map_update_map_advanced_settings) | **POST** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/advancedSettings | Updates the map&#x27;s advanced settings.
[**map_update_map_identifier**](MapApi.md#map_update_map_identifier) | **PATCH** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/identifier | Updates the map identifier.
[**map_update_map_layers**](MapApi.md#map_update_map_layers) | **PATCH** /{tenantUrlCode}/api/v2/maps/{mapId}/layers | Updates a dynamic map&#x27;s layers. The map will lose the associations with previous layers that are not included in the list.
[**map_update_map_toolbar**](MapApi.md#map_update_map_toolbar) | **POST** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/toolbar | Updates the map&#x27;s toolbar settings.
[**map_update_thumbnail**](MapApi.md#map_update_thumbnail) | **PATCH** /{tenantUrlCode}/api/v2/maps/{mapIdentifier}/thumbnail | Updates the map thumbnail.

# **map_add_layers_to_map**
> MapLayersResponse map_add_layers_to_map(body, map_id, tenant_url_code)

Add layers to a dynamic map. The operation adds new layers only, the existing layers are not removed.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.AddMapLayersParameter() # AddMapLayersParameter | 
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Add layers to a dynamic map. The operation adds new layers only, the existing layers are not removed.
    api_response = api_instance.map_add_layers_to_map(body, map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_add_layers_to_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddMapLayersParameter**](AddMapLayersParameter.md)|  | 
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MapLayersResponse**](MapLayersResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_clone_map**
> Map map_clone_map(map_identifier, tenant_url_code)

Clones the map.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Clones the map.
    api_response = api_instance.map_clone_map(map_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_clone_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Map**](Map.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_create_map**
> Map map_create_map(body, tenant_url_code)

Create a map based on the provided parameters.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.MapCreateParameter() # MapCreateParameter | Parameters used to create the map.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Create a map based on the provided parameters.
    api_response = api_instance.map_create_map(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_create_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MapCreateParameter**](MapCreateParameter.md)| Parameters used to create the map. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Map**](Map.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_create_slide**
> Slide map_create_slide(body, map_identifier, tenant_url_code)

Creates a new slide.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.SlideCreateUpdate() # SlideCreateUpdate | 
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a new slide.
    api_response = api_instance.map_create_slide(body, map_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_create_slide: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SlideCreateUpdate**](SlideCreateUpdate.md)|  | 
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Slide**](Slide.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_delete_map**
> map_delete_map(map_id, tenant_url_code)

Deletes a map.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | Map id or a friendly identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes a map.
    api_instance.map_delete_map(map_id, tenant_url_code)
except ApiException as e:
    print("Exception when calling MapApi->map_delete_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| Map id or a friendly identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_delete_map_grid_layer**
> MapLayersResponse map_delete_map_grid_layer(map_identifier, grid_layer_identifier, tenant_url_code)

Removes the grid layer from the map.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_identifier = 'map_identifier_example' # str | 
grid_layer_identifier = 'grid_layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Removes the grid layer from the map.
    api_response = api_instance.map_delete_map_grid_layer(map_identifier, grid_layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_delete_map_grid_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**|  | 
 **grid_layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MapLayersResponse**](MapLayersResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_delete_map_layer**
> MapLayersResponse map_delete_map_layer(map_identifier, layer_identifier, tenant_url_code)

Removes the layer from the map.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_identifier = 'map_identifier_example' # str | 
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Removes the layer from the map.
    api_response = api_instance.map_delete_map_layer(map_identifier, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_delete_map_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**|  | 
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MapLayersResponse**](MapLayersResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_delete_map_wms_layer**
> MapLayersResponse map_delete_map_wms_layer(map_identifier, wms_layer_identifier, tenant_url_code)

Removes the WMS layer from the map.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_identifier = 'map_identifier_example' # str | 
wms_layer_identifier = 'wms_layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Removes the WMS layer from the map.
    api_response = api_instance.map_delete_map_wms_layer(map_identifier, wms_layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_delete_map_wms_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**|  | 
 **wms_layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MapLayersResponse**](MapLayersResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_delete_map_wmts_layer**
> MapLayersResponse map_delete_map_wmts_layer(map_identifier, wmts_layer_identifier, tenant_url_code)

Removes the WMTS layer from the map.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_identifier = 'map_identifier_example' # str | 
wmts_layer_identifier = 'wmts_layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Removes the WMTS layer from the map.
    api_response = api_instance.map_delete_map_wmts_layer(map_identifier, wmts_layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_delete_map_wmts_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**|  | 
 **wmts_layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MapLayersResponse**](MapLayersResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_export_map_data_by_extent**
> str map_export_map_data_by_extent(body, tenant_url_code)

Exports some or all the map's layers data within an extent in Excel format. The file can be downloaded with `DownloadFile/download`.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.LayersExportByExtentParameter() # LayersExportByExtentParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Exports some or all the map's layers data within an extent in Excel format. The file can be downloaded with `DownloadFile/download`.
    api_response = api_instance.map_export_map_data_by_extent(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_export_map_data_by_extent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayersExportByExtentParameter**](LayersExportByExtentParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_export_map_data_by_selection**
> str map_export_map_data_by_selection(body, tenant_url_code)

Exports the map's selection in Excel format. The file can be downloaded with `DownloadFile/download`.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.LayersExportBySelectionParameter() # LayersExportBySelectionParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Exports the map's selection in Excel format. The file can be downloaded with `DownloadFile/download`.
    api_response = api_instance.map_export_map_data_by_selection(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_export_map_data_by_selection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayersExportBySelectionParameter**](LayersExportBySelectionParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_export_map_elements**
> str map_export_map_elements(selected_language, tenant_url_code)

Exports an Excel sheet of all the maps. The file can be downloaded with `DownloadFile/download`. The language is used to localized the sheet's name and columns.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
selected_language = 'selected_language_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Exports an Excel sheet of all the maps. The file can be downloaded with `DownloadFile/download`. The language is used to localized the sheet's name and columns.
    api_response = api_instance.map_export_map_elements(selected_language, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_export_map_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selected_language** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_data_tables_by_map**
> list[DataTable] map_get_data_tables_by_map(map_id, tenant_url_code)

Gets the tables used by this map.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the tables used by this map.
    api_response = api_instance.map_get_data_tables_by_map(map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_get_data_tables_by_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[DataTable]**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_grid_layers_by_map**
> list[GridLayer] map_get_grid_layers_by_map(map_id, tenant_url_code)

Gets the list of grid layers used in a map.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | Map id or a friendly identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the list of grid layers used in a map.
    api_response = api_instance.map_get_grid_layers_by_map(map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_get_grid_layers_by_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| Map id or a friendly identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[GridLayer]**](GridLayer.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_keywords**
> list[KeywordDTO] map_get_keywords(tenant_url_code)

Gets the map's keywords.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the map's keywords.
    api_response = api_instance.map_get_keywords(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_get_keywords: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**list[KeywordDTO]**](KeywordDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_layers_by_map**
> list[Layer] map_get_layers_by_map(map_id, tenant_url_code)

Gets the list of Layers used in a map.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | Map id or a friendly identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the list of Layers used in a map.
    api_response = api_instance.map_get_layers_by_map(map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_get_layers_by_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| Map id or a friendly identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Layer]**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_map**
> Map map_get_map(map_id, tenant_url_code)

Get a map based on the map id or a friendly identifier.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | Map id or a friendly identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Get a map based on the map id or a friendly identifier.
    api_response = api_instance.map_get_map(map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_get_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| Map id or a friendly identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Map**](Map.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_map_advanced_settings**
> MapAdvancedSettings map_get_map_advanced_settings(map_identifier, tenant_url_code)

Gets the map's advanced settings.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the map's advanced settings.
    api_response = api_instance.map_get_map_advanced_settings(map_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_get_map_advanced_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MapAdvancedSettings**](MapAdvancedSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_map_for_viewer**
> MapWithViewerInformation map_get_map_for_viewer(map_identifier, tenant_url_code)

Gets all the data required to open a map.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the data required to open a map.
    api_response = api_instance.map_get_map_for_viewer(map_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_get_map_for_viewer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MapWithViewerInformation**](MapWithViewerInformation.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_map_toolbar**
> MapToolbar map_get_map_toolbar(map_identifier, tenant_url_code)

Gets the map's toolbar settings.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the map's toolbar settings.
    api_response = api_instance.map_get_map_toolbar(map_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_get_map_toolbar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MapToolbar**](MapToolbar.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_map_with_details**
> MapWithDetails map_get_map_with_details(map_identifier, tenant_url_code)

Gets the map, its tables and its layers.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the map, its tables and its layers.
    api_response = api_instance.map_get_map_with_details(map_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_get_map_with_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MapWithDetails**](MapWithDetails.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_maps**
> list[Map] map_get_maps(tenant_url_code)

Get all maps the requesting user has access to.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Get all maps the requesting user has access to.
    api_response = api_instance.map_get_maps(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_get_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Map]**](Map.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_maps_content**
> MapElements map_get_maps_content(body, tenant_url_code)

Gets all the maps and folders the user has access to in a specific folder. If the folder id is omitted, the root folder is used.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetMapsContentParam() # GetMapsContentParam | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the maps and folders the user has access to in a specific folder. If the folder id is omitted, the root folder is used.
    api_response = api_instance.map_get_maps_content(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_get_maps_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetMapsContentParam**](GetMapsContentParam.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MapElements**](MapElements.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_slides**
> list[Slide] map_get_slides(map_identifier, tenant_url_code)

Gets the map's slides.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the map's slides.
    api_response = api_instance.map_get_slides(map_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_get_slides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Slide]**](Slide.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_move_map_layer**
> map_move_map_layer(body, map_identifier, tenant_url_code)

Reorders the map's layers.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.MoveMapLayerParameter() # MoveMapLayerParameter | 
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Reorders the map's layers.
    api_instance.map_move_map_layer(body, map_identifier, tenant_url_code)
except ApiException as e:
    print("Exception when calling MapApi->map_move_map_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoveMapLayerParameter**](MoveMapLayerParameter.md)|  | 
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_run_map_action**
> map_run_map_action(body, map_action_id, map_identifier, tenant_url_code)

Runs a map action.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = NULL # dict(str, str) | 
map_action_id = 'map_action_id_example' # str | 
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Runs a map action.
    api_instance.map_run_map_action(body, map_action_id, map_identifier, tenant_url_code)
except ApiException as e:
    print("Exception when calling MapApi->map_run_map_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, str)**](dict.md)|  | 
 **map_action_id** | **str**|  | 
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_save_default_map_print_layout**
> map_save_default_map_print_layout(body, tenant_url_code)

Updates the default print layout.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreatePrintLayoutParameter() # CreatePrintLayoutParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the default print layout.
    api_instance.map_save_default_map_print_layout(body, tenant_url_code)
except ApiException as e:
    print("Exception when calling MapApi->map_save_default_map_print_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePrintLayoutParameter**](CreatePrintLayoutParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_save_map_print_layout**
> map_save_map_print_layout(body, map_identifier, tenant_url_code)

Updates the map's print layout.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreatePrintLayoutParameter() # CreatePrintLayoutParameter | 
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the map's print layout.
    api_instance.map_save_map_print_layout(body, map_identifier, tenant_url_code)
except ApiException as e:
    print("Exception when calling MapApi->map_save_map_print_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePrintLayoutParameter**](CreatePrintLayoutParameter.md)|  | 
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_search_map**
> MapSearchResults map_search_map(body, map_identifier, tenant_url_code)

Searches for a match in the searchable columns of the map's layers and geocoded addresses.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.SearchMapParameter() # SearchMapParameter | 
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Searches for a match in the searchable columns of the map's layers and geocoded addresses.
    api_response = api_instance.map_search_map(body, map_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_search_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchMapParameter**](SearchMapParameter.md)|  | 
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MapSearchResults**](MapSearchResults.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_search_map_layer**
> LayerSearchResult map_search_map_layer(body, map_identifier, layer_identifier, tenant_url_code)

Searches for a match in the searchable columns of the map's layers.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.SearchMapLayerParameter() # SearchMapLayerParameter | 
map_identifier = 'map_identifier_example' # str | 
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Searches for a match in the searchable columns of the map's layers.
    api_response = api_instance.map_search_map_layer(body, map_identifier, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_search_map_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchMapLayerParameter**](SearchMapLayerParameter.md)|  | 
 **map_identifier** | **str**|  | 
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerSearchResult**](LayerSearchResult.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_share_map**
> Map map_share_map(body, map_identifier, tenant_url_code)

Shares the map with internal users.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ShareMapParameter() # ShareMapParameter | 
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Shares the map with internal users.
    api_response = api_instance.map_share_map(body, map_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_share_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShareMapParameter**](ShareMapParameter.md)|  | 
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Map**](Map.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_share_map_external**
> Map map_share_map_external(body, map_identifier, tenant_url_code)

Shares the map with external users. The map is set to public.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ShareMapExternalParameter() # ShareMapExternalParameter | 
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Shares the map with external users. The map is set to public.
    api_response = api_instance.map_share_map_external(body, map_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_share_map_external: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShareMapExternalParameter**](ShareMapExternalParameter.md)|  | 
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Map**](Map.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_update_map**
> Map map_update_map(body, map_id, tenant_url_code)

Updates a map properties based on the given parameters.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.MapUpdateParameter() # MapUpdateParameter | Parameters used to update the map.
map_id = 'map_id_example' # str | Map id or a friendly identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a map properties based on the given parameters.
    api_response = api_instance.map_update_map(body, map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_update_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MapUpdateParameter**](MapUpdateParameter.md)| Parameters used to update the map. | 
 **map_id** | **str**| Map id or a friendly identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Map**](Map.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_update_map_advanced_settings**
> MapAdvancedSettings map_update_map_advanced_settings(body, map_identifier, tenant_url_code)

Updates the map's advanced settings.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.MapAdvancedSettings() # MapAdvancedSettings | 
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the map's advanced settings.
    api_response = api_instance.map_update_map_advanced_settings(body, map_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_update_map_advanced_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MapAdvancedSettings**](MapAdvancedSettings.md)|  | 
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MapAdvancedSettings**](MapAdvancedSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_update_map_identifier**
> Map map_update_map_identifier(body, map_identifier, tenant_url_code)

Updates the map identifier.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = 'body_example' # str | 
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the map identifier.
    api_response = api_instance.map_update_map_identifier(body, map_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_update_map_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Map**](Map.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_update_map_layers**
> MapLayersResponse map_update_map_layers(body, map_id, tenant_url_code)

Updates a dynamic map's layers. The map will lose the associations with previous layers that are not included in the list.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = [cartovista_cloud_clients.MapLayerParameter()] # list[MapLayerParameter] | 
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a dynamic map's layers. The map will lose the associations with previous layers that are not included in the list.
    api_response = api_instance.map_update_map_layers(body, map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_update_map_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MapLayerParameter]**](MapLayerParameter.md)|  | 
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MapLayersResponse**](MapLayersResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_update_map_toolbar**
> MapToolbar map_update_map_toolbar(body, map_identifier, tenant_url_code)

Updates the map's toolbar settings.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.MapToolbar() # MapToolbar | 
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the map's toolbar settings.
    api_response = api_instance.map_update_map_toolbar(body, map_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_update_map_toolbar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MapToolbar**](MapToolbar.md)|  | 
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MapToolbar**](MapToolbar.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_update_thumbnail**
> Map map_update_thumbnail(map_identifier, tenant_url_code, file=file)

Updates the map thumbnail.

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
api_instance = cartovista_cloud_clients.MapApi(cartovista_cloud_clients.ApiClient(configuration))
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Updates the map thumbnail.
    api_response = api_instance.map_update_thumbnail(map_identifier, tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapApi->map_update_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**Map**](Map.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


