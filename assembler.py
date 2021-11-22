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

        >>> a.convert()
        >>> a.binary_code
        ['0000000000000010']
        """
        parser = Parser(self.file)
        code   = Code()
        
        while parser.has_more_lines():
            parser.advance()
            if parser.instruction_type() == parser.A_INSTRUCTION:
                binary = self.A_PREFIX + \
                         Assembler.convert_decimal_to_binary_bits(int(parser.symbol()))
            elif parser.instruction_type() == parser.C_INSTRUCTION:
                binary = self.C_PREFIX + \
                         code.comp(parser.comp()) + \
                         code.dest(parser.dest()) + \
                         code.jump(parser.jump())
            self.binary_code.append(binary)

    def save(self):
        """
        writes the binary code into a hack file.
        """
        with open(self.file.replace('asm', 'hack'), 'w') as f:
            for code in self.binary_code:
                f.writelines(code + '\n')

    def convert_decimal_to_binary_bits(n: int) -> str:
        """
        >>> Assembler.convert_decimal_to_binary_bits(10)
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
        assembler.save()

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'a': Assembler('test.asm')})
    main()