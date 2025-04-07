# compass.api_client.MulticallApi

All URIs are relative to *https://api.compasslabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**multicall_authorization**](MulticallApi.md#multicall_authorization) | **POST** /v0/multicall/authorization | Get EIP-7702 Authorization
[**multicall_execute**](MulticallApi.md#multicall_execute) | **POST** /v0/multicall/execute | Execute Tx Batching


# **multicall_authorization**
> MulticallAuthorizationResponse multicall_authorization(multicall_authorization_request)

Get EIP-7702 Authorization

Get authorization data for EIP-7702 batching operations.

This authorization is required to prevent replay attacks and ensure transaction
ordering when batching multiple actions into a single transaction. The authorization
includes a nonce and chain ID to guarantee transaction uniqueness and proper network
targeting.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.multicall_authorization_request import MulticallAuthorizationRequest
from compass.api_client.models.multicall_authorization_response import MulticallAuthorizationResponse
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.compasslabs.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "https://api.compasslabs.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with compass.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compass.api_client.MulticallApi(api_client)
    multicall_authorization_request = compass.api_client.MulticallAuthorizationRequest() # MulticallAuthorizationRequest | 

    try:
        # Get EIP-7702 Authorization
        api_response = api_instance.multicall_authorization(multicall_authorization_request)
        print("The response of MulticallApi->multicall_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticallApi->multicall_authorization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multicall_authorization_request** | [**MulticallAuthorizationRequest**](MulticallAuthorizationRequest.md)|  | 

### Return type

[**MulticallAuthorizationResponse**](MulticallAuthorizationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multicall_execute**
> UnsignedMulticallTransaction multicall_execute(multicall_execute_request)

Execute Tx Batching

Execute a batch of transactions in a single multicall using EIP-7702.

This endpoint allows bundling multiple contract calls into a single atomic
transaction, reducing gas costs and ensuring all operations succeed or fail
together. The transaction must be authorized using the /authorization endpoint to
prevent replay attacks.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.multicall_execute_request import MulticallExecuteRequest
from compass.api_client.models.unsigned_multicall_transaction import UnsignedMulticallTransaction
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.compasslabs.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "https://api.compasslabs.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with compass.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compass.api_client.MulticallApi(api_client)
    multicall_execute_request = compass.api_client.MulticallExecuteRequest() # MulticallExecuteRequest | 

    try:
        # Execute Tx Batching
        api_response = api_instance.multicall_execute(multicall_execute_request)
        print("The response of MulticallApi->multicall_execute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticallApi->multicall_execute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multicall_execute_request** | [**MulticallExecuteRequest**](MulticallExecuteRequest.md)|  | 

### Return type

[**UnsignedMulticallTransaction**](UnsignedMulticallTransaction.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

