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
    COMP = {
        '0':   '101010',
        '1':   '111111',
        '-1':  '111010',
        'D':   '001100',
        'A':   '110000',
        'M':   '110000',
        '!D':  '001101',
        '!A':  '110001',
        '!M':  '110001',
        '-D':  '001111',
        '-A':  '110011',
        '-M':  '110011',
        'D+1': '011111',
        'A+1': '110111',
        'M+1': '110111',
        'D-1': '001110',
        'A-1': '110010',
        'M-1': '110010',
        'D+A': '000010',
        'D+M': '000010',
        'D-A': '010011',
        'D-M': '010011',
        'A-D': '000111',
        'M-D': '000111',
        'D&A': '000000',
        'D&M': '000000',
        'D|A': '010101',
        'D|M': '010101'
    }
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

        >>> c.comp('A')
        '0110000'
        >>> c.comp('M')
        '1110000'
        """
        a = '1' if 'M' in symbol else '0'
        return a + self.COMP[symbol]

    def jump(self, symbol: str) -> str:
        """
        translates symbol into 3 bits binary code.
        """
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'c': Code()})