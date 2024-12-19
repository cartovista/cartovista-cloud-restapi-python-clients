# cartovista_cloud_clients.OrganizationApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_accept_organization_disclaimer**](OrganizationApi.md#organization_accept_organization_disclaimer) | **POST** /{tenantUrlCode}/api/v2/organization/disclaimer/accept | Marks the organization&#x27;s disclaimer as seen for the current user.
[**organization_delete_organization**](OrganizationApi.md#organization_delete_organization) | **DELETE** /{tenantUrlCode}/api/v2/organization | Deletes the current organization.
[**organization_get_organization**](OrganizationApi.md#organization_get_organization) | **GET** /{tenantUrlCode}/api/v2/organization | Gets the current organization.
[**organization_get_organization_disclaimers**](OrganizationApi.md#organization_get_organization_disclaimers) | **GET** /{tenantUrlCode}/api/v2/organization/disclaimer | Gets the current organization&#x27;s disclaimer.
[**organization_set_organization_disclaimers**](OrganizationApi.md#organization_set_organization_disclaimers) | **POST** /{tenantUrlCode}/api/v2/organization/disclaimer | Updates the current organization&#x27;s disclaimer.
[**organization_update_license**](OrganizationApi.md#organization_update_license) | **POST** /{tenantUrlCode}/api/v2/organization/license | Updates the current organization&#x27;s license.
[**organization_update_organization**](OrganizationApi.md#organization_update_organization) | **PATCH** /{tenantUrlCode}/api/v2/organization | Updates the current organization.
[**organization_update_organization_logo**](OrganizationApi.md#organization_update_organization_logo) | **PATCH** /{tenantUrlCode}/api/v2/organization/logo | Updates the current organization&#x27;s logo.

# **organization_accept_organization_disclaimer**
> User organization_accept_organization_disclaimer(tenant_url_code)

Marks the organization's disclaimer as seen for the current user.

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
api_instance = cartovista_cloud_clients.OrganizationApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Marks the organization's disclaimer as seen for the current user.
    api_response = api_instance.organization_accept_organization_disclaimer(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->organization_accept_organization_disclaimer: %s\n" % e)
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

# **organization_delete_organization**
> organization_delete_organization(body, tenant_url_code)

Deletes the current organization.

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
api_instance = cartovista_cloud_clients.OrganizationApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.DeleteOrganizationParameter() # DeleteOrganizationParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Deletes the current organization.
    api_instance.organization_delete_organization(body, tenant_url_code)
except ApiException as e:
    print("Exception when calling OrganizationApi->organization_delete_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteOrganizationParameter**](DeleteOrganizationParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_get_organization**
> Organization organization_get_organization(tenant_url_code)

Gets the current organization.

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
api_instance = cartovista_cloud_clients.OrganizationApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the current organization.
    api_response = api_instance.organization_get_organization(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->organization_get_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**Organization**](Organization.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_get_organization_disclaimers**
> list[TenantDisclaimer] organization_get_organization_disclaimers(tenant_url_code)

Gets the current organization's disclaimer.

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
api_instance = cartovista_cloud_clients.OrganizationApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the current organization's disclaimer.
    api_response = api_instance.organization_get_organization_disclaimers(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->organization_get_organization_disclaimers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**list[TenantDisclaimer]**](TenantDisclaimer.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_set_organization_disclaimers**
> Organization organization_set_organization_disclaimers(body, tenant_url_code, reset_accepted_disclaimers=reset_accepted_disclaimers)

Updates the current organization's disclaimer.

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
api_instance = cartovista_cloud_clients.OrganizationApi(cartovista_cloud_clients.ApiClient(configuration))
body = [cartovista_cloud_clients.SetDisclaimerParam()] # list[SetDisclaimerParam] | 
tenant_url_code = 'tenant_url_code_example' # str | 
reset_accepted_disclaimers = false # bool |  (optional) (default to false)

try:
    # Updates the current organization's disclaimer.
    api_response = api_instance.organization_set_organization_disclaimers(body, tenant_url_code, reset_accepted_disclaimers=reset_accepted_disclaimers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->organization_set_organization_disclaimers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[SetDisclaimerParam]**](SetDisclaimerParam.md)|  | 
 **tenant_url_code** | **str**|  | 
 **reset_accepted_disclaimers** | **bool**|  | [optional] [default to false]

### Return type

[**Organization**](Organization.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_update_license**
> organization_update_license(body, tenant_url_code)

Updates the current organization's license.

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
api_instance = cartovista_cloud_clients.OrganizationApi(cartovista_cloud_clients.ApiClient(configuration))
body = 'body_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the current organization's license.
    api_instance.organization_update_license(body, tenant_url_code)
except ApiException as e:
    print("Exception when calling OrganizationApi->organization_update_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_update_organization**
> Organization organization_update_organization(body, tenant_url_code)

Updates the current organization.

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
api_instance = cartovista_cloud_clients.OrganizationApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.UpdateOrganizationParameter() # UpdateOrganizationParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Updates the current organization.
    api_response = api_instance.organization_update_organization(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->organization_update_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOrganizationParameter**](UpdateOrganizationParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**Organization**](Organization.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_update_organization_logo**
> Organization organization_update_organization_logo(tenant_url_code, file=file)

Updates the current organization's logo.

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
api_instance = cartovista_cloud_clients.OrganizationApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Updates the current organization's logo.
    api_response = api_instance.organization_update_organization_logo(tenant_url_code, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->organization_update_organization_logo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


