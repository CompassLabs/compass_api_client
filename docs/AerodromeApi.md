# compass.api_client.AerodromeApi

All URIs are relative to *https://api.compasslabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_request_v0_aerodrome_liquidity_provision_add_liquidity_eth_post**](AerodromeApi.md#process_request_v0_aerodrome_liquidity_provision_add_liquidity_eth_post) | **POST** /v0/aerodrome/liquidity_provision/add_liquidity_eth | Provide liquidity to a pool on Aerodrome using WETH and another token
[**process_request_v0_aerodrome_liquidity_provision_add_liquidity_post**](AerodromeApi.md#process_request_v0_aerodrome_liquidity_provision_add_liquidity_post) | **POST** /v0/aerodrome/liquidity_provision/add_liquidity | Provide liquidity to a pool on Aerodrome
[**process_request_v0_aerodrome_liquidity_provision_remove_liquidity_eth_post**](AerodromeApi.md#process_request_v0_aerodrome_liquidity_provision_remove_liquidity_eth_post) | **POST** /v0/aerodrome/liquidity_provision/remove_liquidity_eth | Remove liquidity from a pool on Aerodrome using WETH and another token
[**process_request_v0_aerodrome_liquidity_provision_remove_liquidity_post**](AerodromeApi.md#process_request_v0_aerodrome_liquidity_provision_remove_liquidity_post) | **POST** /v0/aerodrome/liquidity_provision/remove_liquidity | Remove liquidity from a pool on Aerodrome
[**process_request_v0_aerodrome_swap_eth_for_token_post**](AerodromeApi.md#process_request_v0_aerodrome_swap_eth_for_token_post) | **POST** /v0/aerodrome/swap/eth_for_token | Swap ETH for some of a token on Aerodrome
[**process_request_v0_aerodrome_swap_token_for_eth_post**](AerodromeApi.md#process_request_v0_aerodrome_swap_token_for_eth_post) | **POST** /v0/aerodrome/swap/token_for_eth | Swap a token for ETH on Aerodrome
[**process_request_v0_aerodrome_swap_tokens_post**](AerodromeApi.md#process_request_v0_aerodrome_swap_tokens_post) | **POST** /v0/aerodrome/swap/tokens | Swap one token for another token on Aerodrome


# **process_request_v0_aerodrome_liquidity_provision_add_liquidity_eth_post**
> UnsignedTransaction process_request_v0_aerodrome_liquidity_provision_add_liquidity_eth_post(base_transaction_request_aero_liquidity_provision_eth_call_data)

Provide liquidity to a pool on Aerodrome using WETH and another token

Provide liquidity to a pool.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aero_liquidity_provision_eth_call_data import BaseTransactionRequestAeroLiquidityProvisionEthCallData
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
    api_instance = compass.api_client.AerodromeApi(api_client)
    base_transaction_request_aero_liquidity_provision_eth_call_data = compass.api_client.BaseTransactionRequestAeroLiquidityProvisionEthCallData() # BaseTransactionRequestAeroLiquidityProvisionEthCallData | 

    try:
        # Provide liquidity to a pool on Aerodrome using WETH and another token
        api_response = api_instance.process_request_v0_aerodrome_liquidity_provision_add_liquidity_eth_post(base_transaction_request_aero_liquidity_provision_eth_call_data)
        print("The response of AerodromeApi->process_request_v0_aerodrome_liquidity_provision_add_liquidity_eth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeApi->process_request_v0_aerodrome_liquidity_provision_add_liquidity_eth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aero_liquidity_provision_eth_call_data** | [**BaseTransactionRequestAeroLiquidityProvisionEthCallData**](BaseTransactionRequestAeroLiquidityProvisionEthCallData.md)|  | 

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

# **process_request_v0_aerodrome_liquidity_provision_add_liquidity_post**
> UnsignedTransaction process_request_v0_aerodrome_liquidity_provision_add_liquidity_post(base_transaction_request_aero_liquidity_provision_call_data)

Provide liquidity to a pool on Aerodrome

Provide liquidity to a pool.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aero_liquidity_provision_call_data import BaseTransactionRequestAeroLiquidityProvisionCallData
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
    api_instance = compass.api_client.AerodromeApi(api_client)
    base_transaction_request_aero_liquidity_provision_call_data = compass.api_client.BaseTransactionRequestAeroLiquidityProvisionCallData() # BaseTransactionRequestAeroLiquidityProvisionCallData | 

    try:
        # Provide liquidity to a pool on Aerodrome
        api_response = api_instance.process_request_v0_aerodrome_liquidity_provision_add_liquidity_post(base_transaction_request_aero_liquidity_provision_call_data)
        print("The response of AerodromeApi->process_request_v0_aerodrome_liquidity_provision_add_liquidity_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeApi->process_request_v0_aerodrome_liquidity_provision_add_liquidity_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aero_liquidity_provision_call_data** | [**BaseTransactionRequestAeroLiquidityProvisionCallData**](BaseTransactionRequestAeroLiquidityProvisionCallData.md)|  | 

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

# **process_request_v0_aerodrome_liquidity_provision_remove_liquidity_eth_post**
> UnsignedTransaction process_request_v0_aerodrome_liquidity_provision_remove_liquidity_eth_post(base_transaction_request_aero_remove_liquidity_eth_call_data)

Remove liquidity from a pool on Aerodrome using WETH and another token

Remove liquidity from a pool.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aero_remove_liquidity_eth_call_data import BaseTransactionRequestAeroRemoveLiquidityEthCallData
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
    api_instance = compass.api_client.AerodromeApi(api_client)
    base_transaction_request_aero_remove_liquidity_eth_call_data = compass.api_client.BaseTransactionRequestAeroRemoveLiquidityEthCallData() # BaseTransactionRequestAeroRemoveLiquidityEthCallData | 

    try:
        # Remove liquidity from a pool on Aerodrome using WETH and another token
        api_response = api_instance.process_request_v0_aerodrome_liquidity_provision_remove_liquidity_eth_post(base_transaction_request_aero_remove_liquidity_eth_call_data)
        print("The response of AerodromeApi->process_request_v0_aerodrome_liquidity_provision_remove_liquidity_eth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeApi->process_request_v0_aerodrome_liquidity_provision_remove_liquidity_eth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aero_remove_liquidity_eth_call_data** | [**BaseTransactionRequestAeroRemoveLiquidityEthCallData**](BaseTransactionRequestAeroRemoveLiquidityEthCallData.md)|  | 

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

# **process_request_v0_aerodrome_liquidity_provision_remove_liquidity_post**
> UnsignedTransaction process_request_v0_aerodrome_liquidity_provision_remove_liquidity_post(base_transaction_request_aero_remove_liquidity_call_data)

Remove liquidity from a pool on Aerodrome

Remove liquidity from a pool.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aero_remove_liquidity_call_data import BaseTransactionRequestAeroRemoveLiquidityCallData
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
    api_instance = compass.api_client.AerodromeApi(api_client)
    base_transaction_request_aero_remove_liquidity_call_data = compass.api_client.BaseTransactionRequestAeroRemoveLiquidityCallData() # BaseTransactionRequestAeroRemoveLiquidityCallData | 

    try:
        # Remove liquidity from a pool on Aerodrome
        api_response = api_instance.process_request_v0_aerodrome_liquidity_provision_remove_liquidity_post(base_transaction_request_aero_remove_liquidity_call_data)
        print("The response of AerodromeApi->process_request_v0_aerodrome_liquidity_provision_remove_liquidity_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeApi->process_request_v0_aerodrome_liquidity_provision_remove_liquidity_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aero_remove_liquidity_call_data** | [**BaseTransactionRequestAeroRemoveLiquidityCallData**](BaseTransactionRequestAeroRemoveLiquidityCallData.md)|  | 

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

# **process_request_v0_aerodrome_swap_eth_for_token_post**
> UnsignedTransaction process_request_v0_aerodrome_swap_eth_for_token_post(base_transaction_request_aero_swap_eth_for_token_call_data)

Swap ETH for some of a token on Aerodrome

Swap some quantity of ETH for some quantity of token. Specify the minimum amount you need to receive to make sure you don't accidentally trade at a bad exchange rate.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aero_swap_eth_for_token_call_data import BaseTransactionRequestAeroSwapEthForTokenCallData
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
    api_instance = compass.api_client.AerodromeApi(api_client)
    base_transaction_request_aero_swap_eth_for_token_call_data = compass.api_client.BaseTransactionRequestAeroSwapEthForTokenCallData() # BaseTransactionRequestAeroSwapEthForTokenCallData | 

    try:
        # Swap ETH for some of a token on Aerodrome
        api_response = api_instance.process_request_v0_aerodrome_swap_eth_for_token_post(base_transaction_request_aero_swap_eth_for_token_call_data)
        print("The response of AerodromeApi->process_request_v0_aerodrome_swap_eth_for_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeApi->process_request_v0_aerodrome_swap_eth_for_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aero_swap_eth_for_token_call_data** | [**BaseTransactionRequestAeroSwapEthForTokenCallData**](BaseTransactionRequestAeroSwapEthForTokenCallData.md)|  | 

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

# **process_request_v0_aerodrome_swap_token_for_eth_post**
> UnsignedTransaction process_request_v0_aerodrome_swap_token_for_eth_post(base_transaction_request_aero_swap_token_for_eth_call_data)

Swap a token for ETH on Aerodrome

Swap some of a token for ETH. Specify the minimum amount you need to receive to make sure you don't accidentally trade at a bad exchange rate.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aero_swap_token_for_eth_call_data import BaseTransactionRequestAeroSwapTokenForEthCallData
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
    api_instance = compass.api_client.AerodromeApi(api_client)
    base_transaction_request_aero_swap_token_for_eth_call_data = compass.api_client.BaseTransactionRequestAeroSwapTokenForEthCallData() # BaseTransactionRequestAeroSwapTokenForEthCallData | 

    try:
        # Swap a token for ETH on Aerodrome
        api_response = api_instance.process_request_v0_aerodrome_swap_token_for_eth_post(base_transaction_request_aero_swap_token_for_eth_call_data)
        print("The response of AerodromeApi->process_request_v0_aerodrome_swap_token_for_eth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeApi->process_request_v0_aerodrome_swap_token_for_eth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aero_swap_token_for_eth_call_data** | [**BaseTransactionRequestAeroSwapTokenForEthCallData**](BaseTransactionRequestAeroSwapTokenForEthCallData.md)|  | 

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

# **process_request_v0_aerodrome_swap_tokens_post**
> UnsignedTransaction process_request_v0_aerodrome_swap_tokens_post(base_transaction_request_aero_swap_tokens_call_data)

Swap one token for another token on Aerodrome

Swap one token for another. Specify the minimum amount you need to receive to make sure you don't accidentally trade at a bad exchange rate.

### Example


```python
import compass.api_client
from compass.api_client.models.base_transaction_request_aero_swap_tokens_call_data import BaseTransactionRequestAeroSwapTokensCallData
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
    api_instance = compass.api_client.AerodromeApi(api_client)
    base_transaction_request_aero_swap_tokens_call_data = compass.api_client.BaseTransactionRequestAeroSwapTokensCallData() # BaseTransactionRequestAeroSwapTokensCallData | 

    try:
        # Swap one token for another token on Aerodrome
        api_response = api_instance.process_request_v0_aerodrome_swap_tokens_post(base_transaction_request_aero_swap_tokens_call_data)
        print("The response of AerodromeApi->process_request_v0_aerodrome_swap_tokens_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AerodromeApi->process_request_v0_aerodrome_swap_tokens_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_transaction_request_aero_swap_tokens_call_data** | [**BaseTransactionRequestAeroSwapTokensCallData**](BaseTransactionRequestAeroSwapTokensCallData.md)|  | 

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

