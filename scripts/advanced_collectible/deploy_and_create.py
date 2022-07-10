from brownie import accounts, AdvancedCollectible
from scripts.helpful_scripts import get_account, OPENSEA_URL

def main():
    deploy_and_create()

def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy({"from": account})