# RequestUserAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**user** | **str** | The address of the user. | 

## Example

```python
from compass.api_client.models.request_user_address import RequestUserAddress

# TODO update the JSON string below
json = "{}"
# create an instance of RequestUserAddress from a JSON string
request_user_address_instance = RequestUserAddress.from_json(json)
# print the JSON string representation of the object
print(RequestUserAddress.to_json())

# convert the object into a dict
request_user_address_dict = request_user_address_instance.to_dict()
# create an instance of RequestUserAddress from a dict
request_user_address_from_dict = RequestUserAddress.from_dict(request_user_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


