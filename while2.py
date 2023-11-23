import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'while': 'WHILE',
    'do': 'DO',
    'end': 'END',
    'puts': 'PUTS',
}

tokens = [
    'EQUAL',
    'NUMBER',
    'ID',
    'PLUS',
    'MINUS',
    'LESSTHAN',
    'LESSEQUAL',
    'GREATERTHAN',
    'GREATEREQUAL',
    'INCREMENT',
    'DECREMENT',
] + list(reserved.values())

t_EQUAL = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_LESSTHAN = r'\<'
t_LESSEQUAL = r'\<='
t_GREATERTHAN = r'\>'
t_GREATEREQUAL = r'\>='
t_INCREMENT = r'\+\+'
t_DECREMENT = r'\-\-'
t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_start(p):
    '''
    start : while_loop
    '''
    print("Valid Ruby code!")

def p_while_loop(p):
    '''
    while_loop : WHILE expression DO statements END
    '''
    print("While loop detected!")

def p_statements(p):
    '''
    statements : statements statement
               | statement
    '''


def p_statement(p):
    '''
    statement : assignment
              | expression
              | print_statement
    '''

def p_assignment(p):
    '''
    assignment : ID EQUAL expression
              | ID INCREMENT
              | ID DECREMENT
              | ID PLUS EQUAL expression
              | ID MINUS EQUAL expression
    '''

def p_expression(p):
    '''
    expression : expression PLUS term
              | expression MINUS term
              | expression LESSTHAN term
              | expression LESSEQUAL term
              | expression GREATERTHAN term
              | expression GREATEREQUAL term
              | term
    '''

def p_term(p):
    '''
    term : NUMBER
         | ID
    '''

def p_print_statement(p):
    '''
    print_statement : PUTS ID
    '''

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error: missing token")

parser = yacc.yacc()

while True:
    try:
        s = input('\nEnter the command: ')
        if s == 'exit':
            print("\nExiting...")
            break
        parser.parse(s)
    except EOFError:
        print("\nExiting...")
        break
