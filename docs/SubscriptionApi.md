# cartovista_cloud_clients.SubscriptionApi

All URIs are relative to *https://cloud.cartovista.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_cancel_scheduled_subscription_change**](SubscriptionApi.md#subscription_cancel_scheduled_subscription_change) | **DELETE** /{tenantUrlCode}/api/v2/subscription/cancel-scheduled-change | Cancels scheduled subscription changes.
[**subscription_dismiss_schedule_notice**](SubscriptionApi.md#subscription_dismiss_schedule_notice) | **POST** /{tenantUrlCode}/api/v2/subscription/dismiss-schedule-notice | Closes the subscription scheduled change notice.
[**subscription_dismiss_subscription_banner**](SubscriptionApi.md#subscription_dismiss_subscription_banner) | **POST** /{tenantUrlCode}/api/v2/subscription/dismiss-banner | Closes the subscription expiry warning.
[**subscription_get_content_count**](SubscriptionApi.md#subscription_get_content_count) | **GET** /{tenantUrlCode}/api/v2/subscription/content-count | Gets the number of maps, layers, features and users in the organization.
[**subscription_get_next_invoice_price**](SubscriptionApi.md#subscription_get_next_invoice_price) | **GET** /{tenantUrlCode}/api/v2/subscription/next-invoice-price | Gets the price for the next invoice.
[**subscription_get_plans**](SubscriptionApi.md#subscription_get_plans) | **GET** /{tenantUrlCode}/api/v2/subscription/plans | Gets the subscription plan available for this organization.
[**subscription_get_prorated_price**](SubscriptionApi.md#subscription_get_prorated_price) | **POST** /{tenantUrlCode}/api/v2/subscription/prorated-price | Gets the prorated price for subscription changes.
[**subscription_open_customer_portal**](SubscriptionApi.md#subscription_open_customer_portal) | **GET** /{tenantUrlCode}/api/v2/subscription/customer-portal | Gets a URL to the Stripe portal to manage the subscription.
[**subscription_subscribe**](SubscriptionApi.md#subscription_subscribe) | **POST** /{tenantUrlCode}/api/v2/subscription | Update the subscriptions.
[**subscription_subscription_success**](SubscriptionApi.md#subscription_subscription_success) | **GET** /{tenantUrlCode}/api/v2/subscription/{sessionId} | Callback route used by Stripe.

# **subscription_cancel_scheduled_subscription_change**
> SubscribeResponse subscription_cancel_scheduled_subscription_change(change_to_cancel, tenant_url_code)

Cancels scheduled subscription changes.

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
api_instance = cartovista_cloud_clients.SubscriptionApi(cartovista_cloud_clients.ApiClient(configuration))
change_to_cancel = cartovista_cloud_clients.SubscriptionChangeType() # SubscriptionChangeType | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Cancels scheduled subscription changes.
    api_response = api_instance.subscription_cancel_scheduled_subscription_change(change_to_cancel, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->subscription_cancel_scheduled_subscription_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_to_cancel** | [**SubscriptionChangeType**](.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**SubscribeResponse**](SubscribeResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_dismiss_schedule_notice**
> User subscription_dismiss_schedule_notice(tenant_url_code)

Closes the subscription scheduled change notice.

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
api_instance = cartovista_cloud_clients.SubscriptionApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Closes the subscription scheduled change notice.
    api_response = api_instance.subscription_dismiss_schedule_notice(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->subscription_dismiss_schedule_notice: %s\n" % e)
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

# **subscription_dismiss_subscription_banner**
> User subscription_dismiss_subscription_banner(tenant_url_code)

Closes the subscription expiry warning.

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
api_instance = cartovista_cloud_clients.SubscriptionApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Closes the subscription expiry warning.
    api_response = api_instance.subscription_dismiss_subscription_banner(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->subscription_dismiss_subscription_banner: %s\n" % e)
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

# **subscription_get_content_count**
> ContentCount subscription_get_content_count(tenant_url_code)

Gets the number of maps, layers, features and users in the organization.

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
api_instance = cartovista_cloud_clients.SubscriptionApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the number of maps, layers, features and users in the organization.
    api_response = api_instance.subscription_get_content_count(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->subscription_get_content_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**ContentCount**](ContentCount.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_get_next_invoice_price**
> PriceWithCurrency subscription_get_next_invoice_price(tenant_url_code)

Gets the price for the next invoice.

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
api_instance = cartovista_cloud_clients.SubscriptionApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the price for the next invoice.
    api_response = api_instance.subscription_get_next_invoice_price(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->subscription_get_next_invoice_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**PriceWithCurrency**](PriceWithCurrency.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_get_plans**
> SubscriptionPlans subscription_get_plans(tenant_url_code)

Gets the subscription plan available for this organization.

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
api_instance = cartovista_cloud_clients.SubscriptionApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the subscription plan available for this organization.
    api_response = api_instance.subscription_get_plans(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->subscription_get_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

[**SubscriptionPlans**](SubscriptionPlans.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_get_prorated_price**
> PriceWithCurrency subscription_get_prorated_price(body, tenant_url_code)

Gets the prorated price for subscription changes.

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
api_instance = cartovista_cloud_clients.SubscriptionApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.GetProratedPriceParameter() # GetProratedPriceParameter | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets the prorated price for subscription changes.
    api_response = api_instance.subscription_get_prorated_price(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->subscription_get_prorated_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetProratedPriceParameter**](GetProratedPriceParameter.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**PriceWithCurrency**](PriceWithCurrency.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_open_customer_portal**
> str subscription_open_customer_portal(tenant_url_code)

Gets a URL to the Stripe portal to manage the subscription.

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
api_instance = cartovista_cloud_clients.SubscriptionApi(cartovista_cloud_clients.ApiClient(configuration))
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Gets a URL to the Stripe portal to manage the subscription.
    api_response = api_instance.subscription_open_customer_portal(tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->subscription_open_customer_portal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_subscribe**
> SubscribeResponse subscription_subscribe(body, tenant_url_code)

Update the subscriptions.

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
api_instance = cartovista_cloud_clients.SubscriptionApi(cartovista_cloud_clients.ApiClient(configuration))
body = cartovista_cloud_clients.SubscribeParameters() # SubscribeParameters | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Update the subscriptions.
    api_response = api_instance.subscription_subscribe(body, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->subscription_subscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscribeParameters**](SubscribeParameters.md)|  | 
 **tenant_url_code** | **str**|  | 

### Return type

[**SubscribeResponse**](SubscribeResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_subscription_success**
> str subscription_subscription_success(session_id, tenant_url_code)

Callback route used by Stripe.

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
api_instance = cartovista_cloud_clients.SubscriptionApi(cartovista_cloud_clients.ApiClient(configuration))
session_id = 'session_id_example' # str | 
tenant_url_code = 'tenant_url_code_example' # str | 

try:
    # Callback route used by Stripe.
    api_response = api_instance.subscription_subscription_success(session_id, tenant_url_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->subscription_subscription_success: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **tenant_url_code** | **str**|  | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [secretKey](../README.md#secretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


