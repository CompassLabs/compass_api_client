# PriceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_price_in_usd** | **str** |  | 

## Example

```python
from compass.api_client.models.price_response import PriceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PriceResponse from a JSON string
price_response_instance = PriceResponse.from_json(json)
# print the JSON string representation of the object
print(PriceResponse.to_json())

# convert the object into a dict
price_response_dict = price_response_instance.to_dict()
# create an instance of PriceResponse from a dict
price_response_from_dict = PriceResponse.from_dict(price_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


