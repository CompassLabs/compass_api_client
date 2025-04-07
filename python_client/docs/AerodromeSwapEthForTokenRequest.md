# AerodromeSwapEthForTokenRequest

Request model for swapping ETH for tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**amount_in** | [**AmountIn1**](AmountIn1.md) |  | 
**amount_out_min** | [**AmountOutMin**](AmountOutMin.md) |  | 
**stable** | **bool** | If true, try to trade on a stable pool with a bonding curve of K&#x3D;x^3y+y^3x. If false, try to trade on a volatile pool with a bonding curve of K&#x3D;xy | 
**to** | **str** |  | [optional] 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 

## Example

```python
from compass.api_client.models.aerodrome_swap_eth_for_token_request import AerodromeSwapEthForTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSwapEthForTokenRequest from a JSON string
aerodrome_swap_eth_for_token_request_instance = AerodromeSwapEthForTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AerodromeSwapEthForTokenRequest.to_json())

# convert the object into a dict
aerodrome_swap_eth_for_token_request_dict = aerodrome_swap_eth_for_token_request_instance.to_dict()
# create an instance of AerodromeSwapEthForTokenRequest from a dict
aerodrome_swap_eth_for_token_request_from_dict = AerodromeSwapEthForTokenRequest.from_dict(aerodrome_swap_eth_for_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


