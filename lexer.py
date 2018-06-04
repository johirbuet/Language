'''
Created on Jun 4, 2018

@author: mislam
'''
from ply import lex
def t_LANGLESLASH(token):
    r'</'
    return token 

def t_NUMBER(token):
    r'[0-9]+'
    token.value = int(token.value)
    return token
def t_STRING(token):
    r'\"[^\"]*\"'
    return token
def t_WORD(token):
    r'[^<> ]+'
    return token