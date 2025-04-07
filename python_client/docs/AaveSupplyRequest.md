# AaveSupplyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**Token**](Token.md) | The symbol of the underlying asset to supply as collateral. You can borrow against it.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**amount** | [**Amount2**](Amount2.md) |  | 
**on_behalf_of** | **str** |  | [optional] 
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 

## Example

```python
from compass.api_client.models.aave_supply_request import AaveSupplyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AaveSupplyRequest from a JSON string
aave_supply_request_instance = AaveSupplyRequest.from_json(json)
# print the JSON string representation of the object
print(AaveSupplyRequest.to_json())

# convert the object into a dict
aave_supply_request_dict = aave_supply_request_instance.to_dict()
# create an instance of AaveSupplyRequest from a dict
aave_supply_request_from_dict = AaveSupplyRequest.from_dict(aave_supply_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


