# IncreaseAllowanceAnyRequest

Request model for increasing allowance for any arbitrary ERC20 token address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | [**Token**](Token.md) | The name of the token for which the allowance is increased. | 
**contract_name** | [**ContractName**](ContractName.md) | The name of the contract to increase allowance for. | 
**amount** | [**Amount4**](Amount4.md) |  | 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']

## Example

```python
from compass.api_client.models.increase_allowance_any_request import IncreaseAllowanceAnyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IncreaseAllowanceAnyRequest from a JSON string
increase_allowance_any_request_instance = IncreaseAllowanceAnyRequest.from_json(json)
# print the JSON string representation of the object
print(IncreaseAllowanceAnyRequest.to_json())

# convert the object into a dict
increase_allowance_any_request_dict = increase_allowance_any_request_instance.to_dict()
# create an instance of IncreaseAllowanceAnyRequest from a dict
increase_allowance_any_request_from_dict = IncreaseAllowanceAnyRequest.from_dict(increase_allowance_any_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


