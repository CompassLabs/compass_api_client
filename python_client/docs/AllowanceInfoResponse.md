# AllowanceInfoResponse

Response model for token allowance information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount of tokens allowed to be spent by spender | 
**decimals** | **int** | Number of decimals of the token | 
**token_symbol** | [**Token**](Token.md) | Symbol of the token Note the [supported tokens per chain](/#/#token-table). | 
**token_address** | **str** | Address of the token | 
**contract_address** | **str** | Address of the contract | 

## Example

```python
from compass.api_client.models.allowance_info_response import AllowanceInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllowanceInfoResponse from a JSON string
allowance_info_response_instance = AllowanceInfoResponse.from_json(json)
# print the JSON string representation of the object
print(AllowanceInfoResponse.to_json())

# convert the object into a dict
allowance_info_response_dict = allowance_info_response_instance.to_dict()
# create an instance of AllowanceInfoResponse from a dict
allowance_info_response_from_dict = AllowanceInfoResponse.from_dict(allowance_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


