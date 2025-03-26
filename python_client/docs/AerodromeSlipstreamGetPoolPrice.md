# AerodromeSlipstreamGetPoolPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**token_in** | [**Token**](Token.md) | The symbol of a token in the pool&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**token_out** | [**Token**](Token.md) | The symbol of a token in the pool&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**tick_spacing** | **int** | The tick spacing of the pool | 

## Example

```python
from compass.api_client.models.aerodrome_slipstream_get_pool_price import AerodromeSlipstreamGetPoolPrice

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSlipstreamGetPoolPrice from a JSON string
aerodrome_slipstream_get_pool_price_instance = AerodromeSlipstreamGetPoolPrice.from_json(json)
# print the JSON string representation of the object
print(AerodromeSlipstreamGetPoolPrice.to_json())

# convert the object into a dict
aerodrome_slipstream_get_pool_price_dict = aerodrome_slipstream_get_pool_price_instance.to_dict()
# create an instance of AerodromeSlipstreamGetPoolPrice from a dict
aerodrome_slipstream_get_pool_price_from_dict = AerodromeSlipstreamGetPoolPrice.from_dict(aerodrome_slipstream_get_pool_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


