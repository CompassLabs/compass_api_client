"""
How to get the wallet address and registrant of an ENS address using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.models.get_ens_details_request import GetEnsDetailsRequest
from compass.api_client.api.others_api import OthersApi

generic_api = OthersApi()

chain = "ethereum:mainnet"
ens_name = "vitalik.eth"

payload = {
    "chain": chain,
    "ens_name": ens_name,
}
ens_details = GetEnsDetailsRequest.from_dict(payload)
assert ens_details is not None

response = generic_api.get_ens_details_v0_generic_ens_get_post_with_http_info(
    ens_details
)
print("Wallet address:", response.data.wallet_address)
