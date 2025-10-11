# cartovista_cloud_clients.DataColumnApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_column_create_data_column**](DataColumnApi.md#data_column_create_data_column) | **POST** /{tenantUrlCode}/api/v2/{identifier}/createDataColumn | Creates a new data column for a layer or datatable.
[**data_column_create_data_table_data_columns**](DataColumnApi.md#data_column_create_data_table_data_columns) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/createDataColumns | Creates new data columns in a data table. A layer&#x27;s table can be used.
[**data_column_create_layer_data_columns**](DataColumnApi.md#data_column_create_layer_data_columns) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/createDataColumns | Creates new data columns in a layer.
[**data_column_delete_data_table_data_column**](DataColumnApi.md#data_column_delete_data_table_data_column) | **DELETE** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/DataColumn/{dataColumnIdentifier} | Deletes a column in the table. A layer&#x27;s table can be used.
[**data_column_delete_layer_data_column**](DataColumnApi.md#data_column_delete_layer_data_column) | **DELETE** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/DataColumn/{dataColumnIdentifier} | Deletes a column in the layer.
[**data_column_get_bulk_edit_layer_data_columns**](DataColumnApi.md#data_column_get_bulk_edit_layer_data_columns) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/BulkEditDataColumns | Gets all the data columns usable in the bulk editor in the layer.
[**data_column_get_data_table_data_column**](DataColumnApi.md#data_column_get_data_table_data_column) | **GET** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/DataColumn/{dataColumnIdentifier} | Gets a specific column in the table. A layer&#x27;s table can be used.
[**data_column_get_data_table_data_columns**](DataColumnApi.md#data_column_get_data_table_data_columns) | **GET** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/DataColumns | Gets all the data columns in the table. A layer&#x27;s table can be used.
[**data_column_get_layer_data_column**](DataColumnApi.md#data_column_get_layer_data_column) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/DataColumn/{dataColumnIdentifier} | Gets a specific column in the layer.
[**data_column_get_layer_data_columns**](DataColumnApi.md#data_column_get_layer_data_columns) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/DataColumns | Gets all the data columns in the layer.
[**data_column_recompute_calculated_values**](DataColumnApi.md#data_column_recompute_calculated_values) | **PATCH** /{tenantUrlCode}/api/v2/DataColumn/{dataColumnId}/recompute-calculated-values | 
[**data_column_set_data_table_column_unique_identifier**](DataColumnApi.md#data_column_set_data_table_column_unique_identifier) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/DataColumn/{dataColumnIdentifier}/setUniqueIdentifier | Sets the unique identifier for a table. The column becomes the primary way to identify the row.
[**data_column_set_layer_column_unique_identifier**](DataColumnApi.md#data_column_set_layer_column_unique_identifier) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/DataColumn/{dataColumnIdentifier}/setUniqueIdentifier | Sets the unique identifier for a layer. The column becomes the primary way to identify the feature.
[**data_column_update_calculated_values**](DataColumnApi.md#data_column_update_calculated_values) | **PATCH** /{tenantUrlCode}/api/v2/DataColumn/{dataColumnId}/calculated-values | 
[**data_column_update_data_table_data_column**](DataColumnApi.md#data_column_update_data_table_data_column) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/DataColumn/{dataColumnIdentifier}/update | Updates a column in the table. A layer&#x27;s table can be used.
[**data_column_update_domain_of_values_date_time**](DataColumnApi.md#data_column_update_domain_of_values_date_time) | **PATCH** /{tenantUrlCode}/api/v2/DataColumn/{dataColumnId}/domain-of-values-datetime | 
[**data_column_update_domain_of_values_numeric**](DataColumnApi.md#data_column_update_domain_of_values_numeric) | **PATCH** /{tenantUrlCode}/api/v2/DataColumn/{dataColumnId}/domain-of-values-numeric | 
[**data_column_update_domain_of_values_string**](DataColumnApi.md#data_column_update_domain_of_values_string) | **PATCH** /{tenantUrlCode}/api/v2/DataColumn/{dataColumnId}/domain-of-values-string | 
[**data_column_update_layer_data_column**](DataColumnApi.md#data_column_update_layer_data_column) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/DataColumn/{dataColumnIdentifier}/update | Updates a column in the layer.

# **data_column_create_data_column**
> DataColumn data_column_create_data_column(body, is_spatial_layer, identifier, tenant_url_code)

Creates a new data column for a layer or datatable.

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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DataColumnCreateParameter() # DataColumnCreateParameter | 
is_spatial_layer = true # bool | 
identifier = 'identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a new data column for a layer or datatable.
    api_response = api_instance.data_column_create_data_column(body, is_spatial_layer, identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_create_data_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataColumnCreateParameter**](DataColumnCreateParameter.md)|  | 
 **is_spatial_layer** | **bool**|  | 
 **identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataColumn**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_create_data_table_data_columns**
> ApiInsertReport data_column_create_data_table_data_columns(body, data_table_identifier, tenant_url_code)

Creates new data columns in a data table. A layer's table can be used.

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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
body = [cartovista_cloud_clients.DataColumnCreateParameter()] # list[DataColumnCreateParameter] | 
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates new data columns in a data table. A layer's table can be used.
    api_response = api_instance.data_column_create_data_table_data_columns(body, data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_create_data_table_data_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DataColumnCreateParameter]**](DataColumnCreateParameter.md)|  | 
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiInsertReport**](ApiInsertReport.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_create_layer_data_columns**
> ApiInsertReport data_column_create_layer_data_columns(body, layer_identifier, tenant_url_code)

Creates new data columns in a layer.

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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
body = [cartovista_cloud_clients.DataColumnCreateParameter()] # list[DataColumnCreateParameter] | 
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates new data columns in a layer.
    api_response = api_instance.data_column_create_layer_data_columns(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_create_layer_data_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DataColumnCreateParameter]**](DataColumnCreateParameter.md)|  | 
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiInsertReport**](ApiInsertReport.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_delete_data_table_data_column**
> data_column_delete_data_table_data_column(data_table_identifier, data_column_identifier, tenant_url_code)

Deletes a column in the table. A layer's table can be used.

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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
data_column_identifier = 'data_column_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes a column in the table. A layer's table can be used.
    api_instance.data_column_delete_data_table_data_column(data_table_identifier, data_column_identifier, tenant_url_code)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_delete_data_table_data_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **data_column_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_delete_layer_data_column**
> data_column_delete_layer_data_column(layer_identifier, data_column_identifier, tenant_url_code)

Deletes a column in the layer.

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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
data_column_identifier = 'data_column_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes a column in the layer.
    api_instance.data_column_delete_layer_data_column(layer_identifier, data_column_identifier, tenant_url_code)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_delete_layer_data_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **data_column_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_get_bulk_edit_layer_data_columns**
> list[DataColumn] data_column_get_bulk_edit_layer_data_columns(layer_identifier, tenant_url_code)

Gets all the data columns usable in the bulk editor in the layer.

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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the data columns usable in the bulk editor in the layer.
    api_response = api_instance.data_column_get_bulk_edit_layer_data_columns(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_get_bulk_edit_layer_data_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[DataColumn]**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_get_data_table_data_column**
> DataColumn data_column_get_data_table_data_column(data_table_identifier, data_column_identifier, tenant_url_code)

Gets a specific column in the table. A layer's table can be used.

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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
data_column_identifier = 'data_column_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific column in the table. A layer's table can be used.
    api_response = api_instance.data_column_get_data_table_data_column(data_table_identifier, data_column_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_get_data_table_data_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **data_column_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataColumn**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_get_data_table_data_columns**
> list[DataColumn] data_column_get_data_table_data_columns(data_table_identifier, tenant_url_code)

Gets all the data columns in the table. A layer's table can be used.

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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the data columns in the table. A layer's table can be used.
    api_response = api_instance.data_column_get_data_table_data_columns(data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_get_data_table_data_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[DataColumn]**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_get_layer_data_column**
> DataColumn data_column_get_layer_data_column(layer_identifier, data_column_identifier, tenant_url_code)

Gets a specific column in the layer.

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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
data_column_identifier = 'data_column_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific column in the layer.
    api_response = api_instance.data_column_get_layer_data_column(layer_identifier, data_column_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_get_layer_data_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **data_column_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataColumn**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_get_layer_data_columns**
> list[DataColumn] data_column_get_layer_data_columns(layer_identifier, tenant_url_code)

Gets all the data columns in the layer.

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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the data columns in the layer.
    api_response = api_instance.data_column_get_layer_data_columns(layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_get_layer_data_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[DataColumn]**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_recompute_calculated_values**
> DataColumn data_column_recompute_calculated_values(data_column_id, tenant_url_code)



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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
data_column_id = 'data_column_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.data_column_recompute_calculated_values(data_column_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_recompute_calculated_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_column_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataColumn**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_set_data_table_column_unique_identifier**
> DataColumn data_column_set_data_table_column_unique_identifier(data_table_identifier, data_column_identifier, new_identifier, tenant_url_code)

Sets the unique identifier for a table. The column becomes the primary way to identify the row.

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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
data_column_identifier = 'data_column_identifier_example' # str | 
new_identifier = 'new_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Sets the unique identifier for a table. The column becomes the primary way to identify the row.
    api_response = api_instance.data_column_set_data_table_column_unique_identifier(data_table_identifier, data_column_identifier, new_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_set_data_table_column_unique_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **data_column_identifier** | **str**|  | 
 **new_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataColumn**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_set_layer_column_unique_identifier**
> DataColumn data_column_set_layer_column_unique_identifier(layer_identifier, data_column_identifier, new_identifier, tenant_url_code)

Sets the unique identifier for a layer. The column becomes the primary way to identify the feature.

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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | 
data_column_identifier = 'data_column_identifier_example' # str | 
new_identifier = 'new_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Sets the unique identifier for a layer. The column becomes the primary way to identify the feature.
    api_response = api_instance.data_column_set_layer_column_unique_identifier(layer_identifier, data_column_identifier, new_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_set_layer_column_unique_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**|  | 
 **data_column_identifier** | **str**|  | 
 **new_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataColumn**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_update_calculated_values**
> CalculatedValuesUpdateResponse data_column_update_calculated_values(body, data_column_id, tenant_url_code)



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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CalculatedValuesUpdateParameter() # CalculatedValuesUpdateParameter | 
data_column_id = 'data_column_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.data_column_update_calculated_values(body, data_column_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_update_calculated_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CalculatedValuesUpdateParameter**](CalculatedValuesUpdateParameter.md)|  | 
 **data_column_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**CalculatedValuesUpdateResponse**](CalculatedValuesUpdateResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_update_data_table_data_column**
> DataColumn data_column_update_data_table_data_column(body, data_table_identifier, data_column_identifier, tenant_url_code)

Updates a column in the table. A layer's table can be used.

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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DataColumnUpdateParameter() # DataColumnUpdateParameter | 
data_table_identifier = 'data_table_identifier_example' # str | 
data_column_identifier = 'data_column_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a column in the table. A layer's table can be used.
    api_response = api_instance.data_column_update_data_table_data_column(body, data_table_identifier, data_column_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_update_data_table_data_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataColumnUpdateParameter**](DataColumnUpdateParameter.md)|  | 
 **data_table_identifier** | **str**|  | 
 **data_column_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataColumn**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_update_domain_of_values_date_time**
> DataColumn data_column_update_domain_of_values_date_time(body, data_column_id, tenant_url_code)



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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DomainOfValuesDateTime() # DomainOfValuesDateTime | 
data_column_id = 'data_column_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.data_column_update_domain_of_values_date_time(body, data_column_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_update_domain_of_values_date_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainOfValuesDateTime**](DomainOfValuesDateTime.md)|  | 
 **data_column_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataColumn**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_update_domain_of_values_numeric**
> DataColumn data_column_update_domain_of_values_numeric(body, data_column_id, tenant_url_code)



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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DomainOfValuesNumeric() # DomainOfValuesNumeric | 
data_column_id = 'data_column_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.data_column_update_domain_of_values_numeric(body, data_column_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_update_domain_of_values_numeric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainOfValuesNumeric**](DomainOfValuesNumeric.md)|  | 
 **data_column_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataColumn**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_update_domain_of_values_string**
> DataColumn data_column_update_domain_of_values_string(body, data_column_id, tenant_url_code)



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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DomainOfValuesString() # DomainOfValuesString | 
data_column_id = 'data_column_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.data_column_update_domain_of_values_string(body, data_column_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_update_domain_of_values_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainOfValuesString**](DomainOfValuesString.md)|  | 
 **data_column_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataColumn**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_column_update_layer_data_column**
> DataColumn data_column_update_layer_data_column(body, layer_identifier, data_column_identifier, tenant_url_code)

Updates a column in the layer.

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
# Configure API key authorization: bearer
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataColumnApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DataColumnUpdateParameter() # DataColumnUpdateParameter | 
layer_identifier = 'layer_identifier_example' # str | 
data_column_identifier = 'data_column_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a column in the layer.
    api_response = api_instance.data_column_update_layer_data_column(body, layer_identifier, data_column_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataColumnApi->data_column_update_layer_data_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataColumnUpdateParameter**](DataColumnUpdateParameter.md)|  | 
 **layer_identifier** | **str**|  | 
 **data_column_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataColumn**](DataColumn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)






