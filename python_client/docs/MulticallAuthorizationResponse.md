# MulticallAuthorizationResponse

Response model for multicall authorization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **int** | A unique nonce value for this authorization | 
**address** | **str** | The Ethereum address authorized for multicall | 
**chain_id** | **int** | The chain ID for the blockchain network | 

## Example

```python
from compass.api_client.models.multicall_authorization_response import MulticallAuthorizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MulticallAuthorizationResponse from a JSON string
multicall_authorization_response_instance = MulticallAuthorizationResponse.from_json(json)
# print the JSON string representation of the object
print(MulticallAuthorizationResponse.to_json())

# convert the object into a dict
multicall_authorization_response_dict = multicall_authorization_response_instance.to_dict()
# create an instance of MulticallAuthorizationResponse from a dict
multicall_authorization_response_from_dict = MulticallAuthorizationResponse.from_dict(multicall_authorization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


