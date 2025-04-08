# AerodromeAddLiquidityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_a** | [**Token**](Token.md) | The symbol of the token to provide liquidity for Note the [supported tokens per chain](/#/#token-table). | 
**token_b** | [**Token**](Token.md) | The symbol of the token to provide liquidity for Note the [supported tokens per chain](/#/#token-table). | 
**stable** | **bool** | If true, try to provide liquidity on a stable pool with a bonding curve of K&#x3D;x^3y+y^3x. If false, try to provide liquidity on a volatile pool with a bonding curve of K&#x3D;xy | 
**amount_a_desired** | [**AmountADesired**](AmountADesired.md) |  | 
**amount_b_desired** | [**AmountBDesired**](AmountBDesired.md) |  | 
**amount_a_min** | [**AmountAMin**](AmountAMin.md) |  | 
**amount_b_min** | [**AmountBMin**](AmountBMin.md) |  | 
**to** | **str** |  | [optional] 
**deadline** | **int** |  | 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']

## Example

```python
from compass.api_client.models.aerodrome_add_liquidity_request import AerodromeAddLiquidityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeAddLiquidityRequest from a JSON string
aerodrome_add_liquidity_request_instance = AerodromeAddLiquidityRequest.from_json(json)
# print the JSON string representation of the object
print(AerodromeAddLiquidityRequest.to_json())

# convert the object into a dict
aerodrome_add_liquidity_request_dict = aerodrome_add_liquidity_request_instance.to_dict()
# create an instance of AerodromeAddLiquidityRequest from a dict
aerodrome_add_liquidity_request_from_dict = AerodromeAddLiquidityRequest.from_dict(aerodrome_add_liquidity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


