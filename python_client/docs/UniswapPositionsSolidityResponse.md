# UniswapPositionsSolidityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **int** |  | 
**operator** | **str** |  | 
**token0** | **str** |  | 
**token1** | **str** |  | 
**fee** | **int** |  | 
**tick_lower** | **int** |  | 
**tick_upper** | **int** |  | 
**liquidity** | **int** |  | 
**fee_growth_inside0_last_x128** | **int** |  | 
**fee_growth_inside1_last_x128** | **int** |  | 
**tokens_owed0** | **int** |  | 
**tokens_owed1** | **int** |  | 

## Example

```python
from compass.api_client.models.uniswap_positions_solidity_response import UniswapPositionsSolidityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapPositionsSolidityResponse from a JSON string
uniswap_positions_solidity_response_instance = UniswapPositionsSolidityResponse.from_json(json)
# print the JSON string representation of the object
print(UniswapPositionsSolidityResponse.to_json())

# convert the object into a dict
uniswap_positions_solidity_response_dict = uniswap_positions_solidity_response_instance.to_dict()
# create an instance of UniswapPositionsSolidityResponse from a dict
uniswap_positions_solidity_response_from_dict = UniswapPositionsSolidityResponse.from_dict(uniswap_positions_solidity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


