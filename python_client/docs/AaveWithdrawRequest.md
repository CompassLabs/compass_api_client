# AaveWithdrawRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**asset** | [**Token**](Token.md) | The symbol of the underlying asset to withdraw.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**amount** | [**Amount3**](Amount3.md) |  | 
**recipient** | **str** | The address of the recipient of the withdrawn funds. | 

## Example

```python
from compass.api_client.models.aave_withdraw_request import AaveWithdrawRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AaveWithdrawRequest from a JSON string
aave_withdraw_request_instance = AaveWithdrawRequest.from_json(json)
# print the JSON string representation of the object
print(AaveWithdrawRequest.to_json())

# convert the object into a dict
aave_withdraw_request_dict = aave_withdraw_request_instance.to_dict()
# create an instance of AaveWithdrawRequest from a dict
aave_withdraw_request_from_dict = AaveWithdrawRequest.from_dict(aave_withdraw_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


