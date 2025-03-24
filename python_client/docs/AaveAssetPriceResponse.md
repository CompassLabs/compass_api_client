# AaveAssetPriceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** | The price of the asset in USD. | 

## Example

```python
from compass.api_client.models.aave_asset_price_response import AaveAssetPriceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AaveAssetPriceResponse from a JSON string
aave_asset_price_response_instance = AaveAssetPriceResponse.from_json(json)
# print the JSON string representation of the object
print(AaveAssetPriceResponse.to_json())

# convert the object into a dict
aave_asset_price_response_dict = aave_asset_price_response_instance.to_dict()
# create an instance of AaveAssetPriceResponse from a dict
aave_asset_price_response_from_dict = AaveAssetPriceResponse.from_dict(aave_asset_price_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


