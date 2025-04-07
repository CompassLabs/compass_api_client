# AaveRepayParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**Token**](Token.md) | The symbol of the underlying asset to repay.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**amount** | [**Amount1**](Amount1.md) |  | 
**interest_rate_mode** | [**InterestRateMode**](InterestRateMode.md) | The interest rate mode to borrow | 
**on_behalf_of** | **str** |  | [optional] 

## Example

```python
from compass.api_client.models.aave_repay_params import AaveRepayParams

# TODO update the JSON string below
json = "{}"
# create an instance of AaveRepayParams from a JSON string
aave_repay_params_instance = AaveRepayParams.from_json(json)
# print the JSON string representation of the object
print(AaveRepayParams.to_json())

# convert the object into a dict
aave_repay_params_dict = aave_repay_params_instance.to_dict()
# create an instance of AaveRepayParams from a dict
aave_repay_params_from_dict = AaveRepayParams.from_dict(aave_repay_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


