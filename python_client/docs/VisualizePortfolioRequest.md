# VisualizePortfolioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**user** | **str** | The address of the user. | 

## Example

```python
from compass.api_client.models.visualize_portfolio_request import VisualizePortfolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VisualizePortfolioRequest from a JSON string
visualize_portfolio_request_instance = VisualizePortfolioRequest.from_json(json)
# print the JSON string representation of the object
print(VisualizePortfolioRequest.to_json())

# convert the object into a dict
visualize_portfolio_request_dict = visualize_portfolio_request_instance.to_dict()
# create an instance of VisualizePortfolioRequest from a dict
visualize_portfolio_request_from_dict = VisualizePortfolioRequest.from_dict(visualize_portfolio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


