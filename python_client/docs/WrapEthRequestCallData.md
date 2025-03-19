# WrapEthRequestCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount8**](Amount8.md) |  | 

## Example

```python
from compass.api_client.models.wrap_eth_request_call_data import WrapEthRequestCallData

# TODO update the JSON string below
json = "{}"
# create an instance of WrapEthRequestCallData from a JSON string
wrap_eth_request_call_data_instance = WrapEthRequestCallData.from_json(json)
# print the JSON string representation of the object
print(WrapEthRequestCallData.to_json())

# convert the object into a dict
wrap_eth_request_call_data_dict = wrap_eth_request_call_data_instance.to_dict()
# create an instance of WrapEthRequestCallData from a dict
wrap_eth_request_call_data_from_dict = WrapEthRequestCallData.from_dict(wrap_eth_request_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


