from web3 import Web3

max_gwei = 30
num_daily_tx = 75
RPC_URL = "https://rpc.api.lisk.com"
RPC_ETH = "https://eth.llamarpc.com"
CONTRACT_ADDRESS = "0x4200000000000000000000000000000000000006"
GRAPHQL_URL = "https://portal-api.lisk.com/graphql"
AMOUNT_ETH = 0.0000000001  # ETH amount per transaction
web3 = Web3(Web3.HTTPProvider(RPC_URL))
check_gass = Web3(Web3.HTTPProvider(RPC_ETH))
contract_abi = '''
[
    {
        "constant": false,
        "inputs": [],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
]
'''
