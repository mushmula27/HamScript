import sys
from lexer import Lexer

if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1].endswith('.ham'):
        fname = sys.argv[1]
        with open(fname, 'r') as f:
            source = list(f.read())

        lex = Lexer(source)
    else:
        print('Must supply a .ham file to interpret')
