from rply import Token
from rply.token import SourcePosition

class Lexer:
    """
    The lexer takes a string or list of characters as input and will loop
    through each character in the sources to eventually produce a list of
    tokens that represent the syntax within the file.

    The core of this class is the tokenise() method. This is a generator
    function that will return a single token at a time until there are
    no tokens left to return.

    Properties:
        - self.source =>          this is the list of characters of the
                                  original source code

        - self.idx =>             holds the index within the source list that
                                  has been parsed up to

        - self.lineno =>          the line number within the original source
                                  file that self.idx is sitting on

        - self.columno =>         the current column number within the source
                                  file that self.idx is sitting on

        - self.current_value =>   a list of characters that accumulates as
                                  expressions are parsed. This can be variable
                                  names or language keywords etc. It is reset
                                  every time a new token is emitted

        - self.token_generator => this holds the actual generator that is
                                  produced by self.tokenise. It is then used
                                  within the next() method to emit the next
                                  token

    *** Notes ***
        self.lineno and self.columno are tracked so eventually informative
        errors can be returned to the user when something goes wrong during
        the lexing or parsing stages.

        Every token emitted includes the line number and column number as well
        as index that the token was created. That info is put into an rply
        SourcePosition object created in self.current_pos() and fed into the
        call to the rply Token class in self.emit()

        This can then be used later in the parsing stage when the tokens are
        being parsed into an Abstract Syntax Tree. If there is an error with
        a given token, the line number and column number can be pulled out of
        that token and used to display an informative error.
    """

    EOF = chr(0) # End Of File is represented by hex value 0x00

    def __init__(self, source):
        self.source = list(source)
        self.idx = 0
        self.lineno = 1
        self.columno = 1
        self.current_value = []

        self.token_generator = self.tokenise()

    def next(self):
        """
        This method is a convenience method to integrate with the rply
        ParserGenerator which expects an input object that contains a
        next() method that will return the next token when it is called
        or return None if there are no more tokens left to return
        """

        try:
            next_token = next(self.token_generator)
            # print(n)
            return next_token
        except StopIteration:
            return None

    def tokenise(self):
        """
        Generator function that loops through all characters in the source list
        and looks for known characters and keywords and accumulates the
        characters until a rule for a token is met. At this point the token is
        yielded by the generator and the current_value is reset. This is done
        in the emit method
        """

        while True:
            ch = self.read()

            if ch == self.EOF:
                break
            elif ch in "\r\n":
                self.newline(ch)

                # TODO check we aren't inside an expression or statement.
                # In which case we would not want to yield a newline token
                # Mon 28 May 19:08:35 2018
                while self.peek() in "\r\n \t\f\v":
                    # TODO count spaces / tabs and add indent tokens
                    # Mon 28 May 19:07:56 2018
                    ch = self.read()
                    if ch in "\r\n":
                        self.newline(ch)

                yield self.emit('NEWLINE')

    def emit(self, token):
        """
        Create a string from the current_value list of characters, reset the
        current_value list to be empty and return an rply token
        """

        value = "".join(self.current_value)
        self.clear()
        return Token(token, value, self.current_pos())

    def add(self, ch):
        """ Add a new character to the current_value list """

        self.current_value.append(ch)

    def newline(self, ch):
        """
        Some OSs use a carriage return (\r) and a newline character (\n) at
        the end of every line while others only use a newline. This code
        handles both cases then increments lineno and resets columno to 1
        """

        if ch == "\r" and self.peek() == "\n":
            self.read()
        self.lineno += 1
        self.columno = 1

    def current_pos(self):
        """
        Return the rply SourcePosition object with current index, line number
        and column number
        """
        return SourcePosition(self.idx, self.lineno, self.columno)

    def clear(self):
        """ Clear the current_value list of characters """

        del self.current_value[:]

    def read(self):
        """
        Attempt to read the next character in the source. If fail then return
        the End Of File character. Increment index within source list and
        increment column number and return the next character.
        """

        try:
            ch = self.source[self.idx]
        except IndexError:
            ch = self.EOF
        self.idx += 1
        self.columno += 1
        return ch

    def unread(self):
        """ Move the index back by one and decrement the column number """

        idx = self.idx - 1
        assert idx >= 0
        self.idx = idx
        self.columno -= 1

    def peek(self):
        """
        Take a look at the next character in the source without affecting the
        index pointer
        """

        ch = self.read()
        self.unread()
        return ch
