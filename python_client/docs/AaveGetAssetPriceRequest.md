# AaveGetAssetPriceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**asset** | [**Token**](Token.md) | The symbol of the asset whose price you want.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 

## Example

```python
from compass.api_client.models.aave_get_asset_price_request import AaveGetAssetPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AaveGetAssetPriceRequest from a JSON string
aave_get_asset_price_request_instance = AaveGetAssetPriceRequest.from_json(json)
# print the JSON string representation of the object
print(AaveGetAssetPriceRequest.to_json())

# convert the object into a dict
aave_get_asset_price_request_dict = aave_get_asset_price_request_instance.to_dict()
# create an instance of AaveGetAssetPriceRequest from a dict
aave_get_asset_price_request_from_dict = AaveGetAssetPriceRequest.from_dict(aave_get_asset_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


