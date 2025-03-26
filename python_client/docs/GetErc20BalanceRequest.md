# GetErc20BalanceRequest

Request model for getting an ERC20 token balance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**user** | **str** | The user to get the ERC20 balance of. | 
**token** | [**Token**](Token.md) | The symbol of the token for which the balance is checked.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 

## Example

```python
from compass.api_client.models.get_erc20_balance_request import GetErc20BalanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetErc20BalanceRequest from a JSON string
get_erc20_balance_request_instance = GetErc20BalanceRequest.from_json(json)
# print the JSON string representation of the object
print(GetErc20BalanceRequest.to_json())

# convert the object into a dict
get_erc20_balance_request_dict = get_erc20_balance_request_instance.to_dict()
# create an instance of GetErc20BalanceRequest from a dict
get_erc20_balance_request_from_dict = GetErc20BalanceRequest.from_dict(get_erc20_balance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


