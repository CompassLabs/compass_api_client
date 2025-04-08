# AerodromeSlipstreamGetPoolPriceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**token_in** | [**Token**](Token.md) | The symbol of a token in the pool Note the [supported tokens per chain](/#/#token-table). | 
**token_out** | [**Token**](Token.md) | The symbol of a token in the pool Note the [supported tokens per chain](/#/#token-table). | 
**tick_spacing** | **int** | The tick spacing of the pool | 

## Example

```python
from compass.api_client.models.aerodrome_slipstream_get_pool_price_request import AerodromeSlipstreamGetPoolPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSlipstreamGetPoolPriceRequest from a JSON string
aerodrome_slipstream_get_pool_price_request_instance = AerodromeSlipstreamGetPoolPriceRequest.from_json(json)
# print the JSON string representation of the object
print(AerodromeSlipstreamGetPoolPriceRequest.to_json())

# convert the object into a dict
aerodrome_slipstream_get_pool_price_request_dict = aerodrome_slipstream_get_pool_price_request_instance.to_dict()
# create an instance of AerodromeSlipstreamGetPoolPriceRequest from a dict
aerodrome_slipstream_get_pool_price_request_from_dict = AerodromeSlipstreamGetPoolPriceRequest.from_dict(aerodrome_slipstream_get_pool_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


