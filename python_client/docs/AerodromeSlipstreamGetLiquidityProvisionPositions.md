# AerodromeSlipstreamGetLiquidityProvisionPositions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**user** | **str** | The address of the user to check the balance of | 

## Example

```python
from compass.api_client.models.aerodrome_slipstream_get_liquidity_provision_positions import AerodromeSlipstreamGetLiquidityProvisionPositions

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSlipstreamGetLiquidityProvisionPositions from a JSON string
aerodrome_slipstream_get_liquidity_provision_positions_instance = AerodromeSlipstreamGetLiquidityProvisionPositions.from_json(json)
# print the JSON string representation of the object
print(AerodromeSlipstreamGetLiquidityProvisionPositions.to_json())

# convert the object into a dict
aerodrome_slipstream_get_liquidity_provision_positions_dict = aerodrome_slipstream_get_liquidity_provision_positions_instance.to_dict()
# create an instance of AerodromeSlipstreamGetLiquidityProvisionPositions from a dict
aerodrome_slipstream_get_liquidity_provision_positions_from_dict = AerodromeSlipstreamGetLiquidityProvisionPositions.from_dict(aerodrome_slipstream_get_liquidity_provision_positions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


