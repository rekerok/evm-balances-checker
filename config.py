import requests

round_numbers = 4  # сколько знаков после запятой использовать при выводе
prices_tokens = requests.get("https://api.gateio.ws/api/v4/spot/tickers").json()


def check_balances():
    output_in_usd = True
    chains = {
        "ethereum": [
            "",  # native
            "0xdac17f958d2ee523a2206206994597c13d831ec7",  # usdt
            "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",  # usdc
        ],
        "arbitrum": [
            "",  # native
            "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",  # usdt
            "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",  # usdc
            "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",  # usdce
            "0x2297aEbD383787A160DD0d9F71508148769342E3",  # btc.b
        ],
        "optimism": [
            "",  # native
            "0x94b008aa00579c1307b0ef2c499ad98a8ce58e58",  # usdt
            "0x7f5c764cbc14f9669b88837ca1490cca17c31607",  # usdc
            "0x7f5c764cbc14f9669b88837ca1490cca17c31607",
        ],
        "polygon": [
            "",  # native
            "0xc2132d05d31c914a87c6611c10748aeb04b58e8f",  # usdt
            "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",  # usdc
            "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",  # usdce
            "0x2297aEbD383787A160DD0d9F71508148769342E3",  # btc.b
        ],
        "avalanche": [
            "",  # native
            "0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7",  # usdt
            "0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E",  # usdc
            "0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664",  # usdce
            "0x152b9d0FdC40C096757F570A51E494bd4b943E50",  # btc.b
        ],
        "bsc": [
            "",  # native
            "0x55d398326f99059ff775485246999027b3197955",  # usdt
            "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",  # usdc
            "0x2297aebd383787a160dd0d9f71508148769342e3",  # btc.b
        ],
        "zkera": [
            "",  # native
        ],
        # "fantom": [
        #     "",  # native
        #     "0x1B27A9dE6a775F98aaA5B90B62a4e2A0B84DbDd9",  # usdt
        #     "0x04068DA6C83AFCFA0e13ba15A6696662335D5B75",  # usdc
        # ],
        # # "core": [
        # #     "",  # native
        # # ],
        # # "celo": [
        # #     "",  # native
        # # ],
        "nova": [
            "",  # native
            "0x750ba8b76187092B0D1E87E28daaf484d1b5273b",  # usdc
            "0xf823C3cD3CeBE0a1fA952ba88Dc9EEf8e0Bf46AD",  # arb
            "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",  # dai
            "0x1d05e4e72cD994cdF976181CfB0707345763564d",  # wbtc
        ],
        "base": [
            "",  # native
            "0xd9aAEc86B65D86f6A7B5B1b0c42FFA531710b6CA",  # usdc
        ],
        # "goerli": [
        # "",  # native
        # "0xd9aAEc86B65D86f6A7B5B1b0c42FFA531710b6CA",  # usdc
        # ],
    }

    return chains, output_in_usd
