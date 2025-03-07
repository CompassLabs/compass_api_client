# UniswapImpermanentLossResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**impermanent_loss** | **float** | The impermanent loss of the position. This is the difference between the value of tokens if you had just held them and the value of the tokens currently in the LP position. | 
**total_fees_earned_in_usd** | **float** | The total fees earned in the liquidity position in USD. | 
**fees_earned** | [**Token0Token1**](Token0Token1.md) | The fees earned in the portions of token0 and token1 separately, in units of token0 and token1. | 
**current_lp** | [**Token0Token1**](Token0Token1.md) | The current amount of token0 and token1 in the liquidity position in the units of token0 and token1. | 
**initial_lp** | [**Token0Token1**](Token0Token1.md) | The initial amount of token0 and token1 supplied to the liquidity position in the units of token0 and token1. | 
**initial_value_in_usd** | **float** | The initial value in USD of the liquidity position calculated using the historical price at the time of supplying. | 
**current_value_in_usd** | **float** | The current value of the liquidity position in USD calculated using the current price. | 
**hold_value_in_usd** | **float** | The value of the tokens in USD if you had just held them. | 

## Example

```python
from compass.api_client.models.uniswap_impermanent_loss_response import UniswapImpermanentLossResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapImpermanentLossResponse from a JSON string
uniswap_impermanent_loss_response_instance = UniswapImpermanentLossResponse.from_json(json)
# print the JSON string representation of the object
print(UniswapImpermanentLossResponse.to_json())

# convert the object into a dict
uniswap_impermanent_loss_response_dict = uniswap_impermanent_loss_response_instance.to_dict()
# create an instance of UniswapImpermanentLossResponse from a dict
uniswap_impermanent_loss_response_from_dict = UniswapImpermanentLossResponse.from_dict(uniswap_impermanent_loss_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


