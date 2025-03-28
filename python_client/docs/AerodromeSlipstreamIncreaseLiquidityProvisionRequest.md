# AerodromeSlipstreamIncreaseLiquidityProvisionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**token_id** | **int** | Token ID of the NFT representing the liquidity provisioned position. | 
**amount0_desired** | [**Amount0Desired**](Amount0Desired.md) |  | 
**amount1_desired** | [**Amount1Desired**](Amount1Desired.md) |  | 
**amount0_min** | [**Amount0Min**](Amount0Min.md) |  | 
**amount1_min** | [**Amount1Min**](Amount1Min.md) |  | 

## Example

```python
from compass.api_client.models.aerodrome_slipstream_increase_liquidity_provision_request import AerodromeSlipstreamIncreaseLiquidityProvisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSlipstreamIncreaseLiquidityProvisionRequest from a JSON string
aerodrome_slipstream_increase_liquidity_provision_request_instance = AerodromeSlipstreamIncreaseLiquidityProvisionRequest.from_json(json)
# print the JSON string representation of the object
print(AerodromeSlipstreamIncreaseLiquidityProvisionRequest.to_json())

# convert the object into a dict
aerodrome_slipstream_increase_liquidity_provision_request_dict = aerodrome_slipstream_increase_liquidity_provision_request_instance.to_dict()
# create an instance of AerodromeSlipstreamIncreaseLiquidityProvisionRequest from a dict
aerodrome_slipstream_increase_liquidity_provision_request_from_dict = AerodromeSlipstreamIncreaseLiquidityProvisionRequest.from_dict(aerodrome_slipstream_increase_liquidity_provision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


