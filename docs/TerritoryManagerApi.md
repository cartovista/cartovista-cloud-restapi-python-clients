# cartovista_cloud_clients.TerritoryManagerApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**territory_manager_add_zone**](TerritoryManagerApi.md#territory_manager_add_zone) | **POST** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/zone | 
[**territory_manager_analyze_distances**](TerritoryManagerApi.md#territory_manager_analyze_distances) | **POST** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/distance-analysis | 
[**territory_manager_check_territory_pos_implantation_conflict**](TerritoryManagerApi.md#territory_manager_check_territory_pos_implantation_conflict) | **POST** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/check-territory-pos-implantation | 
[**territory_manager_clone_territory_pos**](TerritoryManagerApi.md#territory_manager_clone_territory_pos) | **POST** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/territory-pos/{posId}/clone | 
[**territory_manager_create_territory**](TerritoryManagerApi.md#territory_manager_create_territory) | **POST** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/territory-pos | 
[**territory_manager_delete_largest_zone**](TerritoryManagerApi.md#territory_manager_delete_largest_zone) | **DELETE** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/largest-zone | 
[**territory_manager_delete_territory_pos**](TerritoryManagerApi.md#territory_manager_delete_territory_pos) | **DELETE** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/territory-pos/{posId} | 
[**territory_manager_export_territor_posy_data**](TerritoryManagerApi.md#territory_manager_export_territor_posy_data) | **POST** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/territory-pos/{territoryPosId}/export-data | Finds the data within the area covered by the territory in multiple layers and generates an Excel file.
[**territory_manager_export_territory_layer**](TerritoryManagerApi.md#territory_manager_export_territory_layer) | **GET** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/export-territory-layer/{language} | 
[**territory_manager_get_default_territory_manager_settings**](TerritoryManagerApi.md#territory_manager_get_default_territory_manager_settings) | **GET** /{tenantUrlCode}/api/v2/TerritoryManager/defaultSettings | 
[**territory_manager_get_scenario**](TerritoryManagerApi.md#territory_manager_get_scenario) | **GET** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId} | 
[**territory_manager_get_territory_block_id_candidates**](TerritoryManagerApi.md#territory_manager_get_territory_block_id_candidates) | **POST** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/territory/candidates | 
[**territory_manager_get_territory_manager_summary**](TerritoryManagerApi.md#territory_manager_get_territory_manager_summary) | **GET** /{tenantUrlCode}/api/v2/TerritoryManager/{mapId}/summary | 
[**territory_manager_redefine_territory_pos**](TerritoryManagerApi.md#territory_manager_redefine_territory_pos) | **POST** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/territory-pos/{posId}/redefine | 
[**territory_manager_unset_scenario_session**](TerritoryManagerApi.md#territory_manager_unset_scenario_session) | **DELETE** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/session | 
[**territory_manager_update_scenario_data_column_configuration**](TerritoryManagerApi.md#territory_manager_update_scenario_data_column_configuration) | **PUT** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/datacolumn-configuration | 
[**territory_manager_update_scenario_info**](TerritoryManagerApi.md#territory_manager_update_scenario_info) | **PATCH** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId} | 
[**territory_manager_update_territories_from_csv**](TerritoryManagerApi.md#territory_manager_update_territories_from_csv) | **POST** /{tenantUrlCode}/api/v2/TerritoryManager/{mapId}/update-from-csv | 
[**territory_manager_update_territory_block_distances_to_pos**](TerritoryManagerApi.md#territory_manager_update_territory_block_distances_to_pos) | **PATCH** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/territories/{territoryId}/calculate-distances | Recalculates the drive time, drive distance and distance between a territory point and the centroid of its blocks.
[**territory_manager_update_territory_location**](TerritoryManagerApi.md#territory_manager_update_territory_location) | **PATCH** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/territory/{territoryPosId}/location | 
[**territory_manager_update_territory_manager_settings**](TerritoryManagerApi.md#territory_manager_update_territory_manager_settings) | **PUT** /{tenantUrlCode}/api/v2/TerritoryManager/{mapId}/settings | 
[**territory_manager_update_territory_manager_urbanicity_value**](TerritoryManagerApi.md#territory_manager_update_territory_manager_urbanicity_value) | **PUT** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/urbanicity-value | 
[**territory_manager_update_territory_point_values**](TerritoryManagerApi.md#territory_manager_update_territory_point_values) | **PUT** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/territory-pos/{posId}/update-point-values | 
[**territory_manager_update_territory_pos_blocks**](TerritoryManagerApi.md#territory_manager_update_territory_pos_blocks) | **POST** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/territory-pos/{posId}/blocks | Updates the territory with the collection of Block paramaters
[**territory_manager_update_territory_pos_exclusivity**](TerritoryManagerApi.md#territory_manager_update_territory_pos_exclusivity) | **PATCH** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/territory-pos/{posId}/exclusivity | 
[**territory_manager_update_territory_pos_name**](TerritoryManagerApi.md#territory_manager_update_territory_pos_name) | **PATCH** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/territory-pos/{posId}/name | 
[**territory_manager_update_territory_pos_pta**](TerritoryManagerApi.md#territory_manager_update_territory_pos_pta) | **PATCH** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/territory-pos/{posId}/pta-zone/{ptaZoneId} | 
[**territory_manager_update_territory_status**](TerritoryManagerApi.md#territory_manager_update_territory_status) | **PATCH** /{tenantUrlCode}/api/v2/TerritoryManager/{scenarioId}/territory-pos/{posId}/status | 

# **territory_manager_add_zone**
> TerritoryManagementZone territory_manager_add_zone(body, scenario_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreateTerritoryZoneParameter() # CreateTerritoryZoneParameter | 
scenario_id = 'scenario_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_add_zone(body, scenario_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_add_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTerritoryZoneParameter**](CreateTerritoryZoneParameter.md)|  | 
 **scenario_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**TerritoryManagementZone**](TerritoryManagementZone.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_analyze_distances**
> list[TerritoryAnalyzedDistance] territory_manager_analyze_distances(body, scenario_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.AnalyzeDistancesParameter() # AnalyzeDistancesParameter | 
scenario_id = 'scenario_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_analyze_distances(body, scenario_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_analyze_distances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnalyzeDistancesParameter**](AnalyzeDistancesParameter.md)|  | 
 **scenario_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[TerritoryAnalyzedDistance]**](TerritoryAnalyzedDistance.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_check_territory_pos_implantation_conflict**
> str territory_manager_check_territory_pos_implantation_conflict(body, scenario_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateTerritoryLocationDTO() # UpdateTerritoryLocationDTO | 
scenario_id = 'scenario_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_check_territory_pos_implantation_conflict(body, scenario_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_check_territory_pos_implantation_conflict: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTerritoryLocationDTO**](UpdateTerritoryLocationDTO.md)|  | 
 **scenario_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_clone_territory_pos**
> TerritoryPosDTO territory_manager_clone_territory_pos(scenario_id, pos_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
scenario_id = 'scenario_id_example' # str | 
pos_id = 'pos_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_clone_territory_pos(scenario_id, pos_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_clone_territory_pos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**|  | 
 **pos_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**TerritoryPosDTO**](TerritoryPosDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_create_territory**
> CreateTerritoryResponse territory_manager_create_territory(body, scenario_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreateTerritoryParameters() # CreateTerritoryParameters | 
scenario_id = 'scenario_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_create_territory(body, scenario_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_create_territory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTerritoryParameters**](CreateTerritoryParameters.md)|  | 
 **scenario_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**CreateTerritoryResponse**](CreateTerritoryResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_delete_largest_zone**
> TerritoryManagementZone territory_manager_delete_largest_zone(scenario_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
scenario_id = 'scenario_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_delete_largest_zone(scenario_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_delete_largest_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**TerritoryManagementZone**](TerritoryManagementZone.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_delete_territory_pos**
> TerritoryPosDTO territory_manager_delete_territory_pos(scenario_id, pos_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
scenario_id = 'scenario_id_example' # str | 
pos_id = 'pos_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_delete_territory_pos(scenario_id, pos_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_delete_territory_pos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**|  | 
 **pos_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**TerritoryPosDTO**](TerritoryPosDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_export_territor_posy_data**
> str territory_manager_export_territor_posy_data(body, scenario_id, territory_pos_id, tenant_url_code)

Finds the data within the area covered by the territory in multiple layers and generates an Excel file.

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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ExportDataParameter() # ExportDataParameter | 
scenario_id = 'scenario_id_example' # str | 
territory_pos_id = 'territory_pos_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Finds the data within the area covered by the territory in multiple layers and generates an Excel file.
    api_response = api_instance.territory_manager_export_territor_posy_data(body, scenario_id, territory_pos_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_export_territor_posy_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportDataParameter**](ExportDataParameter.md)|  | 
 **scenario_id** | **str**|  | 
 **territory_pos_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_export_territory_layer**
> str territory_manager_export_territory_layer(scenario_id, language, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
scenario_id = 'scenario_id_example' # str | 
language = 'language_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_export_territory_layer(scenario_id, language, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_export_territory_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**|  | 
 **language** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_get_default_territory_manager_settings**
> TerritoryManagerDefaultSettings territory_manager_get_default_territory_manager_settings(tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_get_default_territory_manager_settings(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_get_default_territory_manager_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**TerritoryManagerDefaultSettings**](TerritoryManagerDefaultSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_get_scenario**
> ScenarioDTO territory_manager_get_scenario(scenario_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
scenario_id = 'scenario_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_get_scenario(scenario_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_get_scenario: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ScenarioDTO**](ScenarioDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_get_territory_block_id_candidates**
> GetBlockCandidatesResponse territory_manager_get_territory_block_id_candidates(body, scenario_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CandidatesGetParameter() # CandidatesGetParameter | 
scenario_id = 'scenario_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_get_territory_block_id_candidates(body, scenario_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_get_territory_block_id_candidates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CandidatesGetParameter**](CandidatesGetParameter.md)|  | 
 **scenario_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GetBlockCandidatesResponse**](GetBlockCandidatesResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_get_territory_manager_summary**
> TerritoryManagerSummary territory_manager_get_territory_manager_summary(map_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_get_territory_manager_summary(map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_get_territory_manager_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**TerritoryManagerSummary**](TerritoryManagerSummary.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_redefine_territory_pos**
> RedefineResponse territory_manager_redefine_territory_pos(body, scenario_id, pos_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.RedefineParameter() # RedefineParameter | 
scenario_id = 'scenario_id_example' # str | 
pos_id = 'pos_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_redefine_territory_pos(body, scenario_id, pos_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_redefine_territory_pos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RedefineParameter**](RedefineParameter.md)|  | 
 **scenario_id** | **str**|  | 
 **pos_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**RedefineResponse**](RedefineResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_unset_scenario_session**
> bool territory_manager_unset_scenario_session(scenario_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
scenario_id = 'scenario_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_unset_scenario_session(scenario_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_unset_scenario_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_update_scenario_data_column_configuration**
> list[ScenarioDataColumnConfigurationDTO] territory_manager_update_scenario_data_column_configuration(body, scenario_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = [cartovista_cloud_clients.ScenarioUpdateDataColumnConfigurationParam()] # list[ScenarioUpdateDataColumnConfigurationParam] | 
scenario_id = 'scenario_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_update_scenario_data_column_configuration(body, scenario_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_update_scenario_data_column_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ScenarioUpdateDataColumnConfigurationParam]**](ScenarioUpdateDataColumnConfigurationParam.md)|  | 
 **scenario_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[ScenarioDataColumnConfigurationDTO]**](ScenarioDataColumnConfigurationDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_update_scenario_info**
> territory_manager_update_scenario_info(body, scenario_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ScenarioUpdateInfoParameter() # ScenarioUpdateInfoParameter | 
scenario_id = 'scenario_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_instance.territory_manager_update_scenario_info(body, scenario_id, tenant_url_code)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_update_scenario_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScenarioUpdateInfoParameter**](ScenarioUpdateInfoParameter.md)|  | 
 **scenario_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_update_territories_from_csv**
> ScenarioDTO territory_manager_update_territories_from_csv(map_id2, tenant_url_code, map_id, file=file)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
map_id2 = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 
map_id = 'map_id_example' # str | 
file = 'file_example' # str |  (optional)

try:
    api_response = api_instance.territory_manager_update_territories_from_csv(map_id2, tenant_url_code, map_id, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_update_territories_from_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id2** | **str**|  | 
 **tenant_url_code** | **str**|  | 
 **map_id** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**ScenarioDTO**](ScenarioDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_update_territory_block_distances_to_pos**
> TerritoryZoneDTO territory_manager_update_territory_block_distances_to_pos(scenario_id, territory_id, tenant_url_code)

Recalculates the drive time, drive distance and distance between a territory point and the centroid of its blocks.

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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
scenario_id = 'scenario_id_example' # str | 
territory_id = 56 # int | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Recalculates the drive time, drive distance and distance between a territory point and the centroid of its blocks.
    api_response = api_instance.territory_manager_update_territory_block_distances_to_pos(scenario_id, territory_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_update_territory_block_distances_to_pos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**|  | 
 **territory_id** | **int**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**TerritoryZoneDTO**](TerritoryZoneDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_update_territory_location**
> UpdateTerritoryLocationResponse territory_manager_update_territory_location(body, scenario_id, territory_pos_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateTerritoryLocationDTO() # UpdateTerritoryLocationDTO | 
scenario_id = 'scenario_id_example' # str | 
territory_pos_id = 'territory_pos_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_update_territory_location(body, scenario_id, territory_pos_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_update_territory_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTerritoryLocationDTO**](UpdateTerritoryLocationDTO.md)|  | 
 **scenario_id** | **str**|  | 
 **territory_pos_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**UpdateTerritoryLocationResponse**](UpdateTerritoryLocationResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_update_territory_manager_settings**
> TerritoryManagerSettings territory_manager_update_territory_manager_settings(body, map_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.TerritoryManagerSettings() # TerritoryManagerSettings | 
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_update_territory_manager_settings(body, map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_update_territory_manager_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TerritoryManagerSettings**](TerritoryManagerSettings.md)|  | 
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**TerritoryManagerSettings**](TerritoryManagerSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_update_territory_manager_urbanicity_value**
> TerritoryManagerUrbanicity territory_manager_update_territory_manager_urbanicity_value(body, scenario_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.TerritoryManagerUrbanicity() # TerritoryManagerUrbanicity | 
scenario_id = 'scenario_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_update_territory_manager_urbanicity_value(body, scenario_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_update_territory_manager_urbanicity_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TerritoryManagerUrbanicity**](TerritoryManagerUrbanicity.md)|  | 
 **scenario_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**TerritoryManagerUrbanicity**](TerritoryManagerUrbanicity.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_update_territory_point_values**
> DataRow territory_manager_update_territory_point_values(body, scenario_id, pos_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.TerritoryPointDataRowUpdateParameter() # TerritoryPointDataRowUpdateParameter | 
scenario_id = 'scenario_id_example' # str | 
pos_id = 'pos_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_update_territory_point_values(body, scenario_id, pos_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_update_territory_point_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TerritoryPointDataRowUpdateParameter**](TerritoryPointDataRowUpdateParameter.md)|  | 
 **scenario_id** | **str**|  | 
 **pos_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataRow**](DataRow.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_update_territory_pos_blocks**
> UpdateTerritoryBlocksResponse territory_manager_update_territory_pos_blocks(body, scenario_id, pos_id, tenant_url_code)

Updates the territory with the collection of Block paramaters

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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateTerritoryBlocksParameter() # UpdateTerritoryBlocksParameter | The UpdateTerritoryBlocksParameter parameter object to add/remove for the targeted territory.
scenario_id = 'scenario_id_example' # str | The scenario internal system identifier.
pos_id = 'pos_id_example' # str | The territory internal identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the territory with the collection of Block paramaters
    api_response = api_instance.territory_manager_update_territory_pos_blocks(body, scenario_id, pos_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_update_territory_pos_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTerritoryBlocksParameter**](UpdateTerritoryBlocksParameter.md)| The UpdateTerritoryBlocksParameter parameter object to add/remove for the targeted territory. | 
 **scenario_id** | **str**| The scenario internal system identifier. | 
 **pos_id** | **str**| The territory internal identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**UpdateTerritoryBlocksResponse**](UpdateTerritoryBlocksResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_update_territory_pos_exclusivity**
> TerritoryPosExclusivityResponse territory_manager_update_territory_pos_exclusivity(body, scenario_id, pos_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateTerritoryPosExclusivityParameter() # UpdateTerritoryPosExclusivityParameter | 
scenario_id = 'scenario_id_example' # str | 
pos_id = 'pos_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_update_territory_pos_exclusivity(body, scenario_id, pos_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_update_territory_pos_exclusivity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTerritoryPosExclusivityParameter**](UpdateTerritoryPosExclusivityParameter.md)|  | 
 **scenario_id** | **str**|  | 
 **pos_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**TerritoryPosExclusivityResponse**](TerritoryPosExclusivityResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_update_territory_pos_name**
> TerritoryPosDTO territory_manager_update_territory_pos_name(body, scenario_id, pos_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = 'body_example' # str | 
scenario_id = 'scenario_id_example' # str | 
pos_id = 'pos_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_update_territory_pos_name(body, scenario_id, pos_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_update_territory_pos_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **scenario_id** | **str**|  | 
 **pos_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**TerritoryPosDTO**](TerritoryPosDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_update_territory_pos_pta**
> TerritoryPosDTO territory_manager_update_territory_pos_pta(scenario_id, pos_id, pta_zone_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
scenario_id = 'scenario_id_example' # str | 
pos_id = 'pos_id_example' # str | 
pta_zone_id = 56 # int | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_update_territory_pos_pta(scenario_id, pos_id, pta_zone_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_update_territory_pos_pta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**|  | 
 **pos_id** | **str**|  | 
 **pta_zone_id** | **int**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**TerritoryPosDTO**](TerritoryPosDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **territory_manager_update_territory_status**
> TerritoryStatusUpdateResponse territory_manager_update_territory_status(body, scenario_id, pos_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.TerritoryManagerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateTerritoryPosStatusParameter() # UpdateTerritoryPosStatusParameter | 
scenario_id = 'scenario_id_example' # str | 
pos_id = 'pos_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.territory_manager_update_territory_status(body, scenario_id, pos_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerritoryManagerApi->territory_manager_update_territory_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTerritoryPosStatusParameter**](UpdateTerritoryPosStatusParameter.md)|  | 
 **scenario_id** | **str**|  | 
 **pos_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**TerritoryStatusUpdateResponse**](TerritoryStatusUpdateResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


