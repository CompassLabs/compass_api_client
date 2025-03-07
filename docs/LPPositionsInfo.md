# LPPositionsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positions** | [**Dict[str, Position]**](Position.md) | Liquidity provision positions belonging to a particular user. The key is a tuple of the token0, token1, fee, tick_lower, and tick_upper of the position. | 

## Example

```python
from compass.api_client.models.lp_positions_info import LPPositionsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LPPositionsInfo from a JSON string
lp_positions_info_instance = LPPositionsInfo.from_json(json)
# print the JSON string representation of the object
print(LPPositionsInfo.to_json())

# convert the object into a dict
lp_positions_info_dict = lp_positions_info_instance.to_dict()
# create an instance of LPPositionsInfo from a dict
lp_positions_info_from_dict = LPPositionsInfo.from_dict(lp_positions_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


