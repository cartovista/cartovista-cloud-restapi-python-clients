# cartovista_cloud_clients.LayerApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**layer_append_to_layer**](LayerApi.md#layer_append_to_layer) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/append | Appends the content of a file at the end of the layer. The file format must match the layer.
[**layer_cancel_cluster_task**](LayerApi.md#layer_cancel_cluster_task) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/cancelCluster | Cancels the cluster generation for that layer.
[**layer_create_layer**](LayerApi.md#layer_create_layer) | **POST** /{tenantUrlCode}/api/v2/createLayer | Creates a new empty layer.
[**layer_create_layer_from_service**](LayerApi.md#layer_create_layer_from_service) | **POST** /{tenantUrlCode}/api/v2/Layer/createFromService | Creates a layer from an external service (ArcGIS, GeoJSON).
[**layer_create_layer_from_zip**](LayerApi.md#layer_create_layer_from_zip) | **POST** /{tenantUrlCode}/api/v2/Layer/createFromZip | Creates a layer from a ZIP file.
[**layer_de_optimize_layer**](LayerApi.md#layer_de_optimize_layer) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/deoptimize | Disables the ClickHouse optimization for this layer.
[**layer_delete_clusters**](LayerApi.md#layer_delete_clusters) | **DELETE** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/cluster | Deletes the generated clusters for that layer.
[**layer_delete_layer_by_id**](LayerApi.md#layer_delete_layer_by_id) | **DELETE** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier} | Deletes the layer.
[**layer_duplicate_layer**](LayerApi.md#layer_duplicate_layer) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/duplicate | Duplicates the layer and its data.
[**layer_generate_clusters**](LayerApi.md#layer_generate_clusters) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/cluster | Generates clusters for the layer. The layer must be a point layer.
[**layer_generate_layer_icon**](LayerApi.md#layer_generate_layer_icon) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/icon | Regenerates the layer&#x27;s icon.
[**layer_generate_layer_thumbnail**](LayerApi.md#layer_generate_layer_thumbnail) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/thumbnail | Regenerates the layer&#x27;s thumbnail.
[**layer_get_data_table_by_layer_identifier**](LayerApi.md#layer_get_data_table_by_layer_identifier) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/dataTable | Get DataTable of layer by layer identifier.
[**layer_get_data_tables_by_layer_identifier**](LayerApi.md#layer_get_data_tables_by_layer_identifier) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/dataTables | Get DataTables linked to layer by layer identifier.
[**layer_get_file_description**](LayerApi.md#layer_get_file_description) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/getFileDescription | Stores a temporary file for an upcoming data insert or update and returns a description of the file&#x27;s content.
[**layer_get_layer_by_id**](LayerApi.md#layer_get_layer_by_id) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier} | Retrives a specific layer.
[**layer_get_layer_details**](LayerApi.md#layer_get_layer_details) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerId}/details | Gets the layer, its related maps, tables, columns and settings.
[**layer_get_layers**](LayerApi.md#layer_get_layers) | **GET** /{tenantUrlCode}/api/v2/Layers | Gets all the layers.
[**layer_get_layers_extents**](LayerApi.md#layer_get_layers_extents) | **POST** /{tenantUrlCode}/api/v2/Layer/extents | Gets the layers&#x27; extents.
[**layer_get_many_spatial_statistics_by_feature**](LayerApi.md#layer_get_many_spatial_statistics_by_feature) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/manySpatialStatisticsByFeature | Computes the area and/or length of a layer&#x27;s features using any number of filters and spatial filters.
[**layer_get_many_spatial_statistics_by_wkt**](LayerApi.md#layer_get_many_spatial_statistics_by_wkt) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/manySpatialStatisticsByWKT | Computes the area and/or length of a layer&#x27;s features using any number of filters and spatial filters.
[**layer_get_maps_by_layer_identifier**](LayerApi.md#layer_get_maps_by_layer_identifier) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/maps | Get Maps by layer friendly or system identifier.
[**layer_get_spatial_statistics_by_feature**](LayerApi.md#layer_get_spatial_statistics_by_feature) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/spatialStatisticsByFeature | Computes the area and/or length of a layer&#x27;s features. The features can be filtered by value and/or by geometry.
[**layer_get_spatial_statistics_by_wkt**](LayerApi.md#layer_get_spatial_statistics_by_wkt) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/spatialStatisticsByWKT | Computes the area and/or length of a layer&#x27;s features. The features can be filtered by value and/or by geometry.
[**layer_get_transformation_settings**](LayerApi.md#layer_get_transformation_settings) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/transformationSettings | Gets the ids of the columns used to georeference the layer. Will return null if the layer was not created from georeferencing a data table.
[**layer_optimize_layer**](LayerApi.md#layer_optimize_layer) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/optimize | Optimizes the table queries with ClickHouse. The layer must be tiled.
[**layer_set_data_column_unique_id**](LayerApi.md#layer_set_data_column_unique_id) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/setDataColumnUniqueId | Sets the layer&#x27;s unique identifier column. The column becomes the primary way to identify its rows.
[**layer_set_unique_identifier**](LayerApi.md#layer_set_unique_identifier) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/setUniqueIdentifier | Sets the layer&#x27;s unique identifier.
[**layer_synchronize_layer**](LayerApi.md#layer_synchronize_layer) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/synchronize | Synchronizes the layer with its external service. The layer must be linked to an external data provider.
[**layer_update_from_zip**](LayerApi.md#layer_update_from_zip) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/updateFromZip | Updates a layer from a ZIP. The ZIP content&#x27;s format must match the layer.
[**layer_update_layer**](LayerApi.md#layer_update_layer) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/update | Updates the layer&#x27;s properties.
[**layer_update_layer_from_file_description**](LayerApi.md#layer_update_layer_from_file_description) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/updateFromFileDescription | Updates a layer with a file uploaded using &#x60;Layer/{layerIdentifier}/getFileDescription&#x60;.

# **layer_append_to_layer**
> Layer layer_append_to_layer(layer_identifier, tenant_url_code, file=file)

Appends the content of a file at the end of the layer. The file format must match the layer.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Appends the content of a file at the end of the layer. The file format must match the layer.
    api_response = api_instance.layer_append_to_layer(layer_identifier, tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_append_to_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_cancel_cluster_task**
> layer_cancel_cluster_task(layer_identifier, tenant_url_code)

Cancels the cluster generation for that layer.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Cancels the cluster generation for that layer.
    api_instance.layer_cancel_cluster_task(layer_identifier, tenant_url_code)
except ApiException as e:
    print("Exception when calling LayerApi->layer_cancel_cluster_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_create_layer**
> Layer layer_create_layer(body, tenant_url_code)

Creates a new empty layer.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.LayerCreateParameter() # LayerCreateParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a new empty layer.
    api_response = api_instance.layer_create_layer(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_create_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayerCreateParameter**](LayerCreateParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_create_layer_from_service**
> Layer layer_create_layer_from_service(body, tenant_url_code)

Creates a layer from an external service (ArcGIS, GeoJSON).

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreateLayerFromServiceParameter() # CreateLayerFromServiceParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a layer from an external service (ArcGIS, GeoJSON).
    api_response = api_instance.layer_create_layer_from_service(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_create_layer_from_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLayerFromServiceParameter**](CreateLayerFromServiceParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_create_layer_from_zip**
> Layer layer_create_layer_from_zip(tenant_url_code, file=file)

Creates a layer from a ZIP file.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Creates a layer from a ZIP file.
    api_response = api_instance.layer_create_layer_from_zip(tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_create_layer_from_zip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_de_optimize_layer**
> Layer layer_de_optimize_layer(layer_identifier, tenant_url_code)

Disables the ClickHouse optimization for this layer.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Disables the ClickHouse optimization for this layer.
    api_response = api_instance.layer_de_optimize_layer(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_de_optimize_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_delete_clusters**
> Layer layer_delete_clusters(layer_identifier, tenant_url_code)

Deletes the generated clusters for that layer.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes the generated clusters for that layer.
    api_response = api_instance.layer_delete_clusters(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_delete_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_delete_layer_by_id**
> DeleteLayerResponse layer_delete_layer_by_id(layer_identifier, tenant_url_code)

Deletes the layer.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes the layer.
    api_response = api_instance.layer_delete_layer_by_id(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_delete_layer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DeleteLayerResponse**](DeleteLayerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_duplicate_layer**
> Layer layer_duplicate_layer(body, layer_identifier, tenant_url_code)

Duplicates the layer and its data.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DuplicateLayerParameter() # DuplicateLayerParameter | 
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Duplicates the layer and its data.
    api_response = api_instance.layer_duplicate_layer(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_duplicate_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DuplicateLayerParameter**](DuplicateLayerParameter.md)|  | 
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_generate_clusters**
> Layer layer_generate_clusters(layer_identifier, tenant_url_code)

Generates clusters for the layer. The layer must be a point layer.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Generates clusters for the layer. The layer must be a point layer.
    api_response = api_instance.layer_generate_clusters(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_generate_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_generate_layer_icon**
> layer_generate_layer_icon(layer_identifier, tenant_url_code)

Regenerates the layer's icon.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Regenerates the layer's icon.
    api_instance.layer_generate_layer_icon(layer_identifier, tenant_url_code)
except ApiException as e:
    print("Exception when calling LayerApi->layer_generate_layer_icon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_generate_layer_thumbnail**
> layer_generate_layer_thumbnail(layer_identifier, tenant_url_code)

Regenerates the layer's thumbnail.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Regenerates the layer's thumbnail.
    api_instance.layer_generate_layer_thumbnail(layer_identifier, tenant_url_code)
except ApiException as e:
    print("Exception when calling LayerApi->layer_generate_layer_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_get_data_table_by_layer_identifier**
> DataTable layer_get_data_table_by_layer_identifier(layer_identifier, tenant_url_code)

Get DataTable of layer by layer identifier.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Get DataTable of layer by layer identifier.
    api_response = api_instance.layer_get_data_table_by_layer_identifier(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_get_data_table_by_layer_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_get_data_tables_by_layer_identifier**
> list[LayerDataTable] layer_get_data_tables_by_layer_identifier(layer_identifier, tenant_url_code)

Get DataTables linked to layer by layer identifier.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Get DataTables linked to layer by layer identifier.
    api_response = api_instance.layer_get_data_tables_by_layer_identifier(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_get_data_tables_by_layer_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[LayerDataTable]**](LayerDataTable.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_get_file_description**
> FileDescription layer_get_file_description(layer_identifier, tenant_url_code, file=file)

Stores a temporary file for an upcoming data insert or update and returns a description of the file's content.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Stores a temporary file for an upcoming data insert or update and returns a description of the file's content.
    api_response = api_instance.layer_get_file_description(layer_identifier, tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_get_file_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**FileDescription**](FileDescription.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_get_layer_by_id**
> Layer layer_get_layer_by_id(layer_identifier, tenant_url_code)

Retrives a specific layer.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Retrives a specific layer.
    api_response = api_instance.layer_get_layer_by_id(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_get_layer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_get_layer_details**
> LayerWithDetails layer_get_layer_details(layer_id, tenant_url_code)

Gets the layer, its related maps, tables, columns and settings.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_id = 'layer_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the layer, its related maps, tables, columns and settings.
    api_response = api_instance.layer_get_layer_details(layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_get_layer_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerWithDetails**](LayerWithDetails.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_get_layers**
> list[Layer] layer_get_layers(tenant_url_code)

Gets all the layers.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the layers.
    api_response = api_instance.layer_get_layers(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_get_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Layer]**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_get_layers_extents**
> list[ExtentDTO] layer_get_layers_extents(body, tenant_url_code)

Gets the layers' extents.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = ['body_example'] # list[str] | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the layers' extents.
    api_response = api_instance.layer_get_layers_extents(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_get_layers_extents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[ExtentDTO]**](ExtentDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_get_many_spatial_statistics_by_feature**
> list[LayerSpatialStatistics] layer_get_many_spatial_statistics_by_feature(body, layer_identifier, tenant_url_code)

Computes the area and/or length of a layer's features using any number of filters and spatial filters.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetManySpatialStatisticsByFeatureParameter() # GetManySpatialStatisticsByFeatureParameter | The json object that holds the information for spatial statistics reporting.
layer_identifier = 'layer_identifier_example' # str | The layer identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Computes the area and/or length of a layer's features using any number of filters and spatial filters.
    api_response = api_instance.layer_get_many_spatial_statistics_by_feature(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_get_many_spatial_statistics_by_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetManySpatialStatisticsByFeatureParameter**](GetManySpatialStatisticsByFeatureParameter.md)| The json object that holds the information for spatial statistics reporting. | 
 **layer_identifier** | **str**| The layer identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[LayerSpatialStatistics]**](LayerSpatialStatistics.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_get_many_spatial_statistics_by_wkt**
> list[LayerSpatialStatistics] layer_get_many_spatial_statistics_by_wkt(body, layer_identifier, tenant_url_code)

Computes the area and/or length of a layer's features using any number of filters and spatial filters.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetManySpatialStatisticsByWKTParameter() # GetManySpatialStatisticsByWKTParameter | The json object that holds the information for spatial statistics reporting.
layer_identifier = 'layer_identifier_example' # str | The layer identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Computes the area and/or length of a layer's features using any number of filters and spatial filters.
    api_response = api_instance.layer_get_many_spatial_statistics_by_wkt(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_get_many_spatial_statistics_by_wkt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetManySpatialStatisticsByWKTParameter**](GetManySpatialStatisticsByWKTParameter.md)| The json object that holds the information for spatial statistics reporting. | 
 **layer_identifier** | **str**| The layer identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[LayerSpatialStatistics]**](LayerSpatialStatistics.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_get_maps_by_layer_identifier**
> list[Map] layer_get_maps_by_layer_identifier(layer_identifier, tenant_url_code)

Get Maps by layer friendly or system identifier.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Get Maps by layer friendly or system identifier.
    api_response = api_instance.layer_get_maps_by_layer_identifier(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_get_maps_by_layer_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Map]**](Map.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_get_spatial_statistics_by_feature**
> LayerSpatialStatistics layer_get_spatial_statistics_by_feature(body, layer_identifier, tenant_url_code)

Computes the area and/or length of a layer's features. The features can be filtered by value and/or by geometry.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetSpatialStatisticsByFeatureParameter() # GetSpatialStatisticsByFeatureParameter | The json object that holds the information for spatial statistics reporting.
layer_identifier = 'layer_identifier_example' # str | The layer identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Computes the area and/or length of a layer's features. The features can be filtered by value and/or by geometry.
    api_response = api_instance.layer_get_spatial_statistics_by_feature(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_get_spatial_statistics_by_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetSpatialStatisticsByFeatureParameter**](GetSpatialStatisticsByFeatureParameter.md)| The json object that holds the information for spatial statistics reporting. | 
 **layer_identifier** | **str**| The layer identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerSpatialStatistics**](LayerSpatialStatistics.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_get_spatial_statistics_by_wkt**
> LayerSpatialStatistics layer_get_spatial_statistics_by_wkt(body, layer_identifier, tenant_url_code)

Computes the area and/or length of a layer's features. The features can be filtered by value and/or by geometry.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetSpatialStatisticsByWKTParameter() # GetSpatialStatisticsByWKTParameter | The json object that holds the information for spatial statistics reporting.
layer_identifier = 'layer_identifier_example' # str | The layer identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Computes the area and/or length of a layer's features. The features can be filtered by value and/or by geometry.
    api_response = api_instance.layer_get_spatial_statistics_by_wkt(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_get_spatial_statistics_by_wkt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetSpatialStatisticsByWKTParameter**](GetSpatialStatisticsByWKTParameter.md)| The json object that holds the information for spatial statistics reporting. | 
 **layer_identifier** | **str**| The layer identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**LayerSpatialStatistics**](LayerSpatialStatistics.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_get_transformation_settings**
> InlineResponse2001 layer_get_transformation_settings(layer_identifier, tenant_url_code)

Gets the ids of the columns used to georeference the layer. Will return null if the layer was not created from georeferencing a data table.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the ids of the columns used to georeference the layer. Will return null if the layer was not created from georeferencing a data table.
    api_response = api_instance.layer_get_transformation_settings(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_get_transformation_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_optimize_layer**
> Layer layer_optimize_layer(layer_identifier, tenant_url_code)

Optimizes the table queries with ClickHouse. The layer must be tiled.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Optimizes the table queries with ClickHouse. The layer must be tiled.
    api_response = api_instance.layer_optimize_layer(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_optimize_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_set_data_column_unique_id**
> Layer layer_set_data_column_unique_id(layer_identifier, data_column_identifier, tenant_url_code)

Sets the layer's unique identifier column. The column becomes the primary way to identify its rows.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
data_column_identifier = 'data_column_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Sets the layer's unique identifier column. The column becomes the primary way to identify its rows.
    api_response = api_instance.layer_set_data_column_unique_id(layer_identifier, data_column_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_set_data_column_unique_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **data_column_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_set_unique_identifier**
> Layer layer_set_unique_identifier(layer_identifier, new_identifier, tenant_url_code)

Sets the layer's unique identifier.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
new_identifier = 'new_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Sets the layer's unique identifier.
    api_response = api_instance.layer_set_unique_identifier(layer_identifier, new_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_set_unique_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **new_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_synchronize_layer**
> Layer layer_synchronize_layer(layer_identifier, tenant_url_code)

Synchronizes the layer with its external service. The layer must be linked to an external data provider.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Synchronizes the layer with its external service. The layer must be linked to an external data provider.
    api_response = api_instance.layer_synchronize_layer(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_synchronize_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_update_from_zip**
> Layer layer_update_from_zip(layer_identifier, tenant_url_code, file=file)

Updates a layer from a ZIP. The ZIP content's format must match the layer.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Updates a layer from a ZIP. The ZIP content's format must match the layer.
    api_response = api_instance.layer_update_from_zip(layer_identifier, tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_update_from_zip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_update_layer**
> Layer layer_update_layer(body, layer_identifier, tenant_url_code)

Updates the layer's properties.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.LayerUpdateParameter() # LayerUpdateParameter | 
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the layer's properties.
    api_response = api_instance.layer_update_layer(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_update_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayerUpdateParameter**](LayerUpdateParameter.md)|  | 
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_update_layer_from_file_description**
> Layer layer_update_layer_from_file_description(body, layer_identifier, tenant_url_code)

Updates a layer with a file uploaded using `Layer/{layerIdentifier}/getFileDescription`.

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
api_instance = cartovista_cloud_clients.LayerApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.FileDescription() # FileDescription | 
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a layer with a file uploaded using `Layer/{layerIdentifier}/getFileDescription`.
    api_response = api_instance.layer_update_layer_from_file_description(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerApi->layer_update_layer_from_file_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileDescription**](FileDescription.md)|  | 
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

