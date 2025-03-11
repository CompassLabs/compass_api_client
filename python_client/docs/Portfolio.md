# Portfolio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_value_in_usd** | **str** | Total value of the portfolio in USD | 
**token_balances** | [**List[TokenBalance]**](TokenBalance.md) | List of token balances in the portfolio | 

## Example

```python
from compass.api_client.models.portfolio import Portfolio

# TODO update the JSON string below
json = "{}"
# create an instance of Portfolio from a JSON string
portfolio_instance = Portfolio.from_json(json)
# print the JSON string representation of the object
print(Portfolio.to_json())

# convert the object into a dict
portfolio_dict = portfolio_instance.to_dict()
# create an instance of Portfolio from a dict
portfolio_from_dict = Portfolio.from_dict(portfolio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


