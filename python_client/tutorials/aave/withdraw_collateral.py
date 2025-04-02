"""
How to withdraw collateral on Aave using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.models.aave_withdraw_request import AaveWithdrawRequest
from compass.api_client.api.aave_v3_api import AaveV3Api

aave_api = AaveV3Api()

# input parameters
chain = "ethereum:mainnet"
sender = "0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B"
asset = "WETH"
amount = 0.1
recipient = "0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B"

call_data = {}

payload = {
    "chain": chain,
    "sender": sender,
    "asset": asset,
    "amount": amount,
    "recipient": recipient,
}

withdraw_query = AaveWithdrawRequest.from_dict(payload)
assert withdraw_query is not None

try:
    response = aave_api.withdraw_v0_aave_withdraw_post_with_http_info(withdraw_query)
    print("Transaction hash to sign to execute this transaction:", response.data.data)
except Exception as e:
    print("Failed to generate transaction hash:", e)
