from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()
    
    def _add_tokens(self):
        #PRINT
        self.lexer.add('PRINT', r'print')
        #PARENTHESIS
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.add('OPEN_CURLY', r'\{')
        self.lexer.add('CLOSE_CURLY', r'\}')
        self.lexer.add('OPEN_SQUARE', r'\[')
        self.lexer.add('CLOSE_SQUARE', r'\]')
        #SEMICOLON
        self.lexer.add('SEMI_COLON', r'\;')
        #OPERATORS
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MULTI', r'\*')
        self.lexer.add('DIV', r'\/')
        self.lexer.add('MOD', r'\%')
        self.lexer.add('POW', r'\^')
        #NUMBER
        self.lexer.add('NUMBER', r'\d+')
        #IGNORE SPACES
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()