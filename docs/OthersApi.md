# compass.api_client.OthersApi

All URIs are relative to *https://api.compasslabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tokens_v0_generic_supported_tokens_get_post**](OthersApi.md#get_tokens_v0_generic_supported_tokens_get_post) | **POST** /v0/generic/supported_tokens/get | Get supported token
[**process_request_v0_generic_allowance_get_post**](OthersApi.md#process_request_v0_generic_allowance_get_post) | **POST** /v0/generic/allowance/get | Show the allowance of a user on a protocol
[**process_request_v0_generic_allowance_set_any_post**](OthersApi.md#process_request_v0_generic_allowance_set_any_post) | **POST** /v0/generic/allowance/set_any | Sets allowance for any arbitrary ERC20 token address.
[**process_request_v0_generic_allowance_set_post**](OthersApi.md#process_request_v0_generic_allowance_set_post) | **POST** /v0/generic/allowance/set | Change the allowance of a user on a protocol
[**process_request_v0_generic_balance_get_post**](OthersApi.md#process_request_v0_generic_balance_get_post) | **POST** /v0/generic/balance/get | Get an address balance of a token
[**process_request_v0_generic_ens_get_post**](OthersApi.md#process_request_v0_generic_ens_get_post) | **POST** /v0/generic/ens/get | Get the wallet address and registrant of an ENS name
[**process_request_v0_generic_portfolio_get_post**](OthersApi.md#process_request_v0_generic_portfolio_get_post) | **POST** /v0/generic/portfolio/get | Get the portfolio details for a wallet addressincluding balances and values of all tokens.
[**process_request_v0_generic_unwrap_weth_post**](OthersApi.md#process_request_v0_generic_unwrap_weth_post) | **POST** /v0/generic/unwrap_weth | Change WETH into raw ETH
[**process_request_v0_generic_visualize_portfolio_get_post**](OthersApi.md#process_request_v0_generic_visualize_portfolio_get_post) | **POST** /v0/generic/visualize_portfolio/get | Visualize the token portfolio of a wallet address as a pie chart
[**process_request_v0_generic_wrap_eth_post**](OthersApi.md#process_request_v0_generic_wrap_eth_post) | **POST** /v0/generic/wrap_eth | Change raw ETH into WETH


# **get_tokens_v0_generic_supported_tokens_get_post**
> TokenInfo get_tokens_v0_generic_supported_tokens_get_post(get_supported_tokens)

Get supported token

Get the list of supported tokens on a chain by the Compass API.

### Example


```python
import compass.api_client
from compass.api_client.models.get_supported_tokens import GetSupportedTokens
from compass.api_client.models.token_info import TokenInfo
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
    api_instance = compass.api_client.OthersApi(api_client)
    get_supported_tokens = compass.api_client.GetSupportedTokens() # GetSupportedTokens | 

    try:
        # Get supported token
        api_response = api_instance.get_tokens_v0_generic_supported_tokens_get_post(get_supported_tokens)
        print("The response of OthersApi->get_tokens_v0_generic_supported_tokens_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->get_tokens_v0_generic_supported_tokens_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_supported_tokens** | [**GetSupportedTokens**](GetSupportedTokens.md)|  | 

### Return type

[**TokenInfo**](TokenInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_v0_generic_allowance_get_post**
> AllowanceInfo process_request_v0_generic_allowance_get_post(get_erc20_allowance)

Show the allowance of a user on a protocol

In decentralized finance (DeFi) protocols such as Uniswap or AAVE,
        users must set a token allowance to authorize the protocol to spend
        a specified amount of their tokens on their behalf. This is a crucial
        step before engaging in any transactions or operations within these
        protocols, ensuring that the protocol has the necessary permissions
        to manage the user's tokens securely and efficiently.

### Example


```python
import compass.api_client
from compass.api_client.models.allowance_info import AllowanceInfo
from compass.api_client.models.get_erc20_allowance import GetErc20Allowance
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
    api_instance = compass.api_client.OthersApi(api_client)
    get_erc20_allowance = compass.api_client.GetErc20Allowance() # GetErc20Allowance | 

    try:
        # Show the allowance of a user on a protocol
        api_response = api_instance.process_request_v0_generic_allowance_get_post(get_erc20_allowance)
        print("The response of OthersApi->process_request_v0_generic_allowance_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->process_request_v0_generic_allowance_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_erc20_allowance** | [**GetErc20Allowance**](GetErc20Allowance.md)|  | 

### Return type

[**AllowanceInfo**](AllowanceInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_v0_generic_allowance_set_any_post**
> UnsignedTransaction process_request_v0_generic_allowance_set_any_post(base_transaction_request_increase_erc20_allowance_any_call_data)

Sets allowance for any arbitrary ERC20 token address.

This endpoint allows users to set an allowance for any arbitrary ERC20
        token address. In decentralized finance (DeFi), setting an allowance
        is a critical operation that permits a protocol to spend a specified
        amount of tokens on behalf of the user. This functionality is essential
        for enabling secure and efficient token management, facilitating smooth
        transactions and operations within the DeFi ecosystem. By using this
        endpoint, users can specify the token address and the amount they wish
        to authorize, ensuring precise control over their token allowances.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_increase_erc20_allowance_any_call_data import BaseTransactionRequestIncreaseErc20AllowanceAnyCallData
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
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
    api_instance = compass.api_client.OthersApi(api_client)
    base_transaction_request_increase_erc20_allowance_any_call_data = compass.api_client.BaseTransactionRequestIncreaseErc20AllowanceAnyCallData() # BaseTransactionRequestIncreaseErc20AllowanceAnyCallData | 

    try:
        # Sets allowance for any arbitrary ERC20 token address.
        api_response = api_instance.process_request_v0_generic_allowance_set_any_post(base_transaction_request_increase_erc20_allowance_any_call_data)
        print("The response of OthersApi->process_request_v0_generic_allowance_set_any_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->process_request_v0_generic_allowance_set_any_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_increase_erc20_allowance_any_call_data** | [**BaseTransactionRequestIncreaseErc20AllowanceAnyCallData**](BaseTransactionRequestIncreaseErc20AllowanceAnyCallData.md)|  | 

### Return type

[**UnsignedTransaction**](UnsignedTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_v0_generic_allowance_set_post**
> UnsignedTransaction process_request_v0_generic_allowance_set_post(base_transaction_request_increase_erc20_allowance_call_data)

Change the allowance of a user on a protocol

This endpoint allows users to modify the token allowance for a specific
        protocol. In decentralized finance (DeFi), setting an allowance is a
        necessary step to authorize a protocol to spend a specified amount of
        tokens on behalf of the user. This operation is crucial for ensuring
        that the protocol can manage the user's tokens securely and efficiently,
        enabling seamless transactions and operations within the DeFi ecosystem.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_increase_erc20_allowance_call_data import BaseTransactionRequestIncreaseErc20AllowanceCallData
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
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
    api_instance = compass.api_client.OthersApi(api_client)
    base_transaction_request_increase_erc20_allowance_call_data = compass.api_client.BaseTransactionRequestIncreaseErc20AllowanceCallData() # BaseTransactionRequestIncreaseErc20AllowanceCallData | 

    try:
        # Change the allowance of a user on a protocol
        api_response = api_instance.process_request_v0_generic_allowance_set_post(base_transaction_request_increase_erc20_allowance_call_data)
        print("The response of OthersApi->process_request_v0_generic_allowance_set_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->process_request_v0_generic_allowance_set_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_increase_erc20_allowance_call_data** | [**BaseTransactionRequestIncreaseErc20AllowanceCallData**](BaseTransactionRequestIncreaseErc20AllowanceCallData.md)|  | 

### Return type

[**UnsignedTransaction**](UnsignedTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_v0_generic_balance_get_post**
> BalanceInfo process_request_v0_generic_balance_get_post(get_erc20_balance)

Get an address balance of a token

This endpoint allows users to retrieve the balance of a specified ERC20 token
        for any given account address on the blockchain. It requires the token symbol
        and the user's account address as input parameters. The response includes the
        balance amount, the number of decimals the token uses, the token symbol, and
        the token's contract address. This functionality is essential for applications
        that need to display or manage token balances for users.

### Example


```python
import compass.api_client
from compass.api_client.models.balance_info import BalanceInfo
from compass.api_client.models.get_erc20_balance import GetErc20Balance
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
    api_instance = compass.api_client.OthersApi(api_client)
    get_erc20_balance = compass.api_client.GetErc20Balance() # GetErc20Balance | 

    try:
        # Get an address balance of a token
        api_response = api_instance.process_request_v0_generic_balance_get_post(get_erc20_balance)
        print("The response of OthersApi->process_request_v0_generic_balance_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->process_request_v0_generic_balance_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_erc20_balance** | [**GetErc20Balance**](GetErc20Balance.md)|  | 

### Return type

[**BalanceInfo**](BalanceInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_v0_generic_ens_get_post**
> EnsNameInfo process_request_v0_generic_ens_get_post(request_ens_details)

Get the wallet address and registrant of an ENS name

An ENS name is a string ending in `.eth`. E.g. `vitalik.eth`. This endpoint can be used to query the actual ethereum wallet address behind the ENS name.

### Example


```python
import compass.api_client
from compass.api_client.models.ens_name_info import EnsNameInfo
from compass.api_client.models.request_ens_details import RequestEnsDetails
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
    api_instance = compass.api_client.OthersApi(api_client)
    request_ens_details = compass.api_client.RequestEnsDetails() # RequestEnsDetails | 

    try:
        # Get the wallet address and registrant of an ENS name
        api_response = api_instance.process_request_v0_generic_ens_get_post(request_ens_details)
        print("The response of OthersApi->process_request_v0_generic_ens_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->process_request_v0_generic_ens_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_ens_details** | [**RequestEnsDetails**](RequestEnsDetails.md)|  | 

### Return type

[**EnsNameInfo**](EnsNameInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_v0_generic_portfolio_get_post**
> Portfolio process_request_v0_generic_portfolio_get_post(request_user_address)

Get the portfolio details for a wallet addressincluding balances and values of all tokens.

Fetch the detailed portfolio of a specific wallet address on a given blockchain. This includes the total value of the portfolio in USD and a breakdown of token balances, including their respective values and quantities.

### Example


```python
import compass.api_client
from compass.api_client.models.portfolio import Portfolio
from compass.api_client.models.request_user_address import RequestUserAddress
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
    api_instance = compass.api_client.OthersApi(api_client)
    request_user_address = compass.api_client.RequestUserAddress() # RequestUserAddress | 

    try:
        # Get the portfolio details for a wallet addressincluding balances and values of all tokens.
        api_response = api_instance.process_request_v0_generic_portfolio_get_post(request_user_address)
        print("The response of OthersApi->process_request_v0_generic_portfolio_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->process_request_v0_generic_portfolio_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_user_address** | [**RequestUserAddress**](RequestUserAddress.md)|  | 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_v0_generic_unwrap_weth_post**
> UnsignedTransaction process_request_v0_generic_unwrap_weth_post(base_transaction_request_unwrap_weth_request_call_data)

Change WETH into raw ETH

Unwrapping ETH transforms the ERC-20 token into the raw form used for paying gas fees and other basic functions.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_unwrap_weth_request_call_data import BaseTransactionRequestUnwrapWethRequestCallData
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
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
    api_instance = compass.api_client.OthersApi(api_client)
    base_transaction_request_unwrap_weth_request_call_data = compass.api_client.BaseTransactionRequestUnwrapWethRequestCallData() # BaseTransactionRequestUnwrapWethRequestCallData | 

    try:
        # Change WETH into raw ETH
        api_response = api_instance.process_request_v0_generic_unwrap_weth_post(base_transaction_request_unwrap_weth_request_call_data)
        print("The response of OthersApi->process_request_v0_generic_unwrap_weth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->process_request_v0_generic_unwrap_weth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_unwrap_weth_request_call_data** | [**BaseTransactionRequestUnwrapWethRequestCallData**](BaseTransactionRequestUnwrapWethRequestCallData.md)|  | 

### Return type

[**UnsignedTransaction**](UnsignedTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_v0_generic_visualize_portfolio_get_post**
> Image process_request_v0_generic_visualize_portfolio_get_post(request_user_address)

Visualize the token portfolio of a wallet address as a pie chart

Generate a visual representation of the token portfolio for a wallet address. The response is an SVG image of a pie chart depicting the relative distribution of tokens held, colored and labeled with token symbols, percentages and token values in USD.

### Example


```python
import compass.api_client
from compass.api_client.models.image import Image
from compass.api_client.models.request_user_address import RequestUserAddress
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
    api_instance = compass.api_client.OthersApi(api_client)
    request_user_address = compass.api_client.RequestUserAddress() # RequestUserAddress | 

    try:
        # Visualize the token portfolio of a wallet address as a pie chart
        api_response = api_instance.process_request_v0_generic_visualize_portfolio_get_post(request_user_address)
        print("The response of OthersApi->process_request_v0_generic_visualize_portfolio_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->process_request_v0_generic_visualize_portfolio_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_user_address** | [**RequestUserAddress**](RequestUserAddress.md)|  | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_v0_generic_wrap_eth_post**
> UnsignedTransaction process_request_v0_generic_wrap_eth_post(base_transaction_request_wrap_eth_request_call_data)

Change raw ETH into WETH

Wrapping ETH creates an ERC-20 compliant form of ETH that is typically needed for it to be traded on DeFi protocols.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_wrap_eth_request_call_data import BaseTransactionRequestWrapEthRequestCallData
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
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
    api_instance = compass.api_client.OthersApi(api_client)
    base_transaction_request_wrap_eth_request_call_data = compass.api_client.BaseTransactionRequestWrapEthRequestCallData() # BaseTransactionRequestWrapEthRequestCallData | 

    try:
        # Change raw ETH into WETH
        api_response = api_instance.process_request_v0_generic_wrap_eth_post(base_transaction_request_wrap_eth_request_call_data)
        print("The response of OthersApi->process_request_v0_generic_wrap_eth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OthersApi->process_request_v0_generic_wrap_eth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_wrap_eth_request_call_data** | [**BaseTransactionRequestWrapEthRequestCallData**](BaseTransactionRequestWrapEthRequestCallData.md)|  | 

### Return type

[**UnsignedTransaction**](UnsignedTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

