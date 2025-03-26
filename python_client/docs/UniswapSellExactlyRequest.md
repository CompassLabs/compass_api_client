# UniswapSellExactlyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**token_in** | [**Token**](Token.md) | The symbol of the token to swap from&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**fee** | [**FeeEnum**](FeeEnum.md) | The swap fee of the pool | 
**amount_in** | [**AmountIn**](AmountIn.md) |  | 
**amount_out_minimum** | [**AmountOutMinimum**](AmountOutMinimum.md) |  | [optional] 
**wrap_eth** | **bool** | Whether to wrap ETH to WETH, only use when swapping WETH into something | [optional] [default to False]

## Example

```python
from compass.api_client.models.uniswap_sell_exactly_request import UniswapSellExactlyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapSellExactlyRequest from a JSON string
uniswap_sell_exactly_request_instance = UniswapSellExactlyRequest.from_json(json)
# print the JSON string representation of the object
print(UniswapSellExactlyRequest.to_json())

# convert the object into a dict
uniswap_sell_exactly_request_dict = uniswap_sell_exactly_request_instance.to_dict()
# create an instance of UniswapSellExactlyRequest from a dict
uniswap_sell_exactly_request_from_dict = UniswapSellExactlyRequest.from_dict(uniswap_sell_exactly_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


