# AerodromeSlipstreamGetLiquidityProvisionPositionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**user** | **str** | The address of the user to check the balance of | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']

## Example

```python
from compass.api_client.models.aerodrome_slipstream_get_liquidity_provision_positions_request import AerodromeSlipstreamGetLiquidityProvisionPositionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSlipstreamGetLiquidityProvisionPositionsRequest from a JSON string
aerodrome_slipstream_get_liquidity_provision_positions_request_instance = AerodromeSlipstreamGetLiquidityProvisionPositionsRequest.from_json(json)
# print the JSON string representation of the object
print(AerodromeSlipstreamGetLiquidityProvisionPositionsRequest.to_json())

# convert the object into a dict
aerodrome_slipstream_get_liquidity_provision_positions_request_dict = aerodrome_slipstream_get_liquidity_provision_positions_request_instance.to_dict()
# create an instance of AerodromeSlipstreamGetLiquidityProvisionPositionsRequest from a dict
aerodrome_slipstream_get_liquidity_provision_positions_request_from_dict = AerodromeSlipstreamGetLiquidityProvisionPositionsRequest.from_dict(aerodrome_slipstream_get_liquidity_provision_positions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


