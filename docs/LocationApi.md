# cartovista_cloud_clients.LocationApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**location_geocode**](LocationApi.md#location_geocode) | **GET** /{tenantUrlCode}/api/v2/Location/geocode/{address} | Gets a list of locations matching the address. The address can be in &#x60;lat,long&#x60; format.
[**location_get_directions**](LocationApi.md#location_get_directions) | **POST** /{tenantUrlCode}/api/v2/Location/route/directions | Gets a list of itineraries (geometry and steps) between two points.
[**location_get_route_summary**](LocationApi.md#location_get_route_summary) | **GET** /{tenantUrlCode}/api/v2/Location/route/summary | Gets an itinerary (geometry and steps) between two points.
[**location_get_route_summary_with_stops**](LocationApi.md#location_get_route_summary_with_stops) | **POST** /{tenantUrlCode}/api/v2/Location/route/summary/stops | Gets an itinerary (geometry and steps) between two points with additional stops.
[**location_isochrone**](LocationApi.md#location_isochrone) | **POST** /{tenantUrlCode}/api/v2/Location/isochrone | Generates a travel time isochrone.
[**location_reverse_geocode**](LocationApi.md#location_reverse_geocode) | **POST** /{tenantUrlCode}/api/v2/Location/reversegeocode | Gets a list of locations from a pair coordinates.

# **location_geocode**
> list[GeocodedLocation] location_geocode(address, options, tenant_url_code)

Gets a list of locations matching the address. The address can be in `lat,long` format.

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
api_instance = cartovista_cloud_clients.LocationApi(cartovista_cloud_clients.ApiClient(configuration))
address = 'address_example' # str | 
options = 'options_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a list of locations matching the address. The address can be in `lat,long` format.
    api_response = api_instance.location_geocode(address, options, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->location_geocode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **options** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[GeocodedLocation]**](GeocodedLocation.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **location_get_directions**
> list[RouteSummary] location_get_directions(body, tenant_url_code)

Gets a list of itineraries (geometry and steps) between two points.

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
api_instance = cartovista_cloud_clients.LocationApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DirectionParams() # DirectionParams | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a list of itineraries (geometry and steps) between two points.
    api_response = api_instance.location_get_directions(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->location_get_directions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectionParams**](DirectionParams.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[RouteSummary]**](RouteSummary.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **location_get_route_summary**
> RouteSummary location_get_route_summary(origin_latitude, origin_longitude, destination_latitude, destination_longitude, mode, departure, traffic, viewer_readable_coordinates, tenant_url_code)

Gets an itinerary (geometry and steps) between two points.

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
api_instance = cartovista_cloud_clients.LocationApi(cartovista_cloud_clients.ApiClient(configuration))
origin_latitude = 1.2 # float | 
origin_longitude = 1.2 # float | 
destination_latitude = 1.2 # float | 
destination_longitude = 1.2 # float | 
mode = 'mode_example' # str | 
departure = 'departure_example' # str | 
traffic = true # bool | 
viewer_readable_coordinates = true # bool | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets an itinerary (geometry and steps) between two points.
    api_response = api_instance.location_get_route_summary(origin_latitude, origin_longitude, destination_latitude, destination_longitude, mode, departure, traffic, viewer_readable_coordinates, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->location_get_route_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin_latitude** | **float**|  | 
 **origin_longitude** | **float**|  | 
 **destination_latitude** | **float**|  | 
 **destination_longitude** | **float**|  | 
 **mode** | **str**|  | 
 **departure** | **str**|  | 
 **traffic** | **bool**|  | 
 **viewer_readable_coordinates** | **bool**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**RouteSummary**](RouteSummary.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **location_get_route_summary_with_stops**
> RouteSummary location_get_route_summary_with_stops(body, tenant_url_code)

Gets an itinerary (geometry and steps) between two points with additional stops.

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
api_instance = cartovista_cloud_clients.LocationApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.RouteWithStopsParams() # RouteWithStopsParams | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets an itinerary (geometry and steps) between two points with additional stops.
    api_response = api_instance.location_get_route_summary_with_stops(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->location_get_route_summary_with_stops: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RouteWithStopsParams**](RouteWithStopsParams.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**RouteSummary**](RouteSummary.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **location_isochrone**
> Isochrone location_isochrone(body, tenant_url_code)

Generates a travel time isochrone.

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
api_instance = cartovista_cloud_clients.LocationApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.IsochroneParams() # IsochroneParams | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Generates a travel time isochrone.
    api_response = api_instance.location_isochrone(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->location_isochrone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IsochroneParams**](IsochroneParams.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Isochrone**](Isochrone.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **location_reverse_geocode**
> list[GeocodedLocation] location_reverse_geocode(body, tenant_url_code)

Gets a list of locations from a pair coordinates.

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
api_instance = cartovista_cloud_clients.LocationApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ReverseGeocodeParams() # ReverseGeocodeParams | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a list of locations from a pair coordinates.
    api_response = api_instance.location_reverse_geocode(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->location_reverse_geocode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReverseGeocodeParams**](ReverseGeocodeParams.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[GeocodedLocation]**](GeocodedLocation.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


