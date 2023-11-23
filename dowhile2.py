import ply.lex as lex
import ply.yacc as yacc

reserved = {'while': 'WHILE', 'do': 'DO', 'loop': 'LOOP', 'if': 'IF', 'break': 'BREAK', 'end': 'END','puts':'PUTS'}

tokens = ['EQUAL', 'NUMBER', 'ID', 'PLUS', 'MINUS', 'PLUSEQUAL', 'MINUSEQUAL', 'GREATER','LESSER','STRING'] + list(reserved.values())

t_EQUAL = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_PLUSEQUAL = r'\+\='
t_MINUSEQUAL = r'\-\='
t_GREATER = r'\>'
t_LESSER=r'\<'
t_ignore = ' '

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Remove the double quotes from the value
    return t
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0]) 
    t.lexer.skip(1)

lexer = lex.lex()

def p_s(p):
    's : LOOP DO statements END'

def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''

def p_statement(p):
    '''
    statement : assignment
              | conditional
              | BREAK
              | puts_statement
    '''

def p_assignment(p):
    '''
    assignment : ID EQUAL NUMBER
               | ID PLUSEQUAL NUMBER
               | ID MINUSEQUAL NUMBER
               | ID EQUAL ID PLUS NUMBER
               | ID EQUAL ID MINUS NUMBER
    '''

def p_conditional(p):
    '''
    conditional : IF ID GREATER NUMBER
                | IF ID EQUAL NUMBER
                | IF ID LESSER NUMBER
    '''

def p_puts_statement(p):
    '''
    puts_statement : PUTS ID
                     | PUTS STRING
    '''

def p_error(t):
    if t:
        print("Syntax error at '%s'" % t.value)
    else:
        print("Syntax error: missing token")

parser = yacc.yacc()

while True:
    try:
        s = input('\nCommand > ')
        if s == 'exit':
            print("\nExiting...")
            break
        else:
            parser.parse(s)
    except EOFError:
        break
