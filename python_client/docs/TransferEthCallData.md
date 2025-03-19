# TransferEthCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount6**](Amount6.md) |  | 
**to** | **str** | The recipient of the ETH. | 

## Example

```python
from compass.api_client.models.transfer_eth_call_data import TransferEthCallData

# TODO update the JSON string below
json = "{}"
# create an instance of TransferEthCallData from a JSON string
transfer_eth_call_data_instance = TransferEthCallData.from_json(json)
# print the JSON string representation of the object
print(TransferEthCallData.to_json())

# convert the object into a dict
transfer_eth_call_data_dict = transfer_eth_call_data_instance.to_dict()
# create an instance of TransferEthCallData from a dict
transfer_eth_call_data_from_dict = TransferEthCallData.from_dict(transfer_eth_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


