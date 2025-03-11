# BaseTransactionRequestUniswapBuyExactlyCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**call_data** | [**UniswapBuyExactlyCallData**](UniswapBuyExactlyCallData.md) |  | 

## Example

```python
from compass.api_client.models.base_transaction_request_uniswap_buy_exactly_call_data import BaseTransactionRequestUniswapBuyExactlyCallData

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTransactionRequestUniswapBuyExactlyCallData from a JSON string
base_transaction_request_uniswap_buy_exactly_call_data_instance = BaseTransactionRequestUniswapBuyExactlyCallData.from_json(json)
# print the JSON string representation of the object
print(BaseTransactionRequestUniswapBuyExactlyCallData.to_json())

# convert the object into a dict
base_transaction_request_uniswap_buy_exactly_call_data_dict = base_transaction_request_uniswap_buy_exactly_call_data_instance.to_dict()
# create an instance of BaseTransactionRequestUniswapBuyExactlyCallData from a dict
base_transaction_request_uniswap_buy_exactly_call_data_from_dict = BaseTransactionRequestUniswapBuyExactlyCallData.from_dict(base_transaction_request_uniswap_buy_exactly_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


