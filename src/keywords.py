keywords = {
    '\n': 'NEWLINE',
    '=': 'LITERAL_EQUAL',
    '==': 'EQ',

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
