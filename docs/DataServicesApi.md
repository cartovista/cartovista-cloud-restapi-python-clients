# cartovista_cloud_clients.DataServicesApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_services_data_query_execute**](DataServicesApi.md#data_services_data_query_execute) | **POST** /{tenantUrlCode}/DataServices/dataQueryExecute | 
[**data_services_get_feature_count_equal_to_classifications**](DataServicesApi.md#data_services_get_feature_count_equal_to_classifications) | **POST** /{tenantUrlCode}/DataServices/getFeatureCountEqualToClassifications | 
[**data_services_get_feature_count_equal_to_value**](DataServicesApi.md#data_services_get_feature_count_equal_to_value) | **POST** /{tenantUrlCode}/DataServices/getFeatureCountEqualToValue | 
[**data_services_get_feature_count_in_range_of_value**](DataServicesApi.md#data_services_get_feature_count_in_range_of_value) | **POST** /{tenantUrlCode}/DataServices/getFeatureCountInRangeOfValue | 
[**data_services_get_feature_count_out_of_range**](DataServicesApi.md#data_services_get_feature_count_out_of_range) | **POST** /{tenantUrlCode}/DataServices/getFeatureCountOutOfRange | 
[**data_services_get_individual_values**](DataServicesApi.md#data_services_get_individual_values) | **POST** /{tenantUrlCode}/DataServices/getIndividualValues | 
[**data_services_get_individual_values_on_multiple_columns**](DataServicesApi.md#data_services_get_individual_values_on_multiple_columns) | **POST** /{tenantUrlCode}/DataServices/getIndividualValuesOnMultipleColumns | 
[**data_services_get_linking_id_index**](DataServicesApi.md#data_services_get_linking_id_index) | **POST** /{tenantUrlCode}/DataServices/getLinkingIdIndex | 
[**data_services_get_ranges**](DataServicesApi.md#data_services_get_ranges) | **POST** /{tenantUrlCode}/DataServices/getRanges | 

# **data_services_data_query_execute**
> AttributeDataQueryResultDTO data_services_data_query_execute(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.DataServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DataQueryDTO() # DataQueryDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.data_services_data_query_execute(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServicesApi->data_services_data_query_execute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataQueryDTO**](DataQueryDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**AttributeDataQueryResultDTO**](AttributeDataQueryResultDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_services_get_feature_count_equal_to_classifications**
> GetFeatureCountEqualToClassificationsResultDTO data_services_get_feature_count_equal_to_classifications(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.DataServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetFeatureCountEqualToClassificationsOfDataQueryColumnDTO() # GetFeatureCountEqualToClassificationsOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.data_services_get_feature_count_equal_to_classifications(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServicesApi->data_services_get_feature_count_equal_to_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetFeatureCountEqualToClassificationsOfDataQueryColumnDTO**](GetFeatureCountEqualToClassificationsOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GetFeatureCountEqualToClassificationsResultDTO**](GetFeatureCountEqualToClassificationsResultDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_services_get_feature_count_equal_to_value**
> GetFeatureCountEqualToResultDTO data_services_get_feature_count_equal_to_value(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.DataServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetFeatureCountEqualToValueDTOOfDataQueryColumnDTO() # GetFeatureCountEqualToValueDTOOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.data_services_get_feature_count_equal_to_value(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServicesApi->data_services_get_feature_count_equal_to_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetFeatureCountEqualToValueDTOOfDataQueryColumnDTO**](GetFeatureCountEqualToValueDTOOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GetFeatureCountEqualToResultDTO**](GetFeatureCountEqualToResultDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_services_get_feature_count_in_range_of_value**
> GetFeatureCountInRangeOfValueResultDTO data_services_get_feature_count_in_range_of_value(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.DataServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetFeatureCountInRangeOfMessageDTOOfDataQueryColumnDTO() # GetFeatureCountInRangeOfMessageDTOOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.data_services_get_feature_count_in_range_of_value(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServicesApi->data_services_get_feature_count_in_range_of_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetFeatureCountInRangeOfMessageDTOOfDataQueryColumnDTO**](GetFeatureCountInRangeOfMessageDTOOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GetFeatureCountInRangeOfValueResultDTO**](GetFeatureCountInRangeOfValueResultDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_services_get_feature_count_out_of_range**
> GetFeatureCountOutOfRangeResultDTO data_services_get_feature_count_out_of_range(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.DataServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetFeatureCountOutOfRangeMessageDTOOfDataQueryColumnDTO() # GetFeatureCountOutOfRangeMessageDTOOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.data_services_get_feature_count_out_of_range(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServicesApi->data_services_get_feature_count_out_of_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetFeatureCountOutOfRangeMessageDTOOfDataQueryColumnDTO**](GetFeatureCountOutOfRangeMessageDTOOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GetFeatureCountOutOfRangeResultDTO**](GetFeatureCountOutOfRangeResultDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_services_get_individual_values**
> IndividualValuesResultDTO data_services_get_individual_values(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.DataServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.IndividualValuesMessageDTOOfDataQueryColumnDTO() # IndividualValuesMessageDTOOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.data_services_get_individual_values(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServicesApi->data_services_get_individual_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IndividualValuesMessageDTOOfDataQueryColumnDTO**](IndividualValuesMessageDTOOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**IndividualValuesResultDTO**](IndividualValuesResultDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_services_get_individual_values_on_multiple_columns**
> IndividualValuesResultDTO data_services_get_individual_values_on_multiple_columns(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.DataServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.IndividualValuesOnMultipleColumnsMessageDTOOfDataQueryColumnDTO() # IndividualValuesOnMultipleColumnsMessageDTOOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.data_services_get_individual_values_on_multiple_columns(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServicesApi->data_services_get_individual_values_on_multiple_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IndividualValuesOnMultipleColumnsMessageDTOOfDataQueryColumnDTO**](IndividualValuesOnMultipleColumnsMessageDTOOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**IndividualValuesResultDTO**](IndividualValuesResultDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_services_get_linking_id_index**
> GetLinkingIdIndexResultDTO data_services_get_linking_id_index(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.DataServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetLinkingIdIndexMessageDTOOfDataQueryColumnDTO() # GetLinkingIdIndexMessageDTOOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.data_services_get_linking_id_index(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServicesApi->data_services_get_linking_id_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetLinkingIdIndexMessageDTOOfDataQueryColumnDTO**](GetLinkingIdIndexMessageDTOOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GetLinkingIdIndexResultDTO**](GetLinkingIdIndexResultDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_services_get_ranges**
> GetRangesResultDTO data_services_get_ranges(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.DataServicesApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetRangesMessageDTOOfDataQueryColumnDTO() # GetRangesMessageDTOOfDataQueryColumnDTO | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.data_services_get_ranges(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServicesApi->data_services_get_ranges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetRangesMessageDTOOfDataQueryColumnDTO**](GetRangesMessageDTOOfDataQueryColumnDTO.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**GetRangesResultDTO**](GetRangesResultDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


