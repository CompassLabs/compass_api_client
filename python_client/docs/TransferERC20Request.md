# TransferERC20Request

Request model for transferring ERC20 tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | [**Chain**](Chain.md) |  | 
**sender** | **str** | The address of the transaction sender | 
**amount** | [**Amount5**](Amount5.md) |  | 
**token** | [**Token**](Token.md) | The symbol of the token to transfer.&lt;br&gt; Note the [supported tokens per chain](/#/#token-table).&lt;br&gt; | 
**to** | **str** | The recipient of the tokens. | 

## Example

```python
from compass.api_client.models.transfer_erc20_request import TransferERC20Request

# TODO update the JSON string below
json = "{}"
# create an instance of TransferERC20Request from a JSON string
transfer_erc20_request_instance = TransferERC20Request.from_json(json)
# print the JSON string representation of the object
print(TransferERC20Request.to_json())

# convert the object into a dict
transfer_erc20_request_dict = transfer_erc20_request_instance.to_dict()
# create an instance of TransferERC20Request from a dict
transfer_erc20_request_from_dict = TransferERC20Request.from_dict(transfer_erc20_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


