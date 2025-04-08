# AerodromeSlipstreamWithdrawLiquidityProvisionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **int** | Token ID of the NFT representing the liquidity provisioned position. | 
**percentage_for_withdrawal** | [**PercentageForWithdrawal**](PercentageForWithdrawal.md) |  | 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 

## Example

```python
from compass.api_client.models.aerodrome_slipstream_withdraw_liquidity_provision_request import AerodromeSlipstreamWithdrawLiquidityProvisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSlipstreamWithdrawLiquidityProvisionRequest from a JSON string
aerodrome_slipstream_withdraw_liquidity_provision_request_instance = AerodromeSlipstreamWithdrawLiquidityProvisionRequest.from_json(json)
# print the JSON string representation of the object
print(AerodromeSlipstreamWithdrawLiquidityProvisionRequest.to_json())

# convert the object into a dict
aerodrome_slipstream_withdraw_liquidity_provision_request_dict = aerodrome_slipstream_withdraw_liquidity_provision_request_instance.to_dict()
# create an instance of AerodromeSlipstreamWithdrawLiquidityProvisionRequest from a dict
aerodrome_slipstream_withdraw_liquidity_provision_request_from_dict = AerodromeSlipstreamWithdrawLiquidityProvisionRequest.from_dict(aerodrome_slipstream_withdraw_liquidity_provision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


