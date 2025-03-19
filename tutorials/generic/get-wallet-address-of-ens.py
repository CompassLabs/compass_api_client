"""
How to get the wallet address and registrant of an ENS address using Compass API Client.

Requirements:
    `pip install compass.api-client`
"""

from compass.api_client.api.others_api import OthersApi
from compass.api_client.models.request_ens_details import RequestEnsDetails

generic_api = OthersApi()

chain = "ethereum:mainnet"
ens_name = "vitalik.eth"

payload = {
    "chain": chain,
    "ens_name": ens_name,
}
ens_details = RequestEnsDetails.from_dict(payload)

response = generic_api.process_request_v0_generic_ens_get_post_with_http_info(ens_details)
print("Wallet address:", response.data.wallet_address)
