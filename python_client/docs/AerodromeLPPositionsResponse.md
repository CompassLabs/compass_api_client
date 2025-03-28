# AerodromeLPPositionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positions** | [**Dict[str, AerodromePosition]**](AerodromePosition.md) | Liquidity provision positions belonging to a particular user. The key is a tuple of the token0, token1, tick_spacing, tick_lower, and tick_upper of the position. | 

## Example

```python
from compass.api_client.models.aerodrome_lp_positions_response import AerodromeLPPositionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeLPPositionsResponse from a JSON string
aerodrome_lp_positions_response_instance = AerodromeLPPositionsResponse.from_json(json)
# print the JSON string representation of the object
print(AerodromeLPPositionsResponse.to_json())

# convert the object into a dict
aerodrome_lp_positions_response_dict = aerodrome_lp_positions_response_instance.to_dict()
# create an instance of AerodromeLPPositionsResponse from a dict
aerodrome_lp_positions_response_from_dict = AerodromeLPPositionsResponse.from_dict(aerodrome_lp_positions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


