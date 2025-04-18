# UniswapWithdrawLiquidityProvisionParams

Endpoint parameters for liquidity provision withdrawal on uniswap v3.  This action is performed in a multicall on the NonfungiblePosition Manager: https://github.com/Uniswap/v3-periphery/blob/0682387198a24c7cd63566a2c58398533860a5d1/contracts/base/Multicall.sol#L11-L27 First, we call decrease liquidity then collect the tokens owed to the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **int** | Token ID of the NFT representing the liquidity provisioned position. | 
**percentage_for_withdrawal** | [**PercentageForWithdrawal**](PercentageForWithdrawal.md) |  | 

## Example

```python
from compass.api_client.models.uniswap_withdraw_liquidity_provision_params import UniswapWithdrawLiquidityProvisionParams

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapWithdrawLiquidityProvisionParams from a JSON string
uniswap_withdraw_liquidity_provision_params_instance = UniswapWithdrawLiquidityProvisionParams.from_json(json)
# print the JSON string representation of the object
print(UniswapWithdrawLiquidityProvisionParams.to_json())

# convert the object into a dict
uniswap_withdraw_liquidity_provision_params_dict = uniswap_withdraw_liquidity_provision_params_instance.to_dict()
# create an instance of UniswapWithdrawLiquidityProvisionParams from a dict
uniswap_withdraw_liquidity_provision_params_from_dict = UniswapWithdrawLiquidityProvisionParams.from_dict(uniswap_withdraw_liquidity_provision_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


