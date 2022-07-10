from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_contract, get_account
import pytest
from scripts.advanced_collectible.deploy_and_create import deploy_and_create

def test_can_create_advanced_collectible():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    # Act
    advanced_collectible, creation_transaction = deploy_and_create()
    requestId = creation_transaction.events["RequestedCollectible"]["requestId"]
    random_number = 777
        # This is like what the chainlink node would call back with, but mocked "777" for example is the random number
    get_contract("vrf_coordinator").callBackWithRandomness(requestId, random_number, advanced_collectible.address, {"from": get_account()})
    # Assert
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.tokenIdToBreed(0) == random_number % 3