# cartovista_cloud_clients.StatisticsApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistics_get_statistics**](StatisticsApi.md#statistics_get_statistics) | **POST** /{tenantUrlCode}/api/v2/statistics | Gets the usage statistics of the organization.

# **statistics_get_statistics**
> ModificationHistoryPage statistics_get_statistics(body, tenant_url_code)

Gets the usage statistics of the organization.

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
api_instance = cartovista_cloud_clients.StatisticsApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetStatisticsParameters() # GetStatisticsParameters | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the usage statistics of the organization.
    api_response = api_instance.statistics_get_statistics(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_get_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetStatisticsParameters**](GetStatisticsParameters.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ModificationHistoryPage**](ModificationHistoryPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

