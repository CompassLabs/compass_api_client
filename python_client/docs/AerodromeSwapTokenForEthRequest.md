# AerodromeSwapTokenForEthRequest

Request model for swapping tokens for ETH.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_in** | [**Token**](Token.md) | The symbol of the token to swap from Note the [supported tokens per chain](/#/#token-table). | 
**amount_in** | [**AmountIn2**](AmountIn2.md) |  | 
**amount_out_min** | [**AmountOutMin1**](AmountOutMin1.md) |  | 
**stable** | **bool** | If true, try to trade on a stable pool with a bonding curve of K&#x3D;x^3y+y^3x. If false, try to trade on a volatile pool with a bonding curve of K&#x3D;xy | 
**to** | **str** |  | [optional] 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']

## Example

```python
from compass.api_client.models.aerodrome_swap_token_for_eth_request import AerodromeSwapTokenForEthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSwapTokenForEthRequest from a JSON string
aerodrome_swap_token_for_eth_request_instance = AerodromeSwapTokenForEthRequest.from_json(json)
# print the JSON string representation of the object
print(AerodromeSwapTokenForEthRequest.to_json())

# convert the object into a dict
aerodrome_swap_token_for_eth_request_dict = aerodrome_swap_token_for_eth_request_instance.to_dict()
# create an instance of AerodromeSwapTokenForEthRequest from a dict
aerodrome_swap_token_for_eth_request_from_dict = AerodromeSwapTokenForEthRequest.from_dict(aerodrome_swap_token_for_eth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


