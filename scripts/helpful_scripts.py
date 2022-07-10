from brownie import accounts, network, config, Contract, VRFCoordinatorMock, LinkToken
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local", "local-ganache"]
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"
BREED_MAPPING = {0: "PUG", 1: "SHIBA INU", 2: "ST_BERNARD"}

def get_breed(breed_number):
    return BREED_MAPPING[breed_number]

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])

contract_to_mock = {
    "vrf_coordinator": VRFCoordinatorMock,
    "link_token": LinkToken
}

def get_contract(contract_name):
    """ This function will grab the contract addresses from the brownie config programatically

        Args: 
            contract_name (string)

        Returns:
            brownie.network.contract.ProjectContract: The most recently deployed version of this contract
    
    """

    contract_type = contract_to_mock[contract_name]

    # We need to create a mock price feed if in a local environment
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type) <= 0:
            # MockV3Aggregator.length
            deploy_mocks()
        contract = contract_type[-1]
        # MockV3Aggregator[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        # We will need, as always, to deploy a contract
        # Address
        # ABI
        contract = Contract.from_abi(contract_type._name, contract_address, contract_type.abi)
        # MockV3Aggregator.abi
    return contract

def deploy_mocks():
    """
    Use this script if you want to deploy mocks to a testnet
    """
    print(f"The active network in {network.show_active()}")
    print("Deploying mocks...")
    account = get_account()
    print("Deploying Mock Link Token...")
    link_token = LinkToken.deploy({"from": account})
    print(f"Link Token deployed to {link_token.address}")
    print("Deploying Mock VRFCoordinator...")
    vrf_coordinator = VRFCoordinatorMock.deploy(link_token.address, {"from": account})
    print(f"VRFCoordinator deployed to {vrf_coordinator.address}")
    print("Deployed")

def fund_with_link(contract_address, account=None, link_token=None, amount=1000000000000000000):
    account = account if account else get_account()
    link_token = link_token if link_token else get_contract("link_token")
    print(f"here is the link_token: {link_token}")
    funding_tx = link_token.transfer(contract_address, amount, {"from": account})
    print(f"here is tx: {funding_tx}")
    funding_tx.wait(1)
    print(f"Funded contract at {contract_address}!")
    return funding_tx