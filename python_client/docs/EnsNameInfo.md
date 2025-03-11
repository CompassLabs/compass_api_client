# EnsNameInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_address** | **str** | The wallet address of the user | 
**registrant** | **str** | The registrant of the ENS | 

## Example

```python
from compass.api_client.models.ens_name_info import EnsNameInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EnsNameInfo from a JSON string
ens_name_info_instance = EnsNameInfo.from_json(json)
# print the JSON string representation of the object
print(EnsNameInfo.to_json())

# convert the object into a dict
ens_name_info_dict = ens_name_info_instance.to_dict()
# create an instance of EnsNameInfo from a dict
ens_name_info_from_dict = EnsNameInfo.from_dict(ens_name_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


