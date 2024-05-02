# cartovista_cloud_clients.GridLayerSettingsApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_layer_settings_get_default_grid_layer_settings**](GridLayerSettingsApi.md#grid_layer_settings_get_default_grid_layer_settings) | **GET** /{tenantUrlCode}/api/v2/gridLayerSettings/{gridLayerId}/default | Gets the default settings for the grid layer.
[**grid_layer_settings_get_grid_layer_settings**](GridLayerSettingsApi.md#grid_layer_settings_get_grid_layer_settings) | **GET** /{tenantUrlCode}/api/v2/gridLayerSettings/{gridLayerSettingsId} | Gets a specific grid layer settings.
[**grid_layer_settings_get_map_grid_layer_settings**](GridLayerSettingsApi.md#grid_layer_settings_get_map_grid_layer_settings) | **GET** /{tenantUrlCode}/api/v2/gridLayerSettings/{gridLayerSettingsId}/map/{mapId} | Gets the grid layer&#x27;s settings for a specific map.
[**grid_layer_settings_update_alias**](GridLayerSettingsApi.md#grid_layer_settings_update_alias) | **PATCH** /{tenantUrlCode}/api/v2/gridLayerSettings/{gridLayerSettingsId}/alias | Updates the grid layer settings&#x27; alias.
[**grid_layer_settings_update_rendering**](GridLayerSettingsApi.md#grid_layer_settings_update_rendering) | **PATCH** /{tenantUrlCode}/api/v2/gridLayerSettings/{gridLayerSettingsId}/rendering | Updates the grid layer settings&#x27; rendering settings.
[**grid_layer_settings_update_style**](GridLayerSettingsApi.md#grid_layer_settings_update_style) | **PATCH** /{tenantUrlCode}/api/v2/gridLayerSettings/{gridLayerSettingsId}/style | Updates the grid layer settings&#x27; style.
[**grid_layer_settings_update_visibility_ranges**](GridLayerSettingsApi.md#grid_layer_settings_update_visibility_ranges) | **PATCH** /{tenantUrlCode}/api/v2/gridLayerSettings/{gridLayerSettingsId}/visibility-ranges | Updates the grid layer settings&#x27; visibility ranges.

# **grid_layer_settings_get_default_grid_layer_settings**
> GridLayerSettings grid_layer_settings_get_default_grid_layer_settings(grid_layer_id, tenant_url_code)

Gets the default settings for the grid layer.

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
api_instance = cartovista_cloud_clients.GridLayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
grid_layer_id = 'grid_layer_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the default settings for the grid layer.
    api_response = api_instance.grid_layer_settings_get_default_grid_layer_settings(grid_layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerSettingsApi->grid_layer_settings_get_default_grid_layer_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_layer_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GridLayerSettings**](GridLayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_settings_get_grid_layer_settings**
> GridLayerSettings grid_layer_settings_get_grid_layer_settings(grid_layer_settings_id, tenant_url_code)

Gets a specific grid layer settings.

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
api_instance = cartovista_cloud_clients.GridLayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
grid_layer_settings_id = 'grid_layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific grid layer settings.
    api_response = api_instance.grid_layer_settings_get_grid_layer_settings(grid_layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerSettingsApi->grid_layer_settings_get_grid_layer_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GridLayerSettings**](GridLayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_settings_get_map_grid_layer_settings**
> GridLayerSettings grid_layer_settings_get_map_grid_layer_settings(map_id, grid_layer_id, tenant_url_code, grid_layer_settings_id)

Gets the grid layer's settings for a specific map.

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
api_instance = cartovista_cloud_clients.GridLayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | 
grid_layer_id = 'grid_layer_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 
grid_layer_settings_id = 'grid_layer_settings_id_example' # str | 

try:
    # Gets the grid layer's settings for a specific map.
    api_response = api_instance.grid_layer_settings_get_map_grid_layer_settings(map_id, grid_layer_id, tenant_url_code, grid_layer_settings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerSettingsApi->grid_layer_settings_get_map_grid_layer_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **grid_layer_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 
 **grid_layer_settings_id** | **str**|  | 

### Return type

[**GridLayerSettings**](GridLayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_settings_update_alias**
> GridLayerSettings grid_layer_settings_update_alias(body, grid_layer_settings_id, tenant_url_code)

Updates the grid layer settings' alias.

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
api_instance = cartovista_cloud_clients.GridLayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateAliasParameter() # UpdateAliasParameter | 
grid_layer_settings_id = 'grid_layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the grid layer settings' alias.
    api_response = api_instance.grid_layer_settings_update_alias(body, grid_layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerSettingsApi->grid_layer_settings_update_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAliasParameter**](UpdateAliasParameter.md)|  | 
 **grid_layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GridLayerSettings**](GridLayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_settings_update_rendering**
> GridLayerSettings grid_layer_settings_update_rendering(body, grid_layer_settings_id, tenant_url_code)

Updates the grid layer settings' rendering settings.

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
api_instance = cartovista_cloud_clients.GridLayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.LayerSettingsRendering() # LayerSettingsRendering | 
grid_layer_settings_id = 'grid_layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the grid layer settings' rendering settings.
    api_response = api_instance.grid_layer_settings_update_rendering(body, grid_layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerSettingsApi->grid_layer_settings_update_rendering: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayerSettingsRendering**](LayerSettingsRendering.md)|  | 
 **grid_layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GridLayerSettings**](GridLayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_settings_update_style**
> GridLayerSettings grid_layer_settings_update_style(body, grid_layer_settings_id, tenant_url_code)

Updates the grid layer settings' style.

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
api_instance = cartovista_cloud_clients.GridLayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
body = NULL # object | 
grid_layer_settings_id = 'grid_layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the grid layer settings' style.
    api_response = api_instance.grid_layer_settings_update_style(body, grid_layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerSettingsApi->grid_layer_settings_update_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **grid_layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GridLayerSettings**](GridLayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_layer_settings_update_visibility_ranges**
> GridLayerSettings grid_layer_settings_update_visibility_ranges(body, grid_layer_settings_id, tenant_url_code)

Updates the grid layer settings' visibility ranges.

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
api_instance = cartovista_cloud_clients.GridLayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GridLayerSettingsVisibilityRanges() # GridLayerSettingsVisibilityRanges | 
grid_layer_settings_id = 'grid_layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the grid layer settings' visibility ranges.
    api_response = api_instance.grid_layer_settings_update_visibility_ranges(body, grid_layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridLayerSettingsApi->grid_layer_settings_update_visibility_ranges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GridLayerSettingsVisibilityRanges**](GridLayerSettingsVisibilityRanges.md)|  | 
 **grid_layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GridLayerSettings**](GridLayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

