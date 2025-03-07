# AaveAssetPriceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** | The price of the asset in USD. | 

## Example

```python
from compass.api_client.models.aave_asset_price_info import AaveAssetPriceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AaveAssetPriceInfo from a JSON string
aave_asset_price_info_instance = AaveAssetPriceInfo.from_json(json)
# print the JSON string representation of the object
print(AaveAssetPriceInfo.to_json())

# convert the object into a dict
aave_asset_price_info_dict = aave_asset_price_info_instance.to_dict()
# create an instance of AaveAssetPriceInfo from a dict
aave_asset_price_info_from_dict = AaveAssetPriceInfo.from_dict(aave_asset_price_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


