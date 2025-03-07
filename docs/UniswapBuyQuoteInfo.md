# UniswapBuyQuoteInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_in** | **str** | The amount of token_in you would need to give to the pool. | 
**price_after** | **str** | The price of the pool after this trade would happen. (How much token0 you need to buy 1 token1.) | 

## Example

```python
from compass.api_client.models.uniswap_buy_quote_info import UniswapBuyQuoteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapBuyQuoteInfo from a JSON string
uniswap_buy_quote_info_instance = UniswapBuyQuoteInfo.from_json(json)
# print the JSON string representation of the object
print(UniswapBuyQuoteInfo.to_json())

# convert the object into a dict
uniswap_buy_quote_info_dict = uniswap_buy_quote_info_instance.to_dict()
# create an instance of UniswapBuyQuoteInfo from a dict
uniswap_buy_quote_info_from_dict = UniswapBuyQuoteInfo.from_dict(uniswap_buy_quote_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


