# AaveBorrowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**Token**](Token.md) | The symbol of the underlying asset to borrow.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**amount** | [**Amount**](Amount.md) |  | 
**interest_rate_mode** | [**InterestRateMode**](InterestRateMode.md) | The interest rate mode to borrow | 
**on_behalf_of** | **str** |  | [optional] 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 

## Example

```python
from compass.api_client.models.aave_borrow_request import AaveBorrowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AaveBorrowRequest from a JSON string
aave_borrow_request_instance = AaveBorrowRequest.from_json(json)
# print the JSON string representation of the object
print(AaveBorrowRequest.to_json())

# convert the object into a dict
aave_borrow_request_dict = aave_borrow_request_instance.to_dict()
# create an instance of AaveBorrowRequest from a dict
aave_borrow_request_from_dict = AaveBorrowRequest.from_dict(aave_borrow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


