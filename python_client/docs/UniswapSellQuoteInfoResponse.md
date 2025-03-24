# UniswapSellQuoteInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_out** | **str** | The amount of token_out you would receive from the pool. | 
**price_after** | **str** | The price of the pool after this trade would happen. (How much token0 you need to buy 1 token1.) | 

## Example

```python
from compass.api_client.models.uniswap_sell_quote_info_response import UniswapSellQuoteInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapSellQuoteInfoResponse from a JSON string
uniswap_sell_quote_info_response_instance = UniswapSellQuoteInfoResponse.from_json(json)
# print the JSON string representation of the object
print(UniswapSellQuoteInfoResponse.to_json())

# convert the object into a dict
uniswap_sell_quote_info_response_dict = uniswap_sell_quote_info_response_instance.to_dict()
# create an instance of UniswapSellQuoteInfoResponse from a dict
uniswap_sell_quote_info_response_from_dict = UniswapSellQuoteInfoResponse.from_dict(uniswap_sell_quote_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


