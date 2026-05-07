# cartovista_cloud_clients.PoiAnalysisApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poi_analysis_create_custom_poi_analysis**](PoiAnalysisApi.md#poi_analysis_create_custom_poi_analysis) | **POST** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/analysis | Creates a new custom analysis.
[**poi_analysis_create_poi_analysis**](PoiAnalysisApi.md#poi_analysis_create_poi_analysis) | **POST** /{tenantUrlCode}/api/v2/poi-analysis/{mapId} | Creates a POI analysis for the map.
[**poi_analysis_delete_custom_poi_analysis**](PoiAnalysisApi.md#poi_analysis_delete_custom_poi_analysis) | **DELETE** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/analysis/{analysisId} | Deletes a custom analysis.
[**poi_analysis_fix_column**](PoiAnalysisApi.md#poi_analysis_fix_column) | **PATCH** /{tenantUrlCode}/api/v2/poi-analysis/{dataElementId}/fix-column/{columnId} | Updates the data column so it matches the name (if FixName is true) and type (if FixType is true) of the given POI Column.
[**poi_analysis_get_contingency_loading_max_data**](PoiAnalysisApi.md#poi_analysis_get_contingency_loading_max_data) | **GET** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/contingency-loading-max/{scenarioId} | 
[**poi_analysis_get_harmers**](PoiAnalysisApi.md#poi_analysis_get_harmers) | **POST** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/harmers | 
[**poi_analysis_get_poi_analysis**](PoiAnalysisApi.md#poi_analysis_get_poi_analysis) | **GET** /{tenantUrlCode}/api/v2/poi-analysis/{mapId} | Gets the POI analysis used by the map.
[**poi_analysis_get_poi_analysis_data**](PoiAnalysisApi.md#poi_analysis_get_poi_analysis_data) | **GET** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/analysis/{analysisId}/data | Gets the data computed for the custom analysis.
[**poi_analysis_get_poi_analysis_settings**](PoiAnalysisApi.md#poi_analysis_get_poi_analysis_settings) | **GET** /{tenantUrlCode}/api/v2/poi-analysis/settings | Gets the usable options to create a new POI analysis.
[**poi_analysis_get_poi_settings_poi_tables**](PoiAnalysisApi.md#poi_analysis_get_poi_settings_poi_tables) | **GET** /{tenantUrlCode}/api/v2/poi-analysis/updateSettings | Gets the new dropdown table options after a table was linked when creating a new POI analysis.
[**poi_analysis_get_temporary_poi_analysis_data**](PoiAnalysisApi.md#poi_analysis_get_temporary_poi_analysis_data) | **POST** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/analysis/data | Gets the data computed for the custom analysis.
[**poi_analysis_get_temporary_poi_analysis_mask**](PoiAnalysisApi.md#poi_analysis_get_temporary_poi_analysis_mask) | **POST** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/analysis/mask | 
[**poi_analysis_pregenerate_rasters**](PoiAnalysisApi.md#poi_analysis_pregenerate_rasters) | **GET** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/pregenerate | Generates all the missing raster for each scenario, year and kV level.
[**poi_analysis_regenerate_rasters**](PoiAnalysisApi.md#poi_analysis_regenerate_rasters) | **GET** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/regenerate | Regenerate all rasters of the poi associated with the map.
[**poi_analysis_toggle_default_analysis**](PoiAnalysisApi.md#poi_analysis_toggle_default_analysis) | **PATCH** /{tenantUrlCode}/api/v2/poi-analysis/{mapId}/analysis/{analysisId}/default | Toggles the default value of the custom analysis.
[**poi_analysis_validate_data_for_poi**](PoiAnalysisApi.md#poi_analysis_validate_data_for_poi) | **GET** /{tenantUrlCode}/api/v2/poi-analysis/{dataId}/validate-data | Get the errors, if any, of a layer or datatable for a given type.

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

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

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

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

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

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_fix_column**
> DataColumn poi_analysis_fix_column(body, data_element_id, column_id, tenant_url_code)

Updates the data column so it matches the name (if FixName is true) and type (if FixType is true) of the given POI Column.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.FixPoiColumnParameter() # FixPoiColumnParameter | 
data_element_id = 'data_element_id_example' # str | 
column_id = 'column_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the data column so it matches the name (if FixName is true) and type (if FixType is true) of the given POI Column.
    api_response = api_instance.poi_analysis_fix_column(body, data_element_id, column_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_fix_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FixPoiColumnParameter**](FixPoiColumnParameter.md)|  | 
 **data_element_id** | **str**|  | 
 **column_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataColumn**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_get_contingency_loading_max_data**
> PoiContingencyLoadingMaxData poi_analysis_get_contingency_loading_max_data(map_id, scenario_id, tenant_url_code)



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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | 
scenario_id = 'scenario_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.poi_analysis_get_contingency_loading_max_data(map_id, scenario_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_get_contingency_loading_max_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **scenario_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**PoiContingencyLoadingMaxData**](PoiContingencyLoadingMaxData.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_get_harmers**
> list[PoiHarmerData] poi_analysis_get_harmers(body, map_id, tenant_url_code)



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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
body = 'body_example' # str | 
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.poi_analysis_get_harmers(body, map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_get_harmers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[PoiHarmerData]**](PoiHarmerData.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
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

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

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

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

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

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_get_poi_settings_poi_tables**
> dict(str, list[PoiSourceTable]) poi_analysis_get_poi_settings_poi_tables(tenant_url_code)

Gets the new dropdown table options after a table was linked when creating a new POI analysis.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the new dropdown table options after a table was linked when creating a new POI analysis.
    api_response = api_instance.poi_analysis_get_poi_settings_poi_tables(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_get_poi_settings_poi_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

**dict(str, list[PoiSourceTable])**

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_get_temporary_poi_analysis_data**
> list[PoiAnalysisData] poi_analysis_get_temporary_poi_analysis_data(body, map_id, tenant_url_code)

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.TemporaryAnalysisData() # TemporaryAnalysisData | 
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the data computed for the custom analysis.
    api_response = api_instance.poi_analysis_get_temporary_poi_analysis_data(body, map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_get_temporary_poi_analysis_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemporaryAnalysisData**](TemporaryAnalysisData.md)|  | 
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[PoiAnalysisData]**](PoiAnalysisData.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_get_temporary_poi_analysis_mask**
> str poi_analysis_get_temporary_poi_analysis_mask(body, map_id, tenant_url_code)



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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.TemporaryAnalysisMask() # TemporaryAnalysisMask | 
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.poi_analysis_get_temporary_poi_analysis_mask(body, map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_get_temporary_poi_analysis_mask: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemporaryAnalysisMask**](TemporaryAnalysisMask.md)|  | 
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
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

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_regenerate_rasters**
> poi_analysis_regenerate_rasters(map_id, tenant_url_code)

Regenerate all rasters of the poi associated with the map.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Regenerate all rasters of the poi associated with the map.
    api_instance.poi_analysis_regenerate_rasters(map_id, tenant_url_code)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_regenerate_rasters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

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

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poi_analysis_validate_data_for_poi**
> ValidationErrors poi_analysis_validate_data_for_poi(data_id, data_type, tenant_url_code)

Get the errors, if any, of a layer or datatable for a given type.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.PoiAnalysisApi(cartovista_cloud_clients.ApiClient(configuration))
data_id = 'data_id_example' # str | The Id of the data to be validated. Must be a layer for PoiLayer and TransmissionLayer, and a data table for AnalysisTable.
data_type = cartovista_cloud_clients.PoiDataType() # PoiDataType | The type of data to be validated.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Get the errors, if any, of a layer or datatable for a given type.
    api_response = api_instance.poi_analysis_validate_data_for_poi(data_id, data_type, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoiAnalysisApi->poi_analysis_validate_data_for_poi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_id** | **str**| The Id of the data to be validated. Must be a layer for PoiLayer and TransmissionLayer, and a data table for AnalysisTable. | 
 **data_type** | [**PoiDataType**](.md)| The type of data to be validated. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ValidationErrors**](ValidationErrors.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


