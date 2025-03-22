import ply.lex as lex
import ply.yacc as yacc
tokens = ('NUMBER',)
t_ignore = ' \t'
t_NUMBER = r'\d+'
def t_newline(t):
 r'\n'
 t.lexer.lineno += 1
 return t

def t_error(t):
 print(f"Illegal character '{t.value[0]}'")
 t.lexer.skip(1)
lexer = lex.lex()

def p_expr_add(p):
 'expr : expr "+" term'
 p[0] = p[1] + p[3]

def p_expr_sub(p):
 'expr : expr "-" term'
 p[0] = p[1] - p[3]

def p_expr_term(p):
 'expr : term'
 p[0] = p[1]

def p_term_mul(p):
 'term : term "*" factor'
 p[0] = p[1] * p[3]

def p_term_div(p):
 'term : term "/" factor'
 p[0] = p[1] / p[3]

def p_term_factor(p):
 'term : factor'
 p[0] = p[1]

def p_factor_num(p):
 'factor : NUMBER'
 p[0] = int(p[1])

def p_factor_expr(p):
 'factor : "(" expr ")"'
 p[0] = p[2]

def p_error(p):
 print("Syntax error")

parser = yacc.yacc()
while True:
 try:
    s = input('calc > ')
 except EOFError:
    break
 if not s:
    continue
 result = parser.parse(s)
 print(result)