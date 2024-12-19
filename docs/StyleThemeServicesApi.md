# cartovista_cloud_clients.StyleThemeServicesApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**style_theme_services_get_style_sheet_viewer**](StyleThemeServicesApi.md#style_theme_services_get_style_sheet_viewer) | **GET** /StyleThemeServices/GetStyleSheetViewer | 
[**style_theme_services_get_style_sheet_viewer2**](StyleThemeServicesApi.md#style_theme_services_get_style_sheet_viewer2) | **GET** /{tenantUrlCode}/WebPortalServices/StyleThemeServices/GetStyleSheetViewer | 

# **style_theme_services_get_style_sheet_viewer**
> str style_theme_services_get_style_sheet_viewer(tenant_url_code)



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
api_instance = cartovista_cloud_clients.StyleThemeServicesApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.style_theme_services_get_style_sheet_viewer(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StyleThemeServicesApi->style_theme_services_get_style_sheet_viewer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **style_theme_services_get_style_sheet_viewer2**
> str style_theme_services_get_style_sheet_viewer2(tenant_url_code)



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
api_instance = cartovista_cloud_clients.StyleThemeServicesApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.style_theme_services_get_style_sheet_viewer2(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StyleThemeServicesApi->style_theme_services_get_style_sheet_viewer2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


