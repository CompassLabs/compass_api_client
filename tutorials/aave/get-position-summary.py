"""
How to get Aave position summary of a user using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.api.aave_v3_api import AaveV3Api
from compass.api_client.models.aave_get_user_position_summary import AaveGetUserPositionSummary

aave_api = AaveV3Api()

chain = "ethereum:mainnet"
user = "0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"

payload = {
    "chain": chain,
    "user": user,
}
aave_position_summary = AaveGetUserPositionSummary.from_dict(payload)

response = aave_api.process_request_v0_aave_user_position_summary_get_post_with_http_info(aave_position_summary)

print(f"Health Factor: {response.data.health_factor}")
print(f"Max LTV: {response.data.maximum_loan_to_value_ratio}")
print(f"Liquidation Threshold: {response.data.liquidation_threshold}")
print(f"Available Borrows:", response.data.available_borrows)
print(f"Total Debt:", response.data.total_debt)
print(f"Total Collateral:", response.data.total_collateral)
