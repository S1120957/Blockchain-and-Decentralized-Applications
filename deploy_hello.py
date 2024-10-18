from brownie import HelloWorld, accounts

def main():
    acct = accounts.load("deployer_account")
    HelloWorld.deploy("Hello, Blockchain!", {'from': acct})
