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
        returns True if there are more lines in the input
        """
        return len(self.input_file) > 0