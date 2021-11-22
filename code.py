class Code:
    DEST = {
        'null': '000',
        'M':    '001',
        'D':    '010',
        'DM':   '011',
        'MD':   '011',
        'A':    '100',
        'AM':   '101',
        'AD':   '110',
        'ADM':  '111'
    }
    COMP = {}
    JUMP = {}

    def dest(self, symbol: str) -> str:
        """
        translates symbol into 3 bits binary code.

        >>> c.dest('null')
        '000'
        """
        return self.DEST[symbol]

    def comp(self, symbol: str) -> str:
        """
        translates symbol into 7 bits binary code.
        """
        pass

    def jump(self, symbol: str) -> str:
        """
        translates symbol into 3 bits binary code.
        """
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'c': Code()})