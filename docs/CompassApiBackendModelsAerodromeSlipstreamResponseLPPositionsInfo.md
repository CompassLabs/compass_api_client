# CompassApiBackendModelsAerodromeSlipstreamResponseLPPositionsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positions** | [**Dict[str, CompassApiBackendModelsAerodromeSlipstreamResponsePosition]**](CompassApiBackendModelsAerodromeSlipstreamResponsePosition.md) | Liquidity provision positions belonging to a particular user. The key is a tuple of the token0, token1, tick_spacing, tick_lower, and tick_upper of the position. | 

## Example

```python
from compass.api_client.models.compass_api_backend_models_aerodrome_slipstream_response_lp_positions_info import CompassApiBackendModelsAerodromeSlipstreamResponseLPPositionsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CompassApiBackendModelsAerodromeSlipstreamResponseLPPositionsInfo from a JSON string
compass_api_backend_models_aerodrome_slipstream_response_lp_positions_info_instance = CompassApiBackendModelsAerodromeSlipstreamResponseLPPositionsInfo.from_json(json)
# print the JSON string representation of the object
print(CompassApiBackendModelsAerodromeSlipstreamResponseLPPositionsInfo.to_json())

# convert the object into a dict
compass_api_backend_models_aerodrome_slipstream_response_lp_positions_info_dict = compass_api_backend_models_aerodrome_slipstream_response_lp_positions_info_instance.to_dict()
# create an instance of CompassApiBackendModelsAerodromeSlipstreamResponseLPPositionsInfo from a dict
compass_api_backend_models_aerodrome_slipstream_response_lp_positions_info_from_dict = CompassApiBackendModelsAerodromeSlipstreamResponseLPPositionsInfo.from_dict(compass_api_backend_models_aerodrome_slipstream_response_lp_positions_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


