from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():

    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()

    print(stored_value)
    print("This is accoumt 0 :: -- :: ", accounts[0])

    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_val = simple_storage.retrieve()
    print(updated_stored_val)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


# print(account)
# account = accounts.load("frekoode")
# print(account)

# account = accounts.add(config["wallets"]["from_key"])
# print(account)


def main():
    deploy_simple_storage()
