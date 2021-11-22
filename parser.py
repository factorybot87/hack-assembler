class Parser:
    def __init__(self, file: str):
        """
        arguments:
        file: the filename of the hack program 

        attributes:
        file_input: list of lines that reads from file.
        """
        with open(file) as f:
            self.file_input = f.readlines()

    def has_more_lines(self) -> bool:
        """
        returns True if there are more lines in the input.

        >>> p.has_more_lines()
        True
        >>> p.file_input = []
        >>> p.has_more_lines()
        False
        """
        return len(self.file_input) > 0

    def advance(self) -> str:
        """
        reads next instruction from the input. 
        """
        return ''

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'p': Parser('test.asm')})