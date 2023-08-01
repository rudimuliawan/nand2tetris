SYMBOL_ALLOCATOR = {}


class Allocator:

    SYMBOL_ALLOCATOR = {}
    CURRENT_ADDRESS = 16

    def __init__(self) -> None:
        pass

    def allocate_memory(cls, symbol):
        SYMBOL_ALLOCATOR = {
            symbol: Allocator.CURRENT_ADDRESS
        }

        Allocator.CURRENT_ADDRESS += 1
