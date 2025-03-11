# compass.api_client.DefaultApi

All URIs are relative to *https://api.compasslabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_page_auth_login_get**](DefaultApi.md#login_page_auth_login_get) | **GET** /auth/login | Login Page


# **login_page_auth_login_get**
> str login_page_auth_login_get()

Login Page

### Example


```python
import compass.api_client
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.compasslabs.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "https://api.compasslabs.ai"
)


# Enter a context with an instance of the API client
with compass.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compass.api_client.DefaultApi(api_client)

    try:
        # Login Page
        api_response = api_instance.login_page_auth_login_get()
        print("The response of DefaultApi->login_page_auth_login_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->login_page_auth_login_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

