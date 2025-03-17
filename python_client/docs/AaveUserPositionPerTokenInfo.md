# AaveUserPositionPerTokenInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atoken_balance** | **str** | The balance of AAVE aTokens (interest-bearing representations of your deposits). | 
**stable_debt** | **str** | The amount of the user&#39;s debt with a fixed interest rate. | 
**variable_debt** | **str** | The amount of the user&#39;s debt with a variable interest rate. | 
**principal_stable_debt** | **str** | The amount of the user&#39;s debt that was part of the initial principal of all loans with a stable interest rate. | 
**principal_variable_debt** | **str** | The amount of the user&#39;s debt that was part of the initial principal of all loans with a variable interest rate. This is the value stored by AAVE, which may be slightly inaccurate, but reflects what AAVE believes you initially paid. | 
**stable_borrow_rate** | **str** | The current average annualised interest rate for all your stable loans in this pool. | 
**stable_borrow_rate_for_new_loans** | **str** | The annualised interest rate you would pay on a new stable loan. | 
**variable_borrow_rate** | **str** | The current annualised interest rate for variable rate loans in this pool. (This applies to both current and new loans.) | 
**liquidity_rate** | **str** | The annualised interest rate for deposited supplies. | 

## Example

```python
from compass.api_client.models.aave_user_position_per_token_info import AaveUserPositionPerTokenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AaveUserPositionPerTokenInfo from a JSON string
aave_user_position_per_token_info_instance = AaveUserPositionPerTokenInfo.from_json(json)
# print the JSON string representation of the object
print(AaveUserPositionPerTokenInfo.to_json())

# convert the object into a dict
aave_user_position_per_token_info_dict = aave_user_position_per_token_info_instance.to_dict()
# create an instance of AaveUserPositionPerTokenInfo from a dict
aave_user_position_per_token_info_from_dict = AaveUserPositionPerTokenInfo.from_dict(aave_user_position_per_token_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


