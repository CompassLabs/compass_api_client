# UniswapImpermanentLossCallData

Endpoint parameters for checking impermanent loss of a liquidity position on uniswap v3.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**token_id** | **int** | Token ID of the NFT representing the liquidity provisioned position. | 

## Example

```python
from compass.api_client.models.uniswap_impermanent_loss_call_data import UniswapImpermanentLossCallData

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapImpermanentLossCallData from a JSON string
uniswap_impermanent_loss_call_data_instance = UniswapImpermanentLossCallData.from_json(json)
# print the JSON string representation of the object
print(UniswapImpermanentLossCallData.to_json())

# convert the object into a dict
uniswap_impermanent_loss_call_data_dict = uniswap_impermanent_loss_call_data_instance.to_dict()
# create an instance of UniswapImpermanentLossCallData from a dict
uniswap_impermanent_loss_call_data_from_dict = UniswapImpermanentLossCallData.from_dict(uniswap_impermanent_loss_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


