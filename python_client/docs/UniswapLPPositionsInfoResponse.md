# UniswapLPPositionsInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positions** | [**Dict[str, UniswapPositionsSolidityResponse]**](UniswapPositionsSolidityResponse.md) |  Liquidity provision positions belonging to a particular user keyed by the         token of owner index of the position.  | 

## Example

```python
from compass.api_client.models.uniswap_lp_positions_info_response import UniswapLPPositionsInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapLPPositionsInfoResponse from a JSON string
uniswap_lp_positions_info_response_instance = UniswapLPPositionsInfoResponse.from_json(json)
# print the JSON string representation of the object
print(UniswapLPPositionsInfoResponse.to_json())

# convert the object into a dict
uniswap_lp_positions_info_response_dict = uniswap_lp_positions_info_response_instance.to_dict()
# create an instance of UniswapLPPositionsInfoResponse from a dict
uniswap_lp_positions_info_response_from_dict = UniswapLPPositionsInfoResponse.from_dict(uniswap_lp_positions_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


