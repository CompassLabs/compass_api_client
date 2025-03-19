# UnwrapWethRequestCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount7**](Amount7.md) |  | 

## Example

```python
from compass.api_client.models.unwrap_weth_request_call_data import UnwrapWethRequestCallData

# TODO update the JSON string below
json = "{}"
# create an instance of UnwrapWethRequestCallData from a JSON string
unwrap_weth_request_call_data_instance = UnwrapWethRequestCallData.from_json(json)
# print the JSON string representation of the object
print(UnwrapWethRequestCallData.to_json())

# convert the object into a dict
unwrap_weth_request_call_data_dict = unwrap_weth_request_call_data_instance.to_dict()
# create an instance of UnwrapWethRequestCallData from a dict
unwrap_weth_request_call_data_from_dict = UnwrapWethRequestCallData.from_dict(unwrap_weth_request_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


