# cartovista_cloud_clients.OGCApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_gc_get_api**](OGCApi.md#o_gc_get_api) | **GET** /{tenantUrlCode}/api/v2/ogc/{apiKey}/api | Gets the API definition.
[**o_gc_get_capabilities**](OGCApi.md#o_gc_get_capabilities) | **GET** /{tenantUrlCode}/api/v2/ogc/{apiKey} | Gets links to available entries of the OGC feature API.
[**o_gc_get_collection**](OGCApi.md#o_gc_get_collection) | **GET** /{tenantUrlCode}/api/v2/ogc/{apiKey}/collections/{collectionId} | Gets the layer&#x27;s interface
[**o_gc_get_collections**](OGCApi.md#o_gc_get_collections) | **GET** /{tenantUrlCode}/api/v2/ogc/{apiKey}/collections | Gets available layers.
[**o_gc_get_conformance**](OGCApi.md#o_gc_get_conformance) | **GET** /{tenantUrlCode}/api/v2/ogc/{apiKey}/conformance | Gets a list declaring the modules that are implemented by the API.
[**o_gc_get_functions**](OGCApi.md#o_gc_get_functions) | **GET** /{tenantUrlCode}/api/v2/ogc/{apiKey}/functions | Gets the available functions.
[**o_gc_get_item**](OGCApi.md#o_gc_get_item) | **GET** /{tenantUrlCode}/api/v2/ogc/{apiKey}/collections/{collectionId}/items/{featureId} | Gets a layer&#x27;s feature.
[**o_gc_get_items**](OGCApi.md#o_gc_get_items) | **GET** /{tenantUrlCode}/api/v2/ogc/{apiKey}/collections/{collectionId}/items | Gets the layer&#x27;s entities.

# **o_gc_get_api**
> str o_gc_get_api(api_key, tenant_url_code)

Gets the API definition.

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
api_instance = cartovista_cloud_clients.OGCApi(cartovista_cloud_clients.ApiClient(configuration))
api_key = 'api_key_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the API definition.
    api_response = api_instance.o_gc_get_api(api_key, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OGCApi->o_gc_get_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_gc_get_capabilities**
> str o_gc_get_capabilities(api_key, tenant_url_code)

Gets links to available entries of the OGC feature API.

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
api_instance = cartovista_cloud_clients.OGCApi(cartovista_cloud_clients.ApiClient(configuration))
api_key = 'api_key_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets links to available entries of the OGC feature API.
    api_response = api_instance.o_gc_get_capabilities(api_key, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OGCApi->o_gc_get_capabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_gc_get_collection**
> FeatureDto o_gc_get_collection(api_key, collection_id, tenant_url_code)

Gets the layer's interface

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
api_instance = cartovista_cloud_clients.OGCApi(cartovista_cloud_clients.ApiClient(configuration))
api_key = 'api_key_example' # str | 
collection_id = 'collection_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the layer's interface
    api_response = api_instance.o_gc_get_collection(api_key, collection_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OGCApi->o_gc_get_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **collection_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**FeatureDto**](FeatureDto.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_gc_get_collections**
> CollectionsDto o_gc_get_collections(api_key, tenant_url_code)

Gets available layers.

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
api_instance = cartovista_cloud_clients.OGCApi(cartovista_cloud_clients.ApiClient(configuration))
api_key = 'api_key_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets available layers.
    api_response = api_instance.o_gc_get_collections(api_key, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OGCApi->o_gc_get_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**CollectionsDto**](CollectionsDto.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_gc_get_conformance**
> str o_gc_get_conformance(api_key, tenant_url_code)

Gets a list declaring the modules that are implemented by the API.

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
api_instance = cartovista_cloud_clients.OGCApi(cartovista_cloud_clients.ApiClient(configuration))
api_key = 'api_key_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a list declaring the modules that are implemented by the API.
    api_response = api_instance.o_gc_get_conformance(api_key, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OGCApi->o_gc_get_conformance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_gc_get_functions**
> str o_gc_get_functions(api_key, tenant_url_code)

Gets the available functions.

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
api_instance = cartovista_cloud_clients.OGCApi(cartovista_cloud_clients.ApiClient(configuration))
api_key = 'api_key_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the available functions.
    api_response = api_instance.o_gc_get_functions(api_key, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OGCApi->o_gc_get_functions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_gc_get_item**
> str o_gc_get_item(api_key, collection_id, feature_id, tenant_url_code)

Gets a layer's feature.

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
api_instance = cartovista_cloud_clients.OGCApi(cartovista_cloud_clients.ApiClient(configuration))
api_key = 'api_key_example' # str | 
collection_id = 'collection_id_example' # str | 
feature_id = 'feature_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a layer's feature.
    api_response = api_instance.o_gc_get_item(api_key, collection_id, feature_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OGCApi->o_gc_get_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **collection_id** | **str**|  | 
 **feature_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_gc_get_items**
> str o_gc_get_items(api_key, collection_id, tenant_url_code)

Gets the layer's entities.

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
api_instance = cartovista_cloud_clients.OGCApi(cartovista_cloud_clients.ApiClient(configuration))
api_key = 'api_key_example' # str | 
collection_id = 'collection_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the layer's entities.
    api_response = api_instance.o_gc_get_items(api_key, collection_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OGCApi->o_gc_get_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **collection_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

