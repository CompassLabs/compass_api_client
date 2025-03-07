# compass.api_client.AaveV3Api

All URIs are relative to *https://api.compasslabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_request_v0_aave_asset_price_get_post**](AaveV3Api.md#process_request_v0_aave_asset_price_get_post) | **POST** /v0/aave/asset_price/get | Get the price of an asset in USD according to Aave
[**process_request_v0_aave_borrow_post**](AaveV3Api.md#process_request_v0_aave_borrow_post) | **POST** /v0/aave/borrow | Borrow against your collateral
[**process_request_v0_aave_liquidity_change_get_post**](AaveV3Api.md#process_request_v0_aave_liquidity_change_get_post) | **POST** /v0/aave/liquidity/change/get | Gets the change in liquidity index between two blocks, therefore the amount a position will have increased or decreased over the time
[**process_request_v0_aave_repay_post**](AaveV3Api.md#process_request_v0_aave_repay_post) | **POST** /v0/aave/repay | Repay some or all tokens you borrowed
[**process_request_v0_aave_supply_post**](AaveV3Api.md#process_request_v0_aave_supply_post) | **POST** /v0/aave/supply | Supply collateral to earn interest or borrow against
[**process_request_v0_aave_user_position_per_token_get_post**](AaveV3Api.md#process_request_v0_aave_user_position_per_token_get_post) | **POST** /v0/aave/user_position_per_token/get | Get the user&#39;s position for a specific token.
[**process_request_v0_aave_user_position_summary_get_post**](AaveV3Api.md#process_request_v0_aave_user_position_summary_get_post) | **POST** /v0/aave/user_position_summary/get | Get a summary of the user&#39;s position on AAVE. These values will be sums or averages across all open positions.
[**process_request_v0_aave_withdraw_post**](AaveV3Api.md#process_request_v0_aave_withdraw_post) | **POST** /v0/aave/withdraw | Withdraw some or all of your collateral


# **process_request_v0_aave_asset_price_get_post**
> AaveAssetPriceInfo process_request_v0_aave_asset_price_get_post(aave_get_asset_price)

Get the price of an asset in USD according to Aave

This endpoint retrieves the current price of a specified asset in USD as
        determined by the Aave protocol. It utilizes the Aave V3 Oracle to fetch the
        asset price, ensuring accurate and up-to-date information. The request
        requires the asset identifier and the blockchain network (chain) on which the
        asset resides. The response provides the asset price in a standardized format,
        converted from Wei to the base currency decimals defined by Aave.

### Example


```python
import compass.api_client
from compass.api_client.models.aave_asset_price_info import AaveAssetPriceInfo
from compass.api_client.models.aave_get_asset_price import AaveGetAssetPrice
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    aave_get_asset_price = compass.api_client.AaveGetAssetPrice() # AaveGetAssetPrice | 

    try:
        # Get the price of an asset in USD according to Aave
        api_response = api_instance.process_request_v0_aave_asset_price_get_post(aave_get_asset_price)
        print("The response of AaveV3Api->process_request_v0_aave_asset_price_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->process_request_v0_aave_asset_price_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aave_get_asset_price** | [**AaveGetAssetPrice**](AaveGetAssetPrice.md)|  | 

### Return type

[**AaveAssetPriceInfo**](AaveAssetPriceInfo.md)

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

# **process_request_v0_aave_borrow_post**
> UnsignedTransaction process_request_v0_aave_borrow_post(base_transaction_request_aave_borrow_call_data)

Borrow against your collateral

You will pay interest for your borrows. Price changes in the assets may lead to some or all of your collateral being liquidated, if the borrow position becomes unhealthy.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aave_borrow_call_data import BaseTransactionRequestAaveBorrowCallData
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    base_transaction_request_aave_borrow_call_data = compass.api_client.BaseTransactionRequestAaveBorrowCallData() # BaseTransactionRequestAaveBorrowCallData | 

    try:
        # Borrow against your collateral
        api_response = api_instance.process_request_v0_aave_borrow_post(base_transaction_request_aave_borrow_call_data)
        print("The response of AaveV3Api->process_request_v0_aave_borrow_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->process_request_v0_aave_borrow_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aave_borrow_call_data** | [**BaseTransactionRequestAaveBorrowCallData**](BaseTransactionRequestAaveBorrowCallData.md)|  | 

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

# **process_request_v0_aave_liquidity_change_get_post**
> AaveLiquidityChange process_request_v0_aave_liquidity_change_get_post(aave_get_liquidity_change)

Gets the change in liquidity index between two blocks, therefore the amount a position will have increased or decreased over the time

This endpoint retrieves the change in the reserve liquditiy index between
        two provided blocks. This is then converted to a percentage change.
        The liquidity index represents the change in debt and interest accrual over each block.
        Aave does not store individual user balances directly.
        Instead, it keeps a scaled balance and uses the liquidity index
        to compute real balances dynamically.
        If a user was to have deposited tokens at the start block, a positive liquidity
        index change will represent accured interest and a profit.
        If tokens were borrowed at the start block, this debt will increase,
        compound on itself and represent large debt.
        The reverse in both cases is true if the liquidity index is negative.

### Example


```python
import compass.api_client
from compass.api_client.models.aave_get_liquidity_change import AaveGetLiquidityChange
from compass.api_client.models.aave_liquidity_change import AaveLiquidityChange
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    aave_get_liquidity_change = compass.api_client.AaveGetLiquidityChange() # AaveGetLiquidityChange | 

    try:
        # Gets the change in liquidity index between two blocks, therefore the amount a position will have increased or decreased over the time
        api_response = api_instance.process_request_v0_aave_liquidity_change_get_post(aave_get_liquidity_change)
        print("The response of AaveV3Api->process_request_v0_aave_liquidity_change_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->process_request_v0_aave_liquidity_change_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aave_get_liquidity_change** | [**AaveGetLiquidityChange**](AaveGetLiquidityChange.md)|  | 

### Return type

[**AaveLiquidityChange**](AaveLiquidityChange.md)

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

# **process_request_v0_aave_repay_post**
> UnsignedTransaction process_request_v0_aave_repay_post(base_transaction_request_aave_repay_call_data)

Repay some or all tokens you borrowed

This endpoint allows users to repay a portion or the entirety of their borrowed
        tokens on the Aave platform. By repaying borrowed amounts, users can improve their
        health factor, which is a measure of the safety of their loan position. A higher health
        factor reduces the risk of liquidation, ensuring a more secure borrowing experience.
        The endpoint requires specifying the chain and the details of the repayment transaction,
        including the amount and the asset to be repaid.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aave_repay_call_data import BaseTransactionRequestAaveRepayCallData
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    base_transaction_request_aave_repay_call_data = compass.api_client.BaseTransactionRequestAaveRepayCallData() # BaseTransactionRequestAaveRepayCallData | 

    try:
        # Repay some or all tokens you borrowed
        api_response = api_instance.process_request_v0_aave_repay_post(base_transaction_request_aave_repay_call_data)
        print("The response of AaveV3Api->process_request_v0_aave_repay_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->process_request_v0_aave_repay_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aave_repay_call_data** | [**BaseTransactionRequestAaveRepayCallData**](BaseTransactionRequestAaveRepayCallData.md)|  | 

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

# **process_request_v0_aave_supply_post**
> UnsignedTransaction process_request_v0_aave_supply_post(base_transaction_request_aave_supply_call_data)

Supply collateral to earn interest or borrow against

By supplying assets, users can earn interest on their deposits

        The supplied collateral can be used as a basis for borrowing other assets,
        allowing users to leverage their positions.
        In combination with a trading protocol, this can create leverage.  

        Overall, this endpoint is a critical component for users looking to maximize their asset
        utility within the AAVEv3 ecosystem, providing both earning potential and borrowing
        flexibility.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aave_supply_call_data import BaseTransactionRequestAaveSupplyCallData
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    base_transaction_request_aave_supply_call_data = compass.api_client.BaseTransactionRequestAaveSupplyCallData() # BaseTransactionRequestAaveSupplyCallData | 

    try:
        # Supply collateral to earn interest or borrow against
        api_response = api_instance.process_request_v0_aave_supply_post(base_transaction_request_aave_supply_call_data)
        print("The response of AaveV3Api->process_request_v0_aave_supply_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->process_request_v0_aave_supply_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aave_supply_call_data** | [**BaseTransactionRequestAaveSupplyCallData**](BaseTransactionRequestAaveSupplyCallData.md)|  | 

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

# **process_request_v0_aave_user_position_per_token_get_post**
> AaveUserPositionPerTokenInfo process_request_v0_aave_user_position_per_token_get_post(aave_get_user_position_per_token)

Get the user's position for a specific token.

This endpoint retrieves the user's position for a specific token on the AAVE
        platform. It provides key financial metrics including the current aToken balance,
        current stable debt, current variable debt, principal stable debt, principal variable
        debt, stable borrow rate, stable borrow rate for new loans, variable borrow rate, and
        liquidity rate. These metrics are calculated by aggregating data across all open
        positions held by the user for the specified token, offering a detailed view of their
        financial standing within the AAVE ecosystem.

### Example


```python
import compass.api_client
from compass.api_client.models.aave_get_user_position_per_token import AaveGetUserPositionPerToken
from compass.api_client.models.aave_user_position_per_token_info import AaveUserPositionPerTokenInfo
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    aave_get_user_position_per_token = compass.api_client.AaveGetUserPositionPerToken() # AaveGetUserPositionPerToken | 

    try:
        # Get the user's position for a specific token.
        api_response = api_instance.process_request_v0_aave_user_position_per_token_get_post(aave_get_user_position_per_token)
        print("The response of AaveV3Api->process_request_v0_aave_user_position_per_token_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->process_request_v0_aave_user_position_per_token_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aave_get_user_position_per_token** | [**AaveGetUserPositionPerToken**](AaveGetUserPositionPerToken.md)|  | 

### Return type

[**AaveUserPositionPerTokenInfo**](AaveUserPositionPerTokenInfo.md)

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

# **process_request_v0_aave_user_position_summary_get_post**
> AaveUserPositionSummaryInfo process_request_v0_aave_user_position_summary_get_post(aave_get_user_position_summary)

Get a summary of the user's position on AAVE. These values will be sums or averages across all open positions.

This endpoint retrieves a comprehensive summary of a user's position on the
        AAVE platform. It provides key financial metrics including the total collateral
        deposited, total debt accrued, available borrowing capacity, liquidation threshold,
        maximum loan-to-value ratio, and the health factor of the user's account. These metrics
        are calculated by aggregating data across all open positions held by the user, offering
        a holistic view of their financial standing within the AAVE ecosystem.

### Example


```python
import compass.api_client
from compass.api_client.models.aave_get_user_position_summary import AaveGetUserPositionSummary
from compass.api_client.models.aave_user_position_summary_info import AaveUserPositionSummaryInfo
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    aave_get_user_position_summary = compass.api_client.AaveGetUserPositionSummary() # AaveGetUserPositionSummary | 

    try:
        # Get a summary of the user's position on AAVE. These values will be sums or averages across all open positions.
        api_response = api_instance.process_request_v0_aave_user_position_summary_get_post(aave_get_user_position_summary)
        print("The response of AaveV3Api->process_request_v0_aave_user_position_summary_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->process_request_v0_aave_user_position_summary_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aave_get_user_position_summary** | [**AaveGetUserPositionSummary**](AaveGetUserPositionSummary.md)|  | 

### Return type

[**AaveUserPositionSummaryInfo**](AaveUserPositionSummaryInfo.md)

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

# **process_request_v0_aave_withdraw_post**
> UnsignedTransaction process_request_v0_aave_withdraw_post(base_transaction_request_aave_withdraw_call_data)

Withdraw some or all of your collateral

This endpoint facilitates the withdrawal of collateral from the Aave protocol. Users can withdraw a portion or all of their collateral, which may increase the risk of liquidation if there are outstanding borrows. The withdrawal process also includes the collection of any interest earned on the collateral. It is important for users to carefully consider their outstanding debts and the potential impact on their liquidation threshold before proceeding with a withdrawal. This endpoint is designed to provide a seamless and efficient way to manage your collateral within the Aave ecosystem.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aave_withdraw_call_data import BaseTransactionRequestAaveWithdrawCallData
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
    api_instance = compass.api_client.AaveV3Api(api_client)
    base_transaction_request_aave_withdraw_call_data = compass.api_client.BaseTransactionRequestAaveWithdrawCallData() # BaseTransactionRequestAaveWithdrawCallData | 

    try:
        # Withdraw some or all of your collateral
        api_response = api_instance.process_request_v0_aave_withdraw_post(base_transaction_request_aave_withdraw_call_data)
        print("The response of AaveV3Api->process_request_v0_aave_withdraw_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveV3Api->process_request_v0_aave_withdraw_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aave_withdraw_call_data** | [**BaseTransactionRequestAaveWithdrawCallData**](BaseTransactionRequestAaveWithdrawCallData.md)|  | 

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

