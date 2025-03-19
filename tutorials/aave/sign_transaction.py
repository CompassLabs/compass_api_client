from web3 import Web3, HTTPProvider
import os
from dotenv import load_dotenv

load_dotenv()

ethereum_mainnet_rpc_url = os.environ.get("ETHEREUM_MAINNET_RPC_URL")
private_key = os.environ.get("PRIVATE_KEY")
w3 = Web3(HTTPProvider(ethereum_mainnet_rpc_url))

def sign_transaction(transaction_data):
    allowance_signed_transaction = w3.eth.account.sign_transaction(transaction_data, private_key)
    transaction_hash = w3.eth.send_raw_transaction(allowance_signed_transaction.raw_transaction)
    print(transaction_hash.hex())
