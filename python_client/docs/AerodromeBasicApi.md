# compass.api_client.AerodromeBasicApi

All URIs are relative to *https://api.compasslabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aerodrome_basic_liquidity_provision_add_liquidity**](AerodromeBasicApi.md#aerodrome_basic_liquidity_provision_add_liquidity) | **POST** /v0/aerodrome_basic/liquidity_provision/add_liquidity | Provide liquidity
[**aerodrome_basic_liquidity_provision_add_liquidity_eth**](AerodromeBasicApi.md#aerodrome_basic_liquidity_provision_add_liquidity_eth) | **POST** /v0/aerodrome_basic/liquidity_provision/add_liquidity_eth | Provide liquidity using WETH
[**aerodrome_basic_liquidity_provision_remove_liquidity**](AerodromeBasicApi.md#aerodrome_basic_liquidity_provision_remove_liquidity) | **POST** /v0/aerodrome_basic/liquidity_provision/remove_liquidity | Remove liquidity
[**aerodrome_basic_liquidity_provision_remove_liquidity_eth**](AerodromeBasicApi.md#aerodrome_basic_liquidity_provision_remove_liquidity_eth) | **POST** /v0/aerodrome_basic/liquidity_provision/remove_liquidity_eth | Remove liquidity using WETH
[**aerodrome_basic_swap_eth_for_token**](AerodromeBasicApi.md#aerodrome_basic_swap_eth_for_token) | **POST** /v0/aerodrome_basic/swap/eth_for_token | Swap from ETH
[**aerodrome_basic_swap_token_for_eth**](AerodromeBasicApi.md#aerodrome_basic_swap_token_for_eth) | **POST** /v0/aerodrome_basic/swap/token_for_eth | Swap token for ETH
[**aerodrome_basic_swap_tokens**](AerodromeBasicApi.md#aerodrome_basic_swap_tokens) | **POST** /v0/aerodrome_basic/swap/tokens | Swap


# **aerodrome_basic_liquidity_provision_add_liquidity**
> UnsignedTransaction aerodrome_basic_liquidity_provision_add_liquidity(aerodrome_add_liquidity_request)

Provide liquidity

This endpoint allows users to provide liquidity to a specified pool on the
Aerodrome platform.

Users must specify the tokens, desired amounts, minimum amounts, and a deadline for
the transaction. The operation will ensure the pool exists and will use the sender's
address if no recipient is specified.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_add_liquidity_request import AerodromeAddLiquidityRequest
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
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
    api_instance = compass.api_client.AerodromeBasicApi(api_client)
    aerodrome_add_liquidity_request = compass.api_client.AerodromeAddLiquidityRequest() # AerodromeAddLiquidityRequest | 

    try:
        # Provide liquidity
        api_response = api_instance.aerodrome_basic_liquidity_provision_add_liquidity(aerodrome_add_liquidity_request)
        print("The response of AerodromeBasicApi->aerodrome_basic_liquidity_provision_add_liquidity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeBasicApi->aerodrome_basic_liquidity_provision_add_liquidity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_add_liquidity_request** | [**AerodromeAddLiquidityRequest**](AerodromeAddLiquidityRequest.md)|  | 

### Return type

[**UnsignedTransaction**](UnsignedTransaction.md)

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

# **aerodrome_basic_liquidity_provision_add_liquidity_eth**
> UnsignedTransaction aerodrome_basic_liquidity_provision_add_liquidity_eth(aerodrome_add_liquidity_eth_request)

Provide liquidity using WETH

This endpoint allows users to provide liquidity to a specified pool on the
Aerodrome platform using Wrapped Ether (WETH) and another token.

Users must specify the token pair, desired amounts, minimum amounts, and a deadline
for the transaction. The operation will ensure the pool exists and will use the
sender's address if no recipient is specified. The transaction will be executed
through the Aerodrome Basic Router contract, and the specified amount of WETH will
be sent along with the transaction.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_add_liquidity_eth_request import AerodromeAddLiquidityEthRequest
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
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
    api_instance = compass.api_client.AerodromeBasicApi(api_client)
    aerodrome_add_liquidity_eth_request = compass.api_client.AerodromeAddLiquidityEthRequest() # AerodromeAddLiquidityEthRequest | 

    try:
        # Provide liquidity using WETH
        api_response = api_instance.aerodrome_basic_liquidity_provision_add_liquidity_eth(aerodrome_add_liquidity_eth_request)
        print("The response of AerodromeBasicApi->aerodrome_basic_liquidity_provision_add_liquidity_eth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeBasicApi->aerodrome_basic_liquidity_provision_add_liquidity_eth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_add_liquidity_eth_request** | [**AerodromeAddLiquidityEthRequest**](AerodromeAddLiquidityEthRequest.md)|  | 

### Return type

[**UnsignedTransaction**](UnsignedTransaction.md)

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

# **aerodrome_basic_liquidity_provision_remove_liquidity**
> UnsignedTransaction aerodrome_basic_liquidity_provision_remove_liquidity(aerodrome_remove_liquidity_request)

Remove liquidity

This endpoint allows users to remove liquidity from a specified pool on the
Aerodrome platform.

Users must specify the token pair, the amount of liquidity to remove, minimum
amounts for each token, and a deadline for the transaction. The operation will
ensure the pool exists and will use the sender's address if no recipient is
specified. The transaction will be executed through the Aerodrome Basic Router
contract, and the specified amount of liquidity will be withdrawn from the pool.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_remove_liquidity_request import AerodromeRemoveLiquidityRequest
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
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
    api_instance = compass.api_client.AerodromeBasicApi(api_client)
    aerodrome_remove_liquidity_request = compass.api_client.AerodromeRemoveLiquidityRequest() # AerodromeRemoveLiquidityRequest | 

    try:
        # Remove liquidity
        api_response = api_instance.aerodrome_basic_liquidity_provision_remove_liquidity(aerodrome_remove_liquidity_request)
        print("The response of AerodromeBasicApi->aerodrome_basic_liquidity_provision_remove_liquidity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeBasicApi->aerodrome_basic_liquidity_provision_remove_liquidity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_remove_liquidity_request** | [**AerodromeRemoveLiquidityRequest**](AerodromeRemoveLiquidityRequest.md)|  | 

### Return type

[**UnsignedTransaction**](UnsignedTransaction.md)

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

# **aerodrome_basic_liquidity_provision_remove_liquidity_eth**
> UnsignedTransaction aerodrome_basic_liquidity_provision_remove_liquidity_eth(aerodrome_remove_liquidity_eth_request)

Remove liquidity using WETH

This endpoint allows users to remove liquidity from a pool on the Aerodrome
platform using WETH and another token.

Users must specify the token pair, the amount of liquidity to remove, minimum
amounts for each token, and a deadline for the transaction. The operation will
ensure the pool exists and will use the sender's address if no recipient is
specified. The transaction will be executed through the Aerodrome Basic Router
contract, and the specified amount of liquidity will be withdrawn from the pool.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_remove_liquidity_eth_request import AerodromeRemoveLiquidityEthRequest
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
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
    api_instance = compass.api_client.AerodromeBasicApi(api_client)
    aerodrome_remove_liquidity_eth_request = compass.api_client.AerodromeRemoveLiquidityEthRequest() # AerodromeRemoveLiquidityEthRequest | 

    try:
        # Remove liquidity using WETH
        api_response = api_instance.aerodrome_basic_liquidity_provision_remove_liquidity_eth(aerodrome_remove_liquidity_eth_request)
        print("The response of AerodromeBasicApi->aerodrome_basic_liquidity_provision_remove_liquidity_eth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeBasicApi->aerodrome_basic_liquidity_provision_remove_liquidity_eth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_remove_liquidity_eth_request** | [**AerodromeRemoveLiquidityEthRequest**](AerodromeRemoveLiquidityEthRequest.md)|  | 

### Return type

[**UnsignedTransaction**](UnsignedTransaction.md)

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

# **aerodrome_basic_swap_eth_for_token**
> UnsignedTransaction aerodrome_basic_swap_eth_for_token(aerodrome_swap_eth_for_token_request)

Swap from ETH

This endpoint allows you to swap a specified amount of ETH for a desired token on
the Aerodrome platform.

To protect against unfavorable exchange rates, you must specify the minimum amount
of the token you wish to receive. The transaction will only be executed if this
minimum amount is met, ensuring you do not accidentally trade at a disadvantageous
rate.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_swap_eth_for_token_request import AerodromeSwapEthForTokenRequest
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
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
    api_instance = compass.api_client.AerodromeBasicApi(api_client)
    aerodrome_swap_eth_for_token_request = compass.api_client.AerodromeSwapEthForTokenRequest() # AerodromeSwapEthForTokenRequest | 

    try:
        # Swap from ETH
        api_response = api_instance.aerodrome_basic_swap_eth_for_token(aerodrome_swap_eth_for_token_request)
        print("The response of AerodromeBasicApi->aerodrome_basic_swap_eth_for_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeBasicApi->aerodrome_basic_swap_eth_for_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_swap_eth_for_token_request** | [**AerodromeSwapEthForTokenRequest**](AerodromeSwapEthForTokenRequest.md)|  | 

### Return type

[**UnsignedTransaction**](UnsignedTransaction.md)

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

# **aerodrome_basic_swap_token_for_eth**
> UnsignedTransaction aerodrome_basic_swap_token_for_eth(aerodrome_swap_token_for_eth_request)

Swap token for ETH

Swap a specified amount of a token for ETH using the Aerodrome platform.

To protect against unfavorable exchange rates, you must specify the minimum amount
of ETH you wish to receive. The transaction will only be executed if this minimum
amount is met, ensuring you do not trade at a disadvantageous rate.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_swap_token_for_eth_request import AerodromeSwapTokenForEthRequest
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
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
    api_instance = compass.api_client.AerodromeBasicApi(api_client)
    aerodrome_swap_token_for_eth_request = compass.api_client.AerodromeSwapTokenForEthRequest() # AerodromeSwapTokenForEthRequest | 

    try:
        # Swap token for ETH
        api_response = api_instance.aerodrome_basic_swap_token_for_eth(aerodrome_swap_token_for_eth_request)
        print("The response of AerodromeBasicApi->aerodrome_basic_swap_token_for_eth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeBasicApi->aerodrome_basic_swap_token_for_eth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_swap_token_for_eth_request** | [**AerodromeSwapTokenForEthRequest**](AerodromeSwapTokenForEthRequest.md)|  | 

### Return type

[**UnsignedTransaction**](UnsignedTransaction.md)

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

# **aerodrome_basic_swap_tokens**
> UnsignedTransaction aerodrome_basic_swap_tokens(aerodrome_swap_tokens_request)

Swap

Swap one token for another on Aerodrome.

Ensure you specify the minimum amount you expect to receive to avoid trading at an
unfavorable exchange rate. This endpoint facilitates the exchange of tokens by
interacting with the Aerodrome smart contract, ensuring that the transaction is
executed only if the specified minimum output is met.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_swap_tokens_request import AerodromeSwapTokensRequest
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
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
    api_instance = compass.api_client.AerodromeBasicApi(api_client)
    aerodrome_swap_tokens_request = compass.api_client.AerodromeSwapTokensRequest() # AerodromeSwapTokensRequest | 

    try:
        # Swap
        api_response = api_instance.aerodrome_basic_swap_tokens(aerodrome_swap_tokens_request)
        print("The response of AerodromeBasicApi->aerodrome_basic_swap_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeBasicApi->aerodrome_basic_swap_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_swap_tokens_request** | [**AerodromeSwapTokensRequest**](AerodromeSwapTokensRequest.md)|  | 

### Return type

[**UnsignedTransaction**](UnsignedTransaction.md)

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

