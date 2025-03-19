"""
How to borrow against your collateral on Aave using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.api.aave_v3_api import AaveV3Api
from compass.api_client.models.base_transaction_request_aave_borrow_call_data import BaseTransactionRequestAaveBorrowCallData

aave_api = AaveV3Api()

# input parameters
chain = "ethereum:mainnet"
sender = "0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B"
asset = "WETH"
amount = 0.1
interest_rate_mode = 1  # 1 for stable, 2 for variable

# dictionary for call_data - optional on_behalf_of field, defaults to sender
call_data = {"asset": asset, "amount": amount, "interest_rate_mode": interest_rate_mode}

payload = {
    "chain": chain,
    "sender": sender,
    "call_data": call_data,
}

borrow_query = BaseTransactionRequestAaveBorrowCallData.from_dict(payload)

try:
    response = aave_api.process_request_v0_aave_borrow_post_with_http_info(borrow_query)
    print("Transaction hash to sign to execute this transaction:", response.data.data)
except Exception as e:
    print("Failed to generate transaction hash:", e)
