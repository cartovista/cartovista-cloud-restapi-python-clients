# cartovista_cloud_clients.PluginApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plugin_create_plugin**](PluginApi.md#plugin_create_plugin) | **POST** /{tenantUrlCode}/api/v2/plugins | Create a plugin in a specific tenant.
[**plugin_delete_plugin**](PluginApi.md#plugin_delete_plugin) | **DELETE** /{tenantUrlCode}/api/v2/plugins/{id} | Delete a specific plugin.
[**plugin_get_plugin**](PluginApi.md#plugin_get_plugin) | **GET** /{tenantUrlCode}/api/v2/plugins/{id} | Get a specific plugin by id.
[**plugin_get_plugins**](PluginApi.md#plugin_get_plugins) | **GET** /{tenantUrlCode}/api/v2/plugins | Get all the plugins for a specific tenant.
[**plugin_update_plugin**](PluginApi.md#plugin_update_plugin) | **PATCH** /{tenantUrlCode}/api/v2/plugins/{id} | Update a specific plugin.

# **plugin_create_plugin**
> Plugin plugin_create_plugin(body, tenant_url_code)

Create a plugin in a specific tenant.

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
api_instance = cartovista_cloud_clients.PluginApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreateUpdatePlugin() # CreateUpdatePlugin | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Create a plugin in a specific tenant.
    api_response = api_instance.plugin_create_plugin(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginApi->plugin_create_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUpdatePlugin**](CreateUpdatePlugin.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Plugin**](Plugin.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugin_delete_plugin**
> plugin_delete_plugin(id, tenant_url_code)

Delete a specific plugin.

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
api_instance = cartovista_cloud_clients.PluginApi(cartovista_cloud_clients.ApiClient(configuration))
id = 'id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Delete a specific plugin.
    api_instance.plugin_delete_plugin(id, tenant_url_code)
except ApiException as e:
    print("Exception when calling PluginApi->plugin_delete_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugin_get_plugin**
> Plugin plugin_get_plugin(id, tenant_url_code)

Get a specific plugin by id.

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
api_instance = cartovista_cloud_clients.PluginApi(cartovista_cloud_clients.ApiClient(configuration))
id = 'id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Get a specific plugin by id.
    api_response = api_instance.plugin_get_plugin(id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginApi->plugin_get_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Plugin**](Plugin.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugin_get_plugins**
> list[Plugin] plugin_get_plugins(tenant_url_code)

Get all the plugins for a specific tenant.

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
api_instance = cartovista_cloud_clients.PluginApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Get all the plugins for a specific tenant.
    api_response = api_instance.plugin_get_plugins(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginApi->plugin_get_plugins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Plugin]**](Plugin.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugin_update_plugin**
> Plugin plugin_update_plugin(body, id, tenant_url_code)

Update a specific plugin.

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
api_instance = cartovista_cloud_clients.PluginApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreateUpdatePlugin() # CreateUpdatePlugin | 
id = 'id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Update a specific plugin.
    api_response = api_instance.plugin_update_plugin(body, id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginApi->plugin_update_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUpdatePlugin**](CreateUpdatePlugin.md)|  | 
 **id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Plugin**](Plugin.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


