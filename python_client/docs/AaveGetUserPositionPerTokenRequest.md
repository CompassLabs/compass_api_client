# AaveGetUserPositionPerTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**user** | **str** | The user to fetch the token-specific position of. | 
**asset** | [**Token**](Token.md) | The symbol of the asset to fetch the user&#39;s position on.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 

## Example

```python
from compass.api_client.models.aave_get_user_position_per_token_request import AaveGetUserPositionPerTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AaveGetUserPositionPerTokenRequest from a JSON string
aave_get_user_position_per_token_request_instance = AaveGetUserPositionPerTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AaveGetUserPositionPerTokenRequest.to_json())

# convert the object into a dict
aave_get_user_position_per_token_request_dict = aave_get_user_position_per_token_request_instance.to_dict()
# create an instance of AaveGetUserPositionPerTokenRequest from a dict
aave_get_user_position_per_token_request_from_dict = AaveGetUserPositionPerTokenRequest.from_dict(aave_get_user_position_per_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


