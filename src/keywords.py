keywords = {
    '=': 'LITERAL_EQUAL',
    '==': 'EQ',
    '!=': 'NEQ',
    ':': 'COLON',
    ';': 'SEMICOLON',
    'return': 'RETURN',
    ',': 'COMMA',
    '.': 'DOT',
    '(': 'LBRACKET',
    ')': 'RBRACKET',
    '{': 'LPAREN',
    '}': 'RPAREN',
    '[': 'LSQBRACKET',
    ']': 'RSQBRACKET',
    '#': 'HASH',
    'and': 'LOGIC_AND',
    '&&': 'LOGIC_AND',
    'or': 'LOGIC_OR',
    '||': 'LOGIC_OR',
    '*': 'MULTIPLY',
    '/': 'DIVIDE',
    '//': 'INT_DIVIDE',
    '%': 'MODULO',
    '^': 'EXPONENT',
    '+': 'ADDITION',
    '-': 'SUBTRACTION',
    '>': 'GREATER_THAN',
    '<': 'LESS_THAN',
    '>=': 'GREATER_OR_EQUAL',
    '<=': 'LESS_OR_EQUAL',
    '?': 'QUESTION_MARK',
    'None': 'NONE',
    'NULL': 'NULL',


    'albanyexp': 'ASSIGNMENT',
    'auroraBorealis': 'PRINT',
    'if': 'CONDITIONAL',
    'else': 'CONDITIONAL_ALTERNATIVE',
    'well seymour': 'CODE_START',
    'you steam a good ham': 'CODE_END',
}

token_list = list(keywords.values()) + ['IDENTIFIER', 'INTEGER']

keyword_search_list = sorted(keywords.keys())
token_search_list = sorted(token_list)
