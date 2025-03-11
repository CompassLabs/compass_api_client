# BaseTransactionRequestIncreaseErc20AllowanceAnyCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**call_data** | [**IncreaseErc20AllowanceAnyCallData**](IncreaseErc20AllowanceAnyCallData.md) |  | 

## Example

```python
from compass.api_client.models.base_transaction_request_increase_erc20_allowance_any_call_data import BaseTransactionRequestIncreaseErc20AllowanceAnyCallData

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTransactionRequestIncreaseErc20AllowanceAnyCallData from a JSON string
base_transaction_request_increase_erc20_allowance_any_call_data_instance = BaseTransactionRequestIncreaseErc20AllowanceAnyCallData.from_json(json)
# print the JSON string representation of the object
print(BaseTransactionRequestIncreaseErc20AllowanceAnyCallData.to_json())

# convert the object into a dict
base_transaction_request_increase_erc20_allowance_any_call_data_dict = base_transaction_request_increase_erc20_allowance_any_call_data_instance.to_dict()
# create an instance of BaseTransactionRequestIncreaseErc20AllowanceAnyCallData from a dict
base_transaction_request_increase_erc20_allowance_any_call_data_from_dict = BaseTransactionRequestIncreaseErc20AllowanceAnyCallData.from_dict(base_transaction_request_increase_erc20_allowance_any_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


