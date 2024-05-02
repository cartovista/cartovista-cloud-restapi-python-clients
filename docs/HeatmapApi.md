# cartovista_cloud_clients.HeatmapApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heatmap_generate_heatmap**](HeatmapApi.md#heatmap_generate_heatmap) | **POST** /{tenantUrlCode}/api/v2/heatmap/{layerIdentifier} | Generates a new heatmap for the layer.
[**heatmap_get_heatmap_settings**](HeatmapApi.md#heatmap_get_heatmap_settings) | **GET** /{tenantUrlCode}/api/v2/heatmap/{layerIdentifier} | Gets the parameters used to create the heatmap from the layer.
[**heatmap_get_heatmap_settings_details**](HeatmapApi.md#heatmap_get_heatmap_settings_details) | **GET** /{tenantUrlCode}/api/v2/heatmap/{layerIdentifier}/details | 
[**heatmap_update_heatmap**](HeatmapApi.md#heatmap_update_heatmap) | **PATCH** /{tenantUrlCode}/api/v2/heatmap/{layerIdentifier} | Regenerates an existing heatmap and updates its settings.

# **heatmap_generate_heatmap**
> heatmap_generate_heatmap(body, layer_identifier, tenant_url_code)

Generates a new heatmap for the layer.

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
api_instance = cartovista_cloud_clients.HeatmapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GenerateHeatmapParameter() # GenerateHeatmapParameter | 
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Generates a new heatmap for the layer.
    api_instance.heatmap_generate_heatmap(body, layer_identifier, tenant_url_code)
except ApiException as e:
    print("Exception when calling HeatmapApi->heatmap_generate_heatmap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateHeatmapParameter**](GenerateHeatmapParameter.md)|  | 
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heatmap_get_heatmap_settings**
> HeatmapSettings heatmap_get_heatmap_settings(layer_identifier, tenant_url_code)

Gets the parameters used to create the heatmap from the layer.

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
api_instance = cartovista_cloud_clients.HeatmapApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the parameters used to create the heatmap from the layer.
    api_response = api_instance.heatmap_get_heatmap_settings(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeatmapApi->heatmap_get_heatmap_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**HeatmapSettings**](HeatmapSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heatmap_get_heatmap_settings_details**
> HeatmapSettingsDetails heatmap_get_heatmap_settings_details(layer_identifier, tenant_url_code)



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
api_instance = cartovista_cloud_clients.HeatmapApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.heatmap_get_heatmap_settings_details(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeatmapApi->heatmap_get_heatmap_settings_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**HeatmapSettingsDetails**](HeatmapSettingsDetails.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heatmap_update_heatmap**
> heatmap_update_heatmap(body, layer_identifier, tenant_url_code)

Regenerates an existing heatmap and updates its settings.

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
api_instance = cartovista_cloud_clients.HeatmapApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateHeatmapParameter() # UpdateHeatmapParameter | 
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Regenerates an existing heatmap and updates its settings.
    api_instance.heatmap_update_heatmap(body, layer_identifier, tenant_url_code)
except ApiException as e:
    print("Exception when calling HeatmapApi->heatmap_update_heatmap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateHeatmapParameter**](UpdateHeatmapParameter.md)|  | 
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

