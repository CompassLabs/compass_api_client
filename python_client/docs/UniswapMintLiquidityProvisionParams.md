# UniswapMintLiquidityProvisionParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token0** | [**Token**](Token.md) | The symbol of the first token in the pair Note the [supported tokens per chain](/#/#token-table). | 
**token1** | [**Token**](Token.md) | The symbol of the second token in the pair Note the [supported tokens per chain](/#/#token-table). | 
**fee** | [**FeeEnum**](FeeEnum.md) | The swap fee of the pool | 
**tick_lower** | **int** | The lower tick of the range to mint the position in | 
**tick_upper** | **int** | The upper tick of the range to mint the position in | 
**amount0_desired** | [**Amount0Desired**](Amount0Desired.md) |  | 
**amount1_desired** | [**Amount1Desired**](Amount1Desired.md) |  | 
**amount0_min** | [**Amount0Min**](Amount0Min.md) |  | 
**amount1_min** | [**Amount1Min**](Amount1Min.md) |  | 
**recipient** | **str** |  | [optional] 

## Example

```python
from compass.api_client.models.uniswap_mint_liquidity_provision_params import UniswapMintLiquidityProvisionParams

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapMintLiquidityProvisionParams from a JSON string
uniswap_mint_liquidity_provision_params_instance = UniswapMintLiquidityProvisionParams.from_json(json)
# print the JSON string representation of the object
print(UniswapMintLiquidityProvisionParams.to_json())

# convert the object into a dict
uniswap_mint_liquidity_provision_params_dict = uniswap_mint_liquidity_provision_params_instance.to_dict()
# create an instance of UniswapMintLiquidityProvisionParams from a dict
uniswap_mint_liquidity_provision_params_from_dict = UniswapMintLiquidityProvisionParams.from_dict(uniswap_mint_liquidity_provision_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


