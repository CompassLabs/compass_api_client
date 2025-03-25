# WrapEthRequest

Request model for wrapping ETH into WETH.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**amount** | [**Amount8**](Amount8.md) |  | 

## Example

```python
from compass.api_client.models.wrap_eth_request import WrapEthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WrapEthRequest from a JSON string
wrap_eth_request_instance = WrapEthRequest.from_json(json)
# print the JSON string representation of the object
print(WrapEthRequest.to_json())

# convert the object into a dict
wrap_eth_request_dict = wrap_eth_request_instance.to_dict()
# create an instance of WrapEthRequest from a dict
wrap_eth_request_from_dict = WrapEthRequest.from_dict(wrap_eth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


