# cartovista_cloud_clients.DataApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_export_data_elements**](DataApi.md#data_export_data_elements) | **POST** /{tenantUrlCode}/api/v2/data/ExportDataElements/{selectedLanguage} | Exports an Excel sheet of all the layers and tables. The file can be downloaded with &#x60;DownloadFile/download&#x60;. The language is used to localized the sheet&#x27;s name and columns.
[**data_export_data_table**](DataApi.md#data_export_data_table) | **POST** /{tenantUrlCode}/api/v2/data/export/{id} | Exports a table in an Excel file. The file can be downloaded with &#x60;DownloadFile/download&#x60;.
[**data_export_layer**](DataApi.md#data_export_layer) | **POST** /{tenantUrlCode}/api/v2/data/export/{id}/format/{format} | Exports a layer in a specific format. The file can be downloaded with &#x60;DownloadFile/download&#x60;.
[**data_get_data_elements**](DataApi.md#data_get_data_elements) | **POST** /{tenantUrlCode}/api/v2/data/elements | Gets all the layers, tables and folders the user has access to in a specific folder. If the folder id is omitted, the root folder is used.
[**data_search_all_data_elements**](DataApi.md#data_search_all_data_elements) | **POST** /{tenantUrlCode}/api/v2/data/search | Searches and retrieves all the layers and tables the user has access to.

# **data_export_data_elements**
> str data_export_data_elements(selected_language, tenant_url_code)

Exports an Excel sheet of all the layers and tables. The file can be downloaded with `DownloadFile/download`. The language is used to localized the sheet's name and columns.

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
api_instance = cartovista_cloud_clients.DataApi(cartovista_cloud_clients.ApiClient(configuration))
selected_language = 'selected_language_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Exports an Excel sheet of all the layers and tables. The file can be downloaded with `DownloadFile/download`. The language is used to localized the sheet's name and columns.
    api_response = api_instance.data_export_data_elements(selected_language, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->data_export_data_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selected_language** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_export_data_table**
> str data_export_data_table(id, tenant_url_code)

Exports a table in an Excel file. The file can be downloaded with `DownloadFile/download`.

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
api_instance = cartovista_cloud_clients.DataApi(cartovista_cloud_clients.ApiClient(configuration))
id = 'id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Exports a table in an Excel file. The file can be downloaded with `DownloadFile/download`.
    api_response = api_instance.data_export_data_table(id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->data_export_data_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_export_layer**
> str data_export_layer(id, format, tenant_url_code)

Exports a layer in a specific format. The file can be downloaded with `DownloadFile/download`.

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
api_instance = cartovista_cloud_clients.DataApi(cartovista_cloud_clients.ApiClient(configuration))
id = 'id_example' # str | 
format = cartovista_cloud_clients.LayerExportFormat() # LayerExportFormat | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Exports a layer in a specific format. The file can be downloaded with `DownloadFile/download`.
    api_response = api_instance.data_export_layer(id, format, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->data_export_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **format** | [**LayerExportFormat**](.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_get_data_elements**
> DataElements data_get_data_elements(body, tenant_url_code)

Gets all the layers, tables and folders the user has access to in a specific folder. If the folder id is omitted, the root folder is used.

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
api_instance = cartovista_cloud_clients.DataApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetDataElementsParam() # GetDataElementsParam | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the layers, tables and folders the user has access to in a specific folder. If the folder id is omitted, the root folder is used.
    api_response = api_instance.data_get_data_elements(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->data_get_data_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetDataElementsParam**](GetDataElementsParam.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataElements**](DataElements.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_search_all_data_elements**
> SearchDataElements data_search_all_data_elements(body, tenant_url_code)

Searches and retrieves all the layers and tables the user has access to.

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
api_instance = cartovista_cloud_clients.DataApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.SearchDataElementsParameter() # SearchDataElementsParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Searches and retrieves all the layers and tables the user has access to.
    api_response = api_instance.data_search_all_data_elements(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->data_search_all_data_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchDataElementsParameter**](SearchDataElementsParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**SearchDataElements**](SearchDataElements.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


