# UniswapWithdrawLiquidityProvisionCallData

Endpoint parameters for liquidity provision withdrawal on uniswap v3.  This action is performed in a multicall on the NonfungiblePosition Manager: https://github.com/Uniswap/v3-periphery/blob/0682387198a24c7cd63566a2c58398533860a5d1/contracts/base/Multicall.sol#L11-L27 First, we call decrease liquidity then collect the tokens owed to the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **int** | Token ID of the NFT representing the liquidity provisioned position. | 
**percentage_for_withdrawal** | [**PercentageForWithdrawal**](PercentageForWithdrawal.md) |  | 

## Example

```python
from compass.api_client.models.uniswap_withdraw_liquidity_provision_call_data import UniswapWithdrawLiquidityProvisionCallData

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapWithdrawLiquidityProvisionCallData from a JSON string
uniswap_withdraw_liquidity_provision_call_data_instance = UniswapWithdrawLiquidityProvisionCallData.from_json(json)
# print the JSON string representation of the object
print(UniswapWithdrawLiquidityProvisionCallData.to_json())

# convert the object into a dict
uniswap_withdraw_liquidity_provision_call_data_dict = uniswap_withdraw_liquidity_provision_call_data_instance.to_dict()
# create an instance of UniswapWithdrawLiquidityProvisionCallData from a dict
uniswap_withdraw_liquidity_provision_call_data_from_dict = UniswapWithdrawLiquidityProvisionCallData.from_dict(uniswap_withdraw_liquidity_provision_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


