# AerodromeLiquidityProvisionCallData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_a** | [**Token**](Token.md) | The symbol of the token to provide liquidity for&lt;br&gt; Note the supported tokens per chain:&lt;br&gt;**ethereum:mainnet**: [&#39;1INCH&#39;, &#39;AAVE&#39;, &#39;BAL&#39;, &#39;cbBTC&#39;, &#39;cbETH&#39;, &#39;CRV&#39;, &#39;crvUSD&#39;, &#39;DAI&#39;, &#39;ENS&#39;, &#39;ETHx&#39;, &#39;FRAX&#39;, &#39;FXS&#39;, &#39;GHO&#39;, &#39;KNC&#39;, &#39;LDO&#39;, &#39;LINK&#39;, &#39;LUSD&#39;, &#39;MKR&#39;, &#39;osETH&#39;, &#39;PYUSD&#39;, &#39;rETH&#39;, &#39;RPL&#39;, &#39;rsETH&#39;, &#39;sDAI&#39;, &#39;SNX&#39;, &#39;STG&#39;, &#39;sUSDe&#39;, &#39;tBTC&#39;, &#39;UNI&#39;, &#39;USDC&#39;, &#39;USDe&#39;, &#39;USDS&#39;, &#39;USDT&#39;, &#39;WBTC&#39;, &#39;weETH&#39;, &#39;WETH&#39;, &#39;wstETH&#39;]&lt;br&gt;**arbitrum:mainnet**: [&#39;AAVE&#39;, &#39;ARB&#39;, &#39;DAI&#39;, &#39;EURS&#39;, &#39;FRAX&#39;, &#39;GHO&#39;, &#39;LINK&#39;, &#39;LUSD&#39;, &#39;MAI&#39;, &#39;rETH&#39;, &#39;USDC&#39;, &#39;USDCe&#39;, &#39;USDT&#39;, &#39;WBTC&#39;, &#39;weETH&#39;, &#39;WETH&#39;, &#39;wstETH&#39;]&lt;br&gt;**base:mainnet**: [&#39;1INCH&#39;, &#39;AERO&#39;, &#39;ARB&#39;, &#39;BAL&#39;, &#39;cbBTC&#39;, &#39;cbETH&#39;, &#39;CRV&#39;, &#39;crvUSD&#39;, &#39;DAI&#39;, &#39;EUR&#39;, &#39;LUSD&#39;, &#39;MKR&#39;, &#39;osETH&#39;, &#39;rETH&#39;, &#39;SNX&#39;, &#39;STG&#39;, &#39;tBTC&#39;, &#39;USDC&#39;, &#39;UNI&#39;, &#39;USDT&#39;, &#39;VIRTUAL&#39;, &#39;WBTC&#39;, &#39;weETH&#39;, &#39;WETH&#39;, &#39;wstETH&#39;]&lt;br&gt; | 
**token_b** | [**Token**](Token.md) | The symbol of the token to provide liquidity for&lt;br&gt; Note the supported tokens per chain:&lt;br&gt;**ethereum:mainnet**: [&#39;1INCH&#39;, &#39;AAVE&#39;, &#39;BAL&#39;, &#39;cbBTC&#39;, &#39;cbETH&#39;, &#39;CRV&#39;, &#39;crvUSD&#39;, &#39;DAI&#39;, &#39;ENS&#39;, &#39;ETHx&#39;, &#39;FRAX&#39;, &#39;FXS&#39;, &#39;GHO&#39;, &#39;KNC&#39;, &#39;LDO&#39;, &#39;LINK&#39;, &#39;LUSD&#39;, &#39;MKR&#39;, &#39;osETH&#39;, &#39;PYUSD&#39;, &#39;rETH&#39;, &#39;RPL&#39;, &#39;rsETH&#39;, &#39;sDAI&#39;, &#39;SNX&#39;, &#39;STG&#39;, &#39;sUSDe&#39;, &#39;tBTC&#39;, &#39;UNI&#39;, &#39;USDC&#39;, &#39;USDe&#39;, &#39;USDS&#39;, &#39;USDT&#39;, &#39;WBTC&#39;, &#39;weETH&#39;, &#39;WETH&#39;, &#39;wstETH&#39;]&lt;br&gt;**arbitrum:mainnet**: [&#39;AAVE&#39;, &#39;ARB&#39;, &#39;DAI&#39;, &#39;EURS&#39;, &#39;FRAX&#39;, &#39;GHO&#39;, &#39;LINK&#39;, &#39;LUSD&#39;, &#39;MAI&#39;, &#39;rETH&#39;, &#39;USDC&#39;, &#39;USDCe&#39;, &#39;USDT&#39;, &#39;WBTC&#39;, &#39;weETH&#39;, &#39;WETH&#39;, &#39;wstETH&#39;]&lt;br&gt;**base:mainnet**: [&#39;1INCH&#39;, &#39;AERO&#39;, &#39;ARB&#39;, &#39;BAL&#39;, &#39;cbBTC&#39;, &#39;cbETH&#39;, &#39;CRV&#39;, &#39;crvUSD&#39;, &#39;DAI&#39;, &#39;EUR&#39;, &#39;LUSD&#39;, &#39;MKR&#39;, &#39;osETH&#39;, &#39;rETH&#39;, &#39;SNX&#39;, &#39;STG&#39;, &#39;tBTC&#39;, &#39;USDC&#39;, &#39;UNI&#39;, &#39;USDT&#39;, &#39;VIRTUAL&#39;, &#39;WBTC&#39;, &#39;weETH&#39;, &#39;WETH&#39;, &#39;wstETH&#39;]&lt;br&gt; | 
**stable** | **bool** | If true, try to provide liquidity on a stable pool with a bonding curve of K&#x3D;x^3y+y^3x. If false, try to provide liquidity on a volatile pool with a bonding curve of K&#x3D;xy | 
**amount_a_desired** | [**AmountADesired**](AmountADesired.md) |  | 
**amount_b_desired** | [**AmountBDesired**](AmountBDesired.md) |  | 
**amount_a_min** | [**AmountAMin**](AmountAMin.md) |  | 
**amount_b_min** | [**AmountBMin**](AmountBMin.md) |  | 
**to** | **str** |  | [optional] 
**deadline** | **int** |  | 

## Example

```python
from compass.api_client.models.aerodrome_liquidity_provision_call_data import AerodromeLiquidityProvisionCallData

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeLiquidityProvisionCallData from a JSON string
aerodrome_liquidity_provision_call_data_instance = AerodromeLiquidityProvisionCallData.from_json(json)
# print the JSON string representation of the object
print(AerodromeLiquidityProvisionCallData.to_json())

# convert the object into a dict
aerodrome_liquidity_provision_call_data_dict = aerodrome_liquidity_provision_call_data_instance.to_dict()
# create an instance of AerodromeLiquidityProvisionCallData from a dict
aerodrome_liquidity_provision_call_data_from_dict = AerodromeLiquidityProvisionCallData.from_dict(aerodrome_liquidity_provision_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


