# cartovista_cloud_clients.CompositeVariableScoringApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**composite_variable_scoring_can_modify_analyses**](CompositeVariableScoringApi.md#composite_variable_scoring_can_modify_analyses) | **GET** /{tenantUrlCode}/api/v2/score-analysis/{mapIdentifier}/canModifyAnalyses | Checks whether or not the current user can modify the analyses of the given map.
[**composite_variable_scoring_create_composite_scoring_analysis**](CompositeVariableScoringApi.md#composite_variable_scoring_create_composite_scoring_analysis) | **POST** /{tenantUrlCode}/api/v2/score-analysis/{mapId}/layer/{layerId} | Creates a scoring analysis for a map and a layer.
[**composite_variable_scoring_create_variable**](CompositeVariableScoringApi.md#composite_variable_scoring_create_variable) | **POST** /{tenantUrlCode}/api/v2/score-analysis/{analysisId}/variables | Creates a variable for a given analysis. The scores are recomputed.
[**composite_variable_scoring_delete_analysis**](CompositeVariableScoringApi.md#composite_variable_scoring_delete_analysis) | **DELETE** /{tenantUrlCode}/api/v2/score-analysis/{analysisId} | Deletes an analysis. The scores are recomputed
[**composite_variable_scoring_delete_variable**](CompositeVariableScoringApi.md#composite_variable_scoring_delete_variable) | **DELETE** /{tenantUrlCode}/api/v2/score-analysis/{analysisId}/variables/{variableId} | Deletes a variable. The scores are recomputed
[**composite_variable_scoring_get_all_composite_scoring_analysis**](CompositeVariableScoringApi.md#composite_variable_scoring_get_all_composite_scoring_analysis) | **GET** /{tenantUrlCode}/api/v2/score-analysis/{mapId} | Gets all the analyses associated to a map.
[**composite_variable_scoring_get_composite_scoring_analysis_data_table**](CompositeVariableScoringApi.md#composite_variable_scoring_get_composite_scoring_analysis_data_table) | **GET** /{tenantUrlCode}/api/v2/score-analysis/{analysisId}/datatable | Gets a summary of the score column and how it is joined to the existing data.
[**composite_variable_scoring_get_variable**](CompositeVariableScoringApi.md#composite_variable_scoring_get_variable) | **GET** /{tenantUrlCode}/api/v2/score-analysis/{analysisId}/variables/{variableId} | Gets a specific variable.
[**composite_variable_scoring_get_variables**](CompositeVariableScoringApi.md#composite_variable_scoring_get_variables) | **GET** /{tenantUrlCode}/api/v2/score-analysis/{analysisId}/variables | Gets the variables for a specific analysis.
[**composite_variable_scoring_update_analysis_properties**](CompositeVariableScoringApi.md#composite_variable_scoring_update_analysis_properties) | **PATCH** /{tenantUrlCode}/api/v2/score-analysis/{analysisId} | Updates a variable. The scores are recomputed.
[**composite_variable_scoring_update_variable**](CompositeVariableScoringApi.md#composite_variable_scoring_update_variable) | **PATCH** /{tenantUrlCode}/api/v2/score-analysis/{variableId}/variables | Updates a variable. The scores are recomputed.

# **composite_variable_scoring_can_modify_analyses**
> bool composite_variable_scoring_can_modify_analyses(map_identifier, tenant_url_code)

Checks whether or not the current user can modify the analyses of the given map.

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
api_instance = cartovista_cloud_clients.CompositeVariableScoringApi(cartovista_cloud_clients.ApiClient(configuration))
map_identifier = 'map_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Checks whether or not the current user can modify the analyses of the given map.
    api_response = api_instance.composite_variable_scoring_can_modify_analyses(map_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompositeVariableScoringApi->composite_variable_scoring_can_modify_analyses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **composite_variable_scoring_create_composite_scoring_analysis**
> Analysis composite_variable_scoring_create_composite_scoring_analysis(map_id, layer_id, tenant_url_code)

Creates a scoring analysis for a map and a layer.

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
api_instance = cartovista_cloud_clients.CompositeVariableScoringApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | 
layer_id = 'layer_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a scoring analysis for a map and a layer.
    api_response = api_instance.composite_variable_scoring_create_composite_scoring_analysis(map_id, layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompositeVariableScoringApi->composite_variable_scoring_create_composite_scoring_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **layer_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Analysis**](Analysis.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **composite_variable_scoring_create_variable**
> VariableWithUpdatedWeightsDTO composite_variable_scoring_create_variable(body, analysis_id, tenant_url_code)

Creates a variable for a given analysis. The scores are recomputed.

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
api_instance = cartovista_cloud_clients.CompositeVariableScoringApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreateCompositeVariableDTO() # CreateCompositeVariableDTO | 
analysis_id = 'analysis_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a variable for a given analysis. The scores are recomputed.
    api_response = api_instance.composite_variable_scoring_create_variable(body, analysis_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompositeVariableScoringApi->composite_variable_scoring_create_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCompositeVariableDTO**](CreateCompositeVariableDTO.md)|  | 
 **analysis_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**VariableWithUpdatedWeightsDTO**](VariableWithUpdatedWeightsDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **composite_variable_scoring_delete_analysis**
> composite_variable_scoring_delete_analysis(analysis_id, tenant_url_code)

Deletes an analysis. The scores are recomputed

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
api_instance = cartovista_cloud_clients.CompositeVariableScoringApi(cartovista_cloud_clients.ApiClient(configuration))
analysis_id = 'analysis_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes an analysis. The scores are recomputed
    api_instance.composite_variable_scoring_delete_analysis(analysis_id, tenant_url_code)
except ApiException as e:
    print("Exception when calling CompositeVariableScoringApi->composite_variable_scoring_delete_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **composite_variable_scoring_delete_variable**
> VariableWithUpdatedWeightsDTO composite_variable_scoring_delete_variable(analysis_id, variable_id, tenant_url_code)

Deletes a variable. The scores are recomputed

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
api_instance = cartovista_cloud_clients.CompositeVariableScoringApi(cartovista_cloud_clients.ApiClient(configuration))
analysis_id = 'analysis_id_example' # str | 
variable_id = 'variable_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes a variable. The scores are recomputed
    api_response = api_instance.composite_variable_scoring_delete_variable(analysis_id, variable_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompositeVariableScoringApi->composite_variable_scoring_delete_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**|  | 
 **variable_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**VariableWithUpdatedWeightsDTO**](VariableWithUpdatedWeightsDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **composite_variable_scoring_get_all_composite_scoring_analysis**
> list[Analysis] composite_variable_scoring_get_all_composite_scoring_analysis(map_id, tenant_url_code)

Gets all the analyses associated to a map.

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
api_instance = cartovista_cloud_clients.CompositeVariableScoringApi(cartovista_cloud_clients.ApiClient(configuration))
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the analyses associated to a map.
    api_response = api_instance.composite_variable_scoring_get_all_composite_scoring_analysis(map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompositeVariableScoringApi->composite_variable_scoring_get_all_composite_scoring_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Analysis]**](Analysis.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **composite_variable_scoring_get_composite_scoring_analysis_data_table**
> AnalysisDataTableDTO composite_variable_scoring_get_composite_scoring_analysis_data_table(analysis_id, tenant_url_code)

Gets a summary of the score column and how it is joined to the existing data.

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
api_instance = cartovista_cloud_clients.CompositeVariableScoringApi(cartovista_cloud_clients.ApiClient(configuration))
analysis_id = 'analysis_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a summary of the score column and how it is joined to the existing data.
    api_response = api_instance.composite_variable_scoring_get_composite_scoring_analysis_data_table(analysis_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompositeVariableScoringApi->composite_variable_scoring_get_composite_scoring_analysis_data_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**AnalysisDataTableDTO**](AnalysisDataTableDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **composite_variable_scoring_get_variable**
> VariableDTO composite_variable_scoring_get_variable(analysis_id, variable_id, tenant_url_code)

Gets a specific variable.

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
api_instance = cartovista_cloud_clients.CompositeVariableScoringApi(cartovista_cloud_clients.ApiClient(configuration))
analysis_id = 'analysis_id_example' # str | 
variable_id = 'variable_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific variable.
    api_response = api_instance.composite_variable_scoring_get_variable(analysis_id, variable_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompositeVariableScoringApi->composite_variable_scoring_get_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**|  | 
 **variable_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**VariableDTO**](VariableDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **composite_variable_scoring_get_variables**
> list[VariableDTO] composite_variable_scoring_get_variables(analysis_id, tenant_url_code)

Gets the variables for a specific analysis.

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
api_instance = cartovista_cloud_clients.CompositeVariableScoringApi(cartovista_cloud_clients.ApiClient(configuration))
analysis_id = 'analysis_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the variables for a specific analysis.
    api_response = api_instance.composite_variable_scoring_get_variables(analysis_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompositeVariableScoringApi->composite_variable_scoring_get_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[VariableDTO]**](VariableDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **composite_variable_scoring_update_analysis_properties**
> AnalysisDTO composite_variable_scoring_update_analysis_properties(body, analysis_id, tenant_url_code)

Updates a variable. The scores are recomputed.

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
api_instance = cartovista_cloud_clients.CompositeVariableScoringApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateVariableDTO() # UpdateVariableDTO | 
analysis_id = 'analysis_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a variable. The scores are recomputed.
    api_response = api_instance.composite_variable_scoring_update_analysis_properties(body, analysis_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompositeVariableScoringApi->composite_variable_scoring_update_analysis_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateVariableDTO**](UpdateVariableDTO.md)|  | 
 **analysis_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**AnalysisDTO**](AnalysisDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **composite_variable_scoring_update_variable**
> VariableWithUpdatedWeightsDTO composite_variable_scoring_update_variable(body, variable_id, tenant_url_code)

Updates a variable. The scores are recomputed.

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
api_instance = cartovista_cloud_clients.CompositeVariableScoringApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateVariableDTO() # UpdateVariableDTO | 
variable_id = 'variable_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a variable. The scores are recomputed.
    api_response = api_instance.composite_variable_scoring_update_variable(body, variable_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompositeVariableScoringApi->composite_variable_scoring_update_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateVariableDTO**](UpdateVariableDTO.md)|  | 
 **variable_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**VariableWithUpdatedWeightsDTO**](VariableWithUpdatedWeightsDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

