# cartovista_cloud_clients.SignUpApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sign_up_confirm_sign_up**](SignUpApi.md#sign_up_confirm_sign_up) | **POST** /api/v2/SignUp/{userId}/{confirmationCode} | Finalizes the organization creation.
[**sign_up_sign_up**](SignUpApi.md#sign_up_sign_up) | **POST** /api/v2/SignUp | Creates a new organization in a pending state.
[**sign_up_sign_up_license**](SignUpApi.md#sign_up_sign_up_license) | **POST** /api/v2/SignUp/license | Creates a new organization with a license key.
[**sign_up_validate_company_name**](SignUpApi.md#sign_up_validate_company_name) | **GET** /api/v2/SignUp/validateCompanyName | Checks if an organization name is already taken.
[**sign_up_validate_sign_up_code**](SignUpApi.md#sign_up_validate_sign_up_code) | **GET** /api/v2/SignUp/{userId}/{confirmationCode}/validate | Checks if the sign up validation code has not expired.

# **sign_up_confirm_sign_up**
> str sign_up_confirm_sign_up(body, user_id, confirmation_code)

Finalizes the organization creation.

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
api_instance = cartovista_cloud_clients.SignUpApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.ConfirmSignUpParameter() # ConfirmSignUpParameter | 
user_id = 'user_id_example' # str | 
confirmation_code = 'confirmation_code_example' # str | 

try:
    # Finalizes the organization creation.
    api_response = api_instance.sign_up_confirm_sign_up(body, user_id, confirmation_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignUpApi->sign_up_confirm_sign_up: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfirmSignUpParameter**](ConfirmSignUpParameter.md)|  | 
 **user_id** | **str**|  | 
 **confirmation_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_up_sign_up**
> str sign_up_sign_up(body)

Creates a new organization in a pending state.

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
api_instance = cartovista_cloud_clients.SignUpApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.SignUpTrialParameter() # SignUpTrialParameter | 

try:
    # Creates a new organization in a pending state.
    api_response = api_instance.sign_up_sign_up(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignUpApi->sign_up_sign_up: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SignUpTrialParameter**](SignUpTrialParameter.md)|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_up_sign_up_license**
> str sign_up_sign_up_license(body)

Creates a new organization with a license key.

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
api_instance = cartovista_cloud_clients.SignUpApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.SignUpLicenseParameter() # SignUpLicenseParameter | 

try:
    # Creates a new organization with a license key.
    api_response = api_instance.sign_up_sign_up_license(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignUpApi->sign_up_sign_up_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SignUpLicenseParameter**](SignUpLicenseParameter.md)|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_up_validate_company_name**
> bool sign_up_validate_company_name(company_name)

Checks if an organization name is already taken.

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
api_instance = cartovista_cloud_clients.SignUpApi(cartovista_cloud_clients.ApiClient(configuration))
company_name = 'company_name_example' # str | 

try:
    # Checks if an organization name is already taken.
    api_response = api_instance.sign_up_validate_company_name(company_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignUpApi->sign_up_validate_company_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_name** | **str**|  | 

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_up_validate_sign_up_code**
> UserReset sign_up_validate_sign_up_code(user_id, confirmation_code)

Checks if the sign up validation code has not expired.

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
api_instance = cartovista_cloud_clients.SignUpApi(cartovista_cloud_clients.ApiClient(configuration))
user_id = 'user_id_example' # str | 
confirmation_code = 'confirmation_code_example' # str | 

try:
    # Checks if the sign up validation code has not expired.
    api_response = api_instance.sign_up_validate_sign_up_code(user_id, confirmation_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignUpApi->sign_up_validate_sign_up_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **confirmation_code** | **str**|  | 

### Return type

[**UserReset**](UserReset.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

