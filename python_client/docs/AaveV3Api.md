# compass.api_client.AaveV3Api

All URIs are relative to *https://api.compasslabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aave_asset_price**](AaveV3Api.md#aave_asset_price) | **POST** /v0/aave/asset_price/get | Token prices
[**aave_borrow**](AaveV3Api.md#aave_borrow) | **POST** /v0/aave/borrow | Borrow
[**aave_liquidity_change**](AaveV3Api.md#aave_liquidity_change) | **POST** /v0/aave/liquidity/change/get | Liquidity index
[**aave_repay**](AaveV3Api.md#aave_repay) | **POST** /v0/aave/repay | Repay loans
[**aave_supply**](AaveV3Api.md#aave_supply) | **POST** /v0/aave/supply | Supply/Lend
[**aave_user_position_per_token**](AaveV3Api.md#aave_user_position_per_token) | **POST** /v0/aave/user_position_per_token/get | Positions - per token
[**aave_user_position_summary**](AaveV3Api.md#aave_user_position_summary) | **POST** /v0/aave/user_position_summary/get | Positions - total
[**aave_withdraw**](AaveV3Api.md#aave_withdraw) | **POST** /v0/aave/withdraw | Unstake


# **aave_asset_price**
> AaveAssetPriceResponse aave_asset_price(aave_get_asset_price_request)

Token prices

This endpoint retrieves the current price of a specified asset in USD as
determined by the Aave protocol.

It utilizes the Aave V3 Oracle to fetch the asset price, ensuring accurate and up-
to-date information. The request requires the asset identifier and the blockchain
network (chain) on which the asset resides. The response provides the asset price in
a standardized format, converted from Wei to the base currency decimals defined by
Aave.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aave_asset_price_response import AaveAssetPriceResponse
from compass.api_client.models.aave_get_asset_price_request import AaveGetAssetPriceRequest
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    aave_get_asset_price_request = compass.api_client.AaveGetAssetPriceRequest() # AaveGetAssetPriceRequest | 

    try:
        # Token prices
        api_response = api_instance.aave_asset_price(aave_get_asset_price_request)
        print("The response of AaveV3Api->aave_asset_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->aave_asset_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aave_get_asset_price_request** | [**AaveGetAssetPriceRequest**](AaveGetAssetPriceRequest.md)|  | 

### Return type

[**AaveAssetPriceResponse**](AaveAssetPriceResponse.md)

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

# **aave_borrow**
> UnsignedTransaction aave_borrow(aave_borrow_request)

Borrow

You will pay interest for your borrows.

Price changes in the assets may lead to some or all of your collateral being
liquidated, if the borrow position becomes unhealthy.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aave_borrow_request import AaveBorrowRequest
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    aave_borrow_request = compass.api_client.AaveBorrowRequest() # AaveBorrowRequest | 

    try:
        # Borrow
        api_response = api_instance.aave_borrow(aave_borrow_request)
        print("The response of AaveV3Api->aave_borrow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->aave_borrow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aave_borrow_request** | [**AaveBorrowRequest**](AaveBorrowRequest.md)|  | 

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

# **aave_liquidity_change**
> AaveLiquidityChangeResponse aave_liquidity_change(aave_get_liquidity_change_request)

Liquidity index

This endpoint retrieves the change in the reserve liquidity index between two
provided blocks.

This is then converted to a percentage change. The liquidity index represents the
change in debt and interest accrual over each block. Aave does not store individual
user balances directly. Instead, it keeps a scaled balance and uses the liquidity
index to compute real balances dynamically. If a user was to have deposited tokens
at the start block, a positive liquidity index change will represent accrued
interest and a profit. If tokens were borrowed at the start block, this debt will
increase, compound on itself and represent large debt. The reverse in both cases is
true if the liquidity index is negative.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aave_get_liquidity_change_request import AaveGetLiquidityChangeRequest
from compass.api_client.models.aave_liquidity_change_response import AaveLiquidityChangeResponse
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    aave_get_liquidity_change_request = compass.api_client.AaveGetLiquidityChangeRequest() # AaveGetLiquidityChangeRequest | 

    try:
        # Liquidity index
        api_response = api_instance.aave_liquidity_change(aave_get_liquidity_change_request)
        print("The response of AaveV3Api->aave_liquidity_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->aave_liquidity_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aave_get_liquidity_change_request** | [**AaveGetLiquidityChangeRequest**](AaveGetLiquidityChangeRequest.md)|  | 

### Return type

[**AaveLiquidityChangeResponse**](AaveLiquidityChangeResponse.md)

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

# **aave_repay**
> UnsignedTransaction aave_repay(aave_repay_request)

Repay loans

This endpoint allows users to repay a portion or the entirety of their borrowed
tokens on the Aave platform.

By repaying borrowed amounts, users can improve their health factor, which is a
measure of the safety of their loan position. A higher health factor reduces the
risk of liquidation, ensuring a more secure borrowing experience. The endpoint
requires specifying the chain and the details of the repayment transaction,
including the amount and the asset to be repaid.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aave_repay_request import AaveRepayRequest
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    aave_repay_request = compass.api_client.AaveRepayRequest() # AaveRepayRequest | 

    try:
        # Repay loans
        api_response = api_instance.aave_repay(aave_repay_request)
        print("The response of AaveV3Api->aave_repay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->aave_repay: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aave_repay_request** | [**AaveRepayRequest**](AaveRepayRequest.md)|  | 

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

# **aave_supply**
> UnsignedTransaction aave_supply(aave_supply_request)

Supply/Lend

By supplying assets, users can earn interest on their deposits.

The supplied collateral can be used as a basis for borrowing other assets, allowing
users to leverage their positions. In combination with a trading protocol, this can
create leverage.

Overall, this endpoint is a critical component for users looking to maximize their
asset utility within the AAVEv3 ecosystem, providing both earning potential and
borrowing flexibility.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aave_supply_request import AaveSupplyRequest
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    aave_supply_request = compass.api_client.AaveSupplyRequest() # AaveSupplyRequest | 

    try:
        # Supply/Lend
        api_response = api_instance.aave_supply(aave_supply_request)
        print("The response of AaveV3Api->aave_supply:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->aave_supply: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aave_supply_request** | [**AaveSupplyRequest**](AaveSupplyRequest.md)|  | 

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

# **aave_user_position_per_token**
> AaveUserPositionPerTokenResponse aave_user_position_per_token(aave_get_user_position_per_token_request)

Positions - per token

This endpoint retrieves the user's position for a specific token on the AAVE
platform.

It provides key financial metrics including the current aToken balance, current
stable debt, current variable debt, principal stable debt, principal variable debt,
stable borrow rate, stable borrow rate for new loans, variable borrow rate, and
liquidity rate. These metrics are calculated by aggregating data across all open
positions held by the user for the specified token, offering a detailed view of
their financial standing within the AAVE ecosystem.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aave_get_user_position_per_token_request import AaveGetUserPositionPerTokenRequest
from compass.api_client.models.aave_user_position_per_token_response import AaveUserPositionPerTokenResponse
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    aave_get_user_position_per_token_request = compass.api_client.AaveGetUserPositionPerTokenRequest() # AaveGetUserPositionPerTokenRequest | 

    try:
        # Positions - per token
        api_response = api_instance.aave_user_position_per_token(aave_get_user_position_per_token_request)
        print("The response of AaveV3Api->aave_user_position_per_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->aave_user_position_per_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aave_get_user_position_per_token_request** | [**AaveGetUserPositionPerTokenRequest**](AaveGetUserPositionPerTokenRequest.md)|  | 

### Return type

[**AaveUserPositionPerTokenResponse**](AaveUserPositionPerTokenResponse.md)

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

# **aave_user_position_summary**
> AaveUserPositionSummaryResponse aave_user_position_summary(aave_get_user_position_summary_request)

Positions - total

This endpoint retrieves a comprehensive summary of a user's position on the AAVE
platform.

It provides key financial metrics including the total collateral deposited, total
debt accrued, available borrowing capacity, liquidation threshold, maximum loan-to-
value ratio, and the health factor of the user's account. These metrics are
calculated by aggregating data across all open positions held by the user, offering
a holistic view of their financial standing within the AAVE ecosystem.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aave_get_user_position_summary_request import AaveGetUserPositionSummaryRequest
from compass.api_client.models.aave_user_position_summary_response import AaveUserPositionSummaryResponse
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    aave_get_user_position_summary_request = compass.api_client.AaveGetUserPositionSummaryRequest() # AaveGetUserPositionSummaryRequest | 

    try:
        # Positions - total
        api_response = api_instance.aave_user_position_summary(aave_get_user_position_summary_request)
        print("The response of AaveV3Api->aave_user_position_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->aave_user_position_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aave_get_user_position_summary_request** | [**AaveGetUserPositionSummaryRequest**](AaveGetUserPositionSummaryRequest.md)|  | 

### Return type

[**AaveUserPositionSummaryResponse**](AaveUserPositionSummaryResponse.md)

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

# **aave_withdraw**
> UnsignedTransaction aave_withdraw(aave_withdraw_request)

Unstake

This endpoint facilitates the withdrawal of collateral from the Aave protocol.

Users can withdraw a portion or all of their collateral, which may increase the risk
of liquidation if there are outstanding borrows. The withdrawal process also
includes the collection of any interest earned on the collateral. It is important
for users to carefully consider their outstanding debts and the potential impact on
their liquidation threshold before proceeding with a withdrawal. This endpoint is
designed to provide a seamless and efficient way to manage your collateral within
the Aave ecosystem.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import compass.api_client
from compass.api_client.models.aave_withdraw_request import AaveWithdrawRequest
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    aave_withdraw_request = compass.api_client.AaveWithdrawRequest() # AaveWithdrawRequest | 

    try:
        # Unstake
        api_response = api_instance.aave_withdraw(aave_withdraw_request)
        print("The response of AaveV3Api->aave_withdraw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->aave_withdraw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aave_withdraw_request** | [**AaveWithdrawRequest**](AaveWithdrawRequest.md)|  | 

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

