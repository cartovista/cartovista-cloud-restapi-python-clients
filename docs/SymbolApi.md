# cartovista_cloud_clients.SymbolApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**symbol_create_symbol**](SymbolApi.md#symbol_create_symbol) | **POST** /{tenantUrlCode}/api/v2/symbols | Creates a new custom symbol from a file.
[**symbol_delete_symbol**](SymbolApi.md#symbol_delete_symbol) | **DELETE** /{tenantUrlCode}/api/v2/symbols/{id} | Deletes the symbol.
[**symbol_get_symbols**](SymbolApi.md#symbol_get_symbols) | **GET** /{tenantUrlCode}/api/v2/symbols | Gets all the custom symbols.

# **symbol_create_symbol**
> Symbol symbol_create_symbol(tenant_url_code, file=file)

Creates a new custom symbol from a file.

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
api_instance = cartovista_cloud_clients.SymbolApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Creates a new custom symbol from a file.
    api_response = api_instance.symbol_create_symbol(tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SymbolApi->symbol_create_symbol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**Symbol**](Symbol.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **symbol_delete_symbol**
> DeleteSymbolResponse symbol_delete_symbol(id, tenant_url_code)

Deletes the symbol.

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
api_instance = cartovista_cloud_clients.SymbolApi(cartovista_cloud_clients.ApiClient(configuration))
id = 'id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes the symbol.
    api_response = api_instance.symbol_delete_symbol(id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SymbolApi->symbol_delete_symbol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DeleteSymbolResponse**](DeleteSymbolResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **symbol_get_symbols**
> list[Symbol] symbol_get_symbols(tenant_url_code)

Gets all the custom symbols.

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
api_instance = cartovista_cloud_clients.SymbolApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the custom symbols.
    api_response = api_instance.symbol_get_symbols(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SymbolApi->symbol_get_symbols: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Symbol]**](Symbol.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

