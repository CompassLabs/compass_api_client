# UniswapIncreaseLiquidityProvisionParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **int** | Token ID of the NFT representing the liquidity provisioned position. | 
**amount0_desired** | [**Amount0Desired1**](Amount0Desired1.md) |  | 
**amount1_desired** | [**Amount1Desired1**](Amount1Desired1.md) |  | 
**amount0_min** | [**Amount0Min1**](Amount0Min1.md) |  | 
**amount1_min** | [**Amount1Min1**](Amount1Min1.md) |  | 

## Example

```python
from compass.api_client.models.uniswap_increase_liquidity_provision_params import UniswapIncreaseLiquidityProvisionParams

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapIncreaseLiquidityProvisionParams from a JSON string
uniswap_increase_liquidity_provision_params_instance = UniswapIncreaseLiquidityProvisionParams.from_json(json)
# print the JSON string representation of the object
print(UniswapIncreaseLiquidityProvisionParams.to_json())

# convert the object into a dict
uniswap_increase_liquidity_provision_params_dict = uniswap_increase_liquidity_provision_params_instance.to_dict()
# create an instance of UniswapIncreaseLiquidityProvisionParams from a dict
uniswap_increase_liquidity_provision_params_from_dict = UniswapIncreaseLiquidityProvisionParams.from_dict(uniswap_increase_liquidity_provision_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


