class AInstruction:

    @classmethod
    def to_binary(cls, address):
        return format(int(address), "016b")

    def set_symbol(self, symbol):
        self.symbol = symbol
