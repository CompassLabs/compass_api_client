# AerodromeSlipstreamWithdrawLiquidityProvisionRequest

Endpoint parameters for liquidity provision withdrawal on aerodrome slipstream.  This action is performed in a multicall on the NonfungiblePosition Manager: https://github.com/AerodromeSlipstream/v3-periphery/blob/0682387198a24c7cd63566a2c58398533860a5d1/contracts/base/Multicall.sol#L11-L27 First, we call decrease liquidity then collect the tokens owed to the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**token_id** | **int** | Token ID of the NFT representing the liquidity provisioned position. | 
**percentage_for_withdrawal** | [**PercentageForWithdrawal**](PercentageForWithdrawal.md) |  | 

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


