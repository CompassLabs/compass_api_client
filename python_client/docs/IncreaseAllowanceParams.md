# IncreaseAllowanceParams

Parameters model for increasing token allowance for a contract.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | [**Token**](Token.md) | The symbol of the token for which the allowance is increased. Note the [supported tokens per chain](/#/#token-table). | 
**contract_name** | [**ContractName**](ContractName.md) | The name of the contract to increase allowance for. | 
**amount** | [**Amount4**](Amount4.md) |  | 

## Example

```python
from compass.api_client.models.increase_allowance_params import IncreaseAllowanceParams

# TODO update the JSON string below
json = "{}"
# create an instance of IncreaseAllowanceParams from a JSON string
increase_allowance_params_instance = IncreaseAllowanceParams.from_json(json)
# print the JSON string representation of the object
print(IncreaseAllowanceParams.to_json())

# convert the object into a dict
increase_allowance_params_dict = increase_allowance_params_instance.to_dict()
# create an instance of IncreaseAllowanceParams from a dict
increase_allowance_params_from_dict = IncreaseAllowanceParams.from_dict(increase_allowance_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


