from web3 import Web3
from ai_agent.yield_optimizer import YieldOptimizerAgent

# Connect to NEAR/Aurora via Infura or RPC node
web3 = Web3(Web3.HTTPProvider('https://aurora-mainnet.infura.io/v3/YOUR_INFURA_KEY'))

contract_address = '0x8f2c8f1b1e557ac8e657a66f7e54e1b6b6afed9d'
abi = '[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "user",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "yieldTarget",
				"type": "uint256"
			}
		],
		"name": "IntentSubmitted",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_yieldTarget",
				"type": "uint256"
			}
		],
		"name": "submitIntent",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_user",
				"type": "address"
			}
		],
		"name": "getIntent",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address",
						"name": "user",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "yieldTarget",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "timestamp",
						"type": "uint256"
					}
				],
				"internalType": "struct StealthYieldIntent.YieldIntent",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "yieldIntents",
		"outputs": [
			{
				"internalType": "address",
				"name": "user",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "yieldTarget",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]'  # ABI from compiled StealthYieldIntent.sol

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
