# MulticallAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**MulticallActionType**](MulticallActionType.md) |  | 
**body** | [**Body**](Body.md) |  | 

## Example

```python
from compass.api_client.models.multicall_action import MulticallAction

# TODO update the JSON string below
json = "{}"
# create an instance of MulticallAction from a JSON string
multicall_action_instance = MulticallAction.from_json(json)
# print the JSON string representation of the object
print(MulticallAction.to_json())

# convert the object into a dict
multicall_action_dict = multicall_action_instance.to_dict()
# create an instance of MulticallAction from a dict
multicall_action_from_dict = MulticallAction.from_dict(multicall_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


