"""
How to get Aave position summary of a user for a specific token using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.api.aave_v3_api import AaveV3Api
from compass.api_client.models.aave_get_user_position_per_token import AaveGetUserPositionPerToken

aave_api = AaveV3Api()

chain = "ethereum:mainnet"
user = "0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"
asset = "WETH"

payload = {
    "chain": chain,
    "user": user,
    "asset": asset,
}
aave_position_summary = AaveGetUserPositionPerToken.from_dict(payload)

response = aave_api.process_request_v0_aave_user_position_per_token_get_post_with_http_info(aave_position_summary)

print(f"aToken Balance: {response.data.atoken_balance}")
print(f"Liquidity Rate: {response.data.liquidity_rate}")
print(f"Variable Borrow Rate: {response.data.variable_borrow_rate}")
print(f"Stable Borrow Rate: {response.data.stable_borrow_rate}")
print(f"Stable Debt:", response.data.stable_debt)
print(f"Variable Debt:", response.data.variable_debt)
