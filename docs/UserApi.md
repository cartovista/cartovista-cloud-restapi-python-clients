# cartovista_cloud_clients.UserApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_change_password**](UserApi.md#user_change_password) | **PATCH** /{tenantUrlCode}/api/v2/users/{UserIdentifier}/password | Updates the user&#x27;s password.
[**user_confirm_invitation**](UserApi.md#user_confirm_invitation) | **POST** /{tenantUrlCode}/api/v2/users/confirm-invitation | Confirms the invitation and updates the user.
[**user_create_user**](UserApi.md#user_create_user) | **POST** /{tenantUrlCode}/api/v2/users | Creates a new user.
[**user_delete_user**](UserApi.md#user_delete_user) | **DELETE** /{tenantUrlCode}/api/v2/users/{UserIdentifier} | Deletes the user.
[**user_export_user_elements**](UserApi.md#user_export_user_elements) | **POST** /{tenantUrlCode}/api/v2/users/export | Exports an Excel sheet of all the users and groups. The file can be downloaded with &#x60;DownloadFile/download&#x60;. The language is used to localized the sheet&#x27;s name and columns.
[**user_get_current_user**](UserApi.md#user_get_current_user) | **GET** /{tenantUrlCode}/api/v2/users/current | Gets the current authentified user.
[**user_get_first_admin**](UserApi.md#user_get_first_admin) | **GET** /{tenantUrlCode}/api/v2/users/firstAdmin | Gets the oldest active administator user.
[**user_get_importable_groups**](UserApi.md#user_get_importable_groups) | **POST** /{tenantUrlCode}/api/v2/users/getImportableGroups | 
[**user_get_importable_users**](UserApi.md#user_get_importable_users) | **POST** /{tenantUrlCode}/api/v2/users/getImportableUsers | 
[**user_get_user**](UserApi.md#user_get_user) | **GET** /{tenantUrlCode}/api/v2/users/{UserIdentifier} | Gets a specific user.
[**user_get_user_groups**](UserApi.md#user_get_user_groups) | **GET** /{tenantUrlCode}/api/v2/users/{UserIdentifier}/groups | Gets all the groups the user belongs to.
[**user_get_users**](UserApi.md#user_get_users) | **GET** /{tenantUrlCode}/api/v2/users | Gets a all the users in a specific tenant.
[**user_get_users_content**](UserApi.md#user_get_users_content) | **POST** /{tenantUrlCode}/api/v2/users/search | Searches across all the users (email, username, first name and last name), groups (name and description) and folders (name) for the provided search criteria.
[**user_import_groups**](UserApi.md#user_import_groups) | **POST** /{tenantUrlCode}/api/v2/users/import/groups | 
[**user_import_users**](UserApi.md#user_import_users) | **POST** /{tenantUrlCode}/api/v2/users/import | 
[**user_invite_users**](UserApi.md#user_invite_users) | **POST** /{tenantUrlCode}/api/v2/users/invite | Creates new users and sends invitations to the new users.
[**user_update_current_user**](UserApi.md#user_update_current_user) | **PATCH** /{tenantUrlCode}/api/v2/users/current | Updates the user properties modifiable by regular users.
[**user_update_user**](UserApi.md#user_update_user) | **PATCH** /{tenantUrlCode}/api/v2/users/{UserIdentifier} | Updates the user.

# **user_change_password**
> bool user_change_password(body, user_identifier, tenant_url_code)

Updates the user's password.

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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ChangePasswordParameter() # ChangePasswordParameter | 
user_identifier = 'user_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the user's password.
    api_response = api_instance.user_change_password(body, user_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangePasswordParameter**](ChangePasswordParameter.md)|  | 
 **user_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_confirm_invitation**
> str user_confirm_invitation(body, tenant_url_code)

Confirms the invitation and updates the user.

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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ConfirmInvitationParameter() # ConfirmInvitationParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Confirms the invitation and updates the user.
    api_response = api_instance.user_confirm_invitation(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_confirm_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfirmInvitationParameter**](ConfirmInvitationParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_create_user**
> User user_create_user(body, tenant_url_code)

Creates a new user.

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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UserCreateParameter() # UserCreateParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates a new user.
    api_response = api_instance.user_create_user(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreateParameter**](UserCreateParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_delete_user**
> bool user_delete_user(user_identifier, tenant_url_code)

Deletes the user.

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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
user_identifier = 'user_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes the user.
    api_response = api_instance.user_delete_user(user_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_export_user_elements**
> str user_export_user_elements(selected_language, tenant_url_code)

Exports an Excel sheet of all the users and groups. The file can be downloaded with `DownloadFile/download`. The language is used to localized the sheet's name and columns.

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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
selected_language = 'selected_language_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Exports an Excel sheet of all the users and groups. The file can be downloaded with `DownloadFile/download`. The language is used to localized the sheet's name and columns.
    api_response = api_instance.user_export_user_elements(selected_language, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_export_user_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selected_language** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_current_user**
> User user_get_current_user(tenant_url_code)

Gets the current authentified user.

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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the current authentified user.
    api_response = api_instance.user_get_current_user(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_first_admin**
> User user_get_first_admin(tenant_url_code)

Gets the oldest active administator user.

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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the oldest active administator user.
    api_response = api_instance.user_get_first_admin(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_first_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_importable_groups**
> list[Group] user_get_importable_groups(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetImportableUsersParameter() # GetImportableUsersParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.user_get_importable_groups(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_importable_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetImportableUsersParameter**](GetImportableUsersParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Group]**](Group.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_importable_users**
> list[User] user_get_importable_users(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetImportableUsersParameter() # GetImportableUsersParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_response = api_instance.user_get_importable_users(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_importable_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetImportableUsersParameter**](GetImportableUsersParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[User]**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_user**
> User user_get_user(user_identifier, tenant_url_code)

Gets a specific user.

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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
user_identifier = 'user_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a specific user.
    api_response = api_instance.user_get_user(user_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_user_groups**
> list[Group] user_get_user_groups(user_identifier, tenant_url_code)

Gets all the groups the user belongs to.

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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
user_identifier = 'user_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets all the groups the user belongs to.
    api_response = api_instance.user_get_user_groups(user_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**list[Group]**](Group.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_users**
> list[User] user_get_users(tenant_url_code)

Gets a all the users in a specific tenant.

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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a all the users in a specific tenant.
    api_response = api_instance.user_get_users(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**list[User]**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_users_content**
> UsersContent user_get_users_content(body, tenant_url_code)

Searches across all the users (email, username, first name and last name), groups (name and description) and folders (name) for the provided search criteria.

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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetUsersContentParameters() # GetUsersContentParameters | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Searches across all the users (email, username, first name and last name), groups (name and description) and folders (name) for the provided search criteria.
    api_response = api_instance.user_get_users_content(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_users_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetUsersContentParameters**](GetUsersContentParameters.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**UsersContent**](UsersContent.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_import_groups**
> user_import_groups(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ImportGroupsParameter() # ImportGroupsParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_instance.user_import_groups(body, tenant_url_code)
except ApiException as e:
    print("Exception when calling UserApi->user_import_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportGroupsParameter**](ImportGroupsParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_import_users**
> user_import_users(body, tenant_url_code)



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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ImportUsersParameter() # ImportUsersParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    api_instance.user_import_users(body, tenant_url_code)
except ApiException as e:
    print("Exception when calling UserApi->user_import_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportUsersParameter**](ImportUsersParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_invite_users**
> user_invite_users(body, tenant_url_code)

Creates new users and sends invitations to the new users.

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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.InviteUsersParameter() # InviteUsersParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Creates new users and sends invitations to the new users.
    api_instance.user_invite_users(body, tenant_url_code)
except ApiException as e:
    print("Exception when calling UserApi->user_invite_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InviteUsersParameter**](InviteUsersParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update_current_user**
> User user_update_current_user(body, tenant_url_code)

Updates the user properties modifiable by regular users.

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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateCurrentUserParameter() # UpdateCurrentUserParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the user properties modifiable by regular users.
    api_response = api_instance.user_update_current_user(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_update_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCurrentUserParameter**](UpdateCurrentUserParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update_user**
> User user_update_user(body, user_identifier, tenant_url_code)

Updates the user.

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
api_instance = cartovista_cloud_clients.UserApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UserUpdateParameter() # UserUpdateParameter | 
user_identifier = 'user_identifier_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the user.
    api_response = api_instance.user_update_user(body, user_identifier, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserUpdateParameter**](UserUpdateParameter.md)|  | 
 **user_identifier** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


