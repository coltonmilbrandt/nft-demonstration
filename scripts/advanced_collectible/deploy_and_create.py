from brownie import accounts, AdvancedCollectible, network, config
from scripts.helpful_scripts import get_account, OPENSEA_URL, get_contract

def main():
    deploy_and_create()

def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account}
    )