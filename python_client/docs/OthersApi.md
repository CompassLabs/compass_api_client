# compass.api_client.OthersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_allowance_v0_generic_allowance_get_post**](OthersApi.md#get_allowance_v0_generic_allowance_get_post) | **POST** /v0/generic/allowance/get | Show the allowance of a user on a protocol
[**get_balance_v0_generic_balance_get_post**](OthersApi.md#get_balance_v0_generic_balance_get_post) | **POST** /v0/generic/balance/get | Get an ERC20 token&#39;s balance for a user
[**get_ens_details_v0_generic_ens_get_post**](OthersApi.md#get_ens_details_v0_generic_ens_get_post) | **POST** /v0/generic/ens/get | Get the wallet address and registrant of an ENS name
[**get_portfolio_v0_generic_portfolio_get_post**](OthersApi.md#get_portfolio_v0_generic_portfolio_get_post) | **POST** /v0/generic/portfolio/get | Get the portfolio details for a wallet address
[**get_price_v0_generic_price_usd_get_post**](OthersApi.md#get_price_v0_generic_price_usd_get_post) | **POST** /v0/generic/price/usd/get | Get the price of a given token relative to USD
[**get_tokens_v0_generic_supported_tokens_get_post**](OthersApi.md#get_tokens_v0_generic_supported_tokens_get_post) | **POST** /v0/generic/supported_tokens/get | Get supported tokens
[**set_allowance_v0_generic_allowance_set_post**](OthersApi.md#set_allowance_v0_generic_allowance_set_post) | **POST** /v0/generic/allowance/set | Change the allowance of a user on a protocol
[**set_any_allowance_v0_generic_allowance_set_any_post**](OthersApi.md#set_any_allowance_v0_generic_allowance_set_any_post) | **POST** /v0/generic/allowance/set_any | Sets allowance for any arbitrary ERC20 token address
[**transfer_erc20_v0_generic_transfer_erc20_post**](OthersApi.md#transfer_erc20_v0_generic_transfer_erc20_post) | **POST** /v0/generic/transfer/erc20 | Transfer ERC20 tokens to another address
[**transfer_native_token_v0_generic_transfer_native_token_post**](OthersApi.md#transfer_native_token_v0_generic_transfer_native_token_post) | **POST** /v0/generic/transfer/native_token | Transfer native ETH to another address
[**unwrap_weth_v0_generic_unwrap_weth_post**](OthersApi.md#unwrap_weth_v0_generic_unwrap_weth_post) | **POST** /v0/generic/unwrap_weth | Change WETH back into raw ETH
[**visualize_portfolio_v0_generic_visualize_portfolio_get_post**](OthersApi.md#visualize_portfolio_v0_generic_visualize_portfolio_get_post) | **POST** /v0/generic/visualize_portfolio/get | Visualize the token portfolio of a wallet address as a pie chart
[**wrap_eth_v0_generic_wrap_eth_post**](OthersApi.md#wrap_eth_v0_generic_wrap_eth_post) | **POST** /v0/generic/wrap_eth | Change raw ETH into WETH


# **get_allowance_v0_generic_allowance_get_post**
> AllowanceInfoResponse get_allowance_v0_generic_allowance_get_post(get_erc20_allowance_request)

Show the allowance of a user on a protocol

In decentralized finance (DeFi) protocols such as Uniswap or AAVE,
        users must set a token allowance to authorize the protocol to spend
        a specified amount of their tokens on their behalf. This is a crucial
        step before engaging in any transactions or operations within these
        protocols, ensuring that the protocol has the necessary permissions
        to manage the user's tokens securely and efficiently.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.allowance_info_response import AllowanceInfoResponse
from compass.api_client.models.get_erc20_allowance_request import GetErc20AllowanceRequest
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "http://localhost"
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
    api_instance = compass.api_client.OthersApi(api_client)
    get_erc20_allowance_request = compass.api_client.GetErc20AllowanceRequest() # GetErc20AllowanceRequest | 

    try:
        # Show the allowance of a user on a protocol
        api_response = api_instance.get_allowance_v0_generic_allowance_get_post(get_erc20_allowance_request)
        print("The response of OthersApi->get_allowance_v0_generic_allowance_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->get_allowance_v0_generic_allowance_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_erc20_allowance_request** | [**GetErc20AllowanceRequest**](GetErc20AllowanceRequest.md)|  | 

### Return type

[**AllowanceInfoResponse**](AllowanceInfoResponse.md)

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

# **get_balance_v0_generic_balance_get_post**
> BalanceInfoResponse get_balance_v0_generic_balance_get_post(get_erc20_balance_request)

Get an ERC20 token's balance for a user

Returns the balance of a specific ERC20 token for a given user address.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.balance_info_response import BalanceInfoResponse
from compass.api_client.models.get_erc20_balance_request import GetErc20BalanceRequest
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "http://localhost"
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
    api_instance = compass.api_client.OthersApi(api_client)
    get_erc20_balance_request = compass.api_client.GetErc20BalanceRequest() # GetErc20BalanceRequest | 

    try:
        # Get an ERC20 token's balance for a user
        api_response = api_instance.get_balance_v0_generic_balance_get_post(get_erc20_balance_request)
        print("The response of OthersApi->get_balance_v0_generic_balance_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->get_balance_v0_generic_balance_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_erc20_balance_request** | [**GetErc20BalanceRequest**](GetErc20BalanceRequest.md)|  | 

### Return type

[**BalanceInfoResponse**](BalanceInfoResponse.md)

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

# **get_ens_details_v0_generic_ens_get_post**
> EnsNameInfoResponse get_ens_details_v0_generic_ens_get_post(get_ens_details_request)

Get the wallet address and registrant of an ENS name

An ENS name is a string ending in `.eth`. E.g. `vitalik.eth`. This endpoint can be used to query the actual ethereum wallet address behind the ENS name.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.ens_name_info_response import EnsNameInfoResponse
from compass.api_client.models.get_ens_details_request import GetEnsDetailsRequest
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "http://localhost"
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
    api_instance = compass.api_client.OthersApi(api_client)
    get_ens_details_request = compass.api_client.GetEnsDetailsRequest() # GetEnsDetailsRequest | 

    try:
        # Get the wallet address and registrant of an ENS name
        api_response = api_instance.get_ens_details_v0_generic_ens_get_post(get_ens_details_request)
        print("The response of OthersApi->get_ens_details_v0_generic_ens_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->get_ens_details_v0_generic_ens_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_ens_details_request** | [**GetEnsDetailsRequest**](GetEnsDetailsRequest.md)|  | 

### Return type

[**EnsNameInfoResponse**](EnsNameInfoResponse.md)

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

# **get_portfolio_v0_generic_portfolio_get_post**
> Portfolio get_portfolio_v0_generic_portfolio_get_post(portfolio_request)

Get the portfolio details for a wallet address

Fetch the detailed portfolio of a specific wallet address on a given blockchain. This includes the total value of the portfolio in USD and a breakdown of token balances, including their respective values and quantities.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.portfolio import Portfolio
from compass.api_client.models.portfolio_request import PortfolioRequest
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "http://localhost"
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
    api_instance = compass.api_client.OthersApi(api_client)
    portfolio_request = compass.api_client.PortfolioRequest() # PortfolioRequest | 

    try:
        # Get the portfolio details for a wallet address
        api_response = api_instance.get_portfolio_v0_generic_portfolio_get_post(portfolio_request)
        print("The response of OthersApi->get_portfolio_v0_generic_portfolio_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->get_portfolio_v0_generic_portfolio_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_request** | [**PortfolioRequest**](PortfolioRequest.md)|  | 

### Return type

[**Portfolio**](Portfolio.md)

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

# **get_price_v0_generic_price_usd_get_post**
> PriceResponse get_price_v0_generic_price_usd_get_post(price_request)

Get the price of a given token relative to USD

Retrieves the price of the specified token relative to USD using Chainlink's on-chain price feeds. Chainlink is a decentralized oracle that aggregates price data from off-chain sources. This ensures the price is tamper-resistant but the price might be stale with the update frequency of the oracle.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.price_request import PriceRequest
from compass.api_client.models.price_response import PriceResponse
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "http://localhost"
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
    api_instance = compass.api_client.OthersApi(api_client)
    price_request = compass.api_client.PriceRequest() # PriceRequest | 

    try:
        # Get the price of a given token relative to USD
        api_response = api_instance.get_price_v0_generic_price_usd_get_post(price_request)
        print("The response of OthersApi->get_price_v0_generic_price_usd_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->get_price_v0_generic_price_usd_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_request** | [**PriceRequest**](PriceRequest.md)|  | 

### Return type

[**PriceResponse**](PriceResponse.md)

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

# **get_tokens_v0_generic_supported_tokens_get_post**
> TokenInfo get_tokens_v0_generic_supported_tokens_get_post(tokens_request)

Get supported tokens

Get the list of supported tokens on a chain by the Compass API.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.token_info import TokenInfo
from compass.api_client.models.tokens_request import TokensRequest
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "http://localhost"
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
    api_instance = compass.api_client.OthersApi(api_client)
    tokens_request = compass.api_client.TokensRequest() # TokensRequest | 

    try:
        # Get supported tokens
        api_response = api_instance.get_tokens_v0_generic_supported_tokens_get_post(tokens_request)
        print("The response of OthersApi->get_tokens_v0_generic_supported_tokens_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->get_tokens_v0_generic_supported_tokens_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokens_request** | [**TokensRequest**](TokensRequest.md)|  | 

### Return type

[**TokenInfo**](TokenInfo.md)

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

# **set_allowance_v0_generic_allowance_set_post**
> UnsignedTransaction set_allowance_v0_generic_allowance_set_post(increase_allowance_request)

Change the allowance of a user on a protocol

This endpoint allows users to modify the token allowance for a specific
    protocol. In decentralized finance (DeFi), setting an allowance is a
    necessary step to authorize a protocol to spend a specified amount of
    tokens on behalf of the user. This operation is crucial for ensuring
    that the protocol can manage the user's tokens securely and efficiently,
    enabling seamless transactions and operations within the DeFi ecosystem.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.increase_allowance_request import IncreaseAllowanceRequest
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "http://localhost"
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
    api_instance = compass.api_client.OthersApi(api_client)
    increase_allowance_request = compass.api_client.IncreaseAllowanceRequest() # IncreaseAllowanceRequest | 

    try:
        # Change the allowance of a user on a protocol
        api_response = api_instance.set_allowance_v0_generic_allowance_set_post(increase_allowance_request)
        print("The response of OthersApi->set_allowance_v0_generic_allowance_set_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->set_allowance_v0_generic_allowance_set_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **increase_allowance_request** | [**IncreaseAllowanceRequest**](IncreaseAllowanceRequest.md)|  | 

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

# **set_any_allowance_v0_generic_allowance_set_any_post**
> UnsignedTransaction set_any_allowance_v0_generic_allowance_set_any_post(increase_allowance_any_request)

Sets allowance for any arbitrary ERC20 token address

This endpoint allows users to set an allowance for any arbitrary ERC20
    token address. In decentralized finance (DeFi), setting an allowance
    is a critical operation that permits a protocol to spend a specified
    amount of tokens on behalf of the user. This functionality is essential
    for enabling secure and efficient token management, facilitating smooth
    transactions and operations within the DeFi ecosystem. By using this
    endpoint, users can specify the token address and the amount they wish
    to authorize, ensuring precise control over their token allowances.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.increase_allowance_any_request import IncreaseAllowanceAnyRequest
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "http://localhost"
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
    api_instance = compass.api_client.OthersApi(api_client)
    increase_allowance_any_request = compass.api_client.IncreaseAllowanceAnyRequest() # IncreaseAllowanceAnyRequest | 

    try:
        # Sets allowance for any arbitrary ERC20 token address
        api_response = api_instance.set_any_allowance_v0_generic_allowance_set_any_post(increase_allowance_any_request)
        print("The response of OthersApi->set_any_allowance_v0_generic_allowance_set_any_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->set_any_allowance_v0_generic_allowance_set_any_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **increase_allowance_any_request** | [**IncreaseAllowanceAnyRequest**](IncreaseAllowanceAnyRequest.md)|  | 

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

# **transfer_erc20_v0_generic_transfer_erc20_post**
> UnsignedTransaction transfer_erc20_v0_generic_transfer_erc20_post(transfer_erc20_request)

Transfer ERC20 tokens to another address

Sends ERC20 tokens from the sender's address to the specified recipient.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.transfer_erc20_request import TransferERC20Request
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "http://localhost"
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
    api_instance = compass.api_client.OthersApi(api_client)
    transfer_erc20_request = compass.api_client.TransferERC20Request() # TransferERC20Request | 

    try:
        # Transfer ERC20 tokens to another address
        api_response = api_instance.transfer_erc20_v0_generic_transfer_erc20_post(transfer_erc20_request)
        print("The response of OthersApi->transfer_erc20_v0_generic_transfer_erc20_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->transfer_erc20_v0_generic_transfer_erc20_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_erc20_request** | [**TransferERC20Request**](TransferERC20Request.md)|  | 

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

# **transfer_native_token_v0_generic_transfer_native_token_post**
> UnsignedTransaction transfer_native_token_v0_generic_transfer_native_token_post(transfer_eth_request)

Transfer native ETH to another address

Sends native ETH from the sender's address to the specified recipient.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.transfer_eth_request import TransferEthRequest
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "http://localhost"
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
    api_instance = compass.api_client.OthersApi(api_client)
    transfer_eth_request = compass.api_client.TransferEthRequest() # TransferEthRequest | 

    try:
        # Transfer native ETH to another address
        api_response = api_instance.transfer_native_token_v0_generic_transfer_native_token_post(transfer_eth_request)
        print("The response of OthersApi->transfer_native_token_v0_generic_transfer_native_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->transfer_native_token_v0_generic_transfer_native_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_eth_request** | [**TransferEthRequest**](TransferEthRequest.md)|  | 

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

# **unwrap_weth_v0_generic_unwrap_weth_post**
> UnsignedTransaction unwrap_weth_v0_generic_unwrap_weth_post(unwrap_weth_request)

Change WETH back into raw ETH

Unwrapping WETH converts the ERC-20 compliant form of ETH back to native ETH that can be used for gas and other native purposes.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
from compass.api_client.models.unwrap_weth_request import UnwrapWethRequest
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "http://localhost"
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
    api_instance = compass.api_client.OthersApi(api_client)
    unwrap_weth_request = compass.api_client.UnwrapWethRequest() # UnwrapWethRequest | 

    try:
        # Change WETH back into raw ETH
        api_response = api_instance.unwrap_weth_v0_generic_unwrap_weth_post(unwrap_weth_request)
        print("The response of OthersApi->unwrap_weth_v0_generic_unwrap_weth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->unwrap_weth_v0_generic_unwrap_weth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unwrap_weth_request** | [**UnwrapWethRequest**](UnwrapWethRequest.md)|  | 

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

# **visualize_portfolio_v0_generic_visualize_portfolio_get_post**
> Image visualize_portfolio_v0_generic_visualize_portfolio_get_post(visualize_portfolio_request)

Visualize the token portfolio of a wallet address as a pie chart

Generate a visual representation of the token portfolio for a wallet address. The response is an SVG image of a pie chart depicting the relative distribution of tokens held, colored and labeled with token symbols, percentages and token values in USD.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.image import Image
from compass.api_client.models.visualize_portfolio_request import VisualizePortfolioRequest
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "http://localhost"
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
    api_instance = compass.api_client.OthersApi(api_client)
    visualize_portfolio_request = compass.api_client.VisualizePortfolioRequest() # VisualizePortfolioRequest | 

    try:
        # Visualize the token portfolio of a wallet address as a pie chart
        api_response = api_instance.visualize_portfolio_v0_generic_visualize_portfolio_get_post(visualize_portfolio_request)
        print("The response of OthersApi->visualize_portfolio_v0_generic_visualize_portfolio_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->visualize_portfolio_v0_generic_visualize_portfolio_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visualize_portfolio_request** | [**VisualizePortfolioRequest**](VisualizePortfolioRequest.md)|  | 

### Return type

[**Image**](Image.md)

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

# **wrap_eth_v0_generic_wrap_eth_post**
> UnsignedTransaction wrap_eth_v0_generic_wrap_eth_post(wrap_eth_request)

Change raw ETH into WETH

Wrapping ETH creates an ERC-20 compliant form of ETH that is typically needed for it to be traded on DeFi protocols.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
from compass.api_client.models.wrap_eth_request import WrapEthRequest
from compass.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compass.api_client.Configuration(
    host = "http://localhost"
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
    api_instance = compass.api_client.OthersApi(api_client)
    wrap_eth_request = compass.api_client.WrapEthRequest() # WrapEthRequest | 

    try:
        # Change raw ETH into WETH
        api_response = api_instance.wrap_eth_v0_generic_wrap_eth_post(wrap_eth_request)
        print("The response of OthersApi->wrap_eth_v0_generic_wrap_eth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->wrap_eth_v0_generic_wrap_eth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wrap_eth_request** | [**WrapEthRequest**](WrapEthRequest.md)|  | 

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

