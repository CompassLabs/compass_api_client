# UniswapBuyExactlyRequest

Request model for buying exactly an amount of tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_in** | [**Token**](Token.md) | The symbol of the token to swap from Note the [supported tokens per chain](/#/#token-table). | 
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to Note the [supported tokens per chain](/#/#token-table). | 
**fee** | [**FeeEnum**](FeeEnum.md) | The swap fee of the pool | 
**amount_out** | [**AmountOut**](AmountOut.md) |  | 
**amount_in_maximum** | [**AmountInMaximum**](AmountInMaximum.md) |  | 
**wrap_eth** | **bool** | Whether to wrap ETH to WETH, only use when swapping WETH into something | [optional] [default to False]
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']

## Example

```python
from compass.api_client.models.uniswap_buy_exactly_request import UniswapBuyExactlyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapBuyExactlyRequest from a JSON string
uniswap_buy_exactly_request_instance = UniswapBuyExactlyRequest.from_json(json)
# print the JSON string representation of the object
print(UniswapBuyExactlyRequest.to_json())

# convert the object into a dict
uniswap_buy_exactly_request_dict = uniswap_buy_exactly_request_instance.to_dict()
# create an instance of UniswapBuyExactlyRequest from a dict
uniswap_buy_exactly_request_from_dict = UniswapBuyExactlyRequest.from_dict(uniswap_buy_exactly_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


