# compass.api_client.OthersApi

All URIs are relative to *https://api.compasslabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generic_allowance**](OthersApi.md#generic_allowance) | **POST** /v0/generic/allowance/get | Get allowance - Protocol
[**generic_allowance_set**](OthersApi.md#generic_allowance_set) | **POST** /v0/generic/allowance/set | Set Allowance - Protocol
[**generic_allowance_set_any**](OthersApi.md#generic_allowance_set_any) | **POST** /v0/generic/allowance/set_any | Set Allowance - Token
[**generic_balance**](OthersApi.md#generic_balance) | **POST** /v0/generic/balance/get | User token balance
[**generic_ens**](OthersApi.md#generic_ens) | **POST** /v0/generic/ens/get | Resolve ENS
[**generic_portfolio**](OthersApi.md#generic_portfolio) | **POST** /v0/generic/portfolio/get | List user portfolio
[**generic_price_usd**](OthersApi.md#generic_price_usd) | **POST** /v0/generic/price/usd/get | Token price
[**generic_supported_tokens**](OthersApi.md#generic_supported_tokens) | **POST** /v0/generic/supported_tokens/get | List supported tokens
[**generic_transfer_erc20**](OthersApi.md#generic_transfer_erc20) | **POST** /v0/generic/transfer/erc20 | Transfer Token
[**generic_transfer_native_token**](OthersApi.md#generic_transfer_native_token) | **POST** /v0/generic/transfer/native_token | Transfer ETH
[**generic_unwrap_weth**](OthersApi.md#generic_unwrap_weth) | **POST** /v0/generic/unwrap_weth | Unwrap WETH
[**generic_visualize_portfolio**](OthersApi.md#generic_visualize_portfolio) | **POST** /v0/generic/visualize_portfolio/get | Visualize user portfolio
[**generic_wrap_eth**](OthersApi.md#generic_wrap_eth) | **POST** /v0/generic/wrap_eth | Wrap ETH


# **generic_allowance**
> AllowanceInfoResponse generic_allowance(get_erc20_allowance_request)

Get allowance - Protocol

In decentralized finance (DeFi) protocols such as Uniswap or AAVE, users must set
a token allowance to authorize the protocol to spend a specified amount of their
tokens on their behalf.

This is a crucial step before engaging in any transactions or operations within
these protocols, ensuring that the protocol has the necessary permissions to manage
the user's tokens securely and efficiently.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.allowance_info_response import AllowanceInfoResponse
from compass.api_client.models.get_erc20_allowance_request import GetErc20AllowanceRequest
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
    api_instance = compass.api_client.OthersApi(api_client)
    get_erc20_allowance_request = compass.api_client.GetErc20AllowanceRequest() # GetErc20AllowanceRequest | 

    try:
        # Get allowance - Protocol
        api_response = api_instance.generic_allowance(get_erc20_allowance_request)
        print("The response of OthersApi->generic_allowance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->generic_allowance: %s\n" % e)
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

# **generic_allowance_set**
> UnsignedTransaction generic_allowance_set(increase_allowance_request)

Set Allowance - Protocol

This endpoint allows users to modify the token allowance for a specific protocol.

In decentralized finance (DeFi), setting an allowance is a necessary step to
authorize a protocol to spend a specified amount of tokens on behalf of the user.
This operation is crucial for ensuring that the protocol can manage the user's
tokens securely and efficiently, enabling seamless transactions and operations
within the DeFi ecosystem.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.increase_allowance_request import IncreaseAllowanceRequest
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
    api_instance = compass.api_client.OthersApi(api_client)
    increase_allowance_request = compass.api_client.IncreaseAllowanceRequest() # IncreaseAllowanceRequest | 

    try:
        # Set Allowance - Protocol
        api_response = api_instance.generic_allowance_set(increase_allowance_request)
        print("The response of OthersApi->generic_allowance_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->generic_allowance_set: %s\n" % e)
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

# **generic_allowance_set_any**
> UnsignedTransaction generic_allowance_set_any(increase_allowance_any_request)

Set Allowance - Token

This endpoint allows users to set an allowance for any arbitrary ERC20 token
address.

In decentralized finance (DeFi), setting an allowance is a critical operation that
permits a protocol to spend a specified amount of tokens on behalf of the user. This
functionality is essential for enabling secure and efficient token management,
facilitating smooth transactions and operations within the DeFi ecosystem. By using
this endpoint, users can specify the token address and the amount they wish to
authorize, ensuring precise control over their token allowances.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.increase_allowance_any_request import IncreaseAllowanceAnyRequest
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
    api_instance = compass.api_client.OthersApi(api_client)
    increase_allowance_any_request = compass.api_client.IncreaseAllowanceAnyRequest() # IncreaseAllowanceAnyRequest | 

    try:
        # Set Allowance - Token
        api_response = api_instance.generic_allowance_set_any(increase_allowance_any_request)
        print("The response of OthersApi->generic_allowance_set_any:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->generic_allowance_set_any: %s\n" % e)
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

# **generic_balance**
> BalanceInfoResponse generic_balance(get_erc20_balance_request)

User token balance

Returns the balance of a specific ERC20 token for a given user address.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.balance_info_response import BalanceInfoResponse
from compass.api_client.models.get_erc20_balance_request import GetErc20BalanceRequest
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
    api_instance = compass.api_client.OthersApi(api_client)
    get_erc20_balance_request = compass.api_client.GetErc20BalanceRequest() # GetErc20BalanceRequest | 

    try:
        # User token balance
        api_response = api_instance.generic_balance(get_erc20_balance_request)
        print("The response of OthersApi->generic_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->generic_balance: %s\n" % e)
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

# **generic_ens**
> EnsNameInfoResponse generic_ens(get_ens_details_request)

Resolve ENS

An ENS name is a string ending in `.eth`.

E.g. `vitalik.eth`. This endpoint can be used to
query the actual ethereum wallet address behind the ENS name.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.ens_name_info_response import EnsNameInfoResponse
from compass.api_client.models.get_ens_details_request import GetEnsDetailsRequest
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
    api_instance = compass.api_client.OthersApi(api_client)
    get_ens_details_request = compass.api_client.GetEnsDetailsRequest() # GetEnsDetailsRequest | 

    try:
        # Resolve ENS
        api_response = api_instance.generic_ens(get_ens_details_request)
        print("The response of OthersApi->generic_ens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->generic_ens: %s\n" % e)
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

# **generic_portfolio**
> Portfolio generic_portfolio(portfolio_request)

List user portfolio

Fetch the detailed portfolio of a specific wallet address on a given blockchain.

This includes the total value of the portfolio in USD and a breakdown of token
balances, including their respective values and quantities.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.portfolio import Portfolio
from compass.api_client.models.portfolio_request import PortfolioRequest
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
    api_instance = compass.api_client.OthersApi(api_client)
    portfolio_request = compass.api_client.PortfolioRequest() # PortfolioRequest | 

    try:
        # List user portfolio
        api_response = api_instance.generic_portfolio(portfolio_request)
        print("The response of OthersApi->generic_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->generic_portfolio: %s\n" % e)
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

# **generic_price_usd**
> PriceResponse generic_price_usd(price_request)

Token price

Retrieves the price of the specified token relative to USD using Chainlink's on-
chain price feeds..

Chainlink is a decentralized oracle that aggregates price data from off-chain
sources. This ensures the price is tamper-resistant but the price might be stale
with the update frequency of the oracle.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.price_request import PriceRequest
from compass.api_client.models.price_response import PriceResponse
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
    api_instance = compass.api_client.OthersApi(api_client)
    price_request = compass.api_client.PriceRequest() # PriceRequest | 

    try:
        # Token price
        api_response = api_instance.generic_price_usd(price_request)
        print("The response of OthersApi->generic_price_usd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->generic_price_usd: %s\n" % e)
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

# **generic_supported_tokens**
> TokenInfo generic_supported_tokens(tokens_request)

List supported tokens

Get the list of supported tokens on a chain by the Compass API.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.token_info import TokenInfo
from compass.api_client.models.tokens_request import TokensRequest
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
    api_instance = compass.api_client.OthersApi(api_client)
    tokens_request = compass.api_client.TokensRequest() # TokensRequest | 

    try:
        # List supported tokens
        api_response = api_instance.generic_supported_tokens(tokens_request)
        print("The response of OthersApi->generic_supported_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->generic_supported_tokens: %s\n" % e)
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

# **generic_transfer_erc20**
> UnsignedTransaction generic_transfer_erc20(transfer_erc20_request)

Transfer Token

Sends ERC20 tokens from the sender's address to the specified recipient.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.transfer_erc20_request import TransferERC20Request
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
    api_instance = compass.api_client.OthersApi(api_client)
    transfer_erc20_request = compass.api_client.TransferERC20Request() # TransferERC20Request | 

    try:
        # Transfer Token
        api_response = api_instance.generic_transfer_erc20(transfer_erc20_request)
        print("The response of OthersApi->generic_transfer_erc20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->generic_transfer_erc20: %s\n" % e)
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

# **generic_transfer_native_token**
> UnsignedTransaction generic_transfer_native_token(transfer_eth_request)

Transfer ETH

Sends native ETH from the sender's address to the specified recipient.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.transfer_eth_request import TransferEthRequest
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
    api_instance = compass.api_client.OthersApi(api_client)
    transfer_eth_request = compass.api_client.TransferEthRequest() # TransferEthRequest | 

    try:
        # Transfer ETH
        api_response = api_instance.generic_transfer_native_token(transfer_eth_request)
        print("The response of OthersApi->generic_transfer_native_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->generic_transfer_native_token: %s\n" % e)
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

# **generic_unwrap_weth**
> UnsignedTransaction generic_unwrap_weth(unwrap_weth_request)

Unwrap WETH

Unwrapping WETH converts the ERC-20 compliant form of ETH back to native ETH that
can be used for gas and other native purposes.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
from compass.api_client.models.unwrap_weth_request import UnwrapWethRequest
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
    api_instance = compass.api_client.OthersApi(api_client)
    unwrap_weth_request = compass.api_client.UnwrapWethRequest() # UnwrapWethRequest | 

    try:
        # Unwrap WETH
        api_response = api_instance.generic_unwrap_weth(unwrap_weth_request)
        print("The response of OthersApi->generic_unwrap_weth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->generic_unwrap_weth: %s\n" % e)
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

# **generic_visualize_portfolio**
> Image generic_visualize_portfolio(visualize_portfolio_request)

Visualize user portfolio

Generate a visual representation of the token portfolio for a wallet address.

The response is an SVG image of a pie chart depicting the relative distribution of
tokens held, colored and labeled with token symbols, percentages and token values in
USD.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.image import Image
from compass.api_client.models.visualize_portfolio_request import VisualizePortfolioRequest
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
    api_instance = compass.api_client.OthersApi(api_client)
    visualize_portfolio_request = compass.api_client.VisualizePortfolioRequest() # VisualizePortfolioRequest | 

    try:
        # Visualize user portfolio
        api_response = api_instance.generic_visualize_portfolio(visualize_portfolio_request)
        print("The response of OthersApi->generic_visualize_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->generic_visualize_portfolio: %s\n" % e)
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

# **generic_wrap_eth**
> UnsignedTransaction generic_wrap_eth(wrap_eth_request)

Wrap ETH

Wrapping ETH creates an ERC-20 compliant form of ETH that is typically needed for
it to be traded on DeFi protocols.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
from compass.api_client.models.wrap_eth_request import WrapEthRequest
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
    api_instance = compass.api_client.OthersApi(api_client)
    wrap_eth_request = compass.api_client.WrapEthRequest() # WrapEthRequest | 

    try:
        # Wrap ETH
        api_response = api_instance.generic_wrap_eth(wrap_eth_request)
        print("The response of OthersApi->generic_wrap_eth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->generic_wrap_eth: %s\n" % e)
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

