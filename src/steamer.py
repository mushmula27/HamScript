import sys
from lexer import Lexer
from parser import Parser

if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1].endswith('.ham'):
        fname = sys.argv[1]
        with open(fname, 'r') as f:
            source = list(f.read())

        parser = Parser(Lexer(source))
        ast = parser.parse().getast()
        print('\n\n', ast)
    else:
        print('Must supply a .ham file to interpret')
