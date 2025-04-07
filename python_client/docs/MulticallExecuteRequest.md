# MulticallExecuteRequest

Request model for executing a multicall.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**signed_authorization** | [**SignedAuthorization**](SignedAuthorization.md) |  | 
**contract_address** | **str** | The address of the multicall contract | 
**actions** | [**List[MulticallAction]**](MulticallAction.md) | List of possible actions for multicall | 

## Example

```python
from compass.api_client.models.multicall_execute_request import MulticallExecuteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MulticallExecuteRequest from a JSON string
multicall_execute_request_instance = MulticallExecuteRequest.from_json(json)
# print the JSON string representation of the object
print(MulticallExecuteRequest.to_json())

# convert the object into a dict
multicall_execute_request_dict = multicall_execute_request_instance.to_dict()
# create an instance of MulticallExecuteRequest from a dict
multicall_execute_request_from_dict = MulticallExecuteRequest.from_dict(multicall_execute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


