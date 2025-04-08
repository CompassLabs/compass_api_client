# PriceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**token** | [**Token**](Token.md) | The symbol of the token for which to get the price Note the [supported tokens per chain](/#/#token-table). | 

## Example

```python
from compass.api_client.models.price_request import PriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PriceRequest from a JSON string
price_request_instance = PriceRequest.from_json(json)
# print the JSON string representation of the object
print(PriceRequest.to_json())

# convert the object into a dict
price_request_dict = price_request_instance.to_dict()
# create an instance of PriceRequest from a dict
price_request_from_dict = PriceRequest.from_dict(price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


