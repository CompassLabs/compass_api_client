# AaveUserPositionSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_loan_to_value_ratio** | **str** | The loan to value ratio of a user. | 
**health_factor** | **str** | The health factor of a user. If this is above 1 it is safe; below 1 and the         user is in risk of liquidation. This number might be very high (which would mean the user is         safe!) | 
**total_collateral** | **str** | The total collateral (in USD) of a user. | 
**total_debt** | **str** | The total debt (in USD) of a user. | 
**available_borrows** | **str** | The available borrows (in USD) of a user. | 
**liquidation_threshold** | **str** | The liquidation threshold of a user. A user might exceed this due to changing         asset values. | 

## Example

```python
from compass.api_client.models.aave_user_position_summary_response import AaveUserPositionSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AaveUserPositionSummaryResponse from a JSON string
aave_user_position_summary_response_instance = AaveUserPositionSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(AaveUserPositionSummaryResponse.to_json())

# convert the object into a dict
aave_user_position_summary_response_dict = aave_user_position_summary_response_instance.to_dict()
# create an instance of AaveUserPositionSummaryResponse from a dict
aave_user_position_summary_response_from_dict = AaveUserPositionSummaryResponse.from_dict(aave_user_position_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


