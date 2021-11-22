import sys

from parser import Parser
from code import Code

class Assembler:
    WIDTH = 16
    A_PREFIX = '0'
    C_PREFIX = '111'

    def __init__(self, file: str):
        """
        arguments:
        file: the filename of the hack program.

        attribute:
        file: saves the arguments that has same name.
        binary_code: hack program in binary representation
        """
        self.file = file
        self.binary_code = []

    def convert(self):
        """
        converts a hack program to its binary representation.
        """
        parser = Parser(self.file)
        code   = Code()
        
        while parser.has_more_lines():
            parser.advance()
            if parser.instruction_type() == parser.A_INSTRUCTION:
                binary = self.A_PREFIX + \
                         Assembler.convert_decimal_to_15_bits_binary(int(parser.symbol()))
            elif parser.instruction_type() == parser.C_INSTRUCTION:
                binary = self.C_PREFIX + \
                         code.dest(parser.dest()) + \
                         code.comp(parser.comp()) + \
                         code.jump(parser.jump())
            self.binary_code.append(binary)

    def save(self):
        pass

    def convert_decimal_to_15_bits_binary(n: int) -> str:
        """
        >>> Assembler.convert_decimal_to_15_bits_binary(10)
        '000000000001010'
        """
        return str(bin(n))[2:].zfill(Assembler.WIDTH - len(Assembler.A_PREFIX))

def main():
    if len(sys.argv) < 2:
        print('Hack assembler')
        print('\nUsage: python3 assembler.py file')
    else:
        assembler = Assembler(sys.argv[1])
        assembler.convert()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()