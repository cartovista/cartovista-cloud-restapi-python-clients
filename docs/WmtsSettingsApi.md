# cartovista_cloud_clients.WmtsSettingsApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wmts_settings_get_wmts_settings**](WmtsSettingsApi.md#wmts_settings_get_wmts_settings) | **GET** /{tenantUrlCode}/api/v2/wmts-settings/{wmtsSettingsId} | Gets the WMTS settings.
[**wmts_settings_update_wmts_settings**](WmtsSettingsApi.md#wmts_settings_update_wmts_settings) | **PATCH** /{tenantUrlCode}/api/v2/wmts-settings/{wmtsSettingsId} | Updates the WMTS settings.

# **wmts_settings_get_wmts_settings**
> WmtsSettings wmts_settings_get_wmts_settings(wmts_settings_id, tenant_url_code)

Gets the WMTS settings.

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
api_instance = cartovista_cloud_clients.WmtsSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
wmts_settings_id = 'wmts_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the WMTS settings.
    api_response = api_instance.wmts_settings_get_wmts_settings(wmts_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmtsSettingsApi->wmts_settings_get_wmts_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wmts_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**WmtsSettings**](WmtsSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wmts_settings_update_wmts_settings**
> WmtsSettings wmts_settings_update_wmts_settings(body, wmts_settings_id, tenant_url_code)

Updates the WMTS settings.

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
api_instance = cartovista_cloud_clients.WmtsSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateWmtsSettings() # UpdateWmtsSettings | 
wmts_settings_id = 'wmts_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the WMTS settings.
    api_response = api_instance.wmts_settings_update_wmts_settings(body, wmts_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmtsSettingsApi->wmts_settings_update_wmts_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWmtsSettings**](UpdateWmtsSettings.md)|  | 
 **wmts_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**WmtsSettings**](WmtsSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


