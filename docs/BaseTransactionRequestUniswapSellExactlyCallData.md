# BaseTransactionRequestUniswapSellExactlyCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**call_data** | [**UniswapSellExactlyCallData**](UniswapSellExactlyCallData.md) |  | 

## Example

```python
from compass.api_client.models.base_transaction_request_uniswap_sell_exactly_call_data import BaseTransactionRequestUniswapSellExactlyCallData

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTransactionRequestUniswapSellExactlyCallData from a JSON string
base_transaction_request_uniswap_sell_exactly_call_data_instance = BaseTransactionRequestUniswapSellExactlyCallData.from_json(json)
# print the JSON string representation of the object
print(BaseTransactionRequestUniswapSellExactlyCallData.to_json())

# convert the object into a dict
base_transaction_request_uniswap_sell_exactly_call_data_dict = base_transaction_request_uniswap_sell_exactly_call_data_instance.to_dict()
# create an instance of BaseTransactionRequestUniswapSellExactlyCallData from a dict
base_transaction_request_uniswap_sell_exactly_call_data_from_dict = BaseTransactionRequestUniswapSellExactlyCallData.from_dict(base_transaction_request_uniswap_sell_exactly_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


