# CompassApiBackendModelsUniswapResponsePosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **int** |  | 
**operator** | **str** |  | 
**token0** | [**Token**](Token.md) |  | 
**token1** | [**Token**](Token.md) |  | 
**fee** | [**FeeEnum**](FeeEnum.md) |  | 
**tick_lower** | **int** |  | 
**tick_upper** | **int** |  | 
**liquidity** | **int** |  | 
**fee_growth_inside0_last_x128** | **int** |  | 
**fee_growth_inside1_last_x128** | **int** |  | 
**tokens_owed0** | **int** |  | 
**tokens_owed1** | **int** |  | 
**token_id** | **int** |  | 

## Example

```python
from compass.api_client.models.compass_api_backend_models_uniswap_response_position import CompassApiBackendModelsUniswapResponsePosition

# TODO update the JSON string below
json = "{}"
# create an instance of CompassApiBackendModelsUniswapResponsePosition from a JSON string
compass_api_backend_models_uniswap_response_position_instance = CompassApiBackendModelsUniswapResponsePosition.from_json(json)
# print the JSON string representation of the object
print(CompassApiBackendModelsUniswapResponsePosition.to_json())

# convert the object into a dict
compass_api_backend_models_uniswap_response_position_dict = compass_api_backend_models_uniswap_response_position_instance.to_dict()
# create an instance of CompassApiBackendModelsUniswapResponsePosition from a dict
compass_api_backend_models_uniswap_response_position_from_dict = CompassApiBackendModelsUniswapResponsePosition.from_dict(compass_api_backend_models_uniswap_response_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


