# cartovista_cloud_clients.ViewApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**view_create_view_by_expression**](ViewApi.md#view_create_view_by_expression) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerId}/views/createByExpression | Creates a view based on an expression.
[**view_create_views_from_column**](ViewApi.md#view_create_views_from_column) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerId}/views/createByColumn | Creates views based on a layer column id. This will generate one view for each unique value of the selected column.
[**view_delete_views**](ViewApi.md#view_delete_views) | **DELETE** /{tenantUrlCode}/api/v2/Layer/{layerId}/views | Deletes all the views associated with the layer.
[**view_get_view**](ViewApi.md#view_get_view) | **GET** /{tenantUrlCode}/api/v2/Layer/views/{viewId} | Gets a specific view by id.
[**view_get_views**](ViewApi.md#view_get_views) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerId}/views | Gets the list of views associated with a layer.
[**view_update_view**](ViewApi.md#view_update_view) | **PATCH** /{tenantUrlCode}/api/v2/Layer/{layerId}/views/{viewId} | Updates the view parameters.
[**view_update_view_permissions**](ViewApi.md#view_update_view_permissions) | **PATCH** /{tenantUrlCode}/api/v2/Layer/{layerId}/views/{viewId}/permissions | Updates the view permissions. Note: This needs to list all the permissions on the view as the missing permissions will be deleted.

# **view_create_view_by_expression**
> View view_create_view_by_expression(body, layer_id, tenant_url_code)

Creates a view based on an expression.

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
api_instance = cartovista_cloud_clients.ViewApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreateViewByExpressionParameters() # CreateViewByExpressionParameters | The parameters to create the view.
layer_id = 'layer_id_example' # str | The layer system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a view based on an expression.
    api_response = api_instance.view_create_view_by_expression(body, layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewApi->view_create_view_by_expression: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateViewByExpressionParameters**](CreateViewByExpressionParameters.md)| The parameters to create the view. | 
 **layer_id** | **str**| The layer system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**View**](View.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_create_views_from_column**
> list[View] view_create_views_from_column(body, layer_id, tenant_url_code)

Creates views based on a layer column id. This will generate one view for each unique value of the selected column.

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
api_instance = cartovista_cloud_clients.ViewApi(cartovista_cloud_clients.ApiClient(configuration))
body = 'body_example' # str | The column system identifier.
layer_id = 'layer_id_example' # str | The layer system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates views based on a layer column id. This will generate one view for each unique value of the selected column.
    api_response = api_instance.view_create_views_from_column(body, layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewApi->view_create_views_from_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The column system identifier. | 
 **layer_id** | **str**| The layer system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[View]**](View.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_delete_views**
> view_delete_views(layer_id, tenant_url_code)

Deletes all the views associated with the layer.

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
api_instance = cartovista_cloud_clients.ViewApi(cartovista_cloud_clients.ApiClient(configuration))
layer_id = 'layer_id_example' # str | The layer system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes all the views associated with the layer.
    api_instance.view_delete_views(layer_id, tenant_url_code)
except ApiException as e:
    print("Exception when calling ViewApi->view_delete_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_id** | **str**| The layer system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_get_view**
> View view_get_view(view_id, tenant_url_code)

Gets a specific view by id.

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
api_instance = cartovista_cloud_clients.ViewApi(cartovista_cloud_clients.ApiClient(configuration))
view_id = 'view_id_example' # str | The view system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific view by id.
    api_response = api_instance.view_get_view(view_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewApi->view_get_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**View**](View.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_get_views**
> list[View] view_get_views(layer_id, tenant_url_code)

Gets the list of views associated with a layer.

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
api_instance = cartovista_cloud_clients.ViewApi(cartovista_cloud_clients.ApiClient(configuration))
layer_id = 'layer_id_example' # str | The layer system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the list of views associated with a layer.
    api_response = api_instance.view_get_views(layer_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewApi->view_get_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_id** | **str**| The layer system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[View]**](View.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_update_view**
> View view_update_view(body, layer_id, view_id, tenant_url_code)

Updates the view parameters.

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
api_instance = cartovista_cloud_clients.ViewApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateViewParameter() # UpdateViewParameter | The parameters to update.
layer_id = 'layer_id_example' # str | The layer system identifier.
view_id = 'view_id_example' # str | The view system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the view parameters.
    api_response = api_instance.view_update_view(body, layer_id, view_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewApi->view_update_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateViewParameter**](UpdateViewParameter.md)| The parameters to update. | 
 **layer_id** | **str**| The layer system identifier. | 
 **view_id** | **str**| The view system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**View**](View.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_update_view_permissions**
> View view_update_view_permissions(body, layer_id, view_id, tenant_url_code)

Updates the view permissions. Note: This needs to list all the permissions on the view as the missing permissions will be deleted.

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
api_instance = cartovista_cloud_clients.ViewApi(cartovista_cloud_clients.ApiClient(configuration))
body = [cartovista_cloud_clients.ViewReadPermission()] # list[ViewReadPermission] | The list of permissions to assign to the view.
layer_id = 'layer_id_example' # str | The layer system identifier.
view_id = 'view_id_example' # str | The view system identifier.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the view permissions. Note: This needs to list all the permissions on the view as the missing permissions will be deleted.
    api_response = api_instance.view_update_view_permissions(body, layer_id, view_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewApi->view_update_view_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ViewReadPermission]**](ViewReadPermission.md)| The list of permissions to assign to the view. | 
 **layer_id** | **str**| The layer system identifier. | 
 **view_id** | **str**| The view system identifier. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**View**](View.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


