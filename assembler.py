import sys

class Assembler:
    def __init__(self, file: str):
        """
        arguments:
        file: the filename of the hack program
        """
        pass

    def convert(self):
        pass

    def save(self):
        pass

def main():
    if len(sys.argv) < 2:
        print('Hack assembler')
        print('\nUsage: python3 assembler.py file')
    else:
        assembler = Assembler(sys.argv[1])
        assembler.convert()

if __name__ == '__main__':
    main()