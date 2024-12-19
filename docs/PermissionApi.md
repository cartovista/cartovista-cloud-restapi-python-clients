# cartovista_cloud_clients.PermissionApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permission_add_permissions_to_map**](PermissionApi.md#permission_add_permissions_to_map) | **PATCH** /{tenantUrlCode}/api/v2/permission/maps/{friendlyIdentifierOrGuid} | Add permissions to a map and optionally its subcomponents.
[**permission_get_data_table_permissions**](PermissionApi.md#permission_get_data_table_permissions) | **GET** /{tenantUrlCode}/api/v2/permission/dataTable/{friendlyIdentifierOrGuid} | Gets the table&#x27;s permissions.
[**permission_get_layer_permissions**](PermissionApi.md#permission_get_layer_permissions) | **GET** /{tenantUrlCode}/api/v2/permission/layer/{friendlyIdentifierOrGuid} | Gets the layer&#x27;s permissions.
[**permission_get_map_permissions**](PermissionApi.md#permission_get_map_permissions) | **GET** /{tenantUrlCode}/api/v2/permission/maps/{friendlyIdentifierOrGuid} | Gets the map&#x27;s permissions.
[**permission_get_security_identities**](PermissionApi.md#permission_get_security_identities) | **GET** /{tenantUrlCode}/api/v2/permission/security-identities | Gets a list of users and groups that can be added to an object&#x27;s permissions.
[**permission_update_data_table_permissions**](PermissionApi.md#permission_update_data_table_permissions) | **POST** /{tenantUrlCode}/api/v2/permission/dataTable/{friendlyIdentifierOrGuid} | Updates the table&#x27;s permissions.
[**permission_update_layer_permissions**](PermissionApi.md#permission_update_layer_permissions) | **POST** /{tenantUrlCode}/api/v2/permission/layer/{friendlyIdentifierOrGuid} | Updates the layer&#x27;s permissions.
[**permission_update_map_permissions**](PermissionApi.md#permission_update_map_permissions) | **POST** /{tenantUrlCode}/api/v2/permission/maps/{friendlyIdentifierOrGuid} | Update permissions to a map and optionally its subcomponents.

# **permission_add_permissions_to_map**
> permission_add_permissions_to_map(body, friendly_identifier_or_guid, tenant_url_code)

Add permissions to a map and optionally its subcomponents.

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
api_instance = cartovista_cloud_clients.PermissionApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ApplyGenericPermissionsParameter() # ApplyGenericPermissionsParameter | Parameters to apply permissions to the chosen map. Includes permissions to apply and wether permissions should also be applied to linked layers and data tables
friendly_identifier_or_guid = 'friendly_identifier_or_guid_example' # str | Guid or friendlyIdentifier of the targeted map.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Add permissions to a map and optionally its subcomponents.
    api_instance.permission_add_permissions_to_map(body, friendly_identifier_or_guid, tenant_url_code)
except ApiException as e:
    print("Exception when calling PermissionApi->permission_add_permissions_to_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyGenericPermissionsParameter**](ApplyGenericPermissionsParameter.md)| Parameters to apply permissions to the chosen map. Includes permissions to apply and wether permissions should also be applied to linked layers and data tables | 
 **friendly_identifier_or_guid** | **str**| Guid or friendlyIdentifier of the targeted map. | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_get_data_table_permissions**
> list[PermissionPairComplexDTO] permission_get_data_table_permissions(friendly_identifier_or_guid, tenant_url_code)

Gets the table's permissions.

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
api_instance = cartovista_cloud_clients.PermissionApi(cartovista_cloud_clients.ApiClient(configuration))
friendly_identifier_or_guid = 'friendly_identifier_or_guid_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the table's permissions.
    api_response = api_instance.permission_get_data_table_permissions(friendly_identifier_or_guid, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionApi->permission_get_data_table_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_identifier_or_guid** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[PermissionPairComplexDTO]**](PermissionPairComplexDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_get_layer_permissions**
> list[PermissionPairComplexDTO] permission_get_layer_permissions(friendly_identifier_or_guid, tenant_url_code)

Gets the layer's permissions.

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
api_instance = cartovista_cloud_clients.PermissionApi(cartovista_cloud_clients.ApiClient(configuration))
friendly_identifier_or_guid = 'friendly_identifier_or_guid_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the layer's permissions.
    api_response = api_instance.permission_get_layer_permissions(friendly_identifier_or_guid, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionApi->permission_get_layer_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_identifier_or_guid** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[PermissionPairComplexDTO]**](PermissionPairComplexDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_get_map_permissions**
> list[PermissionPairComplexDTO] permission_get_map_permissions(friendly_identifier_or_guid, tenant_url_code)

Gets the map's permissions.

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
api_instance = cartovista_cloud_clients.PermissionApi(cartovista_cloud_clients.ApiClient(configuration))
friendly_identifier_or_guid = 'friendly_identifier_or_guid_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the map's permissions.
    api_response = api_instance.permission_get_map_permissions(friendly_identifier_or_guid, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionApi->permission_get_map_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_identifier_or_guid** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[PermissionPairComplexDTO]**](PermissionPairComplexDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_get_security_identities**
> list[SecurityIdentity] permission_get_security_identities(tenant_url_code)

Gets a list of users and groups that can be added to an object's permissions.

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
api_instance = cartovista_cloud_clients.PermissionApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a list of users and groups that can be added to an object's permissions.
    api_response = api_instance.permission_get_security_identities(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionApi->permission_get_security_identities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**list[SecurityIdentity]**](SecurityIdentity.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_update_data_table_permissions**
> list[PermissionPairComplexDTO] permission_update_data_table_permissions(body, friendly_identifier_or_guid, tenant_url_code)

Updates the table's permissions.

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
api_instance = cartovista_cloud_clients.PermissionApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ApplyGenericPermissionsParameter() # ApplyGenericPermissionsParameter | 
friendly_identifier_or_guid = 'friendly_identifier_or_guid_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the table's permissions.
    api_response = api_instance.permission_update_data_table_permissions(body, friendly_identifier_or_guid, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionApi->permission_update_data_table_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyGenericPermissionsParameter**](ApplyGenericPermissionsParameter.md)|  | 
 **friendly_identifier_or_guid** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[PermissionPairComplexDTO]**](PermissionPairComplexDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_update_layer_permissions**
> list[PermissionPairComplexDTO] permission_update_layer_permissions(body, friendly_identifier_or_guid, tenant_url_code)

Updates the layer's permissions.

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
api_instance = cartovista_cloud_clients.PermissionApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ApplyGenericPermissionsParameter() # ApplyGenericPermissionsParameter | 
friendly_identifier_or_guid = 'friendly_identifier_or_guid_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the layer's permissions.
    api_response = api_instance.permission_update_layer_permissions(body, friendly_identifier_or_guid, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionApi->permission_update_layer_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyGenericPermissionsParameter**](ApplyGenericPermissionsParameter.md)|  | 
 **friendly_identifier_or_guid** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[PermissionPairComplexDTO]**](PermissionPairComplexDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_update_map_permissions**
> list[PermissionPairComplexDTO] permission_update_map_permissions(body, friendly_identifier_or_guid, tenant_url_code)

Update permissions to a map and optionally its subcomponents.

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
api_instance = cartovista_cloud_clients.PermissionApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ApplyGenericPermissionsParameter() # ApplyGenericPermissionsParameter | Parameters to apply permissions to the chosen map. Includes permissions to apply and wether permissions should also be applied to linked layers and data tables
friendly_identifier_or_guid = 'friendly_identifier_or_guid_example' # str | Guid or friendlyIdentifier of the targeted map.
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Update permissions to a map and optionally its subcomponents.
    api_response = api_instance.permission_update_map_permissions(body, friendly_identifier_or_guid, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionApi->permission_update_map_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyGenericPermissionsParameter**](ApplyGenericPermissionsParameter.md)| Parameters to apply permissions to the chosen map. Includes permissions to apply and wether permissions should also be applied to linked layers and data tables | 
 **friendly_identifier_or_guid** | **str**| Guid or friendlyIdentifier of the targeted map. | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[PermissionPairComplexDTO]**](PermissionPairComplexDTO.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


