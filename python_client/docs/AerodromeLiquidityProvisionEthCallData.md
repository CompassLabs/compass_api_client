# AerodromeLiquidityProvisionEthCallData


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

## Example

```python
from compass.api_client.models.aerodrome_liquidity_provision_eth_call_data import AerodromeLiquidityProvisionEthCallData

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeLiquidityProvisionEthCallData from a JSON string
aerodrome_liquidity_provision_eth_call_data_instance = AerodromeLiquidityProvisionEthCallData.from_json(json)
# print the JSON string representation of the object
print(AerodromeLiquidityProvisionEthCallData.to_json())

# convert the object into a dict
aerodrome_liquidity_provision_eth_call_data_dict = aerodrome_liquidity_provision_eth_call_data_instance.to_dict()
# create an instance of AerodromeLiquidityProvisionEthCallData from a dict
aerodrome_liquidity_provision_eth_call_data_from_dict = AerodromeLiquidityProvisionEthCallData.from_dict(aerodrome_liquidity_provision_eth_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


