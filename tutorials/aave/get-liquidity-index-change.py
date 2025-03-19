"""
How to get the change in liquidity index of a token on Aave using Compass API Client.
This gives the amount a position will have increased (if supplied) or decreased (if borrowed) over a certain time period. 

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.api.aave_v3_api import AaveV3Api
from compass.api_client.models.aave_get_liquidity_change import AaveGetLiquidityChange

aave_api = AaveV3Api()

chain = "ethereum:mainnet"
start_block = 22080000
end_block = 22080794
asset = "WETH"

payload = {
    "chain": chain,
    "start_block": start_block,
    "end_block": end_block,
    "asset": asset,
}
liquidity_index_change = AaveGetLiquidityChange.from_dict(payload)

response = aave_api.process_request_v0_aave_liquidity_change_get_post_with_http_info(liquidity_index_change)

print(f"Liquidity index changed by {response.data.liquidity_change}% between {response.data.start_time} and {response.data.end_time}")
