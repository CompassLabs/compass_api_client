# compass.api_client.AerodromeSlipstreamApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_request_v0_aerodrome_slipstream_liquidity_provision_increase_post**](AerodromeSlipstreamApi.md#process_request_v0_aerodrome_slipstream_liquidity_provision_increase_post) | **POST** /v0/aerodrome_slipstream/liquidity_provision/increase | Increase an LP position
[**process_request_v0_aerodrome_slipstream_liquidity_provision_mint_post**](AerodromeSlipstreamApi.md#process_request_v0_aerodrome_slipstream_liquidity_provision_mint_post) | **POST** /v0/aerodrome_slipstream/liquidity_provision/mint | Open a new LP position
[**process_request_v0_aerodrome_slipstream_liquidity_provision_positions_get_post**](AerodromeSlipstreamApi.md#process_request_v0_aerodrome_slipstream_liquidity_provision_positions_get_post) | **POST** /v0/aerodrome_slipstream/liquidity_provision/positions/get | List LP positions
[**process_request_v0_aerodrome_slipstream_liquidity_provision_withdraw_post**](AerodromeSlipstreamApi.md#process_request_v0_aerodrome_slipstream_liquidity_provision_withdraw_post) | **POST** /v0/aerodrome_slipstream/liquidity_provision/withdraw | Withdraw an LP position
[**process_request_v0_aerodrome_slipstream_pool_price_get_post**](AerodromeSlipstreamApi.md#process_request_v0_aerodrome_slipstream_pool_price_get_post) | **POST** /v0/aerodrome_slipstream/pool_price/get | Pool price
[**process_request_v0_aerodrome_slipstream_swap_buy_exactly_post**](AerodromeSlipstreamApi.md#process_request_v0_aerodrome_slipstream_swap_buy_exactly_post) | **POST** /v0/aerodrome_slipstream/swap/buy_exactly | Swap - into specified amount
[**process_request_v0_aerodrome_slipstream_swap_sell_exactly_post**](AerodromeSlipstreamApi.md#process_request_v0_aerodrome_slipstream_swap_sell_exactly_post) | **POST** /v0/aerodrome_slipstream/swap/sell_exactly | Swap - from specified amount


# **process_request_v0_aerodrome_slipstream_liquidity_provision_increase_post**
> UnsignedTransaction process_request_v0_aerodrome_slipstream_liquidity_provision_increase_post(base_transaction_request_aerodrome_slipstream_increase_liquidity_provision_call_data)

Increase an LP position

Increase the liquidity of an existing Liquidity Provider (LP) position.
This endpoint allows users to add more tokens to their current LP position,
enhancing their participation in liquidity provision. By increasing liquidity,
users can potentially earn more rewards and improve their position in the pool.
The process involves specifying additional token amounts and updating the pool details.
The response will confirm the successful increase of the LP position,
providing users with updated information about their enhanced position.
This functionality is vital for users aiming to optimize their liquidity provision strategy,
enabling them to adapt to market conditions and maximize their returns in decentralized finance (DeFi) markets.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aerodrome_slipstream_increase_liquidity_provision_call_data import BaseTransactionRequestAerodromeSlipstreamIncreaseLiquidityProvisionCallData
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
    api_instance = compass.api_client.AerodromeSlipstreamApi(api_client)
    base_transaction_request_aerodrome_slipstream_increase_liquidity_provision_call_data = compass.api_client.BaseTransactionRequestAerodromeSlipstreamIncreaseLiquidityProvisionCallData() # BaseTransactionRequestAerodromeSlipstreamIncreaseLiquidityProvisionCallData | 

    try:
        # Increase an LP position
        api_response = api_instance.process_request_v0_aerodrome_slipstream_liquidity_provision_increase_post(base_transaction_request_aerodrome_slipstream_increase_liquidity_provision_call_data)
        print("The response of AerodromeSlipstreamApi->process_request_v0_aerodrome_slipstream_liquidity_provision_increase_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeSlipstreamApi->process_request_v0_aerodrome_slipstream_liquidity_provision_increase_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aerodrome_slipstream_increase_liquidity_provision_call_data** | [**BaseTransactionRequestAerodromeSlipstreamIncreaseLiquidityProvisionCallData**](BaseTransactionRequestAerodromeSlipstreamIncreaseLiquidityProvisionCallData.md)|  | 

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

# **process_request_v0_aerodrome_slipstream_liquidity_provision_mint_post**
> UnsignedTransaction process_request_v0_aerodrome_slipstream_liquidity_provision_mint_post(base_transaction_request_aerodrome_slipstream_mint_liquidity_provision_call_data)

Open a new LP position

Initiate a new Liquidity Provider (LP) position by minting tokens.
This endpoint allows users to open a new LP position, enabling them to participate in liquidity provision.
The minting process involves creating a new position with specified parameters,
such as token amounts and pool details. The response will confirm the successful creation of the LP position,
providing users with the necessary information to manage their newly minted position.
This functionality is crucial for users looking to expand their liquidity provision activities,
offering them the opportunity to engage in decentralized finance (DeFi) markets effectively.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aerodrome_slipstream_mint_liquidity_provision_call_data import BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData
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
    api_instance = compass.api_client.AerodromeSlipstreamApi(api_client)
    base_transaction_request_aerodrome_slipstream_mint_liquidity_provision_call_data = compass.api_client.BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData() # BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData | 

    try:
        # Open a new LP position
        api_response = api_instance.process_request_v0_aerodrome_slipstream_liquidity_provision_mint_post(base_transaction_request_aerodrome_slipstream_mint_liquidity_provision_call_data)
        print("The response of AerodromeSlipstreamApi->process_request_v0_aerodrome_slipstream_liquidity_provision_mint_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeSlipstreamApi->process_request_v0_aerodrome_slipstream_liquidity_provision_mint_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aerodrome_slipstream_mint_liquidity_provision_call_data** | [**BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData**](BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData.md)|  | 

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

# **process_request_v0_aerodrome_slipstream_liquidity_provision_positions_get_post**
> AerodromeLPPositionsInfo process_request_v0_aerodrome_slipstream_liquidity_provision_positions_get_post(aerodrome_slipstream_get_liquidity_provision_positions)

List LP positions

Retrieve the total number of Liquidity Provider (LP) positions associated with a specific sender.
This endpoint allows users to query and obtain detailed information about their LP positions,
including the number of active positions they hold. The response model, AerodromeLPPositionsInfo,
provides a structured representation of the LP positions data, ensuring clarity and ease of use.
This functionality is essential for users managing their liquidity provision activities,
enabling them to make informed decisions based on their current positions.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_lp_positions_info import AerodromeLPPositionsInfo
from compass.api_client.models.aerodrome_slipstream_get_liquidity_provision_positions import AerodromeSlipstreamGetLiquidityProvisionPositions
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
    api_instance = compass.api_client.AerodromeSlipstreamApi(api_client)
    aerodrome_slipstream_get_liquidity_provision_positions = compass.api_client.AerodromeSlipstreamGetLiquidityProvisionPositions() # AerodromeSlipstreamGetLiquidityProvisionPositions | 

    try:
        # List LP positions
        api_response = api_instance.process_request_v0_aerodrome_slipstream_liquidity_provision_positions_get_post(aerodrome_slipstream_get_liquidity_provision_positions)
        print("The response of AerodromeSlipstreamApi->process_request_v0_aerodrome_slipstream_liquidity_provision_positions_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeSlipstreamApi->process_request_v0_aerodrome_slipstream_liquidity_provision_positions_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_slipstream_get_liquidity_provision_positions** | [**AerodromeSlipstreamGetLiquidityProvisionPositions**](AerodromeSlipstreamGetLiquidityProvisionPositions.md)|  | 

### Return type

[**AerodromeLPPositionsInfo**](AerodromeLPPositionsInfo.md)

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

# **process_request_v0_aerodrome_slipstream_liquidity_provision_withdraw_post**
> UnsignedTransaction process_request_v0_aerodrome_slipstream_liquidity_provision_withdraw_post(base_transaction_request_aerodrome_slipstream_withdraw_liquidity_provision_call_data)

Withdraw an LP position

Withdraw an existing Liquidity Provider (LP) position.
This endpoint allows users to remove their tokens from an LP position,
effectively closing their participation in the liquidity pool.
The withdrawal process involves specifying the LP position to be closed,
and the response will confirm the successful removal of liquidity,
providing users with details about the withdrawn tokens and any remaining balances.
This functionality is essential for users who wish to exit their liquidity provision activities,
enabling them to reclaim their assets and potentially reallocate them to other investment opportunities.
The endpoint ensures a smooth and secure withdrawal process,
facilitating users' strategic management of their decentralized finance (DeFi) portfolios.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aerodrome_slipstream_withdraw_liquidity_provision_call_data import BaseTransactionRequestAerodromeSlipstreamWithdrawLiquidityProvisionCallData
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
    api_instance = compass.api_client.AerodromeSlipstreamApi(api_client)
    base_transaction_request_aerodrome_slipstream_withdraw_liquidity_provision_call_data = compass.api_client.BaseTransactionRequestAerodromeSlipstreamWithdrawLiquidityProvisionCallData() # BaseTransactionRequestAerodromeSlipstreamWithdrawLiquidityProvisionCallData | 

    try:
        # Withdraw an LP position
        api_response = api_instance.process_request_v0_aerodrome_slipstream_liquidity_provision_withdraw_post(base_transaction_request_aerodrome_slipstream_withdraw_liquidity_provision_call_data)
        print("The response of AerodromeSlipstreamApi->process_request_v0_aerodrome_slipstream_liquidity_provision_withdraw_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeSlipstreamApi->process_request_v0_aerodrome_slipstream_liquidity_provision_withdraw_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aerodrome_slipstream_withdraw_liquidity_provision_call_data** | [**BaseTransactionRequestAerodromeSlipstreamWithdrawLiquidityProvisionCallData**](BaseTransactionRequestAerodromeSlipstreamWithdrawLiquidityProvisionCallData.md)|  | 

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

# **process_request_v0_aerodrome_slipstream_pool_price_get_post**
> AerodromeSlipstreamPoolPrice process_request_v0_aerodrome_slipstream_pool_price_get_post(aerodrome_slipstream_get_pool_price)

Pool price

This endpoint retrieves the current price of a pool, indicating how many token0
you can purchase for 1 token1. Note that this is an instantaneous price and may
change during any trade. For a more accurate representation of the trade ratios
between the two assets, consider using the quote endpoint.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_slipstream_get_pool_price import AerodromeSlipstreamGetPoolPrice
from compass.api_client.models.aerodrome_slipstream_pool_price import AerodromeSlipstreamPoolPrice
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
    api_instance = compass.api_client.AerodromeSlipstreamApi(api_client)
    aerodrome_slipstream_get_pool_price = compass.api_client.AerodromeSlipstreamGetPoolPrice() # AerodromeSlipstreamGetPoolPrice | 

    try:
        # Pool price
        api_response = api_instance.process_request_v0_aerodrome_slipstream_pool_price_get_post(aerodrome_slipstream_get_pool_price)
        print("The response of AerodromeSlipstreamApi->process_request_v0_aerodrome_slipstream_pool_price_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeSlipstreamApi->process_request_v0_aerodrome_slipstream_pool_price_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_slipstream_get_pool_price** | [**AerodromeSlipstreamGetPoolPrice**](AerodromeSlipstreamGetPoolPrice.md)|  | 

### Return type

[**AerodromeSlipstreamPoolPrice**](AerodromeSlipstreamPoolPrice.md)

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

# **process_request_v0_aerodrome_slipstream_swap_buy_exactly_post**
> UnsignedTransaction process_request_v0_aerodrome_slipstream_swap_buy_exactly_post(base_transaction_request_aerodrome_slipstream_buy_exactly_call_data)

Swap - into specified amount

This endpoint facilitates the trading of tokens by allowing users to
specify the exact amount of the output token they wish to receive.
Utilizing the Aerodrome Slipstream protocol, the system calculates
the necessary amount of the input token required to achieve the
desired output. This operation is particularly useful for users who
have a specific target amount of the output token in mind and are
willing to provide the corresponding input token amount. The
transaction is executed with consideration of current market
conditions, including liquidity and price impact, ensuring that the
trade is completed efficiently and effectively.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aerodrome_slipstream_buy_exactly_call_data import BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData
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
    api_instance = compass.api_client.AerodromeSlipstreamApi(api_client)
    base_transaction_request_aerodrome_slipstream_buy_exactly_call_data = compass.api_client.BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData() # BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData | 

    try:
        # Swap - into specified amount
        api_response = api_instance.process_request_v0_aerodrome_slipstream_swap_buy_exactly_post(base_transaction_request_aerodrome_slipstream_buy_exactly_call_data)
        print("The response of AerodromeSlipstreamApi->process_request_v0_aerodrome_slipstream_swap_buy_exactly_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeSlipstreamApi->process_request_v0_aerodrome_slipstream_swap_buy_exactly_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aerodrome_slipstream_buy_exactly_call_data** | [**BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData**](BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData.md)|  | 

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

# **process_request_v0_aerodrome_slipstream_swap_sell_exactly_post**
> UnsignedTransaction process_request_v0_aerodrome_slipstream_swap_sell_exactly_post(base_transaction_request_aerodrome_slipstream_sell_exactly_call_data)

Swap - from specified amount

This endpoint allows users to trade a specific amount of one token
into another token using the Aerodrome Slipstream protocol. The
transaction is executed by specifying the exact amount of the input
token to be sold, and the system calculates the amount of the output
token that will be received. The operation ensures that the trade is
conducted within the constraints of the current market conditions,
taking into account the liquidity and price impact. This endpoint is
suitable for users who want to sell a precise quantity of a token
and are willing to accept the resulting amount of the other token.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aerodrome_slipstream_sell_exactly_call_data import BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData
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
    api_instance = compass.api_client.AerodromeSlipstreamApi(api_client)
    base_transaction_request_aerodrome_slipstream_sell_exactly_call_data = compass.api_client.BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData() # BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData | 

    try:
        # Swap - from specified amount
        api_response = api_instance.process_request_v0_aerodrome_slipstream_swap_sell_exactly_post(base_transaction_request_aerodrome_slipstream_sell_exactly_call_data)
        print("The response of AerodromeSlipstreamApi->process_request_v0_aerodrome_slipstream_swap_sell_exactly_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeSlipstreamApi->process_request_v0_aerodrome_slipstream_swap_sell_exactly_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aerodrome_slipstream_sell_exactly_call_data** | [**BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData**](BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData.md)|  | 

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

