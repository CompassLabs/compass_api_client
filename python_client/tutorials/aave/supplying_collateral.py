"""
How to supply collateral on Aave using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.models.aave_supply_request import AaveSupplyRequest
from compass.api_client.api.aave_v3_api import AaveV3Api

aave_api = AaveV3Api()

# input parameters
chain = "ethereum:mainnet"
sender = "0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B"
asset = "WETH"
amount = "0.1"

payload = {"chain": chain, "sender": sender, "asset": asset, "amount": amount}

supply_collateral_query = AaveSupplyRequest.from_dict(payload)
assert supply_collateral_query is not None

try:
    response = aave_api.supply_v0_aave_supply_post_with_http_info(
        supply_collateral_query
    )
    print("Transaction hash to sign to execute this transaction:", response.data.data)
except Exception as e:
    print("Failed to generate transaction hash:", e)
