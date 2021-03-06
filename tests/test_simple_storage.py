from brownie import SimpleStorage, accounts, network

from scripts.deploy import get_account


def test_deploy():
    # Arrange

    account = accounts[0]

    # Acting

    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0

    # Asserting

    assert starting_value == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Acting
    expected = 15
    simple_storage.store(expected, {"from": account})
    # Asserting
    assert expected == simple_storage.retrieve()
