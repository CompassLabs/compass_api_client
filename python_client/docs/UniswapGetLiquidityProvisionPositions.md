# UniswapGetLiquidityProvisionPositions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**user** | **str** | The address of the user to check the balance of | 

## Example

```python
from compass.api_client.models.uniswap_get_liquidity_provision_positions import UniswapGetLiquidityProvisionPositions

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapGetLiquidityProvisionPositions from a JSON string
uniswap_get_liquidity_provision_positions_instance = UniswapGetLiquidityProvisionPositions.from_json(json)
# print the JSON string representation of the object
print(UniswapGetLiquidityProvisionPositions.to_json())

# convert the object into a dict
uniswap_get_liquidity_provision_positions_dict = uniswap_get_liquidity_provision_positions_instance.to_dict()
# create an instance of UniswapGetLiquidityProvisionPositions from a dict
uniswap_get_liquidity_provision_positions_from_dict = UniswapGetLiquidityProvisionPositions.from_dict(uniswap_get_liquidity_provision_positions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


