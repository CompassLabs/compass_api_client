# UnsignedMulticallTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **int** | The chain id of the transaction | 
**data** | **str** | The data of the transaction | 
**var_from** | **str** | The sender of the transaction | 
**gas** | **int** | The gas of the transaction | 
**to** | **str** | The recipient of the transaction | 
**value** | **int** | The value of the transaction | 
**nonce** | **int** | The nonce of the address | 
**max_fee_per_gas** | **int** | The max fee per gas of the transaction | 
**max_priority_fee_per_gas** | **int** | The max priority fee per gas of the transaction | 
**authorization_list** | [**List[SignedAuthorization]**](SignedAuthorization.md) | EIP-7702 authorization | [optional] [default to []]

## Example

```python
from compass.api_client.models.unsigned_multicall_transaction import UnsignedMulticallTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of UnsignedMulticallTransaction from a JSON string
unsigned_multicall_transaction_instance = UnsignedMulticallTransaction.from_json(json)
# print the JSON string representation of the object
print(UnsignedMulticallTransaction.to_json())

# convert the object into a dict
unsigned_multicall_transaction_dict = unsigned_multicall_transaction_instance.to_dict()
# create an instance of UnsignedMulticallTransaction from a dict
unsigned_multicall_transaction_from_dict = UnsignedMulticallTransaction.from_dict(unsigned_multicall_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


