# AaveWithdrawRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**Token**](Token.md) | The symbol of the underlying asset to withdraw. Note the [supported tokens per chain](/#/#token-table). | 
**amount** | [**Amount3**](Amount3.md) |  | 
**recipient** | **str** | The address of the recipient of the withdrawn funds. | 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']

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


