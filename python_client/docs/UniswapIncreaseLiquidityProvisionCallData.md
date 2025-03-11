# UniswapIncreaseLiquidityProvisionCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **int** | Token ID of the NFT representing the liquidity provisioned position. | 
**amount0_desired** | [**Amount0Desired**](Amount0Desired.md) |  | 
**amount1_desired** | [**Amount1Desired**](Amount1Desired.md) |  | 
**amount0_min** | [**Amount0Min**](Amount0Min.md) |  | 
**amount1_min** | [**Amount1Min**](Amount1Min.md) |  | 

## Example

```python
from compass.api_client.models.uniswap_increase_liquidity_provision_call_data import UniswapIncreaseLiquidityProvisionCallData

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapIncreaseLiquidityProvisionCallData from a JSON string
uniswap_increase_liquidity_provision_call_data_instance = UniswapIncreaseLiquidityProvisionCallData.from_json(json)
# print the JSON string representation of the object
print(UniswapIncreaseLiquidityProvisionCallData.to_json())

# convert the object into a dict
uniswap_increase_liquidity_provision_call_data_dict = uniswap_increase_liquidity_provision_call_data_instance.to_dict()
# create an instance of UniswapIncreaseLiquidityProvisionCallData from a dict
uniswap_increase_liquidity_provision_call_data_from_dict = UniswapIncreaseLiquidityProvisionCallData.from_dict(uniswap_increase_liquidity_provision_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


