# cartovista_cloud_clients.DataTableApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_table_append_data_to_data_table**](DataTableApi.md#data_table_append_data_to_data_table) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/append | Appends the content of a file at the end of the table. The file format must match the table.
[**data_table_create_data_table**](DataTableApi.md#data_table_create_data_table) | **POST** /{tenantUrlCode}/api/v2/createDataTable | Creates a new empty table.
[**data_table_create_from_csv**](DataTableApi.md#data_table_create_from_csv) | **POST** /{tenantUrlCode}/api/v2/DataTable/createFromCSV | Creates a table from a CSV file.
[**data_table_create_from_excel**](DataTableApi.md#data_table_create_from_excel) | **POST** /{tenantUrlCode}/api/v2/DataTable/createFromExcel | Creates a new table from an Excel file. If the files has multiple sheets, only the first one is used.
[**data_table_create_from_excel2**](DataTableApi.md#data_table_create_from_excel2) | **POST** /{tenantUrlCode}/api/v2/DataTable/createFromExcel/{sheetName} | Creates a new table from an Excel file using a specific sheet.
[**data_table_de_optimize_data_table**](DataTableApi.md#data_table_de_optimize_data_table) | **GET** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/deoptimize | Disable the ClickHouse optimization for this table.
[**data_table_delete_data_table**](DataTableApi.md#data_table_delete_data_table) | **DELETE** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier} | Deletes the table.
[**data_table_delete_join**](DataTableApi.md#data_table_delete_join) | **DELETE** /{tenantUrlCode}/api/v2/join/{joinId} | Deletes a join between a table and a layer.
[**data_table_geocode_data_table**](DataTableApi.md#data_table_geocode_data_table) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/geocode | Converts a table to a point by building addresses using the list of columns.
[**data_table_georeference_data_table**](DataTableApi.md#data_table_georeference_data_table) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/georeference | Converts a table to a point layer using two of its columns as latitude and longitude.
[**data_table_get_data_table_by_identifier**](DataTableApi.md#data_table_get_data_table_by_identifier) | **GET** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier} | Gets a specifc table.
[**data_table_get_data_table_details**](DataTableApi.md#data_table_get_data_table_details) | **GET** /{tenantUrlCode}/api/v2/DataTables/{dataTableIdentifier}/details | Gets the table, its related maps, tables, columns and settings.
[**data_table_get_data_tables**](DataTableApi.md#data_table_get_data_tables) | **GET** /{tenantUrlCode}/api/v2/DataTables | Gets all the tables the user has access to.
[**data_table_get_expected_join_count**](DataTableApi.md#data_table_get_expected_join_count) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/getExpectedJoinCount | Gets the number of links between a table and a layer. The result can be for a 1-to-1 or 1-to-n join.
[**data_table_get_file_description**](DataTableApi.md#data_table_get_file_description) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/getFileDescription | Stores a temporary file for an upcoming data insert or update and returns a description of the file&#x27;s content.
[**data_table_get_layers_by_data_table_identifier**](DataTableApi.md#data_table_get_layers_by_data_table_identifier) | **GET** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/layers | Gets all the layers associated to the table (joins or parent layer, if any).
[**data_table_get_maps_by_data_table_identifier**](DataTableApi.md#data_table_get_maps_by_data_table_identifier) | **GET** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/maps | Gets all the maps that use the table.
[**data_table_get_time_range_by_data_table_identifier**](DataTableApi.md#data_table_get_time_range_by_data_table_identifier) | **GET** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/timeRange | Gets the table&#x27;s time range. The time series column must be set.
[**data_table_get_time_series_data**](DataTableApi.md#data_table_get_time_series_data) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/timeSeriesData | Returns an aggregation of the table&#x27;s data using the time series column.
[**data_table_get_time_series_data_many_features**](DataTableApi.md#data_table_get_time_series_data_many_features) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/timeSeriesDataManyFeatures | Returns an aggregation of the table&#x27;s data using the time series column.
[**data_table_get_time_series_dates**](DataTableApi.md#data_table_get_time_series_dates) | **GET** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/timeSeriesDates | Returns a list of all the dates in the time series table.
[**data_table_join_data_table**](DataTableApi.md#data_table_join_data_table) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/join | Joins a table to a layer. The number of valid links must be greater than 0.
[**data_table_optimize_data_table**](DataTableApi.md#data_table_optimize_data_table) | **GET** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/optimize | Optimizes the table queries with ClickHouse. If the table belongs to a layer, the layer must be tiled.
[**data_table_set_data_column_unique_id**](DataTableApi.md#data_table_set_data_column_unique_id) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/setDataColumnUniqueId | Sets the table&#x27;s unique identifier column. The column becomes the primary way to identify its rows.
[**data_table_set_time_series_column**](DataTableApi.md#data_table_set_time_series_column) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/time-series-column | Sets the time series column for a table. The column is required for time analyses in maps.
[**data_table_set_unique_identifier**](DataTableApi.md#data_table_set_unique_identifier) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/setUniqueIdentifier | Sets the table&#x27;s identifier.
[**data_table_update_data_table**](DataTableApi.md#data_table_update_data_table) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/update | Updates the table&#x27;s properties.
[**data_table_update_data_table_from_file**](DataTableApi.md#data_table_update_data_table_from_file) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/updateFromFile | Updates a table&#x27;s data with a file. The file&#x27;s format must match the table.
[**data_table_update_data_table_from_file_description**](DataTableApi.md#data_table_update_data_table_from_file_description) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/updateFromFileDescription | Updates a table with a file uploaded using &#x60;DataTable/{dataTableIdentifier}/getFileDescription&#x60;.

# **data_table_append_data_to_data_table**
> DataTable data_table_append_data_to_data_table(data_table_identifier, tenant_url_code, file=file)

Appends the content of a file at the end of the table. The file format must match the table.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Appends the content of a file at the end of the table. The file format must match the table.
    api_response = api_instance.data_table_append_data_to_data_table(data_table_identifier, tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_append_data_to_data_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_create_data_table**
> DataTable data_table_create_data_table(body, tenant_url_code)

Creates a new empty table.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DataTableCreateParameter() # DataTableCreateParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a new empty table.
    api_response = api_instance.data_table_create_data_table(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_create_data_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataTableCreateParameter**](DataTableCreateParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_create_from_csv**
> DataTable data_table_create_from_csv(tenant_url_code, file=file)

Creates a table from a CSV file.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Creates a table from a CSV file.
    api_response = api_instance.data_table_create_from_csv(tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_create_from_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_create_from_excel**
> DataTable data_table_create_from_excel(tenant_url_code, file=file)

Creates a new table from an Excel file. If the files has multiple sheets, only the first one is used.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Creates a new table from an Excel file. If the files has multiple sheets, only the first one is used.
    api_response = api_instance.data_table_create_from_excel(tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_create_from_excel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_create_from_excel2**
> DataTable data_table_create_from_excel2(sheet_name, tenant_url_code, file=file)

Creates a new table from an Excel file using a specific sheet.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
sheet_name = 'sheet_name_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Creates a new table from an Excel file using a specific sheet.
    api_response = api_instance.data_table_create_from_excel2(sheet_name, tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_create_from_excel2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sheet_name** | **str**|  | 
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_de_optimize_data_table**
> DataTable data_table_de_optimize_data_table(data_table_identifier, tenant_url_code)

Disable the ClickHouse optimization for this table.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Disable the ClickHouse optimization for this table.
    api_response = api_instance.data_table_de_optimize_data_table(data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_de_optimize_data_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_delete_data_table**
> DeleteDataTableResponse data_table_delete_data_table(data_table_identifier, tenant_url_code)

Deletes the table.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes the table.
    api_response = api_instance.data_table_delete_data_table(data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_delete_data_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DeleteDataTableResponse**](DeleteDataTableResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_delete_join**
> DeleteJoinResponse data_table_delete_join(body, join_id, tenant_url_code)

Deletes a join between a table and a layer.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DeleteJoinParameter() # DeleteJoinParameter | 
join_id = 'join_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes a join between a table and a layer.
    api_response = api_instance.data_table_delete_join(body, join_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_delete_join: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteJoinParameter**](DeleteJoinParameter.md)|  | 
 **join_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DeleteJoinResponse**](DeleteJoinResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_geocode_data_table**
> data_table_geocode_data_table(body, data_table_identifier, tenant_url_code)

Converts a table to a point by building addresses using the list of columns.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GeocodeDataTableParameter() # GeocodeDataTableParameter | 
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Converts a table to a point by building addresses using the list of columns.
    api_instance.data_table_geocode_data_table(body, data_table_identifier, tenant_url_code)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_geocode_data_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GeocodeDataTableParameter**](GeocodeDataTableParameter.md)|  | 
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_georeference_data_table**
> data_table_georeference_data_table(body, data_table_identifier, tenant_url_code)

Converts a table to a point layer using two of its columns as latitude and longitude.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GeoreferenceDataTableParameter() # GeoreferenceDataTableParameter | 
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Converts a table to a point layer using two of its columns as latitude and longitude.
    api_instance.data_table_georeference_data_table(body, data_table_identifier, tenant_url_code)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_georeference_data_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GeoreferenceDataTableParameter**](GeoreferenceDataTableParameter.md)|  | 
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_get_data_table_by_identifier**
> DataTable data_table_get_data_table_by_identifier(data_table_identifier, tenant_url_code)

Gets a specifc table.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specifc table.
    api_response = api_instance.data_table_get_data_table_by_identifier(data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_get_data_table_by_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_get_data_table_details**
> DataTableWithDetails data_table_get_data_table_details(data_table_identifier, tenant_url_code)

Gets the table, its related maps, tables, columns and settings.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the table, its related maps, tables, columns and settings.
    api_response = api_instance.data_table_get_data_table_details(data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_get_data_table_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataTableWithDetails**](DataTableWithDetails.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_get_data_tables**
> list[DataTable] data_table_get_data_tables(tenant_url_code)

Gets all the tables the user has access to.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the tables the user has access to.
    api_response = api_instance.data_table_get_data_tables(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_get_data_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**list[DataTable]**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_get_expected_join_count**
> JoinCount data_table_get_expected_join_count(body, data_table_identifier, tenant_url_code)

Gets the number of links between a table and a layer. The result can be for a 1-to-1 or 1-to-n join.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DataTableJoinParameter() # DataTableJoinParameter | 
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the number of links between a table and a layer. The result can be for a 1-to-1 or 1-to-n join.
    api_response = api_instance.data_table_get_expected_join_count(body, data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_get_expected_join_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataTableJoinParameter**](DataTableJoinParameter.md)|  | 
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**JoinCount**](JoinCount.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_get_file_description**
> FileDescription data_table_get_file_description(data_table_identifier, tenant_url_code, file=file)

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
# Configure API key authorization: secretKey
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Stores a temporary file for an upcoming data insert or update and returns a description of the file's content.
    api_response = api_instance.data_table_get_file_description(data_table_identifier, tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_get_file_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**FileDescription**](FileDescription.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_get_layers_by_data_table_identifier**
> list[Layer] data_table_get_layers_by_data_table_identifier(data_table_identifier, tenant_url_code)

Gets all the layers associated to the table (joins or parent layer, if any).

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the layers associated to the table (joins or parent layer, if any).
    api_response = api_instance.data_table_get_layers_by_data_table_identifier(data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_get_layers_by_data_table_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Layer]**](Layer.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_get_maps_by_data_table_identifier**
> list[Map] data_table_get_maps_by_data_table_identifier(data_table_identifier, tenant_url_code)

Gets all the maps that use the table.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the maps that use the table.
    api_response = api_instance.data_table_get_maps_by_data_table_identifier(data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_get_maps_by_data_table_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Map]**](Map.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_get_time_range_by_data_table_identifier**
> TimeRangeDTO data_table_get_time_range_by_data_table_identifier(data_table_identifier, tenant_url_code)

Gets the table's time range. The time series column must be set.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the table's time range. The time series column must be set.
    api_response = api_instance.data_table_get_time_range_by_data_table_identifier(data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_get_time_range_by_data_table_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**TimeRangeDTO**](TimeRangeDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_get_time_series_data**
> TimeSeriesData data_table_get_time_series_data(body, data_table_identifier, tenant_url_code)

Returns an aggregation of the table's data using the time series column.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.TimeSeriesOneFeatureDataParameter() # TimeSeriesOneFeatureDataParameter | 
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Returns an aggregation of the table's data using the time series column.
    api_response = api_instance.data_table_get_time_series_data(body, data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_get_time_series_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeSeriesOneFeatureDataParameter**](TimeSeriesOneFeatureDataParameter.md)|  | 
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**TimeSeriesData**](TimeSeriesData.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_get_time_series_data_many_features**
> list[TimeSeriesData] data_table_get_time_series_data_many_features(body, data_table_identifier, tenant_url_code)

Returns an aggregation of the table's data using the time series column.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.TimeSeriesManyFeaturesDataParameter() # TimeSeriesManyFeaturesDataParameter | 
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Returns an aggregation of the table's data using the time series column.
    api_response = api_instance.data_table_get_time_series_data_many_features(body, data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_get_time_series_data_many_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeSeriesManyFeaturesDataParameter**](TimeSeriesManyFeaturesDataParameter.md)|  | 
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[TimeSeriesData]**](TimeSeriesData.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_get_time_series_dates**
> list[datetime] data_table_get_time_series_dates(data_table_identifier, tenant_url_code)

Returns a list of all the dates in the time series table.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Returns a list of all the dates in the time series table.
    api_response = api_instance.data_table_get_time_series_dates(data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_get_time_series_dates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**list[datetime]**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_join_data_table**
> str data_table_join_data_table(body, data_table_identifier, tenant_url_code)

Joins a table to a layer. The number of valid links must be greater than 0.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DataTableJoinParameter() # DataTableJoinParameter | 
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Joins a table to a layer. The number of valid links must be greater than 0.
    api_response = api_instance.data_table_join_data_table(body, data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_join_data_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataTableJoinParameter**](DataTableJoinParameter.md)|  | 
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_optimize_data_table**
> DataTable data_table_optimize_data_table(data_table_identifier, tenant_url_code)

Optimizes the table queries with ClickHouse. If the table belongs to a layer, the layer must be tiled.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Optimizes the table queries with ClickHouse. If the table belongs to a layer, the layer must be tiled.
    api_response = api_instance.data_table_optimize_data_table(data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_optimize_data_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_set_data_column_unique_id**
> DataTable data_table_set_data_column_unique_id(data_table_identifier, data_column_identifier, tenant_url_code)

Sets the table's unique identifier column. The column becomes the primary way to identify its rows.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
data_column_identifier = 'data_column_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Sets the table's unique identifier column. The column becomes the primary way to identify its rows.
    api_response = api_instance.data_table_set_data_column_unique_id(data_table_identifier, data_column_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_set_data_column_unique_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **data_column_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_set_time_series_column**
> DataTable data_table_set_time_series_column(data_table_identifier, data_column_identifier, tenant_url_code)

Sets the time series column for a table. The column is required for time analyses in maps.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
data_column_identifier = 'data_column_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Sets the time series column for a table. The column is required for time analyses in maps.
    api_response = api_instance.data_table_set_time_series_column(data_table_identifier, data_column_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_set_time_series_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **data_column_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_set_unique_identifier**
> DataTable data_table_set_unique_identifier(data_table_identifier, new_identifier, tenant_url_code)

Sets the table's identifier.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
new_identifier = 'new_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Sets the table's identifier.
    api_response = api_instance.data_table_set_unique_identifier(data_table_identifier, new_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_set_unique_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **new_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_update_data_table**
> DataTable data_table_update_data_table(body, data_table_identifier, tenant_url_code)

Updates the table's properties.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DataTableUpdateParameter() # DataTableUpdateParameter | 
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the table's properties.
    api_response = api_instance.data_table_update_data_table(body, data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_update_data_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataTableUpdateParameter**](DataTableUpdateParameter.md)|  | 
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_update_data_table_from_file**
> DataTable data_table_update_data_table_from_file(data_table_identifier, tenant_url_code, file=file)

Updates a table's data with a file. The file's format must match the table.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Updates a table's data with a file. The file's format must match the table.
    api_response = api_instance.data_table_update_data_table_from_file(data_table_identifier, tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_update_data_table_from_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_table_update_data_table_from_file_description**
> DataTable data_table_update_data_table_from_file_description(body, data_table_identifier, tenant_url_code)

Updates a table with a file uploaded using `DataTable/{dataTableIdentifier}/getFileDescription`.

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
api_instance = cartovista_cloud_clients.DataTableApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateTableFromFileParameter() # UpdateTableFromFileParameter | 
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a table with a file uploaded using `DataTable/{dataTableIdentifier}/getFileDescription`.
    api_response = api_instance.data_table_update_data_table_from_file_description(body, data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTableApi->data_table_update_data_table_from_file_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTableFromFileParameter**](UpdateTableFromFileParameter.md)|  | 
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataTable**](DataTable.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


