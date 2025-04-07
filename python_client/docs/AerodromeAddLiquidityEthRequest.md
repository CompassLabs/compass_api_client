# AerodromeAddLiquidityEthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | [**Token**](Token.md) | The symbol of the token to provide liquidity for alongside WETH.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**stable** | **bool** | If true, try to provide liquidity on a stable pool with a bonding curve of K&#x3D;x^3y+y^3x. If false, try to provide liquidity on a volatile pool with a bonding curve of K&#x3D;xy | 
**amount_token_desired** | [**AmountTokenDesired**](AmountTokenDesired.md) |  | 
**amount_eth_desired** | [**AmountEthDesired**](AmountEthDesired.md) |  | 
**amount_token_min** | [**AmountTokenMin**](AmountTokenMin.md) |  | 
**amount_eth_min** | [**AmountEthMin**](AmountEthMin.md) |  | 
**to** | **str** |  | [optional] 
**deadline** | **int** |  | 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 

## Example

```python
from compass.api_client.models.aerodrome_add_liquidity_eth_request import AerodromeAddLiquidityEthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeAddLiquidityEthRequest from a JSON string
aerodrome_add_liquidity_eth_request_instance = AerodromeAddLiquidityEthRequest.from_json(json)
# print the JSON string representation of the object
print(AerodromeAddLiquidityEthRequest.to_json())

# convert the object into a dict
aerodrome_add_liquidity_eth_request_dict = aerodrome_add_liquidity_eth_request_instance.to_dict()
# create an instance of AerodromeAddLiquidityEthRequest from a dict
aerodrome_add_liquidity_eth_request_from_dict = AerodromeAddLiquidityEthRequest.from_dict(aerodrome_add_liquidity_eth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


