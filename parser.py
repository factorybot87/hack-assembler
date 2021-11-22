class Parser:
    A_INSTRUCTION = 0
    C_INSTRUCTION = 1
    L_INSTRUCTION = 2

    def __init__(self, file: str):
        """
        arguments:
        file: the filename of the hack program 

        attributes:
        input_file: list of lines that reads from the file.
        instruction: current instruction reads from the input.
        """
        with open(file) as f:
            self.input_file = f.readlines()
        self.instruction = ''

    def has_more_lines(self) -> bool:
        """
        returns True if there are more lines in the input.

        >>> p.has_more_lines()
        True
        """
        return len(self.input_file) > 0

    def advance(self):
        """
        reads next instruction from the input.
        skips empty line and comment.
        removes inline comment

        >>> p.advance()
        >>> p.instruction
        '@2'
        """
        instruction = self.input_file.pop(0)
        while instruction == '\n' or instruction.startswith('//'):
            instruction = self.input_file.pop(0)
        if '//' in instruction:
            instruction = instruction[:instruction.find('//')]
        self.instruction = instruction.strip()

    def instruction_type(self) -> int:
        """
        returns the type of current instruction.

        >>> p.instruction = '@2'
        >>> p.instruction_type()
        0
        >>> p.instruction = 'D=A'
        >>> p.instruction_type()
        1
        >>> p.instruction = '0;jmp'
        >>> p.instruction_type()
        1
        >>> p.instruction = '(LABEL)'
        >>> p.instruction_type()
        2
        """
        if '@' in self.instruction:
            return self.A_INSTRUCTION
        elif '=' in self.instruction or ';' in self.instruction:
            return self.C_INSTRUCTION
        else:
            return self.L_INSTRUCTION

    def symbol(self) -> str:
        """
        returns xxx if current instruction is @xxx or (xxx)

        >>> p.instruction = '@xxx'
        >>> p.symbol()
        'xxx'
        >>> p.instruction = '(xxx)'
        >>> p.symbol()
        'xxx'
        """
        if self.instruction_type() == self.A_INSTRUCTION:
            return self.instruction[1:]
        else:
            return self.instruction[1:-1]

    def dest(self) -> str:
        """
        returns the dest part of the c instruction.

        >>> p.instruction = 'D=A'
        >>> p.dest()
        'D'
        """
        return self.instruction[:self.instruction.find('=')]

    def comp(self) -> str:
        """
        returns the comp part of the c instruction.

        >>> p.instruction = 'D=A'
        >>> p.comp()
        'A'
        >>> p.instruction = '0;JMP'
        >>> p.comp()
        '0'
        """
        if '=' in self.instruction:
            return self.instruction[self.instruction.find('=') + 1:]
        else:
            return self.instruction[:self.instruction.find(';')]

    def jump(self) -> str:
        """
        returns the jump part of the c instruction

        >>> p.instruction = '0;JMP'
        >>> p.jump()
        'JMP'
        """
        return self.instruction[self.instruction.find(';') + 1:]

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'p': Parser('Add.asm')})