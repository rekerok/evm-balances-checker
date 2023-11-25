class TokenAmount:
    def __init__(self, wei, decimals=18) -> None:
        self.wei = wei
        self.decimals = decimals
        self.ether = self.wei / 10**self.decimals
