# UniswapCheckInRangeRequest

Endpoint parameters for checking if liquidity position is in active tick range on uniswap v3.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**token_id** | **int** | Token ID of the NFT representing the liquidity provisioned position. | 

## Example

```python
from compass.api_client.models.uniswap_check_in_range_request import UniswapCheckInRangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapCheckInRangeRequest from a JSON string
uniswap_check_in_range_request_instance = UniswapCheckInRangeRequest.from_json(json)
# print the JSON string representation of the object
print(UniswapCheckInRangeRequest.to_json())

# convert the object into a dict
uniswap_check_in_range_request_dict = uniswap_check_in_range_request_instance.to_dict()
# create an instance of UniswapCheckInRangeRequest from a dict
uniswap_check_in_range_request_from_dict = UniswapCheckInRangeRequest.from_dict(uniswap_check_in_range_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


