# UniswapGetLiquidityProvisionPositionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**user** | **str** | The address of the user to check the balance of | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']

## Example

```python
from compass.api_client.models.uniswap_get_liquidity_provision_positions_request import UniswapGetLiquidityProvisionPositionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapGetLiquidityProvisionPositionsRequest from a JSON string
uniswap_get_liquidity_provision_positions_request_instance = UniswapGetLiquidityProvisionPositionsRequest.from_json(json)
# print the JSON string representation of the object
print(UniswapGetLiquidityProvisionPositionsRequest.to_json())

# convert the object into a dict
uniswap_get_liquidity_provision_positions_request_dict = uniswap_get_liquidity_provision_positions_request_instance.to_dict()
# create an instance of UniswapGetLiquidityProvisionPositionsRequest from a dict
uniswap_get_liquidity_provision_positions_request_from_dict = UniswapGetLiquidityProvisionPositionsRequest.from_dict(uniswap_get_liquidity_provision_positions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


