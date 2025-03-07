# BaseTransactionRequestUnwrapWethRequestCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**call_data** | [**UnwrapWethRequestCallData**](UnwrapWethRequestCallData.md) |  | 

## Example

```python
from compass.api_client.models.base_transaction_request_unwrap_weth_request_call_data import BaseTransactionRequestUnwrapWethRequestCallData

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTransactionRequestUnwrapWethRequestCallData from a JSON string
base_transaction_request_unwrap_weth_request_call_data_instance = BaseTransactionRequestUnwrapWethRequestCallData.from_json(json)
# print the JSON string representation of the object
print(BaseTransactionRequestUnwrapWethRequestCallData.to_json())

# convert the object into a dict
base_transaction_request_unwrap_weth_request_call_data_dict = base_transaction_request_unwrap_weth_request_call_data_instance.to_dict()
# create an instance of BaseTransactionRequestUnwrapWethRequestCallData from a dict
base_transaction_request_unwrap_weth_request_call_data_from_dict = BaseTransactionRequestUnwrapWethRequestCallData.from_dict(base_transaction_request_unwrap_weth_request_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


