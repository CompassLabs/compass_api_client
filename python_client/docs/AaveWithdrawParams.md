# AaveWithdrawParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**Token**](Token.md) | The symbol of the underlying asset to withdraw.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**amount** | [**Amount3**](Amount3.md) |  | 
**recipient** | **str** | The address of the recipient of the withdrawn funds. | 

## Example

```python
from compass.api_client.models.aave_withdraw_params import AaveWithdrawParams

# TODO update the JSON string below
json = "{}"
# create an instance of AaveWithdrawParams from a JSON string
aave_withdraw_params_instance = AaveWithdrawParams.from_json(json)
# print the JSON string representation of the object
print(AaveWithdrawParams.to_json())

# convert the object into a dict
aave_withdraw_params_dict = aave_withdraw_params_instance.to_dict()
# create an instance of AaveWithdrawParams from a dict
aave_withdraw_params_from_dict = AaveWithdrawParams.from_dict(aave_withdraw_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


