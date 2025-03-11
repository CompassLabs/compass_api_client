# Position


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **int** |  | 
**operator** | **str** |  | 
**token0** | [**Token**](Token.md) |  | 
**token1** | [**Token**](Token.md) |  | 
**fee** | [**FeeEnum**](FeeEnum.md) |  | 
**tick_lower** | **int** |  | 
**tick_upper** | **int** |  | 
**liquidity** | **int** |  | 
**fee_growth_inside0_last_x128** | **int** |  | 
**fee_growth_inside1_last_x128** | **int** |  | 
**tokens_owed0** | **int** |  | 
**tokens_owed1** | **int** |  | 
**token_id** | **int** |  | 

## Example

```python
from compass.api_client.models.position import Position

# TODO update the JSON string below
json = "{}"
# create an instance of Position from a JSON string
position_instance = Position.from_json(json)
# print the JSON string representation of the object
print(Position.to_json())

# convert the object into a dict
position_dict = position_instance.to_dict()
# create an instance of Position from a dict
position_from_dict = Position.from_dict(position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


