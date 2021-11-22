class SymbolTable:
    def __init__(self):
        """
        attributes:
        symbols: contains the built-in symbols and the symbolic references.
        """
        pass
    
    def add_entry(self, symbol: str, address: int):
        """
        adds <symbol, address> pair to the table.
        """
        pass

    def contains(self, symbol: str) -> bool:
        """
        returns True if the symbol table contains the given symbol.
        """
        pass

    def get_address(self, symbol: str) -> int:
        """
        returns the address associated with the symbol.
        """
        pass