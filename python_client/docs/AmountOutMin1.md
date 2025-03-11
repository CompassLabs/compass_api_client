# AmountOutMin1

The minimal amount of ETH you are willing to receive (will revert if the swap gives you less)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from compass.api_client.models.amount_out_min1 import AmountOutMin1

# TODO update the JSON string below
json = "{}"
# create an instance of AmountOutMin1 from a JSON string
amount_out_min1_instance = AmountOutMin1.from_json(json)
# print the JSON string representation of the object
print(AmountOutMin1.to_json())

# convert the object into a dict
amount_out_min1_dict = amount_out_min1_instance.to_dict()
# create an instance of AmountOutMin1 from a dict
amount_out_min1_from_dict = AmountOutMin1.from_dict(amount_out_min1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


