# AerodromeRemoveLiquidityCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_a** | [**Token**](Token.md) | The symbol of the token to remove liquidity for&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**token_b** | [**Token**](Token.md) | The symbol of the token to remove liquidity for&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**stable** | **bool** | If true, try to remove liquidity from a stable pool with a bonding curve of K&#x3D;x^3y+y^3x. If false, try to remove liquidity from a volatile pool with a bonding curve of K&#x3D;xy | 
**liquidity** | [**Liquidity**](Liquidity.md) |  | 
**amount_a_min** | [**AmountAMin1**](AmountAMin1.md) |  | 
**amount_b_min** | [**AmountBMin1**](AmountBMin1.md) |  | 
**to** | **str** |  | [optional] 
**deadline** | **int** |  | 

## Example

```python
from compass.api_client.models.aerodrome_remove_liquidity_call_data import AerodromeRemoveLiquidityCallData

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeRemoveLiquidityCallData from a JSON string
aerodrome_remove_liquidity_call_data_instance = AerodromeRemoveLiquidityCallData.from_json(json)
# print the JSON string representation of the object
print(AerodromeRemoveLiquidityCallData.to_json())

# convert the object into a dict
aerodrome_remove_liquidity_call_data_dict = aerodrome_remove_liquidity_call_data_instance.to_dict()
# create an instance of AerodromeRemoveLiquidityCallData from a dict
aerodrome_remove_liquidity_call_data_from_dict = AerodromeRemoveLiquidityCallData.from_dict(aerodrome_remove_liquidity_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


