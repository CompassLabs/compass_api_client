# compass.api_client.UniswapV3Api

All URIs are relative to *https://api.compasslabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_request_v0_uniswap_liquidity_provision_impermanent_loss_get_post**](UniswapV3Api.md#process_request_v0_uniswap_liquidity_provision_impermanent_loss_get_post) | **POST** /v0/uniswap/liquidity_provision/impermanent_loss/get | Calculate the impermanent loss of a liquidity position on Uniswap.
[**process_request_v0_uniswap_liquidity_provision_in_range_get_post**](UniswapV3Api.md#process_request_v0_uniswap_liquidity_provision_in_range_get_post) | **POST** /v0/uniswap/liquidity_provision/in_range/get | Check if a position is in active tick range
[**process_request_v0_uniswap_liquidity_provision_increase_post**](UniswapV3Api.md#process_request_v0_uniswap_liquidity_provision_increase_post) | **POST** /v0/uniswap/liquidity_provision/increase | Increase an LP position
[**process_request_v0_uniswap_liquidity_provision_mint_post**](UniswapV3Api.md#process_request_v0_uniswap_liquidity_provision_mint_post) | **POST** /v0/uniswap/liquidity_provision/mint | Open a new LP position
[**process_request_v0_uniswap_liquidity_provision_positions_get_post**](UniswapV3Api.md#process_request_v0_uniswap_liquidity_provision_positions_get_post) | **POST** /v0/uniswap/liquidity_provision/positions/get | Retrieve LP positions for a sender
[**process_request_v0_uniswap_liquidity_provision_withdraw_post**](UniswapV3Api.md#process_request_v0_uniswap_liquidity_provision_withdraw_post) | **POST** /v0/uniswap/liquidity_provision/withdraw | Withdraw an LP position
[**process_request_v0_uniswap_pool_price_get_post**](UniswapV3Api.md#process_request_v0_uniswap_pool_price_get_post) | **POST** /v0/uniswap/pool_price/get | Get the current price of a pool (how many token0 you can buy for 1 token1). This is only the instantaneous price; during any trade the price will change. Use the quote endpoint to get a more realistic idea of the ratios of the two assets you could trade.
[**process_request_v0_uniswap_quote_buy_exactly_get_post**](UniswapV3Api.md#process_request_v0_uniswap_quote_buy_exactly_get_post) | **POST** /v0/uniswap/quote/buy_exactly/get | Get the amount of tokens you would need to provide to the pool in order to purchase a fixed quantity of tokens. Also returns what the price would be afterward.
[**process_request_v0_uniswap_quote_sell_exactly_get_post**](UniswapV3Api.md#process_request_v0_uniswap_quote_sell_exactly_get_post) | **POST** /v0/uniswap/quote/sell_exactly/get | Get the amount of tokens you would get from the pool if you provided a fixed quantity of tokens. Also returns what the price would be afterward.
[**process_request_v0_uniswap_swap_buy_exactly_post**](UniswapV3Api.md#process_request_v0_uniswap_swap_buy_exactly_post) | **POST** /v0/uniswap/swap/buy_exactly | Trade the amount of a token it takes to end up with a specified quantity of the other token
[**process_request_v0_uniswap_swap_sell_exactly_post**](UniswapV3Api.md#process_request_v0_uniswap_swap_sell_exactly_post) | **POST** /v0/uniswap/swap/sell_exactly | Trade a specific amount of a token into another.


# **process_request_v0_uniswap_liquidity_provision_impermanent_loss_get_post**
> UniswapImpermanentLossResponse process_request_v0_uniswap_liquidity_provision_impermanent_loss_get_post(uniswap_impermanent_loss_call_data)

Calculate the impermanent loss of a liquidity position on Uniswap.

This endpoint allows users to calculate the impermanent loss associated with
        a specific Liquidity Provider (LP) position on the Uniswap platform. By providing
        the token ID of the LP position and the transaction hash associated with the minting
        transaction, users can determine the impermanent loss incurred due to changes in the
        token prices and liquidity pool conditions.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_impermanent_loss_call_data import UniswapImpermanentLossCallData
from compass.api_client.models.uniswap_impermanent_loss_response import UniswapImpermanentLossResponse
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
    api_instance = compass.api_client.UniswapV3Api(api_client)
    uniswap_impermanent_loss_call_data = compass.api_client.UniswapImpermanentLossCallData() # UniswapImpermanentLossCallData | 

    try:
        # Calculate the impermanent loss of a liquidity position on Uniswap.
        api_response = api_instance.process_request_v0_uniswap_liquidity_provision_impermanent_loss_get_post(uniswap_impermanent_loss_call_data)
        print("The response of UniswapV3Api->process_request_v0_uniswap_liquidity_provision_impermanent_loss_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->process_request_v0_uniswap_liquidity_provision_impermanent_loss_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_impermanent_loss_call_data** | [**UniswapImpermanentLossCallData**](UniswapImpermanentLossCallData.md)|  | 

### Return type

[**UniswapImpermanentLossResponse**](UniswapImpermanentLossResponse.md)

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

# **process_request_v0_uniswap_liquidity_provision_in_range_get_post**
> UniswapCheckInRangeResponse process_request_v0_uniswap_liquidity_provision_in_range_get_post(uniswap_check_in_range_call_data)

Check if a position is in active tick range

This endpoint allows users to check whether a specific Liquidity Provider (LP)
        position is within the active tick range on the Uniswap platform. By providing
        the token ID associated with the position, users can verify if the position is
        currently within the tick range where trading occurs. This information is essential
        for users to monitor the status of their LP positions and ensure that they are
        actively participating in the trading activities within the liquidity pool and
        earning trading fees.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_check_in_range_call_data import UniswapCheckInRangeCallData
from compass.api_client.models.uniswap_check_in_range_response import UniswapCheckInRangeResponse
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
    api_instance = compass.api_client.UniswapV3Api(api_client)
    uniswap_check_in_range_call_data = compass.api_client.UniswapCheckInRangeCallData() # UniswapCheckInRangeCallData | 

    try:
        # Check if a position is in active tick range
        api_response = api_instance.process_request_v0_uniswap_liquidity_provision_in_range_get_post(uniswap_check_in_range_call_data)
        print("The response of UniswapV3Api->process_request_v0_uniswap_liquidity_provision_in_range_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->process_request_v0_uniswap_liquidity_provision_in_range_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_check_in_range_call_data** | [**UniswapCheckInRangeCallData**](UniswapCheckInRangeCallData.md)|  | 

### Return type

[**UniswapCheckInRangeResponse**](UniswapCheckInRangeResponse.md)

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

# **process_request_v0_uniswap_liquidity_provision_increase_post**
> UnsignedTransaction process_request_v0_uniswap_liquidity_provision_increase_post(base_transaction_request_uniswap_increase_liquidity_provision_call_data)

Increase an LP position

This endpoint allows users to increase their existing Liquidity Provider (LP)
        positions on the Uniswap platform. By providing the necessary parameters, users
        can add more liquidity to their current positions, thereby increasing their stake
        in the liquidity pool. This operation is beneficial for users who wish to enhance
        their potential earnings from trading fees within the pool. The endpoint requires
        details such as the token pair, additional amount to be added, and any other
        parameters necessary for the liquidity increase process.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.base_transaction_request_uniswap_increase_liquidity_provision_call_data import BaseTransactionRequestUniswapIncreaseLiquidityProvisionCallData
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
    api_instance = compass.api_client.UniswapV3Api(api_client)
    base_transaction_request_uniswap_increase_liquidity_provision_call_data = compass.api_client.BaseTransactionRequestUniswapIncreaseLiquidityProvisionCallData() # BaseTransactionRequestUniswapIncreaseLiquidityProvisionCallData | 

    try:
        # Increase an LP position
        api_response = api_instance.process_request_v0_uniswap_liquidity_provision_increase_post(base_transaction_request_uniswap_increase_liquidity_provision_call_data)
        print("The response of UniswapV3Api->process_request_v0_uniswap_liquidity_provision_increase_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->process_request_v0_uniswap_liquidity_provision_increase_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_uniswap_increase_liquidity_provision_call_data** | [**BaseTransactionRequestUniswapIncreaseLiquidityProvisionCallData**](BaseTransactionRequestUniswapIncreaseLiquidityProvisionCallData.md)|  | 

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

# **process_request_v0_uniswap_liquidity_provision_mint_post**
> UnsignedTransaction process_request_v0_uniswap_liquidity_provision_mint_post(base_transaction_request_uniswap_mint_liquidity_provision_call_data)

Open a new LP position

This endpoint allows users to open a new Liquidity Provider (LP) position
        on the Uniswap platform. By providing the necessary parameters, users can
        initiate a minting process to create a new LP token, which represents their
        stake in a specific liquidity pool. This operation is essential for users
        looking to participate in liquidity provision, enabling them to earn fees
        from trades that occur within the pool. The endpoint requires details such
        as the token pair, amount, and any additional parameters needed for the
        minting process.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.base_transaction_request_uniswap_mint_liquidity_provision_call_data import BaseTransactionRequestUniswapMintLiquidityProvisionCallData
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
    api_instance = compass.api_client.UniswapV3Api(api_client)
    base_transaction_request_uniswap_mint_liquidity_provision_call_data = compass.api_client.BaseTransactionRequestUniswapMintLiquidityProvisionCallData() # BaseTransactionRequestUniswapMintLiquidityProvisionCallData | 

    try:
        # Open a new LP position
        api_response = api_instance.process_request_v0_uniswap_liquidity_provision_mint_post(base_transaction_request_uniswap_mint_liquidity_provision_call_data)
        print("The response of UniswapV3Api->process_request_v0_uniswap_liquidity_provision_mint_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->process_request_v0_uniswap_liquidity_provision_mint_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_uniswap_mint_liquidity_provision_call_data** | [**BaseTransactionRequestUniswapMintLiquidityProvisionCallData**](BaseTransactionRequestUniswapMintLiquidityProvisionCallData.md)|  | 

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

# **process_request_v0_uniswap_liquidity_provision_positions_get_post**
> UniswapLPPositionsInfo process_request_v0_uniswap_liquidity_provision_positions_get_post(uniswap_get_liquidity_provision_positions)

Retrieve LP positions for a sender

This endpoint retrieves the number of Liquidity Provider (LP) positions
        associated with a specific sender address on the Uniswap platform.
        Users can query this endpoint to obtain detailed information about their
        LP positions, including the total number of positions and relevant metadata.
        This information is crucial for users to manage and analyze their liquidity
        provision activities effectively.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_get_liquidity_provision_positions import UniswapGetLiquidityProvisionPositions
from compass.api_client.models.uniswap_lp_positions_info import UniswapLPPositionsInfo
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
    api_instance = compass.api_client.UniswapV3Api(api_client)
    uniswap_get_liquidity_provision_positions = compass.api_client.UniswapGetLiquidityProvisionPositions() # UniswapGetLiquidityProvisionPositions | 

    try:
        # Retrieve LP positions for a sender
        api_response = api_instance.process_request_v0_uniswap_liquidity_provision_positions_get_post(uniswap_get_liquidity_provision_positions)
        print("The response of UniswapV3Api->process_request_v0_uniswap_liquidity_provision_positions_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->process_request_v0_uniswap_liquidity_provision_positions_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_get_liquidity_provision_positions** | [**UniswapGetLiquidityProvisionPositions**](UniswapGetLiquidityProvisionPositions.md)|  | 

### Return type

[**UniswapLPPositionsInfo**](UniswapLPPositionsInfo.md)

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

# **process_request_v0_uniswap_liquidity_provision_withdraw_post**
> UnsignedTransaction process_request_v0_uniswap_liquidity_provision_withdraw_post(base_transaction_request_uniswap_withdraw_liquidity_provision_call_data)

Withdraw an LP position

This endpoint allows users to withdraw their Liquidity Provider (LP) positions
        from the Uniswap platform. By specifying the necessary parameters, users can
        initiate the withdrawal process to remove their stake from a specific liquidity
        pool. This operation is crucial for users who wish to reclaim their assets or
        reallocate their liquidity to different pools or investments. The endpoint requires
        details such as the token pair, the amount to be withdrawn, and any additional
        parameters needed for the withdrawal process. Users should ensure they meet any
        protocol requirements or conditions before initiating a withdrawal to avoid
        potential issues or penalties.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.base_transaction_request_uniswap_withdraw_liquidity_provision_call_data import BaseTransactionRequestUniswapWithdrawLiquidityProvisionCallData
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
    api_instance = compass.api_client.UniswapV3Api(api_client)
    base_transaction_request_uniswap_withdraw_liquidity_provision_call_data = compass.api_client.BaseTransactionRequestUniswapWithdrawLiquidityProvisionCallData() # BaseTransactionRequestUniswapWithdrawLiquidityProvisionCallData | 

    try:
        # Withdraw an LP position
        api_response = api_instance.process_request_v0_uniswap_liquidity_provision_withdraw_post(base_transaction_request_uniswap_withdraw_liquidity_provision_call_data)
        print("The response of UniswapV3Api->process_request_v0_uniswap_liquidity_provision_withdraw_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->process_request_v0_uniswap_liquidity_provision_withdraw_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_uniswap_withdraw_liquidity_provision_call_data** | [**BaseTransactionRequestUniswapWithdrawLiquidityProvisionCallData**](BaseTransactionRequestUniswapWithdrawLiquidityProvisionCallData.md)|  | 

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

# **process_request_v0_uniswap_pool_price_get_post**
> UniswapPoolPrice process_request_v0_uniswap_pool_price_get_post(uniswap_get_pool_price)

Get the current price of a pool (how many token0 you can buy for 1 token1). This is only the instantaneous price; during any trade the price will change. Use the quote endpoint to get a more realistic idea of the ratios of the two assets you could trade.

This endpoint retrieves the current price of a Uniswap pool, expressed as the amount of token0
    you can buy for 1 token1. It provides the instantaneous price, which may change during any trade.
    For a more realistic idea of the trade ratios, consider using the quote endpoint. The request
    requires specifying the input and output tokens, as well as the fee tier of the pool.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_get_pool_price import UniswapGetPoolPrice
from compass.api_client.models.uniswap_pool_price import UniswapPoolPrice
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
    api_instance = compass.api_client.UniswapV3Api(api_client)
    uniswap_get_pool_price = compass.api_client.UniswapGetPoolPrice() # UniswapGetPoolPrice | 

    try:
        # Get the current price of a pool (how many token0 you can buy for 1 token1). This is only the instantaneous price; during any trade the price will change. Use the quote endpoint to get a more realistic idea of the ratios of the two assets you could trade.
        api_response = api_instance.process_request_v0_uniswap_pool_price_get_post(uniswap_get_pool_price)
        print("The response of UniswapV3Api->process_request_v0_uniswap_pool_price_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->process_request_v0_uniswap_pool_price_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_get_pool_price** | [**UniswapGetPoolPrice**](UniswapGetPoolPrice.md)|  | 

### Return type

[**UniswapPoolPrice**](UniswapPoolPrice.md)

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

# **process_request_v0_uniswap_quote_buy_exactly_get_post**
> UniswapBuyQuoteInfo process_request_v0_uniswap_quote_buy_exactly_get_post(uniswap_get_buy_quote)

Get the amount of tokens you would need to provide to the pool in order to purchase a fixed quantity of tokens. Also returns what the price would be afterward.

This endpoint calculates the amount of input tokens required to purchase a specified amount of output tokens
        from a Uniswap pool. It also provides the resulting price after the transaction. The calculation takes into
        account the current pool state and the specified fee tier.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_buy_quote_info import UniswapBuyQuoteInfo
from compass.api_client.models.uniswap_get_buy_quote import UniswapGetBuyQuote
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
    api_instance = compass.api_client.UniswapV3Api(api_client)
    uniswap_get_buy_quote = compass.api_client.UniswapGetBuyQuote() # UniswapGetBuyQuote | 

    try:
        # Get the amount of tokens you would need to provide to the pool in order to purchase a fixed quantity of tokens. Also returns what the price would be afterward.
        api_response = api_instance.process_request_v0_uniswap_quote_buy_exactly_get_post(uniswap_get_buy_quote)
        print("The response of UniswapV3Api->process_request_v0_uniswap_quote_buy_exactly_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->process_request_v0_uniswap_quote_buy_exactly_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_get_buy_quote** | [**UniswapGetBuyQuote**](UniswapGetBuyQuote.md)|  | 

### Return type

[**UniswapBuyQuoteInfo**](UniswapBuyQuoteInfo.md)

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

# **process_request_v0_uniswap_quote_sell_exactly_get_post**
> UniswapSellQuoteInfo process_request_v0_uniswap_quote_sell_exactly_get_post(uniswap_get_sell_quote)

Get the amount of tokens you would get from the pool if you provided a fixed quantity of tokens. Also returns what the price would be afterward.

This endpoint calculates the amount of output tokens you would receive from a Uniswap pool when providing a
        specified amount of input tokens. It also provides the resulting price after the transaction. The calculation
        considers the current pool state and the specified fee tier.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_get_sell_quote import UniswapGetSellQuote
from compass.api_client.models.uniswap_sell_quote_info import UniswapSellQuoteInfo
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
    api_instance = compass.api_client.UniswapV3Api(api_client)
    uniswap_get_sell_quote = compass.api_client.UniswapGetSellQuote() # UniswapGetSellQuote | 

    try:
        # Get the amount of tokens you would get from the pool if you provided a fixed quantity of tokens. Also returns what the price would be afterward.
        api_response = api_instance.process_request_v0_uniswap_quote_sell_exactly_get_post(uniswap_get_sell_quote)
        print("The response of UniswapV3Api->process_request_v0_uniswap_quote_sell_exactly_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->process_request_v0_uniswap_quote_sell_exactly_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_get_sell_quote** | [**UniswapGetSellQuote**](UniswapGetSellQuote.md)|  | 

### Return type

[**UniswapSellQuoteInfo**](UniswapSellQuoteInfo.md)

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

# **process_request_v0_uniswap_swap_buy_exactly_post**
> UnsignedTransaction process_request_v0_uniswap_swap_buy_exactly_post(base_transaction_request_uniswap_buy_exactly_call_data)

Trade the amount of a token it takes to end up with a specified quantity of the other token

This endpoint allows users to trade a variable amount of one token
        to receive an exact amount of another token using the Uniswap protocol.
        The transaction is executed on the specified blockchain network, and
        the user must provide the necessary transaction details, including the
        token to buy, the token to pay with, and the exact amount to receive.
        If the token being paid with is WETH and needs to be wrapped, the
        appropriate amount will be wrapped automatically.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.base_transaction_request_uniswap_buy_exactly_call_data import BaseTransactionRequestUniswapBuyExactlyCallData
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
    api_instance = compass.api_client.UniswapV3Api(api_client)
    base_transaction_request_uniswap_buy_exactly_call_data = compass.api_client.BaseTransactionRequestUniswapBuyExactlyCallData() # BaseTransactionRequestUniswapBuyExactlyCallData | 

    try:
        # Trade the amount of a token it takes to end up with a specified quantity of the other token
        api_response = api_instance.process_request_v0_uniswap_swap_buy_exactly_post(base_transaction_request_uniswap_buy_exactly_call_data)
        print("The response of UniswapV3Api->process_request_v0_uniswap_swap_buy_exactly_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->process_request_v0_uniswap_swap_buy_exactly_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_uniswap_buy_exactly_call_data** | [**BaseTransactionRequestUniswapBuyExactlyCallData**](BaseTransactionRequestUniswapBuyExactlyCallData.md)|  | 

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

# **process_request_v0_uniswap_swap_sell_exactly_post**
> UnsignedTransaction process_request_v0_uniswap_swap_sell_exactly_post(base_transaction_request_uniswap_sell_exactly_call_data)

Trade a specific amount of a token into another.

This endpoint allows users to trade a specific amount of one token
        into another token using the Uniswap protocol. The transaction is
        executed on the specified blockchain network, and the user must
        provide the necessary transaction details, including the token to
        sell, the token to receive, and the amount to sell. If the token
        being sold is WETH and needs to be wrapped, the appropriate amount
        will be wrapped automatically.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.base_transaction_request_uniswap_sell_exactly_call_data import BaseTransactionRequestUniswapSellExactlyCallData
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
    api_instance = compass.api_client.UniswapV3Api(api_client)
    base_transaction_request_uniswap_sell_exactly_call_data = compass.api_client.BaseTransactionRequestUniswapSellExactlyCallData() # BaseTransactionRequestUniswapSellExactlyCallData | 

    try:
        # Trade a specific amount of a token into another.
        api_response = api_instance.process_request_v0_uniswap_swap_sell_exactly_post(base_transaction_request_uniswap_sell_exactly_call_data)
        print("The response of UniswapV3Api->process_request_v0_uniswap_swap_sell_exactly_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->process_request_v0_uniswap_swap_sell_exactly_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_uniswap_sell_exactly_call_data** | [**BaseTransactionRequestUniswapSellExactlyCallData**](BaseTransactionRequestUniswapSellExactlyCallData.md)|  | 

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

