
import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'for': 'FOR',
    'do': 'DO',
    'end': 'END',
    'in': 'IN',
    'puts': 'PUTS'
}

tokens = [
    'EQUAL',
    'NUMBER',
    'ID',
    'RANGE',
    'PLUS',
    'MINUS',
    'PLUS_EQUAL',
    'MINUS_EQUAL',
] + list(reserved.values())

t_EQUAL = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'\-='

t_ignore = ' '

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_RANGE(t):
    r'\.\.'
    return t

def t_PUTS(t):
    r'puts'
    t.type = reserved.get(t.value)
    return t

def t_NEWLINE(t): #matches the newline character and updates the line count
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_start(p):
    '''
    start : FOR ID IN NUMBER RANGE NUMBER DO statements END
    '''

def p_statements(p):
    '''
    statements : statements statement
               | statement
    '''

def p_statement(p):
    '''
    statement : assignment
              | compound_assignment
              | puts_statement
              | for_loop
    '''

def p_assignment(p):
    '''
    assignment : ID EQUAL expression
    '''

def p_compound_assignment(p):
    '''
    compound_assignment : ID PLUS_EQUAL expression
                        | ID MINUS_EQUAL expression
    '''

def p_puts_statement(p):
    '''
    puts_statement : PUTS ID
    '''

def p_for_loop(p):
    '''
    for_loop : FOR ID IN NUMBER RANGE NUMBER DO statements END
    '''

def p_expression(p):
    '''
    expression : term
               | expression PLUS term
               | expression MINUS term
    '''

def p_term(p):
    '''
    term : NUMBER
         | ID
    '''

def p_error(t):
    if t:
        print("Syntax error at %s" % t.value)
    else:
        print("Syntax error: missing token")

parser = yacc.yacc()

while True:
    try:
        s = input('\nEnter the command:  ')
        if s == 'exit':
            print("\n")
            break
        parser.parse(s)
    except EOFError:
        break
