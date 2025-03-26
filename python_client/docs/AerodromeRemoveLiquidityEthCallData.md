# AerodromeRemoveLiquidityEthCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | [**Token**](Token.md) | The symbol of the token to remove liquidity for alongside WETH.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**stable** | **bool** | If true, try to remove liquidity from a stable pool with a bonding curve of K&#x3D;x^3y+y^3x. If false, try to remove liquidity from a volatile pool with a bonding curve of K&#x3D;xy | 
**liquidity** | [**Liquidity**](Liquidity.md) |  | 
**amount_token_min** | [**AmountTokenMin1**](AmountTokenMin1.md) |  | 
**amount_eth_min** | [**AmountEthMin1**](AmountEthMin1.md) |  | 
**to** | **str** |  | [optional] 
**deadline** | **int** |  | 

## Example

```python
from compass.api_client.models.aerodrome_remove_liquidity_eth_call_data import AerodromeRemoveLiquidityEthCallData

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeRemoveLiquidityEthCallData from a JSON string
aerodrome_remove_liquidity_eth_call_data_instance = AerodromeRemoveLiquidityEthCallData.from_json(json)
# print the JSON string representation of the object
print(AerodromeRemoveLiquidityEthCallData.to_json())

# convert the object into a dict
aerodrome_remove_liquidity_eth_call_data_dict = aerodrome_remove_liquidity_eth_call_data_instance.to_dict()
# create an instance of AerodromeRemoveLiquidityEthCallData from a dict
aerodrome_remove_liquidity_eth_call_data_from_dict = AerodromeRemoveLiquidityEthCallData.from_dict(aerodrome_remove_liquidity_eth_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


