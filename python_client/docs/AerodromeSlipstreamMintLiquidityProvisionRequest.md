# AerodromeSlipstreamMintLiquidityProvisionRequest

Request model for minting a new liquidity position.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token0** | [**Token**](Token.md) | The symbol of the first token in the pair Note the [supported tokens per chain](/#/#token-table). | 
**token1** | [**Token**](Token.md) | The symbol of the second token in the pair Note the [supported tokens per chain](/#/#token-table). | 
**tick_spacing** | **int** | The tick spacing of the pool | 
**tick_lower** | **int** | The lower tick of the range to mint the position in | 
**tick_upper** | **int** | The upper tick of the range to mint the position in | 
**amount0_desired** | [**Amount0Desired**](Amount0Desired.md) |  | 
**amount1_desired** | [**Amount1Desired**](Amount1Desired.md) |  | 
**amount0_min** | [**Amount0Min**](Amount0Min.md) |  | 
**amount1_min** | [**Amount1Min**](Amount1Min.md) |  | 
**recipient** | **str** |  | [optional] 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']

## Example

```python
from compass.api_client.models.aerodrome_slipstream_mint_liquidity_provision_request import AerodromeSlipstreamMintLiquidityProvisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AerodromeSlipstreamMintLiquidityProvisionRequest from a JSON string
aerodrome_slipstream_mint_liquidity_provision_request_instance = AerodromeSlipstreamMintLiquidityProvisionRequest.from_json(json)
# print the JSON string representation of the object
print(AerodromeSlipstreamMintLiquidityProvisionRequest.to_json())

# convert the object into a dict
aerodrome_slipstream_mint_liquidity_provision_request_dict = aerodrome_slipstream_mint_liquidity_provision_request_instance.to_dict()
# create an instance of AerodromeSlipstreamMintLiquidityProvisionRequest from a dict
aerodrome_slipstream_mint_liquidity_provision_request_from_dict = AerodromeSlipstreamMintLiquidityProvisionRequest.from_dict(aerodrome_slipstream_mint_liquidity_provision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


