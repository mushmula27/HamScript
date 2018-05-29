from rply import ParserGenerator, Token, ParsingError
from rply.token import BaseBox, SourcePosition
from keywords import keywords

token_list = list(keywords.values()) + ['IDENTIFIER', 'INTEGER']

def lexer_wrapper(lexer):
    while True:
        try:
            val = next(lexer.token_generator)
            yield val
        except StopIteration:
            return None

class Parser:
    pg = ParserGenerator(token_list, precedence=[], cache_id="steamer")

    def __init__(self, lexer):
        self.lexer = lexer

    def parse(self):
        return self.parser.parse(lexer_wrapper(self.lexer), state=self)

    @pg.production("program : statements")
    def program(self, p):
        return BoxAST('program')

    @pg.production("statements : statements statement")
    def statements(self, p):
        return 'statements'

    @pg.production("statements : statement")
    def statements_statement(self, p):
        return 'statements_statement'


    @pg.production("statement : ASSIGNMENT IDENTIFIER LITERAL_EQUAL INTEGER")
    def assign_integer(self, p):
        return 'assign integer'

    @pg.production("statement : statement opt_nl")
    def assign_integer(self, p):
        return None

    @pg.production("opt_nl : ")
    def opt_nl_none(self, p):
        return None

    @pg.production("opt_nl : NEWLINE")
    def opt_nl_none(self, p):
        return None

    parser = pg.build()

class BoxAST(BaseBox):
    def __init__(self, node):
        self.node = node

    def getast(self, cls=None):
        node = self.node
        if cls is not None:
            assert isinstance(node, cls)
        return node
