"""
How to get the token balance of a wallet using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.api.others_api import OthersApi
from compass.api_client.models.get_erc20_balance import GetErc20Balance

generic_api = OthersApi()

chain = "ethereum:mainnet"
user = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
token = "WETH"

payload = {
    "chain": chain,
    "user": user,
    "token": token,
}
token_balance = GetErc20Balance.from_dict(payload)

response = generic_api.process_request_v0_generic_balance_get_post_with_http_info(token_balance)
print(f"{token} balance:", response.data.amount)
