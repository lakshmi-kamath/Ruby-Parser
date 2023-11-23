import ply.lex as lex
import ply.yacc as yacc
#reserved dictionary holds reserved keywords in the Ruby-like language being parsed.
reserved = {
    'def': 'DEF',
    'end': 'END'
}
#tokens list includes the token names used in the language.
tokens = [
    'ID',
    'LPAREN',
    'RPAREN',
    'COMMA'
] + list(reserved.values())

t_ignore = ' '

# Functions starting with t_ define rules to match and convert input into tokens. 
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','

#handles errors encountered during tokenization.
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

#Functions starting with p_ define grammar rules for the language using yacc syntax.
def p_function_declaration(p):
    '''
    function_declaration : DEF ID parameter_list END
                         | DEF ID END
    '''

def p_parameter_list(p):
    '''
    parameter_list : LPAREN parameters RPAREN
                   | LPAREN RPAREN
    '''

def p_parameters(p):
    '''
    parameters : ID
               | parameters COMMA ID
    '''
#Handles syntax errors encountered during parsing.
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

while True:
    try:
        s = input('\nEnter the Ruby code: ')
        if s == 'exit':
            print("\nExiting...")
            break
        parser.parse(s)
    except EOFError:
        break
