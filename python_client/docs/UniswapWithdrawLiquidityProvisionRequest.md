# UniswapWithdrawLiquidityProvisionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **int** | Token ID of the NFT representing the liquidity provisioned position. | 
**percentage_for_withdrawal** | [**PercentageForWithdrawal**](PercentageForWithdrawal.md) |  | 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']

## Example

```python
from compass.api_client.models.uniswap_withdraw_liquidity_provision_request import UniswapWithdrawLiquidityProvisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapWithdrawLiquidityProvisionRequest from a JSON string
uniswap_withdraw_liquidity_provision_request_instance = UniswapWithdrawLiquidityProvisionRequest.from_json(json)
# print the JSON string representation of the object
print(UniswapWithdrawLiquidityProvisionRequest.to_json())

# convert the object into a dict
uniswap_withdraw_liquidity_provision_request_dict = uniswap_withdraw_liquidity_provision_request_instance.to_dict()
# create an instance of UniswapWithdrawLiquidityProvisionRequest from a dict
uniswap_withdraw_liquidity_provision_request_from_dict = UniswapWithdrawLiquidityProvisionRequest.from_dict(uniswap_withdraw_liquidity_provision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


