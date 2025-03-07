# BaseTransactionRequestIncreaseErc20AllowanceCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**call_data** | [**IncreaseErc20AllowanceCallData**](IncreaseErc20AllowanceCallData.md) |  | 

## Example

```python
from compass.api_client.models.base_transaction_request_increase_erc20_allowance_call_data import BaseTransactionRequestIncreaseErc20AllowanceCallData

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTransactionRequestIncreaseErc20AllowanceCallData from a JSON string
base_transaction_request_increase_erc20_allowance_call_data_instance = BaseTransactionRequestIncreaseErc20AllowanceCallData.from_json(json)
# print the JSON string representation of the object
print(BaseTransactionRequestIncreaseErc20AllowanceCallData.to_json())

# convert the object into a dict
base_transaction_request_increase_erc20_allowance_call_data_dict = base_transaction_request_increase_erc20_allowance_call_data_instance.to_dict()
# create an instance of BaseTransactionRequestIncreaseErc20AllowanceCallData from a dict
base_transaction_request_increase_erc20_allowance_call_data_from_dict = BaseTransactionRequestIncreaseErc20AllowanceCallData.from_dict(base_transaction_request_increase_erc20_allowance_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


