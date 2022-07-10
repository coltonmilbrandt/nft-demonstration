from brownie import accounts, SimpleCollectible
from scripts.helpful_scripts import get_account

sample_token_uri = "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"

def main():
    deploy_and_create()

def deploy_and_create():
    account = get_account()
    print(f"Account: {account.address}")
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! You can now view your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}"
    )
    print("Please wait up to 20 minutes and then hit the refresh button.")
    return simple_collectible
    