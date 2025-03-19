"""
How to visualize the token balances of a wallet using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

import base64
from compass.api_client.api.others_api import OthersApi
from compass.api_client.models.request_user_address import RequestUserAddress

generic_api = OthersApi()

chain = "ethereum:mainnet"
user = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

payload = {
    "chain": chain,
    "user": user,
}
portfolio = RequestUserAddress.from_dict(payload)

response = generic_api.process_request_v0_generic_visualize_portfolio_get_post_with_http_info(portfolio)

image_data = response.data.image.split(",")[1]
decoded_image = base64.b64decode(image_data)

# save to an SVG file
output_file = "portfolio-pie-chart.svg"
with open(output_file, "wb") as file:
    file.write(decoded_image)

print(f"Portfolio visualization saved to {output_file}")
