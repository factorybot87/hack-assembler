class SymbolTable:
    def __init__(self):
        """
        attributes:
        symbol_table: contains the built-in symbols and the symbolic references.
        """
        self.symbol_table = {
            'R0':     0,
            'R1':     1,
            'R2':     2,
            'R3':     3,
            'R4':     4,
            'R5':     5,
            'R6':     6,
            'R7':     7,
            'R8':     8,
            'R9':     9,
            'R10':    10,
            'R11':    11,
            'R12':    12,
            'R13':    13,
            'R14':    14,
            'R15':    15,
            'SP':     0,
            'LCL':    1,
            'ARG':    2,
            'THIS':   3,
            'THAT':   4,
            'SCREEN': 16384,
            'KBD':    24576,
        }
    
    def add_entry(self, symbol: str, address: int):
        """
        adds <symbol, address> pair to the table.
        
        >>> t.add_entry('ANSWER', 42)
        >>> t.symbol_table['ANSWER']
        42
        """
        self.symbol_table[symbol] = address

    def contains(self, symbol: str) -> bool:
        """
        returns True if the symbol table contains the given symbol.
        
        >>> t.contains('R0')
        True
        >>> t.contains('UNIVERSE')
        False
        """
        return not self.symbol_table.get(symbol) is None

    def get_address(self, symbol: str) -> int:
        """
        returns the address associated with the symbol.
        """
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'t': SymbolTable()})