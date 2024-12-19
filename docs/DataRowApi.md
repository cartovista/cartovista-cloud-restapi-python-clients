# cartovista_cloud_clients.DataRowApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_row_create_data_rows**](DataRowApi.md#data_row_create_data_rows) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/createDataRows | Creates new data rows in the table. A subset of the columns can be used. A layer&#x27;s table can be used.
[**data_row_create_update_data_rows**](DataRowApi.md#data_row_create_update_data_rows) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/createUpdateDataRows | Creates new data rows or updates them if they already exists in the table. A subset of the columns can be used. A layer&#x27;s table can be used.
[**data_row_delete_data_row**](DataRowApi.md#data_row_delete_data_row) | **DELETE** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/DataRow/{dataRowIdentifier} | Deletes a specific row in the table. A layer&#x27;s table can be used.
[**data_row_delete_datarows**](DataRowApi.md#data_row_delete_datarows) | **DELETE** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/DataRows | Deletes the rows in the table by identifier. Invalid identifiers are ignored.
[**data_row_get_data_row**](DataRowApi.md#data_row_get_data_row) | **GET** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/DataRow/{dataRowIdentifier} | Gets a specific row in the table. The geometry column is ignored if the table belongs to a layer.
[**data_row_get_data_rows**](DataRowApi.md#data_row_get_data_rows) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/DataRows | Gets the rows in the table.
[**data_row_update_data_row**](DataRowApi.md#data_row_update_data_row) | **POST** /{tenantUrlCode}/api/v2/DataTable/{dataTableIdentifier}/DataRow/{dataRowIdentifier}/update | Updates a specific row in the table. A subset of the columns can be used. A layer&#x27;s table can be used.

# **data_row_create_data_rows**
> ApiInsertReport data_row_create_data_rows(body, data_table_identifier, tenant_url_code)

Creates new data rows in the table. A subset of the columns can be used. A layer's table can be used.

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
api_instance = cartovista_cloud_clients.DataRowApi(cartovista_cloud_clients.ApiClient(configuration))
body = [cartovista_cloud_clients.DataRowCreateParameter()] # list[DataRowCreateParameter] | 
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates new data rows in the table. A subset of the columns can be used. A layer's table can be used.
    api_response = api_instance.data_row_create_data_rows(body, data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRowApi->data_row_create_data_rows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DataRowCreateParameter]**](DataRowCreateParameter.md)|  | 
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiInsertReport**](ApiInsertReport.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_row_create_update_data_rows**
> ApiCreateUpdateReport data_row_create_update_data_rows(body, data_table_identifier, tenant_url_code)

Creates new data rows or updates them if they already exists in the table. A subset of the columns can be used. A layer's table can be used.

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
api_instance = cartovista_cloud_clients.DataRowApi(cartovista_cloud_clients.ApiClient(configuration))
body = [cartovista_cloud_clients.DataRowCreateParameter()] # list[DataRowCreateParameter] | 
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates new data rows or updates them if they already exists in the table. A subset of the columns can be used. A layer's table can be used.
    api_response = api_instance.data_row_create_update_data_rows(body, data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRowApi->data_row_create_update_data_rows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DataRowCreateParameter]**](DataRowCreateParameter.md)|  | 
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiCreateUpdateReport**](ApiCreateUpdateReport.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_row_delete_data_row**
> ApiDeleteReport data_row_delete_data_row(data_table_identifier, data_row_identifier, tenant_url_code)

Deletes a specific row in the table. A layer's table can be used.

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
api_instance = cartovista_cloud_clients.DataRowApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
data_row_identifier = 'data_row_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes a specific row in the table. A layer's table can be used.
    api_response = api_instance.data_row_delete_data_row(data_table_identifier, data_row_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRowApi->data_row_delete_data_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **data_row_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiDeleteReport**](ApiDeleteReport.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_row_delete_datarows**
> ApiDeleteReport data_row_delete_datarows(body, data_table_identifier, tenant_url_code)

Deletes the rows in the table by identifier. Invalid identifiers are ignored.

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
api_instance = cartovista_cloud_clients.DataRowApi(cartovista_cloud_clients.ApiClient(configuration))
body = ['body_example'] # list[str] | 
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes the rows in the table by identifier. Invalid identifiers are ignored.
    api_response = api_instance.data_row_delete_datarows(body, data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRowApi->data_row_delete_datarows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiDeleteReport**](ApiDeleteReport.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_row_get_data_row**
> DataRow data_row_get_data_row(data_table_identifier, data_row_identifier, tenant_url_code)

Gets a specific row in the table. The geometry column is ignored if the table belongs to a layer.

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
api_instance = cartovista_cloud_clients.DataRowApi(cartovista_cloud_clients.ApiClient(configuration))
data_table_identifier = 'data_table_identifier_example' # str | 
data_row_identifier = 'data_row_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific row in the table. The geometry column is ignored if the table belongs to a layer.
    api_response = api_instance.data_row_get_data_row(data_table_identifier, data_row_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRowApi->data_row_get_data_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_table_identifier** | **str**|  | 
 **data_row_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataRow**](DataRow.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_row_get_data_rows**
> list[DataRow] data_row_get_data_rows(body, data_table_identifier, tenant_url_code)

Gets the rows in the table.

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
api_instance = cartovista_cloud_clients.DataRowApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DataRowsGetParameters() # DataRowsGetParameters | 
data_table_identifier = 'data_table_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the rows in the table.
    api_response = api_instance.data_row_get_data_rows(body, data_table_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRowApi->data_row_get_data_rows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataRowsGetParameters**](DataRowsGetParameters.md)|  | 
 **data_table_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[DataRow]**](DataRow.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_row_update_data_row**
> DataRow data_row_update_data_row(body, data_table_identifier, data_row_identifier, tenant_url_code)

Updates a specific row in the table. A subset of the columns can be used. A layer's table can be used.

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
api_instance = cartovista_cloud_clients.DataRowApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DataRowUpdateParameter() # DataRowUpdateParameter | 
data_table_identifier = 'data_table_identifier_example' # str | 
data_row_identifier = 'data_row_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a specific row in the table. A subset of the columns can be used. A layer's table can be used.
    api_response = api_instance.data_row_update_data_row(body, data_table_identifier, data_row_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRowApi->data_row_update_data_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataRowUpdateParameter**](DataRowUpdateParameter.md)|  | 
 **data_table_identifier** | **str**|  | 
 **data_row_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataRow**](DataRow.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


