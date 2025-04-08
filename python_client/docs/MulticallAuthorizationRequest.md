# MulticallAuthorizationRequest

Request model for getting a multicall authorization.  This model is used to authorize a sender address to perform multicall operations, allowing it to call multiple functions on multiple contracts in a single transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) | The blockchain network to use | 
**sender** | **str** | The Ethereum address to use for authorization | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']
**address** | **str** | The Ethereum address to authorize for multicall | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']

## Example

```python
from compass.api_client.models.multicall_authorization_request import MulticallAuthorizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MulticallAuthorizationRequest from a JSON string
multicall_authorization_request_instance = MulticallAuthorizationRequest.from_json(json)
# print the JSON string representation of the object
print(MulticallAuthorizationRequest.to_json())

# convert the object into a dict
multicall_authorization_request_dict = multicall_authorization_request_instance.to_dict()
# create an instance of MulticallAuthorizationRequest from a dict
multicall_authorization_request_from_dict = MulticallAuthorizationRequest.from_dict(multicall_authorization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


