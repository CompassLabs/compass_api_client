# AmountOutMin2

The minimal amount of token you are willing to receive (will revert if the         swap gives you less)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from compass.api_client.models.amount_out_min2 import AmountOutMin2

# TODO update the JSON string below
json = "{}"
# create an instance of AmountOutMin2 from a JSON string
amount_out_min2_instance = AmountOutMin2.from_json(json)
# print the JSON string representation of the object
print(AmountOutMin2.to_json())

# convert the object into a dict
amount_out_min2_dict = amount_out_min2_instance.to_dict()
# create an instance of AmountOutMin2 from a dict
amount_out_min2_from_dict = AmountOutMin2.from_dict(amount_out_min2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


