"""
How to withdraw collateral on Aave using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.api.aave_v3_api import AaveV3Api
from compass.api_client.models.base_transaction_request_aave_withdraw_call_data import BaseTransactionRequestAaveWithdrawCallData

aave_api = AaveV3Api()

# input parameters
chain = "ethereum:mainnet"
sender = "0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B"
asset = "WETH"
amount = 0.1
recipient = "0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B"

call_data = {"asset": asset, "amount": amount, "recipient": recipient}

payload = {
    "chain": chain,
    "sender": sender,
    "call_data": call_data,
}

withdraw_query = BaseTransactionRequestAaveWithdrawCallData.from_dict(payload)

try:
    response = aave_api.process_request_v0_aave_withdraw_post_with_http_info(withdraw_query)
    print("Transaction hash to sign to execute this transaction:", response.data.data)
except Exception as e:
    print("Failed to generate transaction hash:", e)
