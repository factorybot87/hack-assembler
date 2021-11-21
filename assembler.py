import sys

def main():
    if len(sys.argv) < 2:
        print('Hack assembler')
        print('\nUsage: python3 assembler.py file')
    else:
        assembler = Assembler()
        assembler.convert(sys.argv[1])

if __name__ == '__main__':
    main()