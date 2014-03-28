# sudo apt-get install python-ply
import ply.lex as lex
import re

tokens = (
    'LANGLE', # <
    'LANGLESLASH', # </
    'RANGLE', # >
    'EQUAL', # =
    'STRING', # 'hello'
    'WORD') # hello

# lexer states, built-in function of library
# state of 'htmlcomment' is 'exlusive' -- exclusive is built into libary
states = (
    ('htmlcomment', 'exclusive'),
    )

t_ignore = ' ' # shortcut for whitespace
t_htmlcomment_ignore = ' '

def t_htmlcomment(token):
    r'<!--'
    token.lexer.begin('htmlcomment') # enter htmlcomment state

def t_htmlcomment_end(token):
    r'-->'
    # TODO -- fix counting \n while in comment state
    # print 'token.value.count', token.value.count('\n') # this doesn't seem to work...
    # print token.lexer.lineno
    token.lexer.lineno += token.value.count('\n') # still need to account for newlines
    # print token.lexer.lineno
    token.lexer.begin("INITIAL") # go back to intial lexer state -- default state

def t_htmlcomment_error(token):
    token.lexer.skip(1) 
    # similar to writing pass, but gathers everything in the comment to one value

def t_newline(token):
    r'\n'
    # print 'new line!'
    token.lexer.lineno += 1
    pass

def t_error(t):
        print "JavaScript Lexer: Illegal character " + t.value[0]
        t.lexer.skip(1)

def t_LANGLESLASH(token):
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_EQUAL(token):
    r'='
    return token

def t_STRING(token):
    r'"[^"]*"' # accepts empty strings
    token.value = token.value[1:-1]
    return token

def t_WORD(token):
    r'[^ <>\n]+'
    return token


webpage = """hello <!-- 
com
ment --> al
l"""
htmllexer = lex.lex() # tells lexical analysis library to create lexical analyzer
htmllexer.input(webpage) # output of lexical analyzer is list of tokens

while True:
    tok = htmllexer.token() # .token appears to pop off a token from inherent list in htmllexer
    if not tok:
        break
    print tok