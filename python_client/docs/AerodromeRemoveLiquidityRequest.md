# AerodromeRemoveLiquidityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
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
from compass.api_client.models.aerodrome_remove_liquidity_request import AerodromeRemoveLiquidityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeRemoveLiquidityRequest from a JSON string
aerodrome_remove_liquidity_request_instance = AerodromeRemoveLiquidityRequest.from_json(json)
# print the JSON string representation of the object
print(AerodromeRemoveLiquidityRequest.to_json())

# convert the object into a dict
aerodrome_remove_liquidity_request_dict = aerodrome_remove_liquidity_request_instance.to_dict()
# create an instance of AerodromeRemoveLiquidityRequest from a dict
aerodrome_remove_liquidity_request_from_dict = AerodromeRemoveLiquidityRequest.from_dict(aerodrome_remove_liquidity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


