class Parser:
    def __init__(self, file: str):
        """
        arguments:
        file: the filename of the hack program 

        attributes:
        lines: list of lines that reads from file.
        """
        with open(file) as f:
            self.lines = f.readlines()

    def has_more_lines(self) -> bool:
        """
        returns True if there are more lines in the input
        """
        return False