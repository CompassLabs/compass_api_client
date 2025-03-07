# UniswapCheckInRangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_range** | **bool** | Whether the position is in active tick range or not. If not in range, the position is not earning trading fees. | 

## Example

```python
from compass.api_client.models.uniswap_check_in_range_response import UniswapCheckInRangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapCheckInRangeResponse from a JSON string
uniswap_check_in_range_response_instance = UniswapCheckInRangeResponse.from_json(json)
# print the JSON string representation of the object
print(UniswapCheckInRangeResponse.to_json())

# convert the object into a dict
uniswap_check_in_range_response_dict = uniswap_check_in_range_response_instance.to_dict()
# create an instance of UniswapCheckInRangeResponse from a dict
uniswap_check_in_range_response_from_dict = UniswapCheckInRangeResponse.from_dict(uniswap_check_in_range_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


