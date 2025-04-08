# Body


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_in** | [**Token**](Token.md) | The symbol of the token to swap from&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**fee** | [**FeeEnum**](FeeEnum.md) | The swap fee of the pool | 
**amount_out** | [**AmountOut**](AmountOut.md) |  | 
**amount_in_maximum** | [**AmountInMaximum**](AmountInMaximum.md) |  | 
**wrap_eth** | **bool** | Whether to wrap ETH to WETH, only use when swapping WETH into something | [optional] [default to False]
**amount_in** | [**AmountIn**](AmountIn.md) |  | 
**amount_out_minimum** | [**AmountOutMinimum**](AmountOutMinimum.md) |  | [optional] 
**token0** | [**Token**](Token.md) | The symbol of the first token in the pair&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**token1** | [**Token**](Token.md) | The symbol of the second token in the pair&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**tick_lower** | **int** | The lower tick of the range to mint the position in | 
**tick_upper** | **int** | The upper tick of the range to mint the position in | 
**amount0_desired** | [**Amount0Desired1**](Amount0Desired1.md) |  | 
**amount1_desired** | [**Amount1Desired1**](Amount1Desired1.md) |  | 
**amount0_min** | [**Amount0Min1**](Amount0Min1.md) |  | 
**amount1_min** | [**Amount1Min1**](Amount1Min1.md) |  | 
**recipient** | **str** | The address of the recipient of the withdrawn funds. | 
**token_id** | **int** | Token ID of the NFT representing the liquidity provisioned position. | 
**percentage_for_withdrawal** | [**PercentageForWithdrawal**](PercentageForWithdrawal.md) |  | 
**asset** | [**Token**](Token.md) | The symbol of the underlying asset to withdraw.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**amount** | [**Amount4**](Amount4.md) |  | 
**interest_rate_mode** | [**InterestRateMode**](InterestRateMode.md) | The interest rate mode to borrow | 
**on_behalf_of** | **str** |  | [optional] 
**token** | [**Token**](Token.md) | The symbol of the token for which the allowance is increased.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**contract_name** | [**ContractName**](ContractName.md) | The name of the contract to increase allowance for. | 

## Example

```python
from compass.api_client.models.body import Body

# TODO update the JSON string below
json = "{}"
# create an instance of Body from a JSON string
body_instance = Body.from_json(json)
# print the JSON string representation of the object
print(Body.to_json())

# convert the object into a dict
body_dict = body_instance.to_dict()
# create an instance of Body from a dict
body_from_dict = Body.from_dict(body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


