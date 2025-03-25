# TokensRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 

## Example

```python
from compass.api_client.models.tokens_request import TokensRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokensRequest from a JSON string
tokens_request_instance = TokensRequest.from_json(json)
# print the JSON string representation of the object
print(TokensRequest.to_json())

# convert the object into a dict
tokens_request_dict = tokens_request_instance.to_dict()
# create an instance of TokensRequest from a dict
tokens_request_from_dict = TokensRequest.from_dict(tokens_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


