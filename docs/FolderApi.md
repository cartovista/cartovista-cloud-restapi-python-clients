# cartovista_cloud_clients.FolderApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_create_folder**](FolderApi.md#folder_create_folder) | **POST** /{tenantUrlCode}/api/v2/folder | Creates a new folder.
[**folder_delete_folder**](FolderApi.md#folder_delete_folder) | **DELETE** /{tenantUrlCode}/api/v2/folder/{id} | Deletes a folder.
[**folder_get_folder**](FolderApi.md#folder_get_folder) | **GET** /{tenantUrlCode}/api/v2/folder/{id} | Gets a specific folder.
[**folder_get_folders**](FolderApi.md#folder_get_folders) | **POST** /{tenantUrlCode}/api/v2/folder/search | Searches all the folders inside a parent.
[**folder_get_folders_with_path**](FolderApi.md#folder_get_folders_with_path) | **POST** /{tenantUrlCode}/api/v2/folder/folders-with-path | Gets all the folders in a given parent and the path to that parent.
[**folder_update_folder**](FolderApi.md#folder_update_folder) | **PATCH** /{tenantUrlCode}/api/v2/folder/{id} | Updates a folder&#x27;s properties.
[**folder_update_item_parent_folder**](FolderApi.md#folder_update_item_parent_folder) | **PATCH** /{tenantUrlCode}/api/v2/folder/parent | Moves an item to a different folder.

# **folder_create_folder**
> Folder folder_create_folder(body, tenant_url_code)

Creates a new folder.

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
api_instance = cartovista_cloud_clients.FolderApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreateFolder() # CreateFolder | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a new folder.
    api_response = api_instance.folder_create_folder(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderApi->folder_create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFolder**](CreateFolder.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_delete_folder**
> folder_delete_folder(id, tenant_url_code)

Deletes a folder.

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
api_instance = cartovista_cloud_clients.FolderApi(cartovista_cloud_clients.ApiClient(configuration))
id = 'id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes a folder.
    api_instance.folder_delete_folder(id, tenant_url_code)
except ApiException as e:
    print("Exception when calling FolderApi->folder_delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_get_folder**
> Folder folder_get_folder(id, tenant_url_code)

Gets a specific folder.

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
api_instance = cartovista_cloud_clients.FolderApi(cartovista_cloud_clients.ApiClient(configuration))
id = 'id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific folder.
    api_response = api_instance.folder_get_folder(id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderApi->folder_get_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_get_folders**
> list[Folder] folder_get_folders(body, tenant_url_code)

Searches all the folders inside a parent.

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
api_instance = cartovista_cloud_clients.FolderApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetFoldersParameters() # GetFoldersParameters | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Searches all the folders inside a parent.
    api_response = api_instance.folder_get_folders(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderApi->folder_get_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetFoldersParameters**](GetFoldersParameters.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Folder]**](Folder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_get_folders_with_path**
> FoldersWithPath folder_get_folders_with_path(body, tenant_url_code)

Gets all the folders in a given parent and the path to that parent.

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
api_instance = cartovista_cloud_clients.FolderApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetFoldersParameters() # GetFoldersParameters | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the folders in a given parent and the path to that parent.
    api_response = api_instance.folder_get_folders_with_path(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderApi->folder_get_folders_with_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetFoldersParameters**](GetFoldersParameters.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**FoldersWithPath**](FoldersWithPath.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_update_folder**
> Folder folder_update_folder(body, id, tenant_url_code)

Updates a folder's properties.

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
api_instance = cartovista_cloud_clients.FolderApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateFolder() # UpdateFolder | 
id = 'id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a folder's properties.
    api_response = api_instance.folder_update_folder(body, id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderApi->folder_update_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFolder**](UpdateFolder.md)|  | 
 **id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_update_item_parent_folder**
> folder_update_item_parent_folder(body, tenant_url_code)

Moves an item to a different folder.

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
api_instance = cartovista_cloud_clients.FolderApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateItemParentFolder() # UpdateItemParentFolder | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Moves an item to a different folder.
    api_instance.folder_update_item_parent_folder(body, tenant_url_code)
except ApiException as e:
    print("Exception when calling FolderApi->folder_update_item_parent_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateItemParentFolder**](UpdateItemParentFolder.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

