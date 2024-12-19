# cartovista_cloud_clients.SlideApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slide_delete_slide**](SlideApi.md#slide_delete_slide) | **DELETE** /{tenantUrlCode}/api/v2/slides/{slideId} | Deletes the slide.
[**slide_delete_slide_analysis**](SlideApi.md#slide_delete_slide_analysis) | **DELETE** /{tenantUrlCode}/api/v2/slides/{slideId}/analysis/{analysisId} | Deletes the analysis from the slide.
[**slide_get_slide**](SlideApi.md#slide_get_slide) | **GET** /{tenantUrlCode}/api/v2/slides/{slideId} | Gets a specific slide.
[**slide_reorder_slides**](SlideApi.md#slide_reorder_slides) | **PUT** /{tenantUrlCode}/api/v2/slides/{mapId}/reorderSlides | Changes the order of a slide in the slide details view. The order will be the same in the slide ids list.
[**slide_update_default_slide_thumbnail**](SlideApi.md#slide_update_default_slide_thumbnail) | **PATCH** /{tenantUrlCode}/api/v2/maps/{mapId}/default-slide-thumbnail | Updates the map&#x27;s default slide&#x27;s thumbnail.
[**slide_update_slide**](SlideApi.md#slide_update_slide) | **PATCH** /{tenantUrlCode}/api/v2/slides/{slideId} | Updates the slide.
[**slide_update_slide_extent_from_layers**](SlideApi.md#slide_update_slide_extent_from_layers) | **PATCH** /{tenantUrlCode}/api/v2/slides/{slideId}/extent-from-layers | Updates the slide&#x27;s extent by combining the layers&#x27; extents.
[**slide_update_slide_theme_set**](SlideApi.md#slide_update_slide_theme_set) | **PATCH** /{tenantUrlCode}/api/v2/slides/{slideId}/themeset | Updates the slide&#x27;s theme set.

# **slide_delete_slide**
> list[Slide] slide_delete_slide(slide_id, tenant_url_code)

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
configuration = cartovista_cloud_clients.Configuration()
configuration.api_key['secretKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['secretKey'] = 'Bearer'

# create an instance of the API class
api_instance = cartovista_cloud_clients.SlideApi(cartovista_cloud_clients.ApiClient(configuration))
slide_id = 'slide_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes the slide.
    api_response = api_instance.slide_delete_slide(slide_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlideApi->slide_delete_slide: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slide_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Slide]**](Slide.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
configuration = cartovista_cloud_clients.Configuration()
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
configuration = cartovista_cloud_clients.Configuration()
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

# **slide_reorder_slides**
> list[Slide] slide_reorder_slides(body, map_id, tenant_url_code)

Changes the order of a slide in the slide details view. The order will be the same in the slide ids list.

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
api_instance = cartovista_cloud_clients.SlideApi(cartovista_cloud_clients.ApiClient(configuration))
body = ['body_example'] # list[str] | 
map_id = 'map_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Changes the order of a slide in the slide details view. The order will be the same in the slide ids list.
    api_response = api_instance.slide_reorder_slides(body, map_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlideApi->slide_reorder_slides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **map_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Slide]**](Slide.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
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
configuration = cartovista_cloud_clients.Configuration()
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
configuration = cartovista_cloud_clients.Configuration()
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
configuration = cartovista_cloud_clients.Configuration()
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
configuration = cartovista_cloud_clients.Configuration()
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


