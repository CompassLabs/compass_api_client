# GetErc20AllowanceRequest

Request model for getting an ERC20 token allowance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**user** | **str** | The user to get the ERC20 allowance of. | 
**token** | [**Token**](Token.md) | The symbol of the token for which the allowance is checked.&lt;br&gt; Note the supported tokens per chain:&lt;br&gt;**ethereum:mainnet**:     &#x60;1INCH&#x60;, &#x60;AAVE&#x60;, &#x60;BAL&#x60;, &#x60;cbBTC&#x60;, &#x60;cbETH&#x60;, &#x60;CRV&#x60;, &#x60;crvUSD&#x60;, &#x60;DAI&#x60;, &#x60;ENS&#x60;, &#x60;ETHx&#x60;, &#x60;FRAX&#x60;, &#x60;FXS&#x60;, &#x60;GHO&#x60;, &#x60;KNC&#x60;, &#x60;LDO&#x60;, &#x60;LINK&#x60;, &#x60;LUSD&#x60;, &#x60;MKR&#x60;, &#x60;osETH&#x60;, &#x60;PYUSD&#x60;, &#x60;rETH&#x60;, &#x60;RPL&#x60;, &#x60;rsETH&#x60;, &#x60;sDAI&#x60;, &#x60;SNX&#x60;, &#x60;STG&#x60;, &#x60;sUSDe&#x60;, &#x60;tBTC&#x60;, &#x60;UNI&#x60;, &#x60;USDC&#x60;, &#x60;USDe&#x60;, &#x60;USDS&#x60;, &#x60;USDT&#x60;, &#x60;WBTC&#x60;, &#x60;weETH&#x60;, &#x60;WETH&#x60;, &#x60;wstETH&#x60;&lt;br&gt;&lt;br&gt;**arbitrum:mainnet**:     &#x60;AAVE&#x60;, &#x60;ARB&#x60;, &#x60;DAI&#x60;, &#x60;EURS&#x60;, &#x60;FRAX&#x60;, &#x60;GHO&#x60;, &#x60;LINK&#x60;, &#x60;LUSD&#x60;, &#x60;MAI&#x60;, &#x60;rETH&#x60;, &#x60;USDC&#x60;, &#x60;USDCe&#x60;, &#x60;USDT&#x60;, &#x60;WBTC&#x60;, &#x60;weETH&#x60;, &#x60;WETH&#x60;, &#x60;wstETH&#x60;&lt;br&gt;&lt;br&gt;**base:mainnet**:     &#x60;1INCH&#x60;, &#x60;AERO&#x60;, &#x60;ARB&#x60;, &#x60;BAL&#x60;, &#x60;cbBTC&#x60;, &#x60;cbETH&#x60;, &#x60;CRV&#x60;, &#x60;crvUSD&#x60;, &#x60;DAI&#x60;, &#x60;EUR&#x60;, &#x60;LUSD&#x60;, &#x60;MKR&#x60;, &#x60;osETH&#x60;, &#x60;rETH&#x60;, &#x60;SNX&#x60;, &#x60;STG&#x60;, &#x60;tBTC&#x60;, &#x60;USDC&#x60;, &#x60;UNI&#x60;, &#x60;USDT&#x60;, &#x60;VIRTUAL&#x60;, &#x60;WBTC&#x60;, &#x60;weETH&#x60;, &#x60;WETH&#x60;, &#x60;wstETH&#x60;&lt;br&gt;&lt;br&gt; | 
**contract_name** | [**ContractName**](ContractName.md) | The name of the contract to check allowance for. | 

## Example

```python
from compass.api_client.models.get_erc20_allowance_request import GetErc20AllowanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetErc20AllowanceRequest from a JSON string
get_erc20_allowance_request_instance = GetErc20AllowanceRequest.from_json(json)
# print the JSON string representation of the object
print(GetErc20AllowanceRequest.to_json())

# convert the object into a dict
get_erc20_allowance_request_dict = get_erc20_allowance_request_instance.to_dict()
# create an instance of GetErc20AllowanceRequest from a dict
get_erc20_allowance_request_from_dict = GetErc20AllowanceRequest.from_dict(get_erc20_allowance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


