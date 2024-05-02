# cartovista_cloud_clients.VectorServicesApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vector_services_get_clusters_count**](VectorServicesApi.md#vector_services_get_clusters_count) | **POST** /{tenantUrlCode}/VectorServices/getClustersCount | 
[**vector_services_get_clusters_representation**](VectorServicesApi.md#vector_services_get_clusters_representation) | **POST** /{tenantUrlCode}/VectorServices/getClustersRepresentation | 
[**vector_services_get_configuration**](VectorServicesApi.md#vector_services_get_configuration) | **POST** /{tenantUrlCode}/VectorServices/getConfiguration/{layerId} | 
[**vector_services_get_features**](VectorServicesApi.md#vector_services_get_features) | **POST** /{tenantUrlCode}/VectorServices/getFeatures | 
[**vector_services_get_features_combine_min_max_value**](VectorServicesApi.md#vector_services_get_features_combine_min_max_value) | **POST** /{tenantUrlCode}/VectorServices/getFeaturesCombineMinMaxValue | 
[**vector_services_get_features_extent**](VectorServicesApi.md#vector_services_get_features_extent) | **POST** /{tenantUrlCode}/VectorServices/getFeaturesExtent | 
[**vector_services_get_heat_map_items**](VectorServicesApi.md#vector_services_get_heat_map_items) | **POST** /{tenantUrlCode}/VectorServices/getHeatMapItems | 
[**vector_services_get_intersecting_geometries**](VectorServicesApi.md#vector_services_get_intersecting_geometries) | **POST** /{tenantUrlCode}/VectorServices/getIntersectingGeometries | 
[**vector_services_get_selection_stack**](VectorServicesApi.md#vector_services_get_selection_stack) | **POST** /{tenantUrlCode}/VectorServices/getSelectionStack | 
[**vector_services_get_vector_tile**](VectorServicesApi.md#vector_services_get_vector_tile) | **POST** /{tenantUrlCode}/VectorServices/getVectorTile | 

# **vector_services_get_clusters_count**
> GetClustersCountResultDTO vector_services_get_clusters_count(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.VectorServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetClustersCountDTOOfDataQueryColumnDTO() # GetClustersCountDTOOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.vector_services_get_clusters_count(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VectorServicesApi->vector_services_get_clusters_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetClustersCountDTOOfDataQueryColumnDTO**](GetClustersCountDTOOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GetClustersCountResultDTO**](GetClustersCountResultDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vector_services_get_clusters_representation**
> GetClustersRepresentationResultDTO vector_services_get_clusters_representation(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.VectorServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetClustersRepresentationDTOOfDataQueryColumnDTO() # GetClustersRepresentationDTOOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.vector_services_get_clusters_representation(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VectorServicesApi->vector_services_get_clusters_representation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetClustersRepresentationDTOOfDataQueryColumnDTO**](GetClustersRepresentationDTOOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GetClustersRepresentationResultDTO**](GetClustersRepresentationResultDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vector_services_get_configuration**
> GetConfigurationResultDTO vector_services_get_configuration(layer_id, tenant_url_code)



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
api_instance = cartovista_cloud_clients.VectorServicesApi(cartovista_cloud_clients.ApiClient(configuration))
layer_id = 'layer_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.vector_services_get_configuration(layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VectorServicesApi->vector_services_get_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GetConfigurationResultDTO**](GetConfigurationResultDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vector_services_get_features**
> str vector_services_get_features(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.VectorServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetFeaturesParametersOfDataQueryColumnDTO() # GetFeaturesParametersOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.vector_services_get_features(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VectorServicesApi->vector_services_get_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetFeaturesParametersOfDataQueryColumnDTO**](GetFeaturesParametersOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vector_services_get_features_combine_min_max_value**
> GetFeaturesCombineMinMaxValueResultDTO vector_services_get_features_combine_min_max_value(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.VectorServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetFeaturesCombineMinMaxValueDTOOfDataQueryColumnDTO() # GetFeaturesCombineMinMaxValueDTOOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.vector_services_get_features_combine_min_max_value(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VectorServicesApi->vector_services_get_features_combine_min_max_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetFeaturesCombineMinMaxValueDTOOfDataQueryColumnDTO**](GetFeaturesCombineMinMaxValueDTOOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GetFeaturesCombineMinMaxValueResultDTO**](GetFeaturesCombineMinMaxValueResultDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vector_services_get_features_extent**
> GetFeaturesExtentResultDTO vector_services_get_features_extent(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.VectorServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetFeaturesExtentDto() # GetFeaturesExtentDto | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.vector_services_get_features_extent(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VectorServicesApi->vector_services_get_features_extent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetFeaturesExtentDto**](GetFeaturesExtentDto.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GetFeaturesExtentResultDTO**](GetFeaturesExtentResultDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vector_services_get_heat_map_items**
> IVectorSourceResponse vector_services_get_heat_map_items(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.VectorServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetHeatMapItemsDTOOfDataQueryColumnDTO() # GetHeatMapItemsDTOOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.vector_services_get_heat_map_items(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VectorServicesApi->vector_services_get_heat_map_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetHeatMapItemsDTOOfDataQueryColumnDTO**](GetHeatMapItemsDTOOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**IVectorSourceResponse**](IVectorSourceResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vector_services_get_intersecting_geometries**
> list[GeometryDTO] vector_services_get_intersecting_geometries(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.VectorServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetIntersectingGeometriesDTOOfDataQueryColumnDTO() # GetIntersectingGeometriesDTOOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.vector_services_get_intersecting_geometries(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VectorServicesApi->vector_services_get_intersecting_geometries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetIntersectingGeometriesDTOOfDataQueryColumnDTO**](GetIntersectingGeometriesDTOOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[GeometryDTO]**](GeometryDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vector_services_get_selection_stack**
> list[str] vector_services_get_selection_stack(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.VectorServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetSelectionStackMessageDTOOfDataQueryColumnDTO() # GetSelectionStackMessageDTOOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.vector_services_get_selection_stack(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VectorServicesApi->vector_services_get_selection_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetSelectionStackMessageDTOOfDataQueryColumnDTO**](GetSelectionStackMessageDTOOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vector_services_get_vector_tile**
> str vector_services_get_vector_tile(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.VectorServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetVectorTileParameters() # GetVectorTileParameters | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.vector_services_get_vector_tile(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VectorServicesApi->vector_services_get_vector_tile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetVectorTileParameters**](GetVectorTileParameters.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

