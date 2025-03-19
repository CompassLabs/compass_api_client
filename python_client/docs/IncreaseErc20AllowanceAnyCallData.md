# IncreaseErc20AllowanceAnyCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_name** | [**ContractName**](ContractName.md) | The name of the token for which the allowance is increased. | 
**token_address** | **str** | The address of the ERC20 token for which the allowance is increased.&lt;br&gt; Note the supported tokens per chain:&lt;br&gt;**ethereum:mainnet**: [&#39;1INCH&#39;, &#39;AAVE&#39;, &#39;BAL&#39;, &#39;cbBTC&#39;, &#39;cbETH&#39;, &#39;CRV&#39;, &#39;crvUSD&#39;, &#39;DAI&#39;, &#39;ENS&#39;, &#39;ETHx&#39;, &#39;FRAX&#39;, &#39;FXS&#39;, &#39;GHO&#39;, &#39;KNC&#39;, &#39;LDO&#39;, &#39;LINK&#39;, &#39;LUSD&#39;, &#39;MKR&#39;, &#39;osETH&#39;, &#39;PYUSD&#39;, &#39;rETH&#39;, &#39;RPL&#39;, &#39;rsETH&#39;, &#39;sDAI&#39;, &#39;SNX&#39;, &#39;STG&#39;, &#39;sUSDe&#39;, &#39;tBTC&#39;, &#39;UNI&#39;, &#39;USDC&#39;, &#39;USDe&#39;, &#39;USDS&#39;, &#39;USDT&#39;, &#39;WBTC&#39;, &#39;weETH&#39;, &#39;WETH&#39;, &#39;wstETH&#39;]&lt;br&gt;**arbitrum:mainnet**: [&#39;AAVE&#39;, &#39;ARB&#39;, &#39;DAI&#39;, &#39;EURS&#39;, &#39;FRAX&#39;, &#39;GHO&#39;, &#39;LINK&#39;, &#39;LUSD&#39;, &#39;MAI&#39;, &#39;rETH&#39;, &#39;USDC&#39;, &#39;USDCe&#39;, &#39;USDT&#39;, &#39;WBTC&#39;, &#39;weETH&#39;, &#39;WETH&#39;, &#39;wstETH&#39;]&lt;br&gt;**base:mainnet**: [&#39;1INCH&#39;, &#39;AERO&#39;, &#39;ARB&#39;, &#39;BAL&#39;, &#39;cbBTC&#39;, &#39;cbETH&#39;, &#39;CRV&#39;, &#39;crvUSD&#39;, &#39;DAI&#39;, &#39;EUR&#39;, &#39;LUSD&#39;, &#39;MKR&#39;, &#39;osETH&#39;, &#39;rETH&#39;, &#39;SNX&#39;, &#39;STG&#39;, &#39;tBTC&#39;, &#39;USDC&#39;, &#39;UNI&#39;, &#39;USDT&#39;, &#39;VIRTUAL&#39;, &#39;WBTC&#39;, &#39;weETH&#39;, &#39;WETH&#39;, &#39;wstETH&#39;]&lt;br&gt; | 
**contract_name** | [**ContractName**](ContractName.md) | The name of the contract to increase allowance for. | 
**amount** | [**Amount4**](Amount4.md) |  | 

## Example

```python
from compass.api_client.models.increase_erc20_allowance_any_call_data import IncreaseErc20AllowanceAnyCallData

# TODO update the JSON string below
json = "{}"
# create an instance of IncreaseErc20AllowanceAnyCallData from a JSON string
increase_erc20_allowance_any_call_data_instance = IncreaseErc20AllowanceAnyCallData.from_json(json)
# print the JSON string representation of the object
print(IncreaseErc20AllowanceAnyCallData.to_json())

# convert the object into a dict
increase_erc20_allowance_any_call_data_dict = increase_erc20_allowance_any_call_data_instance.to_dict()
# create an instance of IncreaseErc20AllowanceAnyCallData from a dict
increase_erc20_allowance_any_call_data_from_dict = IncreaseErc20AllowanceAnyCallData.from_dict(increase_erc20_allowance_any_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


