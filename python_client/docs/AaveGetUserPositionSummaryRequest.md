# AaveGetUserPositionSummaryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**user** | **str** | The user to get the position summary of. Values are in USD. | 

## Example

```python
from compass.api_client.models.aave_get_user_position_summary_request import AaveGetUserPositionSummaryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AaveGetUserPositionSummaryRequest from a JSON string
aave_get_user_position_summary_request_instance = AaveGetUserPositionSummaryRequest.from_json(json)
# print the JSON string representation of the object
print(AaveGetUserPositionSummaryRequest.to_json())

# convert the object into a dict
aave_get_user_position_summary_request_dict = aave_get_user_position_summary_request_instance.to_dict()
# create an instance of AaveGetUserPositionSummaryRequest from a dict
aave_get_user_position_summary_request_from_dict = AaveGetUserPositionSummaryRequest.from_dict(aave_get_user_position_summary_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


