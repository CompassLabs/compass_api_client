# UniswapGetSellQuoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**token_in** | [**Token**](Token.md) | The symbol of the token to swap from&lt;br&gt; Note the supported tokens per chain:&lt;br&gt;**ethereum:mainnet**:     &#x60;1INCH&#x60;, &#x60;AAVE&#x60;, &#x60;BAL&#x60;, &#x60;cbBTC&#x60;, &#x60;cbETH&#x60;, &#x60;CRV&#x60;, &#x60;crvUSD&#x60;, &#x60;DAI&#x60;, &#x60;ENS&#x60;, &#x60;ETHx&#x60;, &#x60;FRAX&#x60;, &#x60;FXS&#x60;, &#x60;GHO&#x60;, &#x60;KNC&#x60;, &#x60;LDO&#x60;, &#x60;LINK&#x60;, &#x60;LUSD&#x60;, &#x60;MKR&#x60;, &#x60;osETH&#x60;, &#x60;PYUSD&#x60;, &#x60;rETH&#x60;, &#x60;RPL&#x60;, &#x60;rsETH&#x60;, &#x60;sDAI&#x60;, &#x60;SNX&#x60;, &#x60;STG&#x60;, &#x60;sUSDe&#x60;, &#x60;tBTC&#x60;, &#x60;UNI&#x60;, &#x60;USDC&#x60;, &#x60;USDe&#x60;, &#x60;USDS&#x60;, &#x60;USDT&#x60;, &#x60;WBTC&#x60;, &#x60;weETH&#x60;, &#x60;WETH&#x60;, &#x60;wstETH&#x60;&lt;br&gt;&lt;br&gt;**arbitrum:mainnet**:     &#x60;AAVE&#x60;, &#x60;ARB&#x60;, &#x60;DAI&#x60;, &#x60;EURS&#x60;, &#x60;FRAX&#x60;, &#x60;GHO&#x60;, &#x60;LINK&#x60;, &#x60;LUSD&#x60;, &#x60;MAI&#x60;, &#x60;rETH&#x60;, &#x60;USDC&#x60;, &#x60;USDCe&#x60;, &#x60;USDT&#x60;, &#x60;WBTC&#x60;, &#x60;weETH&#x60;, &#x60;WETH&#x60;, &#x60;wstETH&#x60;&lt;br&gt;&lt;br&gt;**base:mainnet**:     &#x60;1INCH&#x60;, &#x60;AERO&#x60;, &#x60;ARB&#x60;, &#x60;BAL&#x60;, &#x60;cbBTC&#x60;, &#x60;cbETH&#x60;, &#x60;CRV&#x60;, &#x60;crvUSD&#x60;, &#x60;DAI&#x60;, &#x60;EUR&#x60;, &#x60;LUSD&#x60;, &#x60;MKR&#x60;, &#x60;osETH&#x60;, &#x60;rETH&#x60;, &#x60;SNX&#x60;, &#x60;STG&#x60;, &#x60;tBTC&#x60;, &#x60;USDC&#x60;, &#x60;UNI&#x60;, &#x60;USDT&#x60;, &#x60;VIRTUAL&#x60;, &#x60;WBTC&#x60;, &#x60;weETH&#x60;, &#x60;WETH&#x60;, &#x60;wstETH&#x60;&lt;br&gt;&lt;br&gt; | 
**token_out** | [**Token**](Token.md) | The symbol of the token to swap to&lt;br&gt; Note the supported tokens per chain:&lt;br&gt;**ethereum:mainnet**:     &#x60;1INCH&#x60;, &#x60;AAVE&#x60;, &#x60;BAL&#x60;, &#x60;cbBTC&#x60;, &#x60;cbETH&#x60;, &#x60;CRV&#x60;, &#x60;crvUSD&#x60;, &#x60;DAI&#x60;, &#x60;ENS&#x60;, &#x60;ETHx&#x60;, &#x60;FRAX&#x60;, &#x60;FXS&#x60;, &#x60;GHO&#x60;, &#x60;KNC&#x60;, &#x60;LDO&#x60;, &#x60;LINK&#x60;, &#x60;LUSD&#x60;, &#x60;MKR&#x60;, &#x60;osETH&#x60;, &#x60;PYUSD&#x60;, &#x60;rETH&#x60;, &#x60;RPL&#x60;, &#x60;rsETH&#x60;, &#x60;sDAI&#x60;, &#x60;SNX&#x60;, &#x60;STG&#x60;, &#x60;sUSDe&#x60;, &#x60;tBTC&#x60;, &#x60;UNI&#x60;, &#x60;USDC&#x60;, &#x60;USDe&#x60;, &#x60;USDS&#x60;, &#x60;USDT&#x60;, &#x60;WBTC&#x60;, &#x60;weETH&#x60;, &#x60;WETH&#x60;, &#x60;wstETH&#x60;&lt;br&gt;&lt;br&gt;**arbitrum:mainnet**:     &#x60;AAVE&#x60;, &#x60;ARB&#x60;, &#x60;DAI&#x60;, &#x60;EURS&#x60;, &#x60;FRAX&#x60;, &#x60;GHO&#x60;, &#x60;LINK&#x60;, &#x60;LUSD&#x60;, &#x60;MAI&#x60;, &#x60;rETH&#x60;, &#x60;USDC&#x60;, &#x60;USDCe&#x60;, &#x60;USDT&#x60;, &#x60;WBTC&#x60;, &#x60;weETH&#x60;, &#x60;WETH&#x60;, &#x60;wstETH&#x60;&lt;br&gt;&lt;br&gt;**base:mainnet**:     &#x60;1INCH&#x60;, &#x60;AERO&#x60;, &#x60;ARB&#x60;, &#x60;BAL&#x60;, &#x60;cbBTC&#x60;, &#x60;cbETH&#x60;, &#x60;CRV&#x60;, &#x60;crvUSD&#x60;, &#x60;DAI&#x60;, &#x60;EUR&#x60;, &#x60;LUSD&#x60;, &#x60;MKR&#x60;, &#x60;osETH&#x60;, &#x60;rETH&#x60;, &#x60;SNX&#x60;, &#x60;STG&#x60;, &#x60;tBTC&#x60;, &#x60;USDC&#x60;, &#x60;UNI&#x60;, &#x60;USDT&#x60;, &#x60;VIRTUAL&#x60;, &#x60;WBTC&#x60;, &#x60;weETH&#x60;, &#x60;WETH&#x60;, &#x60;wstETH&#x60;&lt;br&gt;&lt;br&gt; | 
**fee** | [**FeeEnum**](FeeEnum.md) | The fee to pay for the swap | 
**amount_in** | [**AmountIn**](AmountIn.md) |  | 

## Example

```python
from compass.api_client.models.uniswap_get_sell_quote_request import UniswapGetSellQuoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapGetSellQuoteRequest from a JSON string
uniswap_get_sell_quote_request_instance = UniswapGetSellQuoteRequest.from_json(json)
# print the JSON string representation of the object
print(UniswapGetSellQuoteRequest.to_json())

# convert the object into a dict
uniswap_get_sell_quote_request_dict = uniswap_get_sell_quote_request_instance.to_dict()
# create an instance of UniswapGetSellQuoteRequest from a dict
uniswap_get_sell_quote_request_from_dict = UniswapGetSellQuoteRequest.from_dict(uniswap_get_sell_quote_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


