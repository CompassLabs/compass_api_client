# BalanceInfoResponse

Response model for token balance information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount of tokens a particular address holds | 
**decimals** | **int** | Number of decimals of the token | 
**token_symbol** | [**Token**](Token.md) | Symbol of the token Note the [supported tokens per chain](/#/#token-table). | 
**token_address** | **str** | Address of the token | 

## Example

```python
from compass.api_client.models.balance_info_response import BalanceInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceInfoResponse from a JSON string
balance_info_response_instance = BalanceInfoResponse.from_json(json)
# print the JSON string representation of the object
print(BalanceInfoResponse.to_json())

# convert the object into a dict
balance_info_response_dict = balance_info_response_instance.to_dict()
# create an instance of BalanceInfoResponse from a dict
balance_info_response_from_dict = BalanceInfoResponse.from_dict(balance_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


