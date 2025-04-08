# UnwrapWethRequest

Request model for unwrapping WETH back to native ETH.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount7**](Amount7.md) |  | 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 

## Example

```python
from compass.api_client.models.unwrap_weth_request import UnwrapWethRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnwrapWethRequest from a JSON string
unwrap_weth_request_instance = UnwrapWethRequest.from_json(json)
# print the JSON string representation of the object
print(UnwrapWethRequest.to_json())

# convert the object into a dict
unwrap_weth_request_dict = unwrap_weth_request_instance.to_dict()
# create an instance of UnwrapWethRequest from a dict
unwrap_weth_request_from_dict = UnwrapWethRequest.from_dict(unwrap_weth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


