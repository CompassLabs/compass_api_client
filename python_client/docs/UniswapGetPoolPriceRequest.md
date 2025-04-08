# UniswapGetPoolPriceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**token_in** | [**Token**](Token.md) | The symbol of a token in the pool Note the [supported tokens per chain](/#/#token-table). | 
**token_out** | [**Token**](Token.md) | The symbol of a token in the pool Note the [supported tokens per chain](/#/#token-table). | 
**fee** | [**FeeEnum**](FeeEnum.md) | The fee of the pool | 

## Example

```python
from compass.api_client.models.uniswap_get_pool_price_request import UniswapGetPoolPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapGetPoolPriceRequest from a JSON string
uniswap_get_pool_price_request_instance = UniswapGetPoolPriceRequest.from_json(json)
# print the JSON string representation of the object
print(UniswapGetPoolPriceRequest.to_json())

# convert the object into a dict
uniswap_get_pool_price_request_dict = uniswap_get_pool_price_request_instance.to_dict()
# create an instance of UniswapGetPoolPriceRequest from a dict
uniswap_get_pool_price_request_from_dict = UniswapGetPoolPriceRequest.from_dict(uniswap_get_pool_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


