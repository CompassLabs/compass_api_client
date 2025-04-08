# IncreaseAllowanceRequest

Request model for increasing token allowance for a contract.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | [**Token**](Token.md) | The symbol of the token for which the allowance is increased.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**contract_name** | [**ContractName**](ContractName.md) | The name of the contract to increase allowance for. | 
**amount** | [**Amount4**](Amount4.md) |  | 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 

## Example

```python
from compass.api_client.models.increase_allowance_request import IncreaseAllowanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IncreaseAllowanceRequest from a JSON string
increase_allowance_request_instance = IncreaseAllowanceRequest.from_json(json)
# print the JSON string representation of the object
print(IncreaseAllowanceRequest.to_json())

# convert the object into a dict
increase_allowance_request_dict = increase_allowance_request_instance.to_dict()
# create an instance of IncreaseAllowanceRequest from a dict
increase_allowance_request_from_dict = IncreaseAllowanceRequest.from_dict(increase_allowance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


