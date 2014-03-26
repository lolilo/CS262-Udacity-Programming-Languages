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

t_ignore = ' ' # shortcut for whitespace

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
    r'[^<> ]+'
    return token

webpage = "This is my <b>my</b> webpage!"
htmllexer = lex.lex() # tells lexical analysis library to create lexical analyzer
htmllexer.input(webpage) # output of lexical analyzer is list of tokens

while True:
    tok = htmllexer.token() # .token appears to pop off a token from inherent list in htmllexer
    if not tok:
        break
    print tok