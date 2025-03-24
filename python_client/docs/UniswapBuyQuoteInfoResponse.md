# UniswapBuyQuoteInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_in** | **str** | The amount of token_in you would need to give to the pool. | 
**price_after** | **str** | The price of the pool after this trade would happen. (How much token0 you need to buy 1 token1.) | 

## Example

```python
from compass.api_client.models.uniswap_buy_quote_info_response import UniswapBuyQuoteInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapBuyQuoteInfoResponse from a JSON string
uniswap_buy_quote_info_response_instance = UniswapBuyQuoteInfoResponse.from_json(json)
# print the JSON string representation of the object
print(UniswapBuyQuoteInfoResponse.to_json())

# convert the object into a dict
uniswap_buy_quote_info_response_dict = uniswap_buy_quote_info_response_instance.to_dict()
# create an instance of UniswapBuyQuoteInfoResponse from a dict
uniswap_buy_quote_info_response_from_dict = UniswapBuyQuoteInfoResponse.from_dict(uniswap_buy_quote_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


