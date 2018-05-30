from rply import ParserGenerator, Token, ParsingError
from rply.token import BaseBox, SourcePosition
from keywords import token_list

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

    @pg.production("program : prog_block")
    def program(self, p):
        return BoxAST('program')

    @pg.production("prog_block : code_start statements code_end")
    def program(self, p):
        return BoxAST('program')

    @pg.production("code_start : CODE_START opt_nl")
    def code_start_newline(self, p):
        print('code start nl', p)
        return 'code_startnl'

    @pg.production("code_start : CODE_START")
    def code_start(self, p):
        print('code start', p)
        return 'code_start'

    @pg.production("code_end : CODE_END opt_nl")
    def code_start_newline(self, p):
        print('code end', p)
        return 'code_end'

    @pg.production("code_end : CODE_END")
    def code_start(self, p):
        print('code end newline', p)
        return 'code_endnl'

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
