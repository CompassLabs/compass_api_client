# AerodromeSlipstreamSellExactlyRequest

Request model for selling exactly an amount of tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_in** | [**Token**](Token.md) | The symbol of the token to swap from&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**tick_spacing** | **int** | The tick spacing of the pool | 
**amount_in** | [**AmountIn**](AmountIn.md) |  | 
**amount_out_minimum** | [**AmountOutMinimum**](AmountOutMinimum.md) |  | [optional] 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 

## Example

```python
from compass.api_client.models.aerodrome_slipstream_sell_exactly_request import AerodromeSlipstreamSellExactlyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSlipstreamSellExactlyRequest from a JSON string
aerodrome_slipstream_sell_exactly_request_instance = AerodromeSlipstreamSellExactlyRequest.from_json(json)
# print the JSON string representation of the object
print(AerodromeSlipstreamSellExactlyRequest.to_json())

# convert the object into a dict
aerodrome_slipstream_sell_exactly_request_dict = aerodrome_slipstream_sell_exactly_request_instance.to_dict()
# create an instance of AerodromeSlipstreamSellExactlyRequest from a dict
aerodrome_slipstream_sell_exactly_request_from_dict = AerodromeSlipstreamSellExactlyRequest.from_dict(aerodrome_slipstream_sell_exactly_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


