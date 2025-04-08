# compass.api_client.UniswapV3Api

All URIs are relative to *https://api.compasslabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uniswap_liquidity_provision_in_range**](UniswapV3Api.md#uniswap_liquidity_provision_in_range) | **POST** /v0/uniswap/liquidity_provision/in_range/get | Check if LP is active.
[**uniswap_liquidity_provision_increase**](UniswapV3Api.md#uniswap_liquidity_provision_increase) | **POST** /v0/uniswap/liquidity_provision/increase | Increase an LP position
[**uniswap_liquidity_provision_mint**](UniswapV3Api.md#uniswap_liquidity_provision_mint) | **POST** /v0/uniswap/liquidity_provision/mint | Open a new LP position
[**uniswap_liquidity_provision_positions**](UniswapV3Api.md#uniswap_liquidity_provision_positions) | **POST** /v0/uniswap/liquidity_provision/positions/get | List LP
[**uniswap_liquidity_provision_withdraw**](UniswapV3Api.md#uniswap_liquidity_provision_withdraw) | **POST** /v0/uniswap/liquidity_provision/withdraw | Withdraw an LP position
[**uniswap_pool_price**](UniswapV3Api.md#uniswap_pool_price) | **POST** /v0/uniswap/pool_price/get | Pool price
[**uniswap_quote_buy_exactly**](UniswapV3Api.md#uniswap_quote_buy_exactly) | **POST** /v0/uniswap/quote/buy_exactly/get | Get quote - to specified amount
[**uniswap_quote_sell_exactly**](UniswapV3Api.md#uniswap_quote_sell_exactly) | **POST** /v0/uniswap/quote/sell_exactly/get | Get quote - from specified amount
[**uniswap_swap_buy_exactly**](UniswapV3Api.md#uniswap_swap_buy_exactly) | **POST** /v0/uniswap/swap/buy_exactly | Buy exact amount
[**uniswap_swap_sell_exactly**](UniswapV3Api.md#uniswap_swap_sell_exactly) | **POST** /v0/uniswap/swap/sell_exactly | Sell exact amount


# **uniswap_liquidity_provision_in_range**
> UniswapCheckInRangeResponse uniswap_liquidity_provision_in_range(uniswap_check_in_range_request)

Check if LP is active.

This endpoint allows users to check whether a specific liquidity provider ()
position is within the active tick range on the uniswap platform.

by providing the token id associated with the position, users can verify if the
position is currently within the tick range where trading occurs. this information
is essential for users to monitor the status of their lp positions and ensure that
they are actively participating in the trading activities within the liquidity pool
and earning trading fees.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_check_in_range_request import UniswapCheckInRangeRequest
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
    uniswap_check_in_range_request = compass.api_client.UniswapCheckInRangeRequest() # UniswapCheckInRangeRequest | 

    try:
        # Check if LP is active.
        api_response = api_instance.uniswap_liquidity_provision_in_range(uniswap_check_in_range_request)
        print("The response of UniswapV3Api->uniswap_liquidity_provision_in_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->uniswap_liquidity_provision_in_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_check_in_range_request** | [**UniswapCheckInRangeRequest**](UniswapCheckInRangeRequest.md)|  | 

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

# **uniswap_liquidity_provision_increase**
> UnsignedTransaction uniswap_liquidity_provision_increase(uniswap_increase_liquidity_provision_request)

Increase an LP position

This endpoint allows users to increase their existing Liquidity Provider (LP)
positions on the Uniswap platform.

By providing the necessary parameters, users can add more liquidity to their current
positions, thereby increasing their stake in the liquidity pool. This operation is
beneficial for users who wish to enhance their potential earnings from trading fees
within the pool. The endpoint requires details such as the token pair, additional
amount to be added, and any other parameters necessary for the liquidity increase
process.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_increase_liquidity_provision_request import UniswapIncreaseLiquidityProvisionRequest
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
    uniswap_increase_liquidity_provision_request = compass.api_client.UniswapIncreaseLiquidityProvisionRequest() # UniswapIncreaseLiquidityProvisionRequest | 

    try:
        # Increase an LP position
        api_response = api_instance.uniswap_liquidity_provision_increase(uniswap_increase_liquidity_provision_request)
        print("The response of UniswapV3Api->uniswap_liquidity_provision_increase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->uniswap_liquidity_provision_increase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_increase_liquidity_provision_request** | [**UniswapIncreaseLiquidityProvisionRequest**](UniswapIncreaseLiquidityProvisionRequest.md)|  | 

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

# **uniswap_liquidity_provision_mint**
> UnsignedTransaction uniswap_liquidity_provision_mint(uniswap_mint_liquidity_provision_request)

Open a new LP position

This endpoint allows users to open a new Liquidity Provider (LP) position on the
Uniswap platform.

By providing the necessary parameters, users can initiate a minting process to
create a new LP token, which represents their stake in a specific liquidity pool.
This operation is essential for users looking to participate in liquidity provision,
enabling them to earn fees from trades that occur within the pool. The endpoint
requires details such as the token pair, amount, and any additional parameters
needed for the minting process.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_mint_liquidity_provision_request import UniswapMintLiquidityProvisionRequest
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
    uniswap_mint_liquidity_provision_request = compass.api_client.UniswapMintLiquidityProvisionRequest() # UniswapMintLiquidityProvisionRequest | 

    try:
        # Open a new LP position
        api_response = api_instance.uniswap_liquidity_provision_mint(uniswap_mint_liquidity_provision_request)
        print("The response of UniswapV3Api->uniswap_liquidity_provision_mint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->uniswap_liquidity_provision_mint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_mint_liquidity_provision_request** | [**UniswapMintLiquidityProvisionRequest**](UniswapMintLiquidityProvisionRequest.md)|  | 

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

# **uniswap_liquidity_provision_positions**
> UniswapLPPositionsInfoResponse uniswap_liquidity_provision_positions(uniswap_get_liquidity_provision_positions_request)

List LP

This endpoint retrieves the number of Liquidity Provider (LP) positions
associated with a specific sender address on the Uniswap platform.

Users can query this endpoint to obtain detailed information about their LP
positions, including the total number of positions and relevant metadata. This
information is crucial for users to manage and analyze their liquidity provision
activities effectively.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_get_liquidity_provision_positions_request import UniswapGetLiquidityProvisionPositionsRequest
from compass.api_client.models.uniswap_lp_positions_info_response import UniswapLPPositionsInfoResponse
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
    uniswap_get_liquidity_provision_positions_request = compass.api_client.UniswapGetLiquidityProvisionPositionsRequest() # UniswapGetLiquidityProvisionPositionsRequest | 

    try:
        # List LP
        api_response = api_instance.uniswap_liquidity_provision_positions(uniswap_get_liquidity_provision_positions_request)
        print("The response of UniswapV3Api->uniswap_liquidity_provision_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->uniswap_liquidity_provision_positions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_get_liquidity_provision_positions_request** | [**UniswapGetLiquidityProvisionPositionsRequest**](UniswapGetLiquidityProvisionPositionsRequest.md)|  | 

### Return type

[**UniswapLPPositionsInfoResponse**](UniswapLPPositionsInfoResponse.md)

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

# **uniswap_liquidity_provision_withdraw**
> UnsignedTransaction uniswap_liquidity_provision_withdraw(uniswap_withdraw_liquidity_provision_request)

Withdraw an LP position

This endpoint allows users to withdraw their Liquidity Provider (LP) positions
from the Uniswap platform.

By specifying the necessary parameters, users can initiate the withdrawal process to
remove their stake from a specific liquidity pool. This operation is crucial for
users who wish to reclaim their assets or reallocate their liquidity to different
pools or investments. The endpoint requires details such as the token pair, the
amount to be withdrawn, and any additional parameters needed for the withdrawal
process. Users should ensure they meet any protocol requirements or conditions
before initiating a withdrawal to avoid potential issues or penalties.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_withdraw_liquidity_provision_request import UniswapWithdrawLiquidityProvisionRequest
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
    uniswap_withdraw_liquidity_provision_request = compass.api_client.UniswapWithdrawLiquidityProvisionRequest() # UniswapWithdrawLiquidityProvisionRequest | 

    try:
        # Withdraw an LP position
        api_response = api_instance.uniswap_liquidity_provision_withdraw(uniswap_withdraw_liquidity_provision_request)
        print("The response of UniswapV3Api->uniswap_liquidity_provision_withdraw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->uniswap_liquidity_provision_withdraw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_withdraw_liquidity_provision_request** | [**UniswapWithdrawLiquidityProvisionRequest**](UniswapWithdrawLiquidityProvisionRequest.md)|  | 

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

# **uniswap_pool_price**
> UniswapPoolPriceResponse uniswap_pool_price(uniswap_get_pool_price_request)

Pool price

This endpoint calculates the price of a token in a Uniswap pool.

The price is calculated based on the current pool state and the specified fee tier.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_get_pool_price_request import UniswapGetPoolPriceRequest
from compass.api_client.models.uniswap_pool_price_response import UniswapPoolPriceResponse
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
    uniswap_get_pool_price_request = compass.api_client.UniswapGetPoolPriceRequest() # UniswapGetPoolPriceRequest | 

    try:
        # Pool price
        api_response = api_instance.uniswap_pool_price(uniswap_get_pool_price_request)
        print("The response of UniswapV3Api->uniswap_pool_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->uniswap_pool_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_get_pool_price_request** | [**UniswapGetPoolPriceRequest**](UniswapGetPoolPriceRequest.md)|  | 

### Return type

[**UniswapPoolPriceResponse**](UniswapPoolPriceResponse.md)

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

# **uniswap_quote_buy_exactly**
> UniswapBuyQuoteInfoResponse uniswap_quote_buy_exactly(uniswap_get_buy_quote_request)

Get quote - to specified amount

This endpoint calculates the amount of input tokens required to purchase a
specified amount of output tokens from a Uniswap pool.

It also provides the resulting price after the transaction. The calculation takes
into account the current pool state and the specified fee tier.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_buy_quote_info_response import UniswapBuyQuoteInfoResponse
from compass.api_client.models.uniswap_get_buy_quote_request import UniswapGetBuyQuoteRequest
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
    uniswap_get_buy_quote_request = compass.api_client.UniswapGetBuyQuoteRequest() # UniswapGetBuyQuoteRequest | 

    try:
        # Get quote - to specified amount
        api_response = api_instance.uniswap_quote_buy_exactly(uniswap_get_buy_quote_request)
        print("The response of UniswapV3Api->uniswap_quote_buy_exactly:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->uniswap_quote_buy_exactly: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_get_buy_quote_request** | [**UniswapGetBuyQuoteRequest**](UniswapGetBuyQuoteRequest.md)|  | 

### Return type

[**UniswapBuyQuoteInfoResponse**](UniswapBuyQuoteInfoResponse.md)

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

# **uniswap_quote_sell_exactly**
> UniswapSellQuoteInfoResponse uniswap_quote_sell_exactly(uniswap_get_sell_quote_request)

Get quote - from specified amount

This endpoint calculates the amount of input tokens required to purchase a
specified amount of output tokens from a Uniswap pool.

It also provides the resulting price after the transaction. The calculation takes
into account the current pool state and the specified fee tier.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_get_sell_quote_request import UniswapGetSellQuoteRequest
from compass.api_client.models.uniswap_sell_quote_info_response import UniswapSellQuoteInfoResponse
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
    uniswap_get_sell_quote_request = compass.api_client.UniswapGetSellQuoteRequest() # UniswapGetSellQuoteRequest | 

    try:
        # Get quote - from specified amount
        api_response = api_instance.uniswap_quote_sell_exactly(uniswap_get_sell_quote_request)
        print("The response of UniswapV3Api->uniswap_quote_sell_exactly:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->uniswap_quote_sell_exactly: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_get_sell_quote_request** | [**UniswapGetSellQuoteRequest**](UniswapGetSellQuoteRequest.md)|  | 

### Return type

[**UniswapSellQuoteInfoResponse**](UniswapSellQuoteInfoResponse.md)

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

# **uniswap_swap_buy_exactly**
> UnsignedTransaction uniswap_swap_buy_exactly(uniswap_buy_exactly_request)

Buy exact amount

This endpoint allows users to trade a variable amount of one token to receive an
exact amount of another token using the Uniswap protocol.

The transaction is executed on the specified blockchain network, and the user must
provide the necessary transaction details, including the token to buy, the token to
pay with, and the exact amount to receive. If the token being paid with is WETH and
needs to be wrapped, the appropriate amount will be wrapped automatically.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_buy_exactly_request import UniswapBuyExactlyRequest
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
    uniswap_buy_exactly_request = compass.api_client.UniswapBuyExactlyRequest() # UniswapBuyExactlyRequest | 

    try:
        # Buy exact amount
        api_response = api_instance.uniswap_swap_buy_exactly(uniswap_buy_exactly_request)
        print("The response of UniswapV3Api->uniswap_swap_buy_exactly:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->uniswap_swap_buy_exactly: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_buy_exactly_request** | [**UniswapBuyExactlyRequest**](UniswapBuyExactlyRequest.md)|  | 

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

# **uniswap_swap_sell_exactly**
> UnsignedTransaction uniswap_swap_sell_exactly(uniswap_sell_exactly_request)

Sell exact amount

This endpoint allows users to trade a specific amount of one token into another
token using the Uniswap protocol.

The transaction is executed on the specified blockchain network, and the user must
provide the necessary transaction details, including the token to sell, the token to
receive, and the amount to sell. If the token being sold is WETH and needs to be
wrapped, the appropriate amount will be wrapped automatically.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.uniswap_sell_exactly_request import UniswapSellExactlyRequest
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
    uniswap_sell_exactly_request = compass.api_client.UniswapSellExactlyRequest() # UniswapSellExactlyRequest | 

    try:
        # Sell exact amount
        api_response = api_instance.uniswap_swap_sell_exactly(uniswap_sell_exactly_request)
        print("The response of UniswapV3Api->uniswap_swap_sell_exactly:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniswapV3Api->uniswap_swap_sell_exactly: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uniswap_sell_exactly_request** | [**UniswapSellExactlyRequest**](UniswapSellExactlyRequest.md)|  | 

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

