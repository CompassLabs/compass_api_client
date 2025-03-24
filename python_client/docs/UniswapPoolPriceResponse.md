# UniswapPoolPriceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_in** | [**Token**](Token.md) | The first token  | 
**token_out** | [**Token**](Token.md) | The second token in the pool | 
**price** | **str** | The price of the pool. This is expressed as an instantanteous amount of how many token0 you need to buy 1 token1. In any swap this will not change during the trade; use the quote endpoint to get a better idea of how much you will pay! | 
**tick** | **int** | The current tick in the pool. This is a number that represents the price of the pool according to the uniswap v3 concentrated liquidity concept. | 

## Example

```python
from compass.api_client.models.uniswap_pool_price_response import UniswapPoolPriceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapPoolPriceResponse from a JSON string
uniswap_pool_price_response_instance = UniswapPoolPriceResponse.from_json(json)
# print the JSON string representation of the object
print(UniswapPoolPriceResponse.to_json())

# convert the object into a dict
uniswap_pool_price_response_dict = uniswap_pool_price_response_instance.to_dict()
# create an instance of UniswapPoolPriceResponse from a dict
uniswap_pool_price_response_from_dict = UniswapPoolPriceResponse.from_dict(uniswap_pool_price_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


