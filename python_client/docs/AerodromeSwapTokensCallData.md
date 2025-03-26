# AerodromeSwapTokensCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_in** | [**Token**](Token.md) | The symbol of the token to swap from&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**amount_in** | [**AmountIn2**](AmountIn2.md) |  | 
**amount_out_min** | [**AmountOutMin**](AmountOutMin.md) |  | 
**stable** | **bool** | If true, try to trade on a stable pool with a bonding curve of K&#x3D;x^3y+y^3x. If false, try to trade on a volatile pool with a bonding curve of K&#x3D;xy | 
**to** | **str** |  | [optional] 

## Example

```python
from compass.api_client.models.aerodrome_swap_tokens_call_data import AerodromeSwapTokensCallData

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSwapTokensCallData from a JSON string
aerodrome_swap_tokens_call_data_instance = AerodromeSwapTokensCallData.from_json(json)
# print the JSON string representation of the object
print(AerodromeSwapTokensCallData.to_json())

# convert the object into a dict
aerodrome_swap_tokens_call_data_dict = aerodrome_swap_tokens_call_data_instance.to_dict()
# create an instance of AerodromeSwapTokensCallData from a dict
aerodrome_swap_tokens_call_data_from_dict = AerodromeSwapTokensCallData.from_dict(aerodrome_swap_tokens_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


