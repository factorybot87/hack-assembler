import sys

from parser import Parser
from code import Code
from symbol_table import SymbolTable

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
        binary_code: hack program in binary representation.
        symbol_table: contains the built-in symbols and the symbolic references.
        """
        self.file = file
        self.binary_code = []
        self.symbol_table = SymbolTable()

    def first_pass(self):
        """
        builds a symbol table that contains all the label symbols.

        >>> a.first_pass()
        >>> a.symbol_table.contains('OUTPUT_D')
        True
        >>> a.symbol_table.get_address('OUTPUT_D')
        16
        >>> a.symbol_table.contains('OUTPUT_FIRST')
        True
        >>> a.symbol_table.get_address('OUTPUT_FIRST')
        2
        """
        parser = Parser(self.file)
        line_nunber_counter = -1
        next_available_address = 16

        while parser.has_more_lines():
            parser.advance()
            if parser.instruction_type() == parser.L_INSTRUCTION:
                self.symbol_table.add_entry(parser.symbol(), line_nunber_counter + 1)
            else:
                line_nunber_counter += 1
                if parser.instruction_type() == parser.A_INSTRUCTION:
                    if not parser.symbol().isnumeric() and not self.symbol_table.contains(parser.symbol()):
                        self.symbol_table.add_entry(parser.symbol(), next_available_address)
                        next_available_address += 1

    def second_pass(self):
        """
        converts a hack program to its binary representation.

        >>> a.second_pass()
        >>> a.binary_code
        ['0000000000010000', '1110101010000111', '0000000000000000', '1111110000010000']
        """
        parser = Parser(self.file)
        code   = Code()

        while parser.has_more_lines():
            parser.advance()
            if parser.instruction_type() == parser.A_INSTRUCTION:
                address = parser.symbol() if parser.symbol().isnumeric() else self.symbol_table.get_address(parser.symbol())
                binary = self.A_PREFIX + \
                         Assembler.convert_decimal_to_binary_bits(int(address))
            elif parser.instruction_type() == parser.C_INSTRUCTION:
                binary = self.C_PREFIX + \
                         code.comp(parser.comp()) + \
                         code.dest(parser.dest()) + \
                         code.jump(parser.jump())
            else:
                continue
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
        assembler.first_pass()
        assembler.second_pass()
        assembler.save()

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'a': Assembler('test.asm')})
    main()