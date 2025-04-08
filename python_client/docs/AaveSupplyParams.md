# AaveSupplyParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**Token**](Token.md) | The symbol of the underlying asset to supply as collateral. You can borrow against it. Note the [supported tokens per chain](/#/#token-table). | 
**amount** | [**Amount2**](Amount2.md) |  | 
**on_behalf_of** | **str** |  | [optional] 

## Example

```python
from compass.api_client.models.aave_supply_params import AaveSupplyParams

# TODO update the JSON string below
json = "{}"
# create an instance of AaveSupplyParams from a JSON string
aave_supply_params_instance = AaveSupplyParams.from_json(json)
# print the JSON string representation of the object
print(AaveSupplyParams.to_json())

# convert the object into a dict
aave_supply_params_dict = aave_supply_params_instance.to_dict()
# create an instance of AaveSupplyParams from a dict
aave_supply_params_from_dict = AaveSupplyParams.from_dict(aave_supply_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


