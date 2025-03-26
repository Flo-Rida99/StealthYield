from web3 import Web3
from ai_agent.yield_optimizer import YieldOptimizerAgent

# Connect to NEAR/Aurora via Infura or RPC node
web3 = Web3(Web3.HTTPProvider('https://aurora-mainnet.infura.io/v3/YOUR_INFURA_KEY'))

contract_address = 'YOUR_DEPLOYED_CONTRACT_ADDRESS'
abi = '[ABI_JSON]'  # ABI from compiled StealthYieldIntent.sol

contract = web3.eth.contract(address=contract_address, abi=abi)

def fetch_user_intent(user_address):
    intent = contract.functions.getIntent(user_address).call()
    return {
        'user': intent[0],
        'yieldTarget': intent[1],
        'timestamp': intent[2]
    }

if __name__ == "__main__":
    user_address = 'USER_ETH_ADDRESS'
    user_intent = fetch_user_intent(user_address)

    agent = YieldOptimizerAgent(user_intent)
    agent.optimize_portfolio()
