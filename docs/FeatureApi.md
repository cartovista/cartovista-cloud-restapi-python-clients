# cartovista_cloud_clients.FeatureApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feature_create_features_from_geo_json**](FeatureApi.md#feature_create_features_from_geo_json) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Features/createFromGeoJSON | Creates a feature using the provided geometry in GeoJSON format.
[**feature_create_features_from_long_lat**](FeatureApi.md#feature_create_features_from_long_lat) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Features/createFromLongLat | Creates features from the provided latutude and longitude coordinates. The layer must be a point layer. Use \&quot;proj4\&quot;: \&quot;+proj&#x3D;longlat +ellps&#x3D;WGS84 +datum&#x3D;WGS84 +no_defs\&quot;.
[**feature_create_features_from_wkt**](FeatureApi.md#feature_create_features_from_wkt) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Features/createFromWKT | Creates a feature using the provided geometry in WKT format.
[**feature_create_update_features_from_geo_json**](FeatureApi.md#feature_create_update_features_from_geo_json) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Features/createUpdateFromGeoJSON | Creates a feature or updates it if it already exists with the input geometry in GeoJSON format.
[**feature_create_update_features_from_long_lat**](FeatureApi.md#feature_create_update_features_from_long_lat) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Features/createUpdateFromLongLat | Creates features or update them if they already exist with provided latutude and longitude coordinates. The layer must be a point layer. Use \&quot;proj4\&quot;: \&quot;+proj&#x3D;longlat +ellps&#x3D;WGS84 +datum&#x3D;WGS84 +no_defs\&quot;.
[**feature_create_update_features_from_wkt**](FeatureApi.md#feature_create_update_features_from_wkt) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Features/createUpdateFromWKT | Creates a feature or updates it if it already exists with the input geometry in WKT format.
[**feature_delete_feature**](FeatureApi.md#feature_delete_feature) | **DELETE** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Feature/{featureIdentifier} | Deletes a specific feature.
[**feature_delete_features**](FeatureApi.md#feature_delete_features) | **DELETE** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Features | Deletes a set of features. Invalid identifiers are ignored.
[**feature_delete_features_by_values**](FeatureApi.md#feature_delete_features_by_values) | **DELETE** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Features/column/{columnIdentifier} | Deletes all the features where the column values are included in the list of values.
[**feature_get_feature_data**](FeatureApi.md#feature_get_feature_data) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Feature/{featureIdentifier}/data | Gets a feature&#x27;s data.
[**feature_get_feature_in_geo_json**](FeatureApi.md#feature_get_feature_in_geo_json) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Feature/{featureIdentifier}/GeoJSON | Gets a specific feature with its geometry in GeoJSON format.
[**feature_get_feature_in_long_lat**](FeatureApi.md#feature_get_feature_in_long_lat) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Feature/{featureIdentifier}/LongLat | Gets a specific feature with its coordinates. The layer must be a point layer.
[**feature_get_feature_in_wkt**](FeatureApi.md#feature_get_feature_in_wkt) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Feature/{featureIdentifier}/WKT | Gets a specific feature with its geometry in WKT format.
[**feature_get_features**](FeatureApi.md#feature_get_features) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Features | Gets the rows in the layer.
[**feature_get_features_at_location_in_geo_json**](FeatureApi.md#feature_get_features_at_location_in_geo_json) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/{latitude}/{longitude}/GeoJSON | Return all the features with all their associated data intersecting the specified coordinates.
[**feature_get_features_at_location_in_long_lat**](FeatureApi.md#feature_get_features_at_location_in_long_lat) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/{latitude}/{longitude}/LongLat | Return all the features with all their associated data intersecting the specified coordinates. Important: this api call will only work if the queried layer has points. For any other geometry type, use the GeoJSON or WKT call instead.
[**feature_get_features_at_location_in_wkt**](FeatureApi.md#feature_get_features_at_location_in_wkt) | **GET** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/{latitude}/{longitude}/WKT | Return all the features with all their associated data intersecting the specified coordinates.
[**feature_get_features_in_geo_json**](FeatureApi.md#feature_get_features_in_geo_json) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Features/GeoJSON | Gets the layer&#x27;s features with the geometries in GeoJSON format.
[**feature_get_features_in_long_lat**](FeatureApi.md#feature_get_features_in_long_lat) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Features/LongLat | Retrives the layer&#x27;s features with their coordinates. The layer must be a point layer.
[**feature_get_features_in_wkt**](FeatureApi.md#feature_get_features_in_wkt) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Features/WKT | Gets the layer&#x27;s features with the geometries in WKT format.
[**feature_update_from_geo_json**](FeatureApi.md#feature_update_from_geo_json) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Feature/{featureIdentifier}/updateFromGeoJSON | Updates a feature&#x27;s geometry from a GeoJSON.
[**feature_update_from_long_lat**](FeatureApi.md#feature_update_from_long_lat) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Feature/{featureIdentifier}/updateFromLongLat | Updates a feature&#x27;s geometry with coordinates. The layer must a point layer. Use \&quot;proj4\&quot;: \&quot;+proj&#x3D;longlat +ellps&#x3D;WGS84 +datum&#x3D;WGS84 +no_defs\&quot;.
[**feature_update_geometry_from_wkt**](FeatureApi.md#feature_update_geometry_from_wkt) | **POST** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Feature/{featureIdentifier}/updateGeometryFromWKT | Updates a feature&#x27;s geometry from a WKT.
[**feature_update_values**](FeatureApi.md#feature_update_values) | **PATCH** /{tenantUrlCode}/api/v2/Layer/{layerIdentifier}/Feature/{featureIdentifier}/updateValues | Updates a feature&#x27;s data. A subset of the columns can be used.

# **feature_create_features_from_geo_json**
> ApiInsertReport feature_create_features_from_geo_json(body, layer_identifier, tenant_url_code)

Creates a feature using the provided geometry in GeoJSON format.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = [cartovista_cloud_clients.FeatureGeoJSONCreateParameter()] # list[FeatureGeoJSONCreateParameter] | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a feature using the provided geometry in GeoJSON format.
    api_response = api_instance.feature_create_features_from_geo_json(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_create_features_from_geo_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[FeatureGeoJSONCreateParameter]**](FeatureGeoJSONCreateParameter.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiInsertReport**](ApiInsertReport.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_create_features_from_long_lat**
> ApiInsertReport feature_create_features_from_long_lat(body, layer_identifier, tenant_url_code)

Creates features from the provided latutude and longitude coordinates. The layer must be a point layer. Use \"proj4\": \"+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs\".

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = [cartovista_cloud_clients.FeatureLongLatCreateParameter()] # list[FeatureLongLatCreateParameter] | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates features from the provided latutude and longitude coordinates. The layer must be a point layer. Use \"proj4\": \"+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs\".
    api_response = api_instance.feature_create_features_from_long_lat(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_create_features_from_long_lat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[FeatureLongLatCreateParameter]**](FeatureLongLatCreateParameter.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiInsertReport**](ApiInsertReport.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_create_features_from_wkt**
> ApiInsertReport feature_create_features_from_wkt(body, layer_identifier, tenant_url_code)

Creates a feature using the provided geometry in WKT format.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = [cartovista_cloud_clients.FeatureWKTCreateParameter()] # list[FeatureWKTCreateParameter] | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a feature using the provided geometry in WKT format.
    api_response = api_instance.feature_create_features_from_wkt(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_create_features_from_wkt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[FeatureWKTCreateParameter]**](FeatureWKTCreateParameter.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiInsertReport**](ApiInsertReport.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_create_update_features_from_geo_json**
> ApiInsertReport feature_create_update_features_from_geo_json(body, layer_identifier, tenant_url_code)

Creates a feature or updates it if it already exists with the input geometry in GeoJSON format.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = [cartovista_cloud_clients.FeatureGeoJSONCreateParameter()] # list[FeatureGeoJSONCreateParameter] | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a feature or updates it if it already exists with the input geometry in GeoJSON format.
    api_response = api_instance.feature_create_update_features_from_geo_json(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_create_update_features_from_geo_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[FeatureGeoJSONCreateParameter]**](FeatureGeoJSONCreateParameter.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiInsertReport**](ApiInsertReport.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_create_update_features_from_long_lat**
> ApiInsertReport feature_create_update_features_from_long_lat(body, layer_identifier, tenant_url_code)

Creates features or update them if they already exist with provided latutude and longitude coordinates. The layer must be a point layer. Use \"proj4\": \"+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs\".

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = [cartovista_cloud_clients.FeatureLongLatCreateParameter()] # list[FeatureLongLatCreateParameter] | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates features or update them if they already exist with provided latutude and longitude coordinates. The layer must be a point layer. Use \"proj4\": \"+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs\".
    api_response = api_instance.feature_create_update_features_from_long_lat(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_create_update_features_from_long_lat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[FeatureLongLatCreateParameter]**](FeatureLongLatCreateParameter.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiInsertReport**](ApiInsertReport.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_create_update_features_from_wkt**
> ApiCreateUpdateReport feature_create_update_features_from_wkt(body, layer_identifier, tenant_url_code)

Creates a feature or updates it if it already exists with the input geometry in WKT format.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = [cartovista_cloud_clients.FeatureWKTCreateParameter()] # list[FeatureWKTCreateParameter] | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a feature or updates it if it already exists with the input geometry in WKT format.
    api_response = api_instance.feature_create_update_features_from_wkt(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_create_update_features_from_wkt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[FeatureWKTCreateParameter]**](FeatureWKTCreateParameter.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiCreateUpdateReport**](ApiCreateUpdateReport.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_delete_feature**
> ApiDeleteReport feature_delete_feature(layer_identifier, feature_identifier, tenant_url_code)

Deletes a specific feature.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | The layer to query
feature_identifier = 'feature_identifier_example' # str | The feature to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes a specific feature.
    api_response = api_instance.feature_delete_feature(layer_identifier, feature_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_delete_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**| The layer to query | 
 **feature_identifier** | **str**| The feature to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiDeleteReport**](ApiDeleteReport.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_delete_features**
> ApiDeleteReport feature_delete_features(body, layer_identifier, tenant_url_code)

Deletes a set of features. Invalid identifiers are ignored.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = ['body_example'] # list[str] | The features to query
layer_identifier = 'layer_identifier_example' # str | The layer to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes a set of features. Invalid identifiers are ignored.
    api_response = api_instance.feature_delete_features(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_delete_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The features to query | 
 **layer_identifier** | **str**| The layer to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiDeleteReport**](ApiDeleteReport.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_delete_features_by_values**
> ApiDeleteReport feature_delete_features_by_values(body, layer_identifier, column_identifier, tenant_url_code)

Deletes all the features where the column values are included in the list of values.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = ['body_example'] # list[str] | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
column_identifier = 'column_identifier_example' # str | The column to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes all the features where the column values are included in the list of values.
    api_response = api_instance.feature_delete_features_by_values(body, layer_identifier, column_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_delete_features_by_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **column_identifier** | **str**| The column to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**ApiDeleteReport**](ApiDeleteReport.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_get_feature_data**
> DataRow feature_get_feature_data(layer_identifier, feature_identifier, tenant_url_code)

Gets a feature's data.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | The layer to query
feature_identifier = 'feature_identifier_example' # str | The feature to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a feature's data.
    api_response = api_instance.feature_get_feature_data(layer_identifier, feature_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_get_feature_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**| The layer to query | 
 **feature_identifier** | **str**| The feature to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataRow**](DataRow.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_get_feature_in_geo_json**
> FeatureGeoJSON feature_get_feature_in_geo_json(layer_identifier, feature_identifier, tenant_url_code)

Gets a specific feature with its geometry in GeoJSON format.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | The layer to query
feature_identifier = 'feature_identifier_example' # str | The feature to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific feature with its geometry in GeoJSON format.
    api_response = api_instance.feature_get_feature_in_geo_json(layer_identifier, feature_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_get_feature_in_geo_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**| The layer to query | 
 **feature_identifier** | **str**| The feature to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**FeatureGeoJSON**](FeatureGeoJSON.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_get_feature_in_long_lat**
> FeatureLongLat feature_get_feature_in_long_lat(layer_identifier, feature_identifier, tenant_url_code)

Gets a specific feature with its coordinates. The layer must be a point layer.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | The layer to query
feature_identifier = 'feature_identifier_example' # str | The feature to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific feature with its coordinates. The layer must be a point layer.
    api_response = api_instance.feature_get_feature_in_long_lat(layer_identifier, feature_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_get_feature_in_long_lat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**| The layer to query | 
 **feature_identifier** | **str**| The feature to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**FeatureLongLat**](FeatureLongLat.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_get_feature_in_wkt**
> FeatureWKT feature_get_feature_in_wkt(layer_identifier, feature_identifier, tenant_url_code)

Gets a specific feature with its geometry in WKT format.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | The layer to query
feature_identifier = 'feature_identifier_example' # str | The feature to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific feature with its geometry in WKT format.
    api_response = api_instance.feature_get_feature_in_wkt(layer_identifier, feature_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_get_feature_in_wkt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**| The layer to query | 
 **feature_identifier** | **str**| The feature to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**FeatureWKT**](FeatureWKT.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_get_features**
> list[DataRow] feature_get_features(body, layer_identifier, tenant_url_code)

Gets the rows in the layer.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.FeaturesGetParameters() # FeaturesGetParameters | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the rows in the layer.
    api_response = api_instance.feature_get_features(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_get_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeaturesGetParameters**](FeaturesGetParameters.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[DataRow]**](DataRow.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_get_features_at_location_in_geo_json**
> list[FeatureGeoJSON] feature_get_features_at_location_in_geo_json(layer_identifier, latitude, longitude, tenant_url_code)

Return all the features with all their associated data intersecting the specified coordinates.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | The layer to query
latitude = 1.2 # float | The latitude of the coordinate to query
longitude = 1.2 # float | The longitudew of the coordinate to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Return all the features with all their associated data intersecting the specified coordinates.
    api_response = api_instance.feature_get_features_at_location_in_geo_json(layer_identifier, latitude, longitude, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_get_features_at_location_in_geo_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**| The layer to query | 
 **latitude** | **float**| The latitude of the coordinate to query | 
 **longitude** | **float**| The longitudew of the coordinate to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[FeatureGeoJSON]**](FeatureGeoJSON.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_get_features_at_location_in_long_lat**
> list[FeatureLongLat] feature_get_features_at_location_in_long_lat(layer_identifier, latitude, longitude, tenant_url_code)

Return all the features with all their associated data intersecting the specified coordinates. Important: this api call will only work if the queried layer has points. For any other geometry type, use the GeoJSON or WKT call instead.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | The layer to query
latitude = 1.2 # float | The latitude of the coordinate to query
longitude = 1.2 # float | The longitudew of the coordinate to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Return all the features with all their associated data intersecting the specified coordinates. Important: this api call will only work if the queried layer has points. For any other geometry type, use the GeoJSON or WKT call instead.
    api_response = api_instance.feature_get_features_at_location_in_long_lat(layer_identifier, latitude, longitude, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_get_features_at_location_in_long_lat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**| The layer to query | 
 **latitude** | **float**| The latitude of the coordinate to query | 
 **longitude** | **float**| The longitudew of the coordinate to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[FeatureLongLat]**](FeatureLongLat.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_get_features_at_location_in_wkt**
> list[FeatureWKT] feature_get_features_at_location_in_wkt(layer_identifier, latitude, longitude, tenant_url_code)

Return all the features with all their associated data intersecting the specified coordinates.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
layer_identifier = 'layer_identifier_example' # str | The layer to query
latitude = 1.2 # float | The latitude of the coordinate to query
longitude = 1.2 # float | The longitudew of the coordinate to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Return all the features with all their associated data intersecting the specified coordinates.
    api_response = api_instance.feature_get_features_at_location_in_wkt(layer_identifier, latitude, longitude, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_get_features_at_location_in_wkt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_identifier** | **str**| The layer to query | 
 **latitude** | **float**| The latitude of the coordinate to query | 
 **longitude** | **float**| The longitudew of the coordinate to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[FeatureWKT]**](FeatureWKT.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_get_features_in_geo_json**
> list[FeatureGeoJSON] feature_get_features_in_geo_json(body, layer_identifier, tenant_url_code)

Gets the layer's features with the geometries in GeoJSON format.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.FeaturesGetParameters() # FeaturesGetParameters | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the layer's features with the geometries in GeoJSON format.
    api_response = api_instance.feature_get_features_in_geo_json(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_get_features_in_geo_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeaturesGetParameters**](FeaturesGetParameters.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[FeatureGeoJSON]**](FeatureGeoJSON.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_get_features_in_long_lat**
> list[FeatureLongLat] feature_get_features_in_long_lat(body, layer_identifier, tenant_url_code)

Retrives the layer's features with their coordinates. The layer must be a point layer.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.FeaturesGetParameters() # FeaturesGetParameters | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Retrives the layer's features with their coordinates. The layer must be a point layer.
    api_response = api_instance.feature_get_features_in_long_lat(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_get_features_in_long_lat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeaturesGetParameters**](FeaturesGetParameters.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[FeatureLongLat]**](FeatureLongLat.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_get_features_in_wkt**
> list[FeatureWKT] feature_get_features_in_wkt(body, layer_identifier, tenant_url_code)

Gets the layer's features with the geometries in WKT format.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.FeaturesGetParameters() # FeaturesGetParameters | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the layer's features with the geometries in WKT format.
    api_response = api_instance.feature_get_features_in_wkt(body, layer_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_get_features_in_wkt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeaturesGetParameters**](FeaturesGetParameters.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[FeatureWKT]**](FeatureWKT.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_update_from_geo_json**
> FeatureGeoJSON feature_update_from_geo_json(body, layer_identifier, feature_identifier, tenant_url_code)

Updates a feature's geometry from a GeoJSON.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.FeatureGeoJSONUpdateParameter() # FeatureGeoJSONUpdateParameter | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
feature_identifier = 'feature_identifier_example' # str | The feature to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a feature's geometry from a GeoJSON.
    api_response = api_instance.feature_update_from_geo_json(body, layer_identifier, feature_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_update_from_geo_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeatureGeoJSONUpdateParameter**](FeatureGeoJSONUpdateParameter.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **feature_identifier** | **str**| The feature to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**FeatureGeoJSON**](FeatureGeoJSON.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_update_from_long_lat**
> FeatureLongLat feature_update_from_long_lat(body, layer_identifier, feature_identifier, tenant_url_code)

Updates a feature's geometry with coordinates. The layer must a point layer. Use \"proj4\": \"+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs\".

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.FeatureLongLatUpdateParameter() # FeatureLongLatUpdateParameter | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
feature_identifier = 'feature_identifier_example' # str | The feature to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a feature's geometry with coordinates. The layer must a point layer. Use \"proj4\": \"+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs\".
    api_response = api_instance.feature_update_from_long_lat(body, layer_identifier, feature_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_update_from_long_lat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeatureLongLatUpdateParameter**](FeatureLongLatUpdateParameter.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **feature_identifier** | **str**| The feature to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**FeatureLongLat**](FeatureLongLat.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_update_geometry_from_wkt**
> FeatureWKT feature_update_geometry_from_wkt(body, layer_identifier, feature_identifier, tenant_url_code)

Updates a feature's geometry from a WKT.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.FeatureWKTUpdateParameter() # FeatureWKTUpdateParameter | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
feature_identifier = 'feature_identifier_example' # str | The feature to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a feature's geometry from a WKT.
    api_response = api_instance.feature_update_geometry_from_wkt(body, layer_identifier, feature_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_update_geometry_from_wkt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeatureWKTUpdateParameter**](FeatureWKTUpdateParameter.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **feature_identifier** | **str**| The feature to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**FeatureWKT**](FeatureWKT.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feature_update_values**
> DataRow feature_update_values(body, layer_identifier, feature_identifier, tenant_url_code)

Updates a feature's data. A subset of the columns can be used.

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
api_instance = cartovista_cloud_clients.FeatureApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DataRowUpdateParameter() # DataRowUpdateParameter | 
layer_identifier = 'layer_identifier_example' # str | The layer to query
feature_identifier = 'feature_identifier_example' # str | The feature to query
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a feature's data. A subset of the columns can be used.
    api_response = api_instance.feature_update_values(body, layer_identifier, feature_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->feature_update_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataRowUpdateParameter**](DataRowUpdateParameter.md)|  | 
 **layer_identifier** | **str**| The layer to query | 
 **feature_identifier** | **str**| The feature to query | 
 **tenant_url_code** | **str**|  | 

### Return type

[**DataRow**](DataRow.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


