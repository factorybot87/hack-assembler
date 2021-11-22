class Parser:
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
        >>> p.input_file = []
        >>> p.has_more_lines()
        False
        """
        return len(self.input_file) > 0

    def advance(self):
        """
        reads next instruction from the input.
        skips empty line and comment.
        removes inline comment
        """
        instruction = self.input_file.pop(0)
        while instruction == '\n' or instruction.startswith('//'):
            instruction = self.input_file.pop(0)
        if '//' in instruction:
            instruction = instruction[:instruction.find('//')]
        self.instruction = instruction.strip()
            
if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'p': Parser('Add.asm')})