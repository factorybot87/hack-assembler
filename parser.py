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