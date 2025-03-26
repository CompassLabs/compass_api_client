# AerodromeSwapEthForTokenCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to&lt;br&gt; Note the supported tokens per chain:&lt;br&gt;**ethereum:mainnet**:     &#x60;1INCH&#x60;, &#x60;AAVE&#x60;, &#x60;BAL&#x60;, &#x60;cbBTC&#x60;, &#x60;cbETH&#x60;, &#x60;CRV&#x60;, &#x60;crvUSD&#x60;, &#x60;DAI&#x60;, &#x60;ENS&#x60;, &#x60;ETHx&#x60;, &#x60;FRAX&#x60;, &#x60;FXS&#x60;, &#x60;GHO&#x60;, &#x60;KNC&#x60;, &#x60;LDO&#x60;, &#x60;LINK&#x60;, &#x60;LUSD&#x60;, &#x60;MKR&#x60;, &#x60;osETH&#x60;, &#x60;PYUSD&#x60;, &#x60;rETH&#x60;, &#x60;RPL&#x60;, &#x60;rsETH&#x60;, &#x60;sDAI&#x60;, &#x60;SNX&#x60;, &#x60;STG&#x60;, &#x60;sUSDe&#x60;, &#x60;tBTC&#x60;, &#x60;UNI&#x60;, &#x60;USDC&#x60;, &#x60;USDe&#x60;, &#x60;USDS&#x60;, &#x60;USDT&#x60;, &#x60;WBTC&#x60;, &#x60;weETH&#x60;, &#x60;WETH&#x60;, &#x60;wstETH&#x60;&lt;br&gt;&lt;br&gt;**arbitrum:mainnet**:     &#x60;AAVE&#x60;, &#x60;ARB&#x60;, &#x60;DAI&#x60;, &#x60;EURS&#x60;, &#x60;FRAX&#x60;, &#x60;GHO&#x60;, &#x60;LINK&#x60;, &#x60;LUSD&#x60;, &#x60;MAI&#x60;, &#x60;rETH&#x60;, &#x60;USDC&#x60;, &#x60;USDCe&#x60;, &#x60;USDT&#x60;, &#x60;WBTC&#x60;, &#x60;weETH&#x60;, &#x60;WETH&#x60;, &#x60;wstETH&#x60;&lt;br&gt;&lt;br&gt;**base:mainnet**:     &#x60;1INCH&#x60;, &#x60;AERO&#x60;, &#x60;ARB&#x60;, &#x60;BAL&#x60;, &#x60;cbBTC&#x60;, &#x60;cbETH&#x60;, &#x60;CRV&#x60;, &#x60;crvUSD&#x60;, &#x60;DAI&#x60;, &#x60;EUR&#x60;, &#x60;LUSD&#x60;, &#x60;MKR&#x60;, &#x60;osETH&#x60;, &#x60;rETH&#x60;, &#x60;SNX&#x60;, &#x60;STG&#x60;, &#x60;tBTC&#x60;, &#x60;USDC&#x60;, &#x60;UNI&#x60;, &#x60;USDT&#x60;, &#x60;VIRTUAL&#x60;, &#x60;WBTC&#x60;, &#x60;weETH&#x60;, &#x60;WETH&#x60;, &#x60;wstETH&#x60;&lt;br&gt;&lt;br&gt; | 
**amount_in** | [**AmountIn1**](AmountIn1.md) |  | 
**amount_out_min** | [**AmountOutMin**](AmountOutMin.md) |  | 
**stable** | **bool** | If true, try to trade on a stable pool with a bonding curve of K&#x3D;x^3y+y^3x. If false, try to trade on a volatile pool with a bonding curve of K&#x3D;xy | 
**to** | **str** |  | [optional] 

## Example

```python
from compass.api_client.models.aerodrome_swap_eth_for_token_call_data import AerodromeSwapEthForTokenCallData

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSwapEthForTokenCallData from a JSON string
aerodrome_swap_eth_for_token_call_data_instance = AerodromeSwapEthForTokenCallData.from_json(json)
# print the JSON string representation of the object
print(AerodromeSwapEthForTokenCallData.to_json())

# convert the object into a dict
aerodrome_swap_eth_for_token_call_data_dict = aerodrome_swap_eth_for_token_call_data_instance.to_dict()
# create an instance of AerodromeSwapEthForTokenCallData from a dict
aerodrome_swap_eth_for_token_call_data_from_dict = AerodromeSwapEthForTokenCallData.from_dict(aerodrome_swap_eth_for_token_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


