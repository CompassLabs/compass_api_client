# AerodromeSlipstreamBuyExactlyCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_in** | [**Token**](Token.md) | The symbol of the token to swap from&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**tick_spacing** | **int** | The tick spacing of the pool | 
**amount_out** | [**AmountOut**](AmountOut.md) |  | 
**amount_in_maximum** | [**AmountInMaximum**](AmountInMaximum.md) |  | 

## Example

```python
from compass.api_client.models.aerodrome_slipstream_buy_exactly_call_data import AerodromeSlipstreamBuyExactlyCallData

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSlipstreamBuyExactlyCallData from a JSON string
aerodrome_slipstream_buy_exactly_call_data_instance = AerodromeSlipstreamBuyExactlyCallData.from_json(json)
# print the JSON string representation of the object
print(AerodromeSlipstreamBuyExactlyCallData.to_json())

# convert the object into a dict
aerodrome_slipstream_buy_exactly_call_data_dict = aerodrome_slipstream_buy_exactly_call_data_instance.to_dict()
# create an instance of AerodromeSlipstreamBuyExactlyCallData from a dict
aerodrome_slipstream_buy_exactly_call_data_from_dict = AerodromeSlipstreamBuyExactlyCallData.from_dict(aerodrome_slipstream_buy_exactly_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


