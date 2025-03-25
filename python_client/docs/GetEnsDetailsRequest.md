# GetEnsDetailsRequest

Request model for getting ENS details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**ens_name** | **str** | The ENS address of the user. | 

## Example

```python
from compass.api_client.models.get_ens_details_request import GetEnsDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetEnsDetailsRequest from a JSON string
get_ens_details_request_instance = GetEnsDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(GetEnsDetailsRequest.to_json())

# convert the object into a dict
get_ens_details_request_dict = get_ens_details_request_instance.to_dict()
# create an instance of GetEnsDetailsRequest from a dict
get_ens_details_request_from_dict = GetEnsDetailsRequest.from_dict(get_ens_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


