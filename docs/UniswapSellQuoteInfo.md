# UniswapSellQuoteInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_out** | **str** | The amount of token_out you would receive from the pool. | 
**price_after** | **str** | The price of the pool after this trade would happen. (How much token0 you need to buy 1 token1.) | 

## Example

```python
from compass.api_client.models.uniswap_sell_quote_info import UniswapSellQuoteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapSellQuoteInfo from a JSON string
uniswap_sell_quote_info_instance = UniswapSellQuoteInfo.from_json(json)
# print the JSON string representation of the object
print(UniswapSellQuoteInfo.to_json())

# convert the object into a dict
uniswap_sell_quote_info_dict = uniswap_sell_quote_info_instance.to_dict()
# create an instance of UniswapSellQuoteInfo from a dict
uniswap_sell_quote_info_from_dict = UniswapSellQuoteInfo.from_dict(uniswap_sell_quote_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


