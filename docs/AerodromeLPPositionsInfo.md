# AerodromeLPPositionsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positions** | [**Dict[str, AerodromePosition]**](AerodromePosition.md) | Liquidity provision positions belonging to a particular user. The key is a tuple of the token0, token1, tick_spacing, tick_lower, and tick_upper of the position. | 

## Example

```python
from compass.api_client.models.aerodrome_lp_positions_info import AerodromeLPPositionsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeLPPositionsInfo from a JSON string
aerodrome_lp_positions_info_instance = AerodromeLPPositionsInfo.from_json(json)
# print the JSON string representation of the object
print(AerodromeLPPositionsInfo.to_json())

# convert the object into a dict
aerodrome_lp_positions_info_dict = aerodrome_lp_positions_info_instance.to_dict()
# create an instance of AerodromeLPPositionsInfo from a dict
aerodrome_lp_positions_info_from_dict = AerodromeLPPositionsInfo.from_dict(aerodrome_lp_positions_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


