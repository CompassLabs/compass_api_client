# UniswapLPPositionsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positions** | [**Dict[str, UniswapPosition]**](UniswapPosition.md) | Liquidity provision positions belonging to a particular user. The key is a tuple of the token0, token1, fee, tick_lower, and tick_upper of the position. | 

## Example

```python
from compass.api_client.models.uniswap_lp_positions_info import UniswapLPPositionsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapLPPositionsInfo from a JSON string
uniswap_lp_positions_info_instance = UniswapLPPositionsInfo.from_json(json)
# print the JSON string representation of the object
print(UniswapLPPositionsInfo.to_json())

# convert the object into a dict
uniswap_lp_positions_info_dict = uniswap_lp_positions_info_instance.to_dict()
# create an instance of UniswapLPPositionsInfo from a dict
uniswap_lp_positions_info_from_dict = UniswapLPPositionsInfo.from_dict(uniswap_lp_positions_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


