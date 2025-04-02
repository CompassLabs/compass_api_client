"""
How to repay debt on Aave using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.models.aave_repay_request import AaveRepayRequest
from compass.api_client.api.aave_v3_api import AaveV3Api

aave_api = AaveV3Api()

# input parameters
chain = "arbitrum:mainnet"
sender = "0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B"
asset = "USDT"
amount = 1
interest_rate_mode = 2  # 1 for stable, 2 for variable

payload = {
    "chain": chain,
    "sender": sender,
    "asset": asset,
    "amount": amount,
    "interest_rate_mode": interest_rate_mode,
}

repay_query = AaveRepayRequest.from_dict(payload)
assert repay_query is not None

try:
    response = aave_api.repay_v0_aave_repay_post_with_http_info(repay_query)
    print("Transaction hash to sign to execute this transaction:", response.data.data)
except Exception as e:
    print("Failed to generate transaction hash:", e)
