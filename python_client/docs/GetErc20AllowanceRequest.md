# GetErc20AllowanceRequest

Request model for getting an ERC20 token allowance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**user** | **str** | The user to get the ERC20 allowance of. | 
**token** | [**Token**](Token.md) | The symbol of the token for which the allowance is checked. Note the [supported tokens per chain](/#/#token-table). | 
**contract_name** | [**ContractName**](ContractName.md) | The name of the contract to check allowance for. | 

## Example

```python
from compass.api_client.models.get_erc20_allowance_request import GetErc20AllowanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetErc20AllowanceRequest from a JSON string
get_erc20_allowance_request_instance = GetErc20AllowanceRequest.from_json(json)
# print the JSON string representation of the object
print(GetErc20AllowanceRequest.to_json())

# convert the object into a dict
get_erc20_allowance_request_dict = get_erc20_allowance_request_instance.to_dict()
# create an instance of GetErc20AllowanceRequest from a dict
get_erc20_allowance_request_from_dict = GetErc20AllowanceRequest.from_dict(get_erc20_allowance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


