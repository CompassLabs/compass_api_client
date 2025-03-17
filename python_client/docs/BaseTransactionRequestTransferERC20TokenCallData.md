# BaseTransactionRequestTransferERC20TokenCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**call_data** | [**TransferERC20TokenCallData**](TransferERC20TokenCallData.md) |  | 

## Example

```python
from compass.api_client.models.base_transaction_request_transfer_erc20_token_call_data import BaseTransactionRequestTransferERC20TokenCallData

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTransactionRequestTransferERC20TokenCallData from a JSON string
base_transaction_request_transfer_erc20_token_call_data_instance = BaseTransactionRequestTransferERC20TokenCallData.from_json(json)
# print the JSON string representation of the object
print(BaseTransactionRequestTransferERC20TokenCallData.to_json())

# convert the object into a dict
base_transaction_request_transfer_erc20_token_call_data_dict = base_transaction_request_transfer_erc20_token_call_data_instance.to_dict()
# create an instance of BaseTransactionRequestTransferERC20TokenCallData from a dict
base_transaction_request_transfer_erc20_token_call_data_from_dict = BaseTransactionRequestTransferERC20TokenCallData.from_dict(base_transaction_request_transfer_erc20_token_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


