# AerodromeSwapEthForTokenCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**amount_in** | [**AmountIn1**](AmountIn1.md) |  | 
**amount_out_min** | [**AmountOutMin**](AmountOutMin.md) |  | 
**stable** | **bool** | If true, try to trade on a stable pool with a bonding curve of K&#x3D;x^3y+y^3x. If false, try to trade on a volatile pool with a bonding curve of K&#x3D;xy | 
**to** | **str** |  | [optional] 

## Example

```python
from compass.api_client.models.aerodrome_swap_eth_for_token_call_data import AerodromeSwapEthForTokenCallData

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSwapEthForTokenCallData from a JSON string
aerodrome_swap_eth_for_token_call_data_instance = AerodromeSwapEthForTokenCallData.from_json(json)
# print the JSON string representation of the object
print(AerodromeSwapEthForTokenCallData.to_json())

# convert the object into a dict
aerodrome_swap_eth_for_token_call_data_dict = aerodrome_swap_eth_for_token_call_data_instance.to_dict()
# create an instance of AerodromeSwapEthForTokenCallData from a dict
aerodrome_swap_eth_for_token_call_data_from_dict = AerodromeSwapEthForTokenCallData.from_dict(aerodrome_swap_eth_for_token_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


