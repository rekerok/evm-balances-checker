import json
import os
from .config_networks import networks
from config import prices_tokens

ROOT_DIR = ""
ABIS_DIR = os.path.join(ROOT_DIR, "abis")
FILES_DIR = os.path.join(ROOT_DIR, "files")
PATH_ERC20_TOKEN = os.path.join(ABIS_DIR, "ERC20Token.json")
PATH_FILE_WALLETS = os.path.join(FILES_DIR, "wallets.txt")


def get_abi_erc_token():
    with open(PATH_ERC20_TOKEN) as json_file:
        data = json.load(json_file)
    return data


def get_wallets_list():
    with open(PATH_FILE_WALLETS, "r") as wallets_txt:
        wallets = wallets_txt.read().splitlines(keepends=False)
        wallets = list(filter(None, wallets))
    return wallets


def get_rpc_network(network="ethereum"):
    return networks[network]["rpc"]


def get_tokens_prices(names_token):
    pass


def get_price_token(symbol):
    if symbol.upper() == "BTCB" or symbol.upper() == "BTC.B":
        symbol = "BTC"
    if symbol.upper() == "USDBC":
        symbol = "USDC"
    for i in prices_tokens:
        if i["currency_pair"] == f"{symbol}_USD":
            return float(i["last"])
        if i["currency_pair"] == f"{symbol}_USDT":
            return float(i["last"])
        if i["currency_pair"] == f"{symbol}_USDC":
            return float(i["last"])
        
    return 0
