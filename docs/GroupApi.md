# cartovista_cloud_clients.GroupApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_add_users_to_group**](GroupApi.md#group_add_users_to_group) | **POST** /{tenantUrlCode}/api/v2/Groups/{groupIdOrIdentifier}/users | Adds a collection of users to the group using their id and/or usernames.
[**group_create_group**](GroupApi.md#group_create_group) | **POST** /{tenantUrlCode}/api/v2/Groups/Groups | Creates a group.
[**group_delete_group**](GroupApi.md#group_delete_group) | **DELETE** /{tenantUrlCode}/api/v2/Groups/{groupIdOrIdentifier} | Deletes a specific group.
[**group_get_group**](GroupApi.md#group_get_group) | **GET** /{tenantUrlCode}/api/v2/Groups/{groupIdOrIdentifier} | Gets a specific group by id or identifier.
[**group_get_groups**](GroupApi.md#group_get_groups) | **GET** /{tenantUrlCode}/api/v2/Groups | Gets all the groups.
[**group_remove_users_from_group**](GroupApi.md#group_remove_users_from_group) | **DELETE** /{tenantUrlCode}/api/v2/Groups/{groupIdOrIdentifier}/users | Removes a collection of users to the group using their id and/or usernames.
[**group_update_group**](GroupApi.md#group_update_group) | **PATCH** /{tenantUrlCode}/api/v2/Groups/{groupIdOrIdentifier} | Updates a group.

# **group_add_users_to_group**
> Group group_add_users_to_group(body, group_id_or_identifier, tenant_url_code)

Adds a collection of users to the group using their id and/or usernames.

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
api_instance = cartovista_cloud_clients.GroupApi(cartovista_cloud_clients.ApiClient(configuration))
body = ['body_example'] # list[str] | 
group_id_or_identifier = 'group_id_or_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Adds a collection of users to the group using their id and/or usernames.
    api_response = api_instance.group_add_users_to_group(body, group_id_or_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_add_users_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **group_id_or_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Group**](Group.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_create_group**
> Group group_create_group(body, tenant_url_code)

Creates a group.

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
api_instance = cartovista_cloud_clients.GroupApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.CreateGroupParameter() # CreateGroupParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a group.
    api_response = api_instance.group_create_group(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateGroupParameter**](CreateGroupParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Group**](Group.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_delete_group**
> group_delete_group(group_id_or_identifier, tenant_url_code)

Deletes a specific group.

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
api_instance = cartovista_cloud_clients.GroupApi(cartovista_cloud_clients.ApiClient(configuration))
group_id_or_identifier = 'group_id_or_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes a specific group.
    api_instance.group_delete_group(group_id_or_identifier, tenant_url_code)
except ApiException as e:
    print("Exception when calling GroupApi->group_delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id_or_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_get_group**
> Group group_get_group(group_id_or_identifier, tenant_url_code)

Gets a specific group by id or identifier.

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
api_instance = cartovista_cloud_clients.GroupApi(cartovista_cloud_clients.ApiClient(configuration))
group_id_or_identifier = 'group_id_or_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific group by id or identifier.
    api_response = api_instance.group_get_group(group_id_or_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id_or_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Group**](Group.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_get_groups**
> list[Group] group_get_groups(tenant_url_code)

Gets all the groups.

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
api_instance = cartovista_cloud_clients.GroupApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the groups.
    api_response = api_instance.group_get_groups(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_get_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Group]**](Group.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_remove_users_from_group**
> Group group_remove_users_from_group(body, group_id_or_identifier, tenant_url_code)

Removes a collection of users to the group using their id and/or usernames.

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
api_instance = cartovista_cloud_clients.GroupApi(cartovista_cloud_clients.ApiClient(configuration))
body = ['body_example'] # list[str] | 
group_id_or_identifier = 'group_id_or_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Removes a collection of users to the group using their id and/or usernames.
    api_response = api_instance.group_remove_users_from_group(body, group_id_or_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_remove_users_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **group_id_or_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Group**](Group.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_update_group**
> Group group_update_group(body, group_id_or_identifier, tenant_url_code)

Updates a group.

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
api_instance = cartovista_cloud_clients.GroupApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateGroupParameter() # UpdateGroupParameter | 
group_id_or_identifier = 'group_id_or_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates a group.
    api_response = api_instance.group_update_group(body, group_id_or_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateGroupParameter**](UpdateGroupParameter.md)|  | 
 **group_id_or_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Group**](Group.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


