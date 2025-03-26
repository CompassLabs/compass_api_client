# AerodromeSlipstreamSellExactlyCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_in** | [**Token**](Token.md) | The symbol of the token to swap from&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**tick_spacing** | **int** | The tick spacing of the pool | 
**amount_in** | [**AmountIn**](AmountIn.md) |  | 
**amount_out_minimum** | [**AmountOutMinimum**](AmountOutMinimum.md) |  | [optional] 

## Example

```python
from compass.api_client.models.aerodrome_slipstream_sell_exactly_call_data import AerodromeSlipstreamSellExactlyCallData

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSlipstreamSellExactlyCallData from a JSON string
aerodrome_slipstream_sell_exactly_call_data_instance = AerodromeSlipstreamSellExactlyCallData.from_json(json)
# print the JSON string representation of the object
print(AerodromeSlipstreamSellExactlyCallData.to_json())

# convert the object into a dict
aerodrome_slipstream_sell_exactly_call_data_dict = aerodrome_slipstream_sell_exactly_call_data_instance.to_dict()
# create an instance of AerodromeSlipstreamSellExactlyCallData from a dict
aerodrome_slipstream_sell_exactly_call_data_from_dict = AerodromeSlipstreamSellExactlyCallData.from_dict(aerodrome_slipstream_sell_exactly_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


