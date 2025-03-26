# UniswapGetSellQuoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**token_in** | [**Token**](Token.md) | The symbol of the token to swap from&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**fee** | [**FeeEnum**](FeeEnum.md) | The fee to pay for the swap | 
**amount_in** | [**AmountIn**](AmountIn.md) |  | 

## Example

```python
from compass.api_client.models.uniswap_get_sell_quote_request import UniswapGetSellQuoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapGetSellQuoteRequest from a JSON string
uniswap_get_sell_quote_request_instance = UniswapGetSellQuoteRequest.from_json(json)
# print the JSON string representation of the object
print(UniswapGetSellQuoteRequest.to_json())

# convert the object into a dict
uniswap_get_sell_quote_request_dict = uniswap_get_sell_quote_request_instance.to_dict()
# create an instance of UniswapGetSellQuoteRequest from a dict
uniswap_get_sell_quote_request_from_dict = UniswapGetSellQuoteRequest.from_dict(uniswap_get_sell_quote_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


