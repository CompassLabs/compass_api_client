"""
How to fetch on-chain prices from Aave using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.models.aave_get_asset_price_request import (
    AaveGetAssetPriceRequest,
)
from compass.api_client.api.aave_v3_api import AaveV3Api

aave_api = AaveV3Api()

chain = "ethereum:mainnet"
asset = "WETH"

payload = {
    "chain": chain,
    "asset": asset,
}
aave_get_asset_price_instance = AaveGetAssetPriceRequest.from_dict(payload)
assert aave_get_asset_price_instance is not None

response = aave_api.get_asset_price_v0_aave_asset_price_get_post_with_http_info(
    aave_get_asset_price_instance
)

print(f"Price of {asset}: $" + str(response.data.price))
