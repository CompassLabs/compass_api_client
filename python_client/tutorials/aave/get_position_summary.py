"""
How to get Aave position summary of a user using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.models.aave_get_user_position_summary_request import (
    AaveGetUserPositionSummaryRequest,
)
from compass.api_client.api.aave_v3_api import AaveV3Api

aave_api = AaveV3Api()

chain = "ethereum:mainnet"
user = "0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"

payload = {
    "chain": chain,
    "user": user,
}
aave_position_summary = AaveGetUserPositionSummaryRequest.from_dict(payload)
assert aave_position_summary is not None

response = aave_api.get_user_position_summary_v0_aave_user_position_summary_get_post_with_http_info(
    aave_position_summary
)

print(f"Health Factor: {response.data.health_factor}")
print(f"Max LTV: {response.data.maximum_loan_to_value_ratio}")
print(f"Liquidation Threshold: {response.data.liquidation_threshold}")
print("Available Borrows:", response.data.available_borrows)
print("Total Debt:", response.data.total_debt)
print("Total Collateral:", response.data.total_collateral)
