# cartovista_cloud_clients.PortalApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portal_cancel_upload**](PortalApi.md#portal_cancel_upload) | **POST** /{tenantUrlCode}/api/v2/Portal/upload/{uploadId}/cancel | Cancels the file upload.
[**portal_finalize_upload**](PortalApi.md#portal_finalize_upload) | **POST** /{tenantUrlCode}/api/v2/Portal/upload/{uploadId}/finalize | Finalizes a data import with a file uploaded using &#x60;upload&#x60;.
[**portal_get_definition**](PortalApi.md#portal_get_definition) | **GET** /{tenantUrlCode}/api/v2/Portal/upload/{uploadId}/definition | Gets a description of the file&#x27;s content.
[**portal_get_subscription_and_user**](PortalApi.md#portal_get_subscription_and_user) | **GET** /{tenantUrlCode}/api/v2/Portal | Gets the current user and the organization&#x27;s subscription/license details.
[**portal_upload**](PortalApi.md#portal_upload) | **POST** /{tenantUrlCode}/api/v2/Portal/upload | Uploads a temporary file for layer use.

# **portal_cancel_upload**
> bool portal_cancel_upload(upload_id, tenant_url_code)

Cancels the file upload.

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
api_instance = cartovista_cloud_clients.PortalApi(cartovista_cloud_clients.ApiClient(configuration))
upload_id = 'upload_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Cancels the file upload.
    api_response = api_instance.portal_cancel_upload(upload_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portal_cancel_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_finalize_upload**
> portal_finalize_upload(body, upload_id, tenant_url_code)

Finalizes a data import with a file uploaded using `upload`.

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
api_instance = cartovista_cloud_clients.PortalApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.FinalizeUploadParameters() # FinalizeUploadParameters | 
upload_id = 'upload_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Finalizes a data import with a file uploaded using `upload`.
    api_instance.portal_finalize_upload(body, upload_id, tenant_url_code)
except ApiException as e:
    print("Exception when calling PortalApi->portal_finalize_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FinalizeUploadParameters**](FinalizeUploadParameters.md)|  | 
 **upload_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_get_definition**
> FileDescription portal_get_definition(upload_id, tenant_url_code)

Gets a description of the file's content.

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
api_instance = cartovista_cloud_clients.PortalApi(cartovista_cloud_clients.ApiClient(configuration))
upload_id = 'upload_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a description of the file's content.
    api_response = api_instance.portal_get_definition(upload_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portal_get_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**FileDescription**](FileDescription.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_get_subscription_and_user**
> SubscriptionAndUser portal_get_subscription_and_user(tenant_url_code)

Gets the current user and the organization's subscription/license details.

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
api_instance = cartovista_cloud_clients.PortalApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the current user and the organization's subscription/license details.
    api_response = api_instance.portal_get_subscription_and_user(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portal_get_subscription_and_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**SubscriptionAndUser**](SubscriptionAndUser.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_upload**
> str portal_upload(upload_id, tenant_url_code, file=file)

Uploads a temporary file for layer use.

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
api_instance = cartovista_cloud_clients.PortalApi(cartovista_cloud_clients.ApiClient(configuration))
upload_id = 'upload_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Uploads a temporary file for layer use.
    api_response = api_instance.portal_upload(upload_id, tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portal_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


