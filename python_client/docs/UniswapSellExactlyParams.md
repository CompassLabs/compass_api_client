# UniswapSellExactlyParams

Parameters model for selling exactly an amount of tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_in** | [**Token**](Token.md) | The symbol of the token to swap from Note the [supported tokens per chain](/#/#token-table). | 
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to Note the [supported tokens per chain](/#/#token-table). | 
**fee** | [**FeeEnum**](FeeEnum.md) | The swap fee of the pool | 
**amount_in** | [**AmountIn**](AmountIn.md) |  | 
**amount_out_minimum** | [**AmountOutMinimum**](AmountOutMinimum.md) |  | [optional] 
**wrap_eth** | **bool** | Whether to wrap ETH to WETH, only use when swapping WETH into something | [optional] [default to False]

## Example

```python
from compass.api_client.models.uniswap_sell_exactly_params import UniswapSellExactlyParams

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapSellExactlyParams from a JSON string
uniswap_sell_exactly_params_instance = UniswapSellExactlyParams.from_json(json)
# print the JSON string representation of the object
print(UniswapSellExactlyParams.to_json())

# convert the object into a dict
uniswap_sell_exactly_params_dict = uniswap_sell_exactly_params_instance.to_dict()
# create an instance of UniswapSellExactlyParams from a dict
uniswap_sell_exactly_params_from_dict = UniswapSellExactlyParams.from_dict(uniswap_sell_exactly_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


