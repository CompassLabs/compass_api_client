# AaveGetUserPositionSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**user** | **str** | The user to get the position summary of. Values are in USD. | 

## Example

```python
from compass.api_client.models.aave_get_user_position_summary import AaveGetUserPositionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AaveGetUserPositionSummary from a JSON string
aave_get_user_position_summary_instance = AaveGetUserPositionSummary.from_json(json)
# print the JSON string representation of the object
print(AaveGetUserPositionSummary.to_json())

# convert the object into a dict
aave_get_user_position_summary_dict = aave_get_user_position_summary_instance.to_dict()
# create an instance of AaveGetUserPositionSummary from a dict
aave_get_user_position_summary_from_dict = AaveGetUserPositionSummary.from_dict(aave_get_user_position_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


