# CompassApiBackendModelsUniswapResponseLPPositionsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positions** | [**Dict[str, CompassApiBackendModelsUniswapResponsePosition]**](CompassApiBackendModelsUniswapResponsePosition.md) | Liquidity provision positions belonging to a particular user. The key is a tuple of the token0, token1, fee, tick_lower, and tick_upper of the position. | 

## Example

```python
from compass.api_client.models.compass_api_backend_models_uniswap_response_lp_positions_info import CompassApiBackendModelsUniswapResponseLPPositionsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CompassApiBackendModelsUniswapResponseLPPositionsInfo from a JSON string
compass_api_backend_models_uniswap_response_lp_positions_info_instance = CompassApiBackendModelsUniswapResponseLPPositionsInfo.from_json(json)
# print the JSON string representation of the object
print(CompassApiBackendModelsUniswapResponseLPPositionsInfo.to_json())

# convert the object into a dict
compass_api_backend_models_uniswap_response_lp_positions_info_dict = compass_api_backend_models_uniswap_response_lp_positions_info_instance.to_dict()
# create an instance of CompassApiBackendModelsUniswapResponseLPPositionsInfo from a dict
compass_api_backend_models_uniswap_response_lp_positions_info_from_dict = CompassApiBackendModelsUniswapResponseLPPositionsInfo.from_dict(compass_api_backend_models_uniswap_response_lp_positions_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


