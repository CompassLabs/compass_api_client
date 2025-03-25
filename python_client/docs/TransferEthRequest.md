# TransferEthRequest

Request model for transferring native ETH.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**amount** | [**Amount6**](Amount6.md) |  | 
**to** | **str** | The recipient of the ETH. | 

## Example

```python
from compass.api_client.models.transfer_eth_request import TransferEthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferEthRequest from a JSON string
transfer_eth_request_instance = TransferEthRequest.from_json(json)
# print the JSON string representation of the object
print(TransferEthRequest.to_json())

# convert the object into a dict
transfer_eth_request_dict = transfer_eth_request_instance.to_dict()
# create an instance of TransferEthRequest from a dict
transfer_eth_request_from_dict = TransferEthRequest.from_dict(transfer_eth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


