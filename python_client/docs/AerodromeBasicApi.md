# compass.api_client.AerodromeBasicApi

All URIs are relative to *https://api.compasslabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_request_v0_aerodrome_basic_liquidity_provision_add_liquidity_eth_post**](AerodromeBasicApi.md#process_request_v0_aerodrome_basic_liquidity_provision_add_liquidity_eth_post) | **POST** /v0/aerodrome_basic/liquidity_provision/add_liquidity_eth | Provide liquidity to a pool on Aerodrome using WETH and another token
[**process_request_v0_aerodrome_basic_liquidity_provision_add_liquidity_post**](AerodromeBasicApi.md#process_request_v0_aerodrome_basic_liquidity_provision_add_liquidity_post) | **POST** /v0/aerodrome_basic/liquidity_provision/add_liquidity | Provide liquidity to a pool on Aerodrome
[**process_request_v0_aerodrome_basic_liquidity_provision_remove_liquidity_eth_post**](AerodromeBasicApi.md#process_request_v0_aerodrome_basic_liquidity_provision_remove_liquidity_eth_post) | **POST** /v0/aerodrome_basic/liquidity_provision/remove_liquidity_eth | Remove liquidity from a pool on Aerodrome using WETH and another token
[**process_request_v0_aerodrome_basic_liquidity_provision_remove_liquidity_post**](AerodromeBasicApi.md#process_request_v0_aerodrome_basic_liquidity_provision_remove_liquidity_post) | **POST** /v0/aerodrome_basic/liquidity_provision/remove_liquidity | Remove liquidity from a pool on Aerodrome
[**process_request_v0_aerodrome_basic_swap_eth_for_token_post**](AerodromeBasicApi.md#process_request_v0_aerodrome_basic_swap_eth_for_token_post) | **POST** /v0/aerodrome_basic/swap/eth_for_token | Swap ETH for some of a token on Aerodrome
[**process_request_v0_aerodrome_basic_swap_token_for_eth_post**](AerodromeBasicApi.md#process_request_v0_aerodrome_basic_swap_token_for_eth_post) | **POST** /v0/aerodrome_basic/swap/token_for_eth | Swap a token for ETH on Aerodrome
[**process_request_v0_aerodrome_basic_swap_tokens_post**](AerodromeBasicApi.md#process_request_v0_aerodrome_basic_swap_tokens_post) | **POST** /v0/aerodrome_basic/swap/tokens | Swap one token for another token on Aerodrome


# **process_request_v0_aerodrome_basic_liquidity_provision_add_liquidity_eth_post**
> UnsignedTransaction process_request_v0_aerodrome_basic_liquidity_provision_add_liquidity_eth_post(base_transaction_request_aerodrome_liquidity_provision_eth_call_data)

Provide liquidity to a pool on Aerodrome using WETH and another token

This endpoint allows users to provide liquidity to a specified pool on the
        Aerodrome platform using Wrapped Ether (WETH) and another token. Users must
        specify the token pair, desired amounts, minimum amounts, and a deadline for
        the transaction. The operation will ensure the pool exists and will use the
        sender's address if no recipient is specified. The transaction will be executed
        through the Aerodrome Basic Router contract, and the specified amount of WETH
        will be sent along with the transaction.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aerodrome_liquidity_provision_eth_call_data import BaseTransactionRequestAerodromeLiquidityProvisionEthCallData
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
    api_instance = compass.api_client.AerodromeBasicApi(api_client)
    base_transaction_request_aerodrome_liquidity_provision_eth_call_data = compass.api_client.BaseTransactionRequestAerodromeLiquidityProvisionEthCallData() # BaseTransactionRequestAerodromeLiquidityProvisionEthCallData | 

    try:
        # Provide liquidity to a pool on Aerodrome using WETH and another token
        api_response = api_instance.process_request_v0_aerodrome_basic_liquidity_provision_add_liquidity_eth_post(base_transaction_request_aerodrome_liquidity_provision_eth_call_data)
        print("The response of AerodromeBasicApi->process_request_v0_aerodrome_basic_liquidity_provision_add_liquidity_eth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeBasicApi->process_request_v0_aerodrome_basic_liquidity_provision_add_liquidity_eth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aerodrome_liquidity_provision_eth_call_data** | [**BaseTransactionRequestAerodromeLiquidityProvisionEthCallData**](BaseTransactionRequestAerodromeLiquidityProvisionEthCallData.md)|  | 

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

# **process_request_v0_aerodrome_basic_liquidity_provision_add_liquidity_post**
> UnsignedTransaction process_request_v0_aerodrome_basic_liquidity_provision_add_liquidity_post(base_transaction_request_aerodrome_liquidity_provision_call_data)

Provide liquidity to a pool on Aerodrome

This endpoint allows users to provide liquidity to a specified pool on the
        Aerodrome platform. Users must specify the tokens, desired amounts, minimum
        amounts, and a deadline for the transaction. The operation will ensure the
        pool exists and will use the sender's address if no recipient is specified.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aerodrome_liquidity_provision_call_data import BaseTransactionRequestAerodromeLiquidityProvisionCallData
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
    api_instance = compass.api_client.AerodromeBasicApi(api_client)
    base_transaction_request_aerodrome_liquidity_provision_call_data = compass.api_client.BaseTransactionRequestAerodromeLiquidityProvisionCallData() # BaseTransactionRequestAerodromeLiquidityProvisionCallData | 

    try:
        # Provide liquidity to a pool on Aerodrome
        api_response = api_instance.process_request_v0_aerodrome_basic_liquidity_provision_add_liquidity_post(base_transaction_request_aerodrome_liquidity_provision_call_data)
        print("The response of AerodromeBasicApi->process_request_v0_aerodrome_basic_liquidity_provision_add_liquidity_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeBasicApi->process_request_v0_aerodrome_basic_liquidity_provision_add_liquidity_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aerodrome_liquidity_provision_call_data** | [**BaseTransactionRequestAerodromeLiquidityProvisionCallData**](BaseTransactionRequestAerodromeLiquidityProvisionCallData.md)|  | 

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

# **process_request_v0_aerodrome_basic_liquidity_provision_remove_liquidity_eth_post**
> UnsignedTransaction process_request_v0_aerodrome_basic_liquidity_provision_remove_liquidity_eth_post(base_transaction_request_aerodrome_remove_liquidity_eth_call_data)

Remove liquidity from a pool on Aerodrome using WETH and another token

This endpoint allows users to remove liquidity from a pool on the Aerodrome
        platform using WETH and another token. Users must specify the token pair, the
        amount of liquidity to remove, minimum amounts for each token, and a deadline
        for the transaction. The operation will ensure the pool exists and will use
        the sender's address if no recipient is specified. The transaction will be
        executed through the Aerodrome Basic Router contract, and the specified amount
        of liquidity will be withdrawn from the pool.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aerodrome_remove_liquidity_eth_call_data import BaseTransactionRequestAerodromeRemoveLiquidityEthCallData
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
    api_instance = compass.api_client.AerodromeBasicApi(api_client)
    base_transaction_request_aerodrome_remove_liquidity_eth_call_data = compass.api_client.BaseTransactionRequestAerodromeRemoveLiquidityEthCallData() # BaseTransactionRequestAerodromeRemoveLiquidityEthCallData | 

    try:
        # Remove liquidity from a pool on Aerodrome using WETH and another token
        api_response = api_instance.process_request_v0_aerodrome_basic_liquidity_provision_remove_liquidity_eth_post(base_transaction_request_aerodrome_remove_liquidity_eth_call_data)
        print("The response of AerodromeBasicApi->process_request_v0_aerodrome_basic_liquidity_provision_remove_liquidity_eth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeBasicApi->process_request_v0_aerodrome_basic_liquidity_provision_remove_liquidity_eth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aerodrome_remove_liquidity_eth_call_data** | [**BaseTransactionRequestAerodromeRemoveLiquidityEthCallData**](BaseTransactionRequestAerodromeRemoveLiquidityEthCallData.md)|  | 

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

# **process_request_v0_aerodrome_basic_liquidity_provision_remove_liquidity_post**
> UnsignedTransaction process_request_v0_aerodrome_basic_liquidity_provision_remove_liquidity_post(base_transaction_request_aerodrome_remove_liquidity_call_data)

Remove liquidity from a pool on Aerodrome

This endpoint allows users to remove liquidity from a specified pool on the
        Aerodrome platform. Users must specify the token pair, the amount of liquidity
        to remove, minimum amounts for each token, and a deadline for the transaction.
        The operation will ensure the pool exists and will use the sender's address if
        no recipient is specified. The transaction will be executed through the
        Aerodrome Basic Router contract, and the specified amount of liquidity will be
        withdrawn from the pool.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aerodrome_remove_liquidity_call_data import BaseTransactionRequestAerodromeRemoveLiquidityCallData
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
    api_instance = compass.api_client.AerodromeBasicApi(api_client)
    base_transaction_request_aerodrome_remove_liquidity_call_data = compass.api_client.BaseTransactionRequestAerodromeRemoveLiquidityCallData() # BaseTransactionRequestAerodromeRemoveLiquidityCallData | 

    try:
        # Remove liquidity from a pool on Aerodrome
        api_response = api_instance.process_request_v0_aerodrome_basic_liquidity_provision_remove_liquidity_post(base_transaction_request_aerodrome_remove_liquidity_call_data)
        print("The response of AerodromeBasicApi->process_request_v0_aerodrome_basic_liquidity_provision_remove_liquidity_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeBasicApi->process_request_v0_aerodrome_basic_liquidity_provision_remove_liquidity_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aerodrome_remove_liquidity_call_data** | [**BaseTransactionRequestAerodromeRemoveLiquidityCallData**](BaseTransactionRequestAerodromeRemoveLiquidityCallData.md)|  | 

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

# **process_request_v0_aerodrome_basic_swap_eth_for_token_post**
> UnsignedTransaction process_request_v0_aerodrome_basic_swap_eth_for_token_post(base_transaction_request_aerodrome_swap_eth_for_token_call_data)

Swap ETH for some of a token on Aerodrome

This endpoint allows you to swap a specified amount of ETH for a
        desired token on the Aerodrome platform. To protect against
        unfavorable exchange rates, you must specify the minimum amount
        of the token you wish to receive. The transaction will only be
        executed if this minimum amount is met, ensuring you do not
        accidentally trade at a disadvantageous rate.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aerodrome_swap_eth_for_token_call_data import BaseTransactionRequestAerodromeSwapEthForTokenCallData
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
    api_instance = compass.api_client.AerodromeBasicApi(api_client)
    base_transaction_request_aerodrome_swap_eth_for_token_call_data = compass.api_client.BaseTransactionRequestAerodromeSwapEthForTokenCallData() # BaseTransactionRequestAerodromeSwapEthForTokenCallData | 

    try:
        # Swap ETH for some of a token on Aerodrome
        api_response = api_instance.process_request_v0_aerodrome_basic_swap_eth_for_token_post(base_transaction_request_aerodrome_swap_eth_for_token_call_data)
        print("The response of AerodromeBasicApi->process_request_v0_aerodrome_basic_swap_eth_for_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeBasicApi->process_request_v0_aerodrome_basic_swap_eth_for_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aerodrome_swap_eth_for_token_call_data** | [**BaseTransactionRequestAerodromeSwapEthForTokenCallData**](BaseTransactionRequestAerodromeSwapEthForTokenCallData.md)|  | 

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

# **process_request_v0_aerodrome_basic_swap_token_for_eth_post**
> UnsignedTransaction process_request_v0_aerodrome_basic_swap_token_for_eth_post(base_transaction_request_aerodrome_swap_token_for_eth_call_data)

Swap a token for ETH on Aerodrome

Swap a specified amount of a token for ETH using the Aerodrome platform.
        To protect against unfavorable exchange rates, you must specify the minimum
        amount of ETH you wish to receive. The transaction will only be executed if
        this minimum amount is met, ensuring you do not trade at a disadvantageous rate.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aerodrome_swap_token_for_eth_call_data import BaseTransactionRequestAerodromeSwapTokenForEthCallData
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
    api_instance = compass.api_client.AerodromeBasicApi(api_client)
    base_transaction_request_aerodrome_swap_token_for_eth_call_data = compass.api_client.BaseTransactionRequestAerodromeSwapTokenForEthCallData() # BaseTransactionRequestAerodromeSwapTokenForEthCallData | 

    try:
        # Swap a token for ETH on Aerodrome
        api_response = api_instance.process_request_v0_aerodrome_basic_swap_token_for_eth_post(base_transaction_request_aerodrome_swap_token_for_eth_call_data)
        print("The response of AerodromeBasicApi->process_request_v0_aerodrome_basic_swap_token_for_eth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeBasicApi->process_request_v0_aerodrome_basic_swap_token_for_eth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aerodrome_swap_token_for_eth_call_data** | [**BaseTransactionRequestAerodromeSwapTokenForEthCallData**](BaseTransactionRequestAerodromeSwapTokenForEthCallData.md)|  | 

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

# **process_request_v0_aerodrome_basic_swap_tokens_post**
> UnsignedTransaction process_request_v0_aerodrome_basic_swap_tokens_post(base_transaction_request_aerodrome_swap_tokens_call_data)

Swap one token for another token on Aerodrome

Swap one token for another on Aerodrome.
        Ensure you specify the minimum amount you expect to receive to
        avoid trading at an unfavorable exchange rate. This endpoint
        facilitates the exchange of tokens by interacting with the
        Aerodrome smart contract, ensuring that the transaction is
        executed only if the specified minimum output is met.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aerodrome_swap_tokens_call_data import BaseTransactionRequestAerodromeSwapTokensCallData
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
    api_instance = compass.api_client.AerodromeBasicApi(api_client)
    base_transaction_request_aerodrome_swap_tokens_call_data = compass.api_client.BaseTransactionRequestAerodromeSwapTokensCallData() # BaseTransactionRequestAerodromeSwapTokensCallData | 

    try:
        # Swap one token for another token on Aerodrome
        api_response = api_instance.process_request_v0_aerodrome_basic_swap_tokens_post(base_transaction_request_aerodrome_swap_tokens_call_data)
        print("The response of AerodromeBasicApi->process_request_v0_aerodrome_basic_swap_tokens_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeBasicApi->process_request_v0_aerodrome_basic_swap_tokens_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aerodrome_swap_tokens_call_data** | [**BaseTransactionRequestAerodromeSwapTokensCallData**](BaseTransactionRequestAerodromeSwapTokensCallData.md)|  | 

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

