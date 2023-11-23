import ply.lex as lex
import ply.yacc as yacc

tokens = ['COMMENT', 'MULTI_LINE_COMMENT'] #Tokens are used by lexer to recognise patterns in the input text

#matches any text starting with #.
def t_COMMENT(t):
    r'\#.*'
    return t

# matches everything between =begin and =end, including newlines.
def t_MULTI_LINE_COMMENT(t):
    r'=begin((.|\n)*?)=end' #regular expression
    return t

#Handles errors encountered by the lexer, printing a message for illegal characters and skipping them.
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex() #creates instance of lexer

#Defines the structure of a statement which can either be a single-line comment (COMMENT) or a multi-line comment (MULTI_LINE_COMMENT). Prints the comment found.
def p_statement(p):
    '''statement : COMMENT
                 | MULTI_LINE_COMMENT'''
    print("Comment:", p[1])

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()  #creates instance of the parser

while True:
    try:
        s = input('\nEnter Ruby code:  ')
        if s == 'exit':
            print("\nExiting the parser...")
            break
        parser.parse(s)
    except EOFError:
        break
