# AerodromeRemoveLiquidityEthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']
**token** | [**Token**](Token.md) | The symbol of the token to remove liquidity for alongside WETH. Note the [supported tokens per chain](/#/#token-table). | 
**stable** | **bool** | If true, try to remove liquidity from a stable pool with a bonding curve of K&#x3D;x^3y+y^3x. If false, try to remove liquidity from a volatile pool with a bonding curve of K&#x3D;xy | 
**liquidity** | [**Liquidity**](Liquidity.md) |  | 
**amount_token_min** | [**AmountTokenMin1**](AmountTokenMin1.md) |  | 
**amount_eth_min** | [**AmountEthMin1**](AmountEthMin1.md) |  | 
**to** | **str** |  | [optional] 
**deadline** | **int** |  | 

## Example

```python
from compass.api_client.models.aerodrome_remove_liquidity_eth_request import AerodromeRemoveLiquidityEthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeRemoveLiquidityEthRequest from a JSON string
aerodrome_remove_liquidity_eth_request_instance = AerodromeRemoveLiquidityEthRequest.from_json(json)
# print the JSON string representation of the object
print(AerodromeRemoveLiquidityEthRequest.to_json())

# convert the object into a dict
aerodrome_remove_liquidity_eth_request_dict = aerodrome_remove_liquidity_eth_request_instance.to_dict()
# create an instance of AerodromeRemoveLiquidityEthRequest from a dict
aerodrome_remove_liquidity_eth_request_from_dict = AerodromeRemoveLiquidityEthRequest.from_dict(aerodrome_remove_liquidity_eth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


