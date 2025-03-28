# cartovista_cloud_clients.SlideApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slide_create_slide_folder**](SlideApi.md#slide_create_slide_folder) | **POST** /{tenantUrlCode}/api/v2/slide-folder | Creates a slide folder.
[**slide_delete_slide**](SlideApi.md#slide_delete_slide) | **DELETE** /{tenantUrlCode}/api/v2/slides/{slideId} | Deletes the slide.
[**slide_delete_slide_analysis**](SlideApi.md#slide_delete_slide_analysis) | **DELETE** /{tenantUrlCode}/api/v2/slides/{slideId}/analysis/{analysisId} | Deletes the analysis from the slide.
[**slide_delete_slide_folder**](SlideApi.md#slide_delete_slide_folder) | **DELETE** /{tenantUrlCode}/api/v2/slide-folder/{slideFolderId} | Deletes the slide folder.
[**slide_get_slide**](SlideApi.md#slide_get_slide) | **GET** /{tenantUrlCode}/api/v2/slides/{slideId} | Gets a specific slide.
[**slide_get_slide_folder**](SlideApi.md#slide_get_slide_folder) | **GET** /{tenantUrlCode}/api/v2/slide-folder/{folderId} | Gets a specific folder.
[**slide_move_slide_item**](SlideApi.md#slide_move_slide_item) | **PATCH** /{tenantUrlCode}/api/v2/slides/{itemId}/move | Moves a slide item to a specified parent folder and position.
[**slide_update_default_slide_thumbnail**](SlideApi.md#slide_update_default_slide_thumbnail) | **PATCH** /{tenantUrlCode}/api/v2/maps/{mapId}/default-slide-thumbnail | Updates the map&#x27;s default slide&#x27;s thumbnail.
[**slide_update_slide**](SlideApi.md#slide_update_slide) | **PATCH** /{tenantUrlCode}/api/v2/slides/{slideId} | Updates the slide.
[**slide_update_slide_extent_from_layers**](SlideApi.md#slide_update_slide_extent_from_layers) | **PATCH** /{tenantUrlCode}/api/v2/slides/{slideId}/extent-from-layers | Updates the slide&#x27;s extent by combining the layers&#x27; extents.
[**slide_update_slide_folder**](SlideApi.md#slide_update_slide_folder) | **PATCH** /{tenantUrlCode}/api/v2/slide-folder/{slideFolderId} | Updates the slide folder.
[**slide_update_slide_theme_set**](SlideApi.md#slide_update_slide_theme_set) | **PATCH** /{tenantUrlCode}/api/v2/slides/{slideId}/themeset | Updates the slide&#x27;s theme set.

# **slide_create_slide_folder**
> SlideFolder slide_create_slide_folder(body, tenant_url_code)

Creates a slide folder.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.SlideApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.SlideFolderCreateParam() # SlideFolderCreateParam | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a slide folder.
    api_response = api_instance.slide_create_slide_folder(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlideApi->slide_create_slide_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SlideFolderCreateParam**](SlideFolderCreateParam.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**SlideFolder**](SlideFolder.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slide_delete_slide**
> slide_delete_slide(slide_id, tenant_url_code)

Deletes the slide.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.SlideApi(cartovista_cloud_clients.ApiClient(configuration))
slide_id = 'slide_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes the slide.
    api_instance.slide_delete_slide(slide_id, tenant_url_code)
except ApiException as e:
    print("Exception when calling SlideApi->slide_delete_slide: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slide_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slide_delete_slide_analysis**
> Slide slide_delete_slide_analysis(slide_id, analysis_id, tenant_url_code)

Deletes the analysis from the slide.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.SlideApi(cartovista_cloud_clients.ApiClient(configuration))
slide_id = 'slide_id_example' # str | 
analysis_id = 'analysis_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes the analysis from the slide.
    api_response = api_instance.slide_delete_slide_analysis(slide_id, analysis_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlideApi->slide_delete_slide_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slide_id** | **str**|  | 
 **analysis_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Slide**](Slide.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slide_delete_slide_folder**
> slide_delete_slide_folder(slide_folder_id, tenant_url_code)

Deletes the slide folder.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.SlideApi(cartovista_cloud_clients.ApiClient(configuration))
slide_folder_id = 'slide_folder_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes the slide folder.
    api_instance.slide_delete_slide_folder(slide_folder_id, tenant_url_code)
except ApiException as e:
    print("Exception when calling SlideApi->slide_delete_slide_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slide_folder_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slide_get_slide**
> Slide slide_get_slide(slide_id, tenant_url_code)

Gets a specific slide.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.SlideApi(cartovista_cloud_clients.ApiClient(configuration))
slide_id = 'slide_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific slide.
    api_response = api_instance.slide_get_slide(slide_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlideApi->slide_get_slide: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slide_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Slide**](Slide.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slide_get_slide_folder**
> SlideFolder slide_get_slide_folder(folder_id, tenant_url_code)

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
# Configure API key authorization: secretKey
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.SlideApi(cartovista_cloud_clients.ApiClient(configuration))
folder_id = 'folder_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific folder.
    api_response = api_instance.slide_get_slide_folder(folder_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlideApi->slide_get_slide_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**SlideFolder**](SlideFolder.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slide_move_slide_item**
> MoveSlideItemResponse slide_move_slide_item(item_id, is_item_folder, new_parent_folder, preceding_item_id, tenant_url_code)

Moves a slide item to a specified parent folder and position.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.SlideApi(cartovista_cloud_clients.ApiClient(configuration))
item_id = 'item_id_example' # str | 
is_item_folder = true # bool | 
new_parent_folder = 'new_parent_folder_example' # str | 
preceding_item_id = 'preceding_item_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Moves a slide item to a specified parent folder and position.
    api_response = api_instance.slide_move_slide_item(item_id, is_item_folder, new_parent_folder, preceding_item_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlideApi->slide_move_slide_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **is_item_folder** | **bool**|  | 
 **new_parent_folder** | **str**|  | 
 **preceding_item_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**MoveSlideItemResponse**](MoveSlideItemResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slide_update_default_slide_thumbnail**
> DefaultSlideThumbnailUpdateResponse slide_update_default_slide_thumbnail(body, map_id, tenant_url_code)

Updates the map's default slide's thumbnail.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.SlideApi(cartovista_cloud_clients.ApiClient(configuration))
body = 'body_example' # str | 
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the map's default slide's thumbnail.
    api_response = api_instance.slide_update_default_slide_thumbnail(body, map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlideApi->slide_update_default_slide_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DefaultSlideThumbnailUpdateResponse**](DefaultSlideThumbnailUpdateResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slide_update_slide**
> Slide slide_update_slide(body, slide_id, tenant_url_code)

Updates the slide.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.SlideApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.SlideCreateUpdate() # SlideCreateUpdate | 
slide_id = 'slide_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the slide.
    api_response = api_instance.slide_update_slide(body, slide_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlideApi->slide_update_slide: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SlideCreateUpdate**](SlideCreateUpdate.md)|  | 
 **slide_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Slide**](Slide.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slide_update_slide_extent_from_layers**
> Slide slide_update_slide_extent_from_layers(body, slide_id, tenant_url_code)

Updates the slide's extent by combining the layers' extents.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.SlideApi(cartovista_cloud_clients.ApiClient(configuration))
body = ['body_example'] # list[str] | 
slide_id = 'slide_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the slide's extent by combining the layers' extents.
    api_response = api_instance.slide_update_slide_extent_from_layers(body, slide_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlideApi->slide_update_slide_extent_from_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **slide_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Slide**](Slide.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slide_update_slide_folder**
> SlideFolder slide_update_slide_folder(body, slide_folder_id, tenant_url_code)

Updates the slide folder.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.SlideApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.SlideFolderUpdateParam() # SlideFolderUpdateParam | 
slide_folder_id = 'slide_folder_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the slide folder.
    api_response = api_instance.slide_update_slide_folder(body, slide_folder_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlideApi->slide_update_slide_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SlideFolderUpdateParam**](SlideFolderUpdateParam.md)|  | 
 **slide_folder_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**SlideFolder**](SlideFolder.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slide_update_slide_theme_set**
> Slide slide_update_slide_theme_set(body, slide_id, tenant_url_code)

Updates the slide's theme set.

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
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.SlideApi(cartovista_cloud_clients.ApiClient(configuration))
body = 'body_example' # str | 
slide_id = 'slide_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the slide's theme set.
    api_response = api_instance.slide_update_slide_theme_set(body, slide_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlideApi->slide_update_slide_theme_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **slide_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Slide**](Slide.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

