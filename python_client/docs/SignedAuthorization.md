# SignedAuthorization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **int** |  | 
**address** | **str** |  | 
**chain_id** | **int** |  | 
**r** | [**R**](R.md) |  | 
**s** | [**S**](S.md) |  | 
**y_parity** | **int** |  | 

## Example

```python
from compass.api_client.models.signed_authorization import SignedAuthorization

# TODO update the JSON string below
json = "{}"
# create an instance of SignedAuthorization from a JSON string
signed_authorization_instance = SignedAuthorization.from_json(json)
# print the JSON string representation of the object
print(SignedAuthorization.to_json())

# convert the object into a dict
signed_authorization_dict = signed_authorization_instance.to_dict()
# create an instance of SignedAuthorization from a dict
signed_authorization_from_dict = SignedAuthorization.from_dict(signed_authorization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


