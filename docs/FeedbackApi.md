# cartovista_cloud_clients.FeedbackApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feedback_send_feedback**](FeedbackApi.md#feedback_send_feedback) | **POST** /{tenantUrlCode}/api/v2/feedback/{mapId} | Saves user feedback about a map.

# **feedback_send_feedback**
> feedback_send_feedback(body, map_id, tenant_url_code)

Saves user feedback about a map.

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
api_instance = cartovista_cloud_clients.FeedbackApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.FeedbackContent() # FeedbackContent | 
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Saves user feedback about a map.
    api_instance.feedback_send_feedback(body, map_id, tenant_url_code)
except ApiException as e:
    print("Exception when calling FeedbackApi->feedback_send_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeedbackContent**](FeedbackContent.md)|  | 
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

