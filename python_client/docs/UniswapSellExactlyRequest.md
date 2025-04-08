# UniswapSellExactlyRequest

Request model for selling exactly an amount of tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_in** | [**Token**](Token.md) | The symbol of the token to swap from Note the [supported tokens per chain](/#/#token-table). | 
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to Note the [supported tokens per chain](/#/#token-table). | 
**fee** | [**FeeEnum**](FeeEnum.md) | The swap fee of the pool | 
**amount_in** | [**AmountIn**](AmountIn.md) |  | 
**amount_out_minimum** | [**AmountOutMinimum**](AmountOutMinimum.md) |  | [optional] 
**wrap_eth** | **bool** | Whether to wrap ETH to WETH, only use when swapping WETH into something | [optional] [default to False]
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']

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


