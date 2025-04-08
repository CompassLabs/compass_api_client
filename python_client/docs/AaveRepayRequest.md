# AaveRepayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**Token**](Token.md) | The symbol of the underlying asset to repay. Note the [supported tokens per chain](/#/#token-table). | 
**amount** | [**Amount1**](Amount1.md) |  | 
**interest_rate_mode** | [**InterestRateMode**](InterestRateMode.md) | The interest rate mode to borrow | 
**on_behalf_of** | **str** |  | [optional] 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | [default to '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B']

## Example

```python
from compass.api_client.models.aave_repay_request import AaveRepayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AaveRepayRequest from a JSON string
aave_repay_request_instance = AaveRepayRequest.from_json(json)
# print the JSON string representation of the object
print(AaveRepayRequest.to_json())

# convert the object into a dict
aave_repay_request_dict = aave_repay_request_instance.to_dict()
# create an instance of AaveRepayRequest from a dict
aave_repay_request_from_dict = AaveRepayRequest.from_dict(aave_repay_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


