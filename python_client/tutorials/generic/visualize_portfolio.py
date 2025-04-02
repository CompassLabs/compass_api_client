"""
How to visualize the token balances of a wallet using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.models.visualize_portfolio_request import (
    VisualizePortfolioRequest,
)
import base64
from compass.api_client.api.others_api import OthersApi

generic_api = OthersApi()

chain = "ethereum:mainnet"
user = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

payload = {
    "chain": chain,
    "user": user,
}
portfolio = VisualizePortfolioRequest.from_dict(payload)
assert portfolio is not None

response = generic_api.visualize_portfolio_v0_generic_visualize_portfolio_get_post_with_http_info(
    portfolio
)

image_data = response.data.image.split(",")[1]
decoded_image = base64.b64decode(image_data)

# save to an SVG file
output_file = "portfolio-pie-chart.svg"
with open(output_file, "wb") as file:
    file.write(decoded_image)

print(f"Portfolio visualization saved to {output_file}")
