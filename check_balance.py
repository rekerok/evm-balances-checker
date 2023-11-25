import csv
import eth_utils
from tqdm import tqdm
from web3 import Web3
from config import check_balances, round_numbers
from utils.tokenAmount import TokenAmount
from utils.utils import *
from utils.config_networks import networks


chaines, output_in_usd = check_balances()
tokens_name = dict()


def collect_balances():
    addresses = get_wallets_list()
    balances = []
    for address in tqdm(addresses):
        address = eth_utils.address.to_checksum_address(address)
        wallet_balances = {address: []}

        for network, coins in chaines.items():
            coins_name = list()
            network_balances = {network: []}
            for coin_address in coins:
                w3 = Web3(Web3.HTTPProvider(get_rpc_network(network)))

                if coin_address == "":
                    amount_token = TokenAmount(wei=w3.eth.get_balance(address))
                    name_token = networks[network]["currency"]

                else:
                    coin_address = eth_utils.address.to_checksum_address(coin_address)
                    contract = w3.eth.contract(
                        address=coin_address, abi=get_abi_erc_token()
                    )
                    amount_token = TokenAmount(
                        wei=contract.functions.balanceOf(address).call(),
                        decimals=contract.functions.decimals().call(),
                    )
                    name_token = contract.functions.symbol().call().upper()

                coin_balance = {
                    name_token: {
                        "amount": amount_token.ether,
                        "usd": get_price_token(name_token.upper()) * amount_token.ether,
                    }
                }
                network_balances[network].append(coin_balance)
                coins_name.append(name_token)
            wallet_balances[address].append(network_balances)
            tokens_name[network] = coins_name
        balances.append(wallet_balances)
    return balances


def get_rows_balance(balances, len_handler):
    result = []
    counter = 1
    for wallet in balances:
        wallet_info = [counter]
        counter += 1
        wallet_address = list(wallet.keys())[0]
        wallet_data = wallet[wallet_address]
        wallet_info.append(
            wallet_address
        )  # Начинаем формировать список для текущего кошелька
        for network_data in wallet_data:
            network_name = list(network_data.keys())[0]
            network_tokens = network_data[network_name]

            for token in network_tokens:
                token_name = list(token.keys())[0]
                token_usd = token[token_name]["usd" if output_in_usd else "amount"]

                # Добавляем информацию о текущей монете в список для текущего кошелька
                wallet_info.append(round(token_usd, round_numbers))
        # Вычисляем общую сумму на кошельке в USD и добавляем ее в конец списка для текущего кошелька
        wallet_total_usd = round(
            sum(wallet_info[2:len_handler]), round_numbers
        )  # Суммируем значения usd каждой монеты
        wallet_info.append(wallet_total_usd)
        result.append(wallet_info)
    return result


def get_balance_coins(balances):
    balance_of_one_token = dict()
    for wallet in balances:
        for network_data in wallet.values():
            for coins in network_data:
                for values in coins[list(coins.keys())[0]]:
                    name_token = list(values.keys())[0]
                    amount = values[name_token]["amount"]
                    amount_usd = values[name_token]["usd"]
                    if name_token in balance_of_one_token:
                        balance_of_one_token[name_token]["amount"] += amount
                        balance_of_one_token[name_token]["usd"] += amount_usd
                    else:
                        balance_of_one_token[name_token] = {
                            "amount": amount,
                            "usd": amount_usd,
                        }
    return balance_of_one_token


def get_rows_tokens(balance_coins):
    result = list()
    for coin, values in balance_coins.items():
        result.append([coin, values["amount"], values["usd"]])
    return result


def create_csv_file(balances):
    with open("files/balance.csv", "w") as file:
        writer = csv.writer(file)
        handler = list()
        handler.extend(["number", "wallet"])
        for network, coins in tokens_name.items():
            for coin in coins:
                handler.append(f"{network}-{coin}")
        handler.append("total no wallet usd")
        writer.writerow(handler)
        writer.writerows(get_rows_balance(balances, len(handler)))
        writer.writerow([] * 2)

        handler_coins = ["coin", "amount", "usd"]
        writer.writerow(handler_coins)
        rows_tokens = get_rows_tokens(get_balance_coins(balances))
        writer.writerows(rows_tokens)


def check_balance():
    balances = collect_balances()
    create_csv_file(balances)
