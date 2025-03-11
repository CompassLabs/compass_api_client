# GetLiquidityProvisionPositions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**user** | **str** | The address of the user to check the balance of | 

## Example

```python
from compass.api_client.models.get_liquidity_provision_positions import GetLiquidityProvisionPositions

# TODO update the JSON string below
json = "{}"
# create an instance of GetLiquidityProvisionPositions from a JSON string
get_liquidity_provision_positions_instance = GetLiquidityProvisionPositions.from_json(json)
# print the JSON string representation of the object
print(GetLiquidityProvisionPositions.to_json())

# convert the object into a dict
get_liquidity_provision_positions_dict = get_liquidity_provision_positions_instance.to_dict()
# create an instance of GetLiquidityProvisionPositions from a dict
get_liquidity_provision_positions_from_dict = GetLiquidityProvisionPositions.from_dict(get_liquidity_provision_positions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


