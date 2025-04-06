# compass.api_client.AerodromeSlipstreamApi

All URIs are relative to *https://api.compasslabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aerodrome_slipstream_liquidity_provision_increase**](AerodromeSlipstreamApi.md#aerodrome_slipstream_liquidity_provision_increase) | **POST** /v0/aerodrome_slipstream/liquidity_provision/increase | Increase an LP position
[**aerodrome_slipstream_liquidity_provision_mint**](AerodromeSlipstreamApi.md#aerodrome_slipstream_liquidity_provision_mint) | **POST** /v0/aerodrome_slipstream/liquidity_provision/mint | Open a new LP position
[**aerodrome_slipstream_liquidity_provision_positions**](AerodromeSlipstreamApi.md#aerodrome_slipstream_liquidity_provision_positions) | **POST** /v0/aerodrome_slipstream/liquidity_provision/positions/get | List LP positions
[**aerodrome_slipstream_liquidity_provision_withdraw**](AerodromeSlipstreamApi.md#aerodrome_slipstream_liquidity_provision_withdraw) | **POST** /v0/aerodrome_slipstream/liquidity_provision/withdraw | Withdraw an LP position
[**aerodrome_slipstream_pool_price**](AerodromeSlipstreamApi.md#aerodrome_slipstream_pool_price) | **POST** /v0/aerodrome_slipstream/pool_price/get | Pool price
[**aerodrome_slipstream_swap_buy_exactly**](AerodromeSlipstreamApi.md#aerodrome_slipstream_swap_buy_exactly) | **POST** /v0/aerodrome_slipstream/swap/buy_exactly | Swap - into specified amount
[**aerodrome_slipstream_swap_sell_exactly**](AerodromeSlipstreamApi.md#aerodrome_slipstream_swap_sell_exactly) | **POST** /v0/aerodrome_slipstream/swap/sell_exactly | Swap - from specified amount


# **aerodrome_slipstream_liquidity_provision_increase**
> UnsignedTransaction aerodrome_slipstream_liquidity_provision_increase(aerodrome_slipstream_increase_liquidity_provision_request)

Increase an LP position

Increase the liquidity of an existing Liquidity Provider (LP) position.

This endpoint allows users to add more tokens to their current LP position,
enhancing their participation in liquidity provision. By increasing liquidity, users
can potentially earn more rewards and improve their position in the pool. The
process involves specifying additional token amounts and updating the pool details.
The response will confirm the successful increase of the LP position, providing
users with updated information about their enhanced position. This functionality is
vital for users aiming to optimize their liquidity provision strategy, enabling them
to adapt to market conditions and maximize their returns in decentralized finance
(DeFi) markets.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_slipstream_increase_liquidity_provision_request import AerodromeSlipstreamIncreaseLiquidityProvisionRequest
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
    api_instance = compass.api_client.AerodromeSlipstreamApi(api_client)
    aerodrome_slipstream_increase_liquidity_provision_request = compass.api_client.AerodromeSlipstreamIncreaseLiquidityProvisionRequest() # AerodromeSlipstreamIncreaseLiquidityProvisionRequest | 

    try:
        # Increase an LP position
        api_response = api_instance.aerodrome_slipstream_liquidity_provision_increase(aerodrome_slipstream_increase_liquidity_provision_request)
        print("The response of AerodromeSlipstreamApi->aerodrome_slipstream_liquidity_provision_increase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeSlipstreamApi->aerodrome_slipstream_liquidity_provision_increase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_slipstream_increase_liquidity_provision_request** | [**AerodromeSlipstreamIncreaseLiquidityProvisionRequest**](AerodromeSlipstreamIncreaseLiquidityProvisionRequest.md)|  | 

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

# **aerodrome_slipstream_liquidity_provision_mint**
> UnsignedTransaction aerodrome_slipstream_liquidity_provision_mint(aerodrome_slipstream_mint_liquidity_provision_request)

Open a new LP position

Initiate a new Liquidity Provider (LP) position by minting tokens.

This endpoint allows users to open a new LP position, enabling them to participate
in liquidity provision. The minting process involves creating a new position with
specified parameters, such as token amounts and pool details. The response will
confirm the successful creation of the LP position, providing users with the
necessary information to manage their newly minted position. This functionality is
crucial for users looking to expand their liquidity provision activities, offering
them the opportunity to engage in decentralized finance (DeFi) markets effectively.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_slipstream_mint_liquidity_provision_request import AerodromeSlipstreamMintLiquidityProvisionRequest
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
    api_instance = compass.api_client.AerodromeSlipstreamApi(api_client)
    aerodrome_slipstream_mint_liquidity_provision_request = compass.api_client.AerodromeSlipstreamMintLiquidityProvisionRequest() # AerodromeSlipstreamMintLiquidityProvisionRequest | 

    try:
        # Open a new LP position
        api_response = api_instance.aerodrome_slipstream_liquidity_provision_mint(aerodrome_slipstream_mint_liquidity_provision_request)
        print("The response of AerodromeSlipstreamApi->aerodrome_slipstream_liquidity_provision_mint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeSlipstreamApi->aerodrome_slipstream_liquidity_provision_mint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_slipstream_mint_liquidity_provision_request** | [**AerodromeSlipstreamMintLiquidityProvisionRequest**](AerodromeSlipstreamMintLiquidityProvisionRequest.md)|  | 

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

# **aerodrome_slipstream_liquidity_provision_positions**
> AerodromeLPPositionsResponse aerodrome_slipstream_liquidity_provision_positions(aerodrome_slipstream_get_liquidity_provision_positions_request)

List LP positions

Retrieve the total number of Liquidity Provider (LP) positions associated with a
specific sender.

This endpoint allows users to query and obtain detailed information about their LP
positions, including the number of active positions they hold. The response model,
AerodromeLPPositionsInfo, provides a structured representation of the LP positions
data, ensuring clarity and ease of use. This functionality is essential for users
managing their liquidity provision activities, enabling them to make informed
decisions based on their current positions.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_lp_positions_response import AerodromeLPPositionsResponse
from compass.api_client.models.aerodrome_slipstream_get_liquidity_provision_positions_request import AerodromeSlipstreamGetLiquidityProvisionPositionsRequest
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
    api_instance = compass.api_client.AerodromeSlipstreamApi(api_client)
    aerodrome_slipstream_get_liquidity_provision_positions_request = compass.api_client.AerodromeSlipstreamGetLiquidityProvisionPositionsRequest() # AerodromeSlipstreamGetLiquidityProvisionPositionsRequest | 

    try:
        # List LP positions
        api_response = api_instance.aerodrome_slipstream_liquidity_provision_positions(aerodrome_slipstream_get_liquidity_provision_positions_request)
        print("The response of AerodromeSlipstreamApi->aerodrome_slipstream_liquidity_provision_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeSlipstreamApi->aerodrome_slipstream_liquidity_provision_positions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_slipstream_get_liquidity_provision_positions_request** | [**AerodromeSlipstreamGetLiquidityProvisionPositionsRequest**](AerodromeSlipstreamGetLiquidityProvisionPositionsRequest.md)|  | 

### Return type

[**AerodromeLPPositionsResponse**](AerodromeLPPositionsResponse.md)

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

# **aerodrome_slipstream_liquidity_provision_withdraw**
> UnsignedTransaction aerodrome_slipstream_liquidity_provision_withdraw(aerodrome_slipstream_withdraw_liquidity_provision_request)

Withdraw an LP position

Withdraw an existing Liquidity Provider (LP) position.

This endpoint allows users to remove their tokens from an LP position, effectively
closing their participation in the liquidity pool. The withdrawal process involves
specifying the LP position to be closed, and the response will confirm the
successful removal of liquidity, providing users with details about the withdrawn
tokens and any remaining balances. This functionality is essential for users who
wish to exit their liquidity provision activities, enabling them to reclaim their
assets and potentially reallocate them to other investment opportunities. The
endpoint ensures a smooth and secure withdrawal process, facilitating users'
strategic management of their decentralized finance (DeFi) portfolios.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_slipstream_withdraw_liquidity_provision_request import AerodromeSlipstreamWithdrawLiquidityProvisionRequest
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
    api_instance = compass.api_client.AerodromeSlipstreamApi(api_client)
    aerodrome_slipstream_withdraw_liquidity_provision_request = compass.api_client.AerodromeSlipstreamWithdrawLiquidityProvisionRequest() # AerodromeSlipstreamWithdrawLiquidityProvisionRequest | 

    try:
        # Withdraw an LP position
        api_response = api_instance.aerodrome_slipstream_liquidity_provision_withdraw(aerodrome_slipstream_withdraw_liquidity_provision_request)
        print("The response of AerodromeSlipstreamApi->aerodrome_slipstream_liquidity_provision_withdraw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeSlipstreamApi->aerodrome_slipstream_liquidity_provision_withdraw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_slipstream_withdraw_liquidity_provision_request** | [**AerodromeSlipstreamWithdrawLiquidityProvisionRequest**](AerodromeSlipstreamWithdrawLiquidityProvisionRequest.md)|  | 

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

# **aerodrome_slipstream_pool_price**
> AerodromeSlipstreamPoolPriceResponse aerodrome_slipstream_pool_price(aerodrome_slipstream_get_pool_price_request)

Pool price

This endpoint retrieves the current price of a pool, indicating how many token0
you can purchase for 1 token1.

Note that this is an instantaneous price and may change during any trade. For a more
accurate representation of the trade ratios between the two assets, consider using
the quote endpoint.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_slipstream_get_pool_price_request import AerodromeSlipstreamGetPoolPriceRequest
from compass.api_client.models.aerodrome_slipstream_pool_price_response import AerodromeSlipstreamPoolPriceResponse
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
    api_instance = compass.api_client.AerodromeSlipstreamApi(api_client)
    aerodrome_slipstream_get_pool_price_request = compass.api_client.AerodromeSlipstreamGetPoolPriceRequest() # AerodromeSlipstreamGetPoolPriceRequest | 

    try:
        # Pool price
        api_response = api_instance.aerodrome_slipstream_pool_price(aerodrome_slipstream_get_pool_price_request)
        print("The response of AerodromeSlipstreamApi->aerodrome_slipstream_pool_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeSlipstreamApi->aerodrome_slipstream_pool_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_slipstream_get_pool_price_request** | [**AerodromeSlipstreamGetPoolPriceRequest**](AerodromeSlipstreamGetPoolPriceRequest.md)|  | 

### Return type

[**AerodromeSlipstreamPoolPriceResponse**](AerodromeSlipstreamPoolPriceResponse.md)

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

# **aerodrome_slipstream_swap_buy_exactly**
> UnsignedTransaction aerodrome_slipstream_swap_buy_exactly(aerodrome_slipstream_buy_exactly_request)

Swap - into specified amount

This endpoint facilitates the trading of tokens by allowing users to specify the
exact amount of the output token they wish to receive.

Utilizing the Aerodrome Slipstream protocol, the system calculates the necessary
amount of the input token required to achieve the desired output. This operation is
particularly useful for users who have a specific target amount of the output token
in mind and are willing to provide the corresponding input token amount. The
transaction is executed with consideration of current market conditions, including
liquidity and price impact, ensuring that the trade is completed efficiently and
effectively.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_slipstream_buy_exactly_request import AerodromeSlipstreamBuyExactlyRequest
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
    api_instance = compass.api_client.AerodromeSlipstreamApi(api_client)
    aerodrome_slipstream_buy_exactly_request = compass.api_client.AerodromeSlipstreamBuyExactlyRequest() # AerodromeSlipstreamBuyExactlyRequest | 

    try:
        # Swap - into specified amount
        api_response = api_instance.aerodrome_slipstream_swap_buy_exactly(aerodrome_slipstream_buy_exactly_request)
        print("The response of AerodromeSlipstreamApi->aerodrome_slipstream_swap_buy_exactly:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeSlipstreamApi->aerodrome_slipstream_swap_buy_exactly: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_slipstream_buy_exactly_request** | [**AerodromeSlipstreamBuyExactlyRequest**](AerodromeSlipstreamBuyExactlyRequest.md)|  | 

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

# **aerodrome_slipstream_swap_sell_exactly**
> UnsignedTransaction aerodrome_slipstream_swap_sell_exactly(aerodrome_slipstream_sell_exactly_request)

Swap - from specified amount

This endpoint allows users to trade a specific amount of one token into another
token using the Aerodrome Slipstream protocol.

The transaction is executed by specifying the exact amount of the input token to be
sold, and the system calculates the amount of the output token that will be
received. The operation ensures that the trade is conducted within the constraints
of the current market conditions, taking into account the liquidity and price
impact. This endpoint is suitable for users who want to sell a precise quantity of a
token and are willing to accept the resulting amount of the other token.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aerodrome_slipstream_sell_exactly_request import AerodromeSlipstreamSellExactlyRequest
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
    api_instance = compass.api_client.AerodromeSlipstreamApi(api_client)
    aerodrome_slipstream_sell_exactly_request = compass.api_client.AerodromeSlipstreamSellExactlyRequest() # AerodromeSlipstreamSellExactlyRequest | 

    try:
        # Swap - from specified amount
        api_response = api_instance.aerodrome_slipstream_swap_sell_exactly(aerodrome_slipstream_sell_exactly_request)
        print("The response of AerodromeSlipstreamApi->aerodrome_slipstream_swap_sell_exactly:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeSlipstreamApi->aerodrome_slipstream_swap_sell_exactly: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aerodrome_slipstream_sell_exactly_request** | [**AerodromeSlipstreamSellExactlyRequest**](AerodromeSlipstreamSellExactlyRequest.md)|  | 

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

