# BaseTransactionRequestAerodromeSwapTokenForEthCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**call_data** | [**AerodromeSwapTokenForEthCallData**](AerodromeSwapTokenForEthCallData.md) |  | 

## Example

```python
from compass.api_client.models.base_transaction_request_aerodrome_swap_token_for_eth_call_data import BaseTransactionRequestAerodromeSwapTokenForEthCallData

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTransactionRequestAerodromeSwapTokenForEthCallData from a JSON string
base_transaction_request_aerodrome_swap_token_for_eth_call_data_instance = BaseTransactionRequestAerodromeSwapTokenForEthCallData.from_json(json)
# print the JSON string representation of the object
print(BaseTransactionRequestAerodromeSwapTokenForEthCallData.to_json())

# convert the object into a dict
base_transaction_request_aerodrome_swap_token_for_eth_call_data_dict = base_transaction_request_aerodrome_swap_token_for_eth_call_data_instance.to_dict()
# create an instance of BaseTransactionRequestAerodromeSwapTokenForEthCallData from a dict
base_transaction_request_aerodrome_swap_token_for_eth_call_data_from_dict = BaseTransactionRequestAerodromeSwapTokenForEthCallData.from_dict(base_transaction_request_aerodrome_swap_token_for_eth_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


