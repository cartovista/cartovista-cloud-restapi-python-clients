# cartovista_cloud_clients.PoiAnalysisApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poi_analysis_create_custom_poi_analysis**](PoiAnalysisApi.md#poi_analysis_create_custom_poi_analysis) | **POST** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/analysis | Creates a new custom analysis.
[**poi_analysis_create_poi_analysis**](PoiAnalysisApi.md#poi_analysis_create_poi_analysis) | **POST** /{tenantUrlCode}/api/v2/poi-analysis/{mapId} | Creates a POI analysis for the map.
[**poi_analysis_delete_custom_poi_analysis**](PoiAnalysisApi.md#poi_analysis_delete_custom_poi_analysis) | **DELETE** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/analysis/{analysisId} | Deletes a custom analysis.
[**poi_analysis_get_poi_analysis**](PoiAnalysisApi.md#poi_analysis_get_poi_analysis) | **GET** /{tenantUrlCode}/api/v2/poi-analysis/{mapId} | Gets the POI analysis used by the map.
[**poi_analysis_get_poi_analysis_data**](PoiAnalysisApi.md#poi_analysis_get_poi_analysis_data) | **GET** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/analysis/{analysisId}/data | Gets the data computed for the custom analysis.
[**poi_analysis_get_poi_analysis_settings**](PoiAnalysisApi.md#poi_analysis_get_poi_analysis_settings) | **GET** /{tenantUrlCode}/api/v2/poi-analysis/settings | Gets the usable options to create a new POI analysis.
[**poi_analysis_pregenerate_rasters**](PoiAnalysisApi.md#poi_analysis_pregenerate_rasters) | **GET** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/pregenerate | Generates all the missing raster for each scenario, year and kV level.
[**poi_analysis_toggle_default_analysis**](PoiAnalysisApi.md#poi_analysis_toggle_default_analysis) | **PATCH** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/analysis/{analysisId}/default | Toggles the default value of the custom analysis.

# **poi_analysis_create_custom_poi_analysis**
> CustomPoiAnalysisWithNewId poi_analysis_create_custom_poi_analysis(body, map_id, tenant_url_code)

Creates a new custom analysis.

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
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreateCustomPoiAnalysisParameter() # CreateCustomPoiAnalysisParameter | 
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a new custom analysis.
    api_response = api_instance.poi_analysis_create_custom_poi_analysis(body, map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_create_custom_poi_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustomPoiAnalysisParameter**](CreateCustomPoiAnalysisParameter.md)|  | 
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**CustomPoiAnalysisWithNewId**](CustomPoiAnalysisWithNewId.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_create_poi_analysis**
> poi_analysis_create_poi_analysis(body, map_id, tenant_url_code)

Creates a POI analysis for the map.

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
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreatePoiAnalysisParameter() # CreatePoiAnalysisParameter | 
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a POI analysis for the map.
    api_instance.poi_analysis_create_poi_analysis(body, map_id, tenant_url_code)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_create_poi_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePoiAnalysisParameter**](CreatePoiAnalysisParameter.md)|  | 
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_delete_custom_poi_analysis**
> list[CustomPoiAnalysis] poi_analysis_delete_custom_poi_analysis(map_id, analysis_id, tenant_url_code)

Deletes a custom analysis.

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
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | 
analysis_id = 'analysis_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes a custom analysis.
    api_response = api_instance.poi_analysis_delete_custom_poi_analysis(map_id, analysis_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_delete_custom_poi_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **analysis_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[CustomPoiAnalysis]**](CustomPoiAnalysis.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_get_poi_analysis**
> PoiAnalysis poi_analysis_get_poi_analysis(map_id, tenant_url_code)

Gets the POI analysis used by the map.

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
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the POI analysis used by the map.
    api_response = api_instance.poi_analysis_get_poi_analysis(map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_get_poi_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**PoiAnalysis**](PoiAnalysis.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_get_poi_analysis_data**
> list[PoiAnalysisData] poi_analysis_get_poi_analysis_data(map_id, analysis_id, tenant_url_code)

Gets the data computed for the custom analysis.

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
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | 
analysis_id = 'analysis_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the data computed for the custom analysis.
    api_response = api_instance.poi_analysis_get_poi_analysis_data(map_id, analysis_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_get_poi_analysis_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **analysis_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[PoiAnalysisData]**](PoiAnalysisData.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_get_poi_analysis_settings**
> PoiAnalysisSettings poi_analysis_get_poi_analysis_settings(tenant_url_code)

Gets the usable options to create a new POI analysis.

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
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the usable options to create a new POI analysis.
    api_response = api_instance.poi_analysis_get_poi_analysis_settings(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_get_poi_analysis_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**PoiAnalysisSettings**](PoiAnalysisSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_pregenerate_rasters**
> poi_analysis_pregenerate_rasters(map_id, tenant_url_code)

Generates all the missing raster for each scenario, year and kV level.

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
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Generates all the missing raster for each scenario, year and kV level.
    api_instance.poi_analysis_pregenerate_rasters(map_id, tenant_url_code)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_pregenerate_rasters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_toggle_default_analysis**
> list[CustomPoiAnalysis] poi_analysis_toggle_default_analysis(body, map_id, analysis_id, tenant_url_code)

Toggles the default value of the custom analysis.

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
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
body = True # bool | 
map_id = 'map_id_example' # str | 
analysis_id = 'analysis_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Toggles the default value of the custom analysis.
    api_response = api_instance.poi_analysis_toggle_default_analysis(body, map_id, analysis_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_toggle_default_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**bool**](bool.md)|  | 
 **map_id** | **str**|  | 
 **analysis_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[CustomPoiAnalysis]**](CustomPoiAnalysis.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


