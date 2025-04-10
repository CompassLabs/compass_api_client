# UniswapIncreaseLiquidityProvisionRequest

Request model for increasing liquidity provision in Uniswap V3.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **int** | Token ID of the NFT representing the liquidity provisioned position. | 
**amount0_desired** | [**Amount0Desired1**](Amount0Desired1.md) |  | 
**amount1_desired** | [**Amount1Desired1**](Amount1Desired1.md) |  | 
**amount0_min** | [**Amount0Min1**](Amount0Min1.md) |  | 
**amount1_min** | [**Amount1Min1**](Amount1Min1.md) |  | 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']

## Example

```python
from compass.api_client.models.uniswap_increase_liquidity_provision_request import UniswapIncreaseLiquidityProvisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapIncreaseLiquidityProvisionRequest from a JSON string
uniswap_increase_liquidity_provision_request_instance = UniswapIncreaseLiquidityProvisionRequest.from_json(json)
# print the JSON string representation of the object
print(UniswapIncreaseLiquidityProvisionRequest.to_json())

# convert the object into a dict
uniswap_increase_liquidity_provision_request_dict = uniswap_increase_liquidity_provision_request_instance.to_dict()
# create an instance of UniswapIncreaseLiquidityProvisionRequest from a dict
uniswap_increase_liquidity_provision_request_from_dict = UniswapIncreaseLiquidityProvisionRequest.from_dict(uniswap_increase_liquidity_provision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


