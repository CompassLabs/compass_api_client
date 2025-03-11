# RequestEnsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**ens_name** | **str** | The ENS address of the user. | 

## Example

```python
from compass.api_client.models.request_ens_details import RequestEnsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RequestEnsDetails from a JSON string
request_ens_details_instance = RequestEnsDetails.from_json(json)
# print the JSON string representation of the object
print(RequestEnsDetails.to_json())

# convert the object into a dict
request_ens_details_dict = request_ens_details_instance.to_dict()
# create an instance of RequestEnsDetails from a dict
request_ens_details_from_dict = RequestEnsDetails.from_dict(request_ens_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


