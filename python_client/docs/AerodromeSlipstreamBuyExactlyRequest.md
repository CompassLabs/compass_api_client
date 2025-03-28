# AerodromeSlipstreamBuyExactlyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**token_in** | [**Token**](Token.md) | The symbol of the token to swap from&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**tick_spacing** | **int** | The tick spacing of the pool | 
**amount_out** | [**AmountOut**](AmountOut.md) |  | 
**amount_in_maximum** | [**AmountInMaximum**](AmountInMaximum.md) |  | 

## Example

```python
from compass.api_client.models.aerodrome_slipstream_buy_exactly_request import AerodromeSlipstreamBuyExactlyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSlipstreamBuyExactlyRequest from a JSON string
aerodrome_slipstream_buy_exactly_request_instance = AerodromeSlipstreamBuyExactlyRequest.from_json(json)
# print the JSON string representation of the object
print(AerodromeSlipstreamBuyExactlyRequest.to_json())

# convert the object into a dict
aerodrome_slipstream_buy_exactly_request_dict = aerodrome_slipstream_buy_exactly_request_instance.to_dict()
# create an instance of AerodromeSlipstreamBuyExactlyRequest from a dict
aerodrome_slipstream_buy_exactly_request_from_dict = AerodromeSlipstreamBuyExactlyRequest.from_dict(aerodrome_slipstream_buy_exactly_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


