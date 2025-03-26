# AaveGetLiquidityChangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**start_block** | **int** | The starting block. | 
**end_block** | **int** |  | [optional] 
**asset** | [**Token**](Token.md) | The symbol of the asset to fetch liquidity index change for.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 

## Example

```python
from compass.api_client.models.aave_get_liquidity_change_request import AaveGetLiquidityChangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AaveGetLiquidityChangeRequest from a JSON string
aave_get_liquidity_change_request_instance = AaveGetLiquidityChangeRequest.from_json(json)
# print the JSON string representation of the object
print(AaveGetLiquidityChangeRequest.to_json())

# convert the object into a dict
aave_get_liquidity_change_request_dict = aave_get_liquidity_change_request_instance.to_dict()
# create an instance of AaveGetLiquidityChangeRequest from a dict
aave_get_liquidity_change_request_from_dict = AaveGetLiquidityChangeRequest.from_dict(aave_get_liquidity_change_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


