# AaveLiquidityChangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**liquidity_change** | **str** | The change in the liqudiity index between the two times, expressed as a percentage. | 
**start_time** | **datetime** | Dateime of starting block | 
**end_time** | **datetime** | Dateime of ending block | 

## Example

```python
from compass.api_client.models.aave_liquidity_change_response import AaveLiquidityChangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AaveLiquidityChangeResponse from a JSON string
aave_liquidity_change_response_instance = AaveLiquidityChangeResponse.from_json(json)
# print the JSON string representation of the object
print(AaveLiquidityChangeResponse.to_json())

# convert the object into a dict
aave_liquidity_change_response_dict = aave_liquidity_change_response_instance.to_dict()
# create an instance of AaveLiquidityChangeResponse from a dict
aave_liquidity_change_response_from_dict = AaveLiquidityChangeResponse.from_dict(aave_liquidity_change_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


