# cartovista_cloud_clients.ConfigApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_get_configuration**](ConfigApi.md#config_get_configuration) | **GET** /api/v2/Config | Gets the configuration required for the portal to work.

# **config_get_configuration**
> PortalConfiguration config_get_configuration()

Gets the configuration required for the portal to work.

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
api_instance = cartovista_cloud_clients.ConfigApi(cartovista_cloud_clients.ApiClient(configuration))

try:
    # Gets the configuration required for the portal to work.
    api_response = api_instance.config_get_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->config_get_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PortalConfiguration**](PortalConfiguration.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

