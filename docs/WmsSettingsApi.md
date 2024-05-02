# cartovista_cloud_clients.WmsSettingsApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wms_settings_get_wms_settings**](WmsSettingsApi.md#wms_settings_get_wms_settings) | **GET** /{tenantUrlCode}/api/v2/wms-settings/{wmsSettingsId} | Gets the WMS settings.
[**wms_settings_update_wms_settings**](WmsSettingsApi.md#wms_settings_update_wms_settings) | **PATCH** /{tenantUrlCode}/api/v2/wms-settings/{wmsSettingsId} | Updates the WMS settings.

# **wms_settings_get_wms_settings**
> WmsSettings wms_settings_get_wms_settings(wms_settings_id, tenant_url_code)

Gets the WMS settings.

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
api_instance = cartovista_cloud_clients.WmsSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
wms_settings_id = 'wms_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the WMS settings.
    api_response = api_instance.wms_settings_get_wms_settings(wms_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmsSettingsApi->wms_settings_get_wms_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wms_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**WmsSettings**](WmsSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wms_settings_update_wms_settings**
> WmsSettings wms_settings_update_wms_settings(body, wms_settings_id, tenant_url_code)

Updates the WMS settings.

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
api_instance = cartovista_cloud_clients.WmsSettingsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateWmsSettings() # UpdateWmsSettings | 
wms_settings_id = 'wms_settings_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the WMS settings.
    api_response = api_instance.wms_settings_update_wms_settings(body, wms_settings_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WmsSettingsApi->wms_settings_update_wms_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWmsSettings**](UpdateWmsSettings.md)|  | 
 **wms_settings_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**WmsSettings**](WmsSettings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

