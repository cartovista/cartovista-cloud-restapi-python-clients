# cartovista_cloud_clients.LayerSettingsApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**layer_settings_get_default_layer_settings**](LayerSettingsApi.md#layer_settings_get_default_layer_settings) | **GET** /{tenantUrlCode}/api/v2/layerSettings/{layerId}/default | Gets the default settings for the layer.
[**layer_settings_get_layer_settings**](LayerSettingsApi.md#layer_settings_get_layer_settings) | **GET** /{tenantUrlCode}/api/v2/layerSettings/{layerSettingsId} | Gets a specific layer settings.
[**layer_settings_get_map_layer_settings**](LayerSettingsApi.md#layer_settings_get_map_layer_settings) | **GET** /{tenantUrlCode}/api/v2/layerSettings/{layerSettingsId}/map/{mapId} | Gets the layer settings for a specific map.
[**layer_settings_update_alias**](LayerSettingsApi.md#layer_settings_update_alias) | **PATCH** /{tenantUrlCode}/api/v2/layerSettings/{layerSettingsId}/alias | Updates the layer settings&#x27; alias.
[**layer_settings_update_effect**](LayerSettingsApi.md#layer_settings_update_effect) | **PATCH** /{tenantUrlCode}/api/v2/layerSettings/{layerSettingsId}/effects | Updates the layer settings&#x27; effects.
[**layer_settings_update_general**](LayerSettingsApi.md#layer_settings_update_general) | **PATCH** /{tenantUrlCode}/api/v2/layerSettings/{layerSettingsId}/general | Updates the layer settings&#x27; general settings.
[**layer_settings_update_geometry_style**](LayerSettingsApi.md#layer_settings_update_geometry_style) | **PATCH** /{tenantUrlCode}/api/v2/layerSettings/{layerSettingsId}/geometryStyle | Updates the layer settings&#x27; geometry style. The style object must match the layer&#x27;s geometry type.
[**layer_settings_update_interactivity**](LayerSettingsApi.md#layer_settings_update_interactivity) | **PATCH** /{tenantUrlCode}/api/v2/layerSettings/{layerSettingsId}/interactivity | Updates the layer settings&#x27; interactivity settings.
[**layer_settings_update_label**](LayerSettingsApi.md#layer_settings_update_label) | **PATCH** /{tenantUrlCode}/api/v2/layerSettings/{layerSettingsId}/label | Updates the layer settings&#x27; label settings.
[**layer_settings_update_rendering**](LayerSettingsApi.md#layer_settings_update_rendering) | **PATCH** /{tenantUrlCode}/api/v2/layerSettings/{layerSettingsId}/rendering | Updates the layer settings&#x27; rendering settings.
[**layer_settings_update_visibility_ranges**](LayerSettingsApi.md#layer_settings_update_visibility_ranges) | **PATCH** /{tenantUrlCode}/api/v2/layerSettings/{layerSettingsId}/visibility-ranges | Updates the layer settings&#x27; visibility ranges.

# **layer_settings_get_default_layer_settings**
> LayerSettings layer_settings_get_default_layer_settings(layer_id, tenant_url_code)

Gets the default settings for the layer.

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
api_instance = cartovista_cloud_clients.LayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
layer_id = 'layer_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the default settings for the layer.
    api_response = api_instance.layer_settings_get_default_layer_settings(layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerSettingsApi->layer_settings_get_default_layer_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerSettings**](LayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_settings_get_layer_settings**
> LayerSettings layer_settings_get_layer_settings(layer_settings_id, tenant_url_code)

Gets a specific layer settings.

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
api_instance = cartovista_cloud_clients.LayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
layer_settings_id = 'layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific layer settings.
    api_response = api_instance.layer_settings_get_layer_settings(layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerSettingsApi->layer_settings_get_layer_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerSettings**](LayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_settings_get_map_layer_settings**
> LayerSettings layer_settings_get_map_layer_settings(map_id, layer_settings_id, tenant_url_code)

Gets the layer settings for a specific map.

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
api_instance = cartovista_cloud_clients.LayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | 
layer_settings_id = 'layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the layer settings for a specific map.
    api_response = api_instance.layer_settings_get_map_layer_settings(map_id, layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerSettingsApi->layer_settings_get_map_layer_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerSettings**](LayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_settings_update_alias**
> LayerSettings layer_settings_update_alias(body, layer_settings_id, tenant_url_code)

Updates the layer settings' alias.

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
api_instance = cartovista_cloud_clients.LayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateAliasParameter2() # UpdateAliasParameter2 | 
layer_settings_id = 'layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the layer settings' alias.
    api_response = api_instance.layer_settings_update_alias(body, layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerSettingsApi->layer_settings_update_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAliasParameter2**](UpdateAliasParameter2.md)|  | 
 **layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerSettings**](LayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_settings_update_effect**
> LayerSettings layer_settings_update_effect(body, layer_settings_id, tenant_url_code)

Updates the layer settings' effects.

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
api_instance = cartovista_cloud_clients.LayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.LayerSettingsEffects() # LayerSettingsEffects | 
layer_settings_id = 'layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the layer settings' effects.
    api_response = api_instance.layer_settings_update_effect(body, layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerSettingsApi->layer_settings_update_effect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayerSettingsEffects**](LayerSettingsEffects.md)|  | 
 **layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerSettings**](LayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_settings_update_general**
> LayerSettings layer_settings_update_general(body, layer_settings_id, tenant_url_code)

Updates the layer settings' general settings.

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
api_instance = cartovista_cloud_clients.LayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.LayerSettingsGeneral() # LayerSettingsGeneral | 
layer_settings_id = 'layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the layer settings' general settings.
    api_response = api_instance.layer_settings_update_general(body, layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerSettingsApi->layer_settings_update_general: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayerSettingsGeneral**](LayerSettingsGeneral.md)|  | 
 **layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerSettings**](LayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_settings_update_geometry_style**
> LayerSettings layer_settings_update_geometry_style(body, layer_settings_id, tenant_url_code)

Updates the layer settings' geometry style. The style object must match the layer's geometry type.

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
api_instance = cartovista_cloud_clients.LayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
body = NULL # object | 
layer_settings_id = 'layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the layer settings' geometry style. The style object must match the layer's geometry type.
    api_response = api_instance.layer_settings_update_geometry_style(body, layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerSettingsApi->layer_settings_update_geometry_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerSettings**](LayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_settings_update_interactivity**
> LayerSettings layer_settings_update_interactivity(body, layer_settings_id, tenant_url_code)

Updates the layer settings' interactivity settings.

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
api_instance = cartovista_cloud_clients.LayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.LayerSettingsInteractivity() # LayerSettingsInteractivity | 
layer_settings_id = 'layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the layer settings' interactivity settings.
    api_response = api_instance.layer_settings_update_interactivity(body, layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerSettingsApi->layer_settings_update_interactivity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayerSettingsInteractivity**](LayerSettingsInteractivity.md)|  | 
 **layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerSettings**](LayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_settings_update_label**
> LayerSettings layer_settings_update_label(body, layer_settings_id, tenant_url_code)

Updates the layer settings' label settings.

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
api_instance = cartovista_cloud_clients.LayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.LayerSettingsLabel() # LayerSettingsLabel | 
layer_settings_id = 'layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the layer settings' label settings.
    api_response = api_instance.layer_settings_update_label(body, layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerSettingsApi->layer_settings_update_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayerSettingsLabel**](LayerSettingsLabel.md)|  | 
 **layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerSettings**](LayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_settings_update_rendering**
> LayerSettings layer_settings_update_rendering(body, layer_settings_id, tenant_url_code)

Updates the layer settings' rendering settings.

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
api_instance = cartovista_cloud_clients.LayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.LayerSettingsRendering() # LayerSettingsRendering | 
layer_settings_id = 'layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the layer settings' rendering settings.
    api_response = api_instance.layer_settings_update_rendering(body, layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerSettingsApi->layer_settings_update_rendering: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayerSettingsRendering**](LayerSettingsRendering.md)|  | 
 **layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerSettings**](LayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_settings_update_visibility_ranges**
> LayerSettings layer_settings_update_visibility_ranges(body, layer_settings_id, tenant_url_code)

Updates the layer settings' visibility ranges.

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
api_instance = cartovista_cloud_clients.LayerSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.LayerSettingsVisibilityRanges() # LayerSettingsVisibilityRanges | 
layer_settings_id = 'layer_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the layer settings' visibility ranges.
    api_response = api_instance.layer_settings_update_visibility_ranges(body, layer_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerSettingsApi->layer_settings_update_visibility_ranges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayerSettingsVisibilityRanges**](LayerSettingsVisibilityRanges.md)|  | 
 **layer_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerSettings**](LayerSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

