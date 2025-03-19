"""
How to get the token balances of a wallet using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.api.others_api import OthersApi
from compass.api_client.models.request_user_address import RequestUserAddress

generic_api = OthersApi()

chain = "ethereum:mainnet"
user = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

payload = {
    "chain": chain,
    "user": user,
}
portfolio = RequestUserAddress.from_dict(payload)

response = generic_api.process_request_v0_generic_portfolio_get_post_with_http_info(portfolio)
print(f"Total portfolio value: ${float(response.data.total_value_in_usd):.2f}")
for token in response.data.token_balances:
    print(f"{token.amount} {token.token_symbol.name} = ${float(token.token_value_in_usd):.2f}")
