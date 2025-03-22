import ply.lex as lex
import ply.yacc as yacc

# Токены
tokens = (
    'INCLUDE', 'INT', 'MAIN', 'RETURN', 'COUT', 'CIN', 'ENDL', 'STRING', 'NUMBER',
    'ID', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON', 'LESSLESS', 'LESS',
    'GREATERGREATER', 'GREATER', 'EQUALS'
)

# Регулярные выражения для токенов
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_LESSLESS = r'<<'
t_GREATERGREATER = r'>>'
t_LESS = r'<'
t_GREATER = r'>'
t_EQUALS = r'='
t_ignore = ' \t'

# Ключевые слова
def t_INCLUDE(t):
    r'\#include'
    return t

def t_INT(t):
    r'int'
    return t

def t_MAIN(t):
    r'main'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_COUT(t):
    r'std::cout'
    return t

def t_CIN(t):
    r'std::cin'
    return t

def t_ENDL(t):
    r'std::endl'
    return t

# Строки
def t_STRING(t):
    r'\"[^"]*\"'
    return t

# Числа
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Идентификаторы
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Новая строка
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ошибка
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Лексер
lexer = lex.lex()

# Грамматика
def p_program(p):
    '''program : include_directive main_function'''
    p[0] = (p[1], p[2])

def p_include_directive(p):
    '''include_directive : INCLUDE LESS ID GREATER'''
    p[0] = ('include', p[3])

def p_main_function(p):
    '''main_function : INT MAIN LPAREN RPAREN LBRACE statements RBRACE'''
    p[0] = ('main_function', p[6])

def p_statements(p):
    '''statements : statement
                 | statements statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : expression SEMICOLON
                 | declaration SEMICOLON
                 | return_statement SEMICOLON'''
    p[0] = p[1]

def p_declaration(p):
    '''declaration : INT ID'''
    p[0] = ('declaration', p[2])

def p_expression(p):
    '''expression : COUT LESSLESS STRING LESSLESS ENDL
                  | COUT LESSLESS ID LESSLESS ENDL
                  | CIN GREATERGREATER ID'''
    if p[1] == 'std::cout':
        p[0] = ('print', p[3])
    elif p[1] == 'std::cin':
        p[0] = ('input', p[3])

def p_return_statement(p):
    '''return_statement : RETURN NUMBER'''
    p[0] = ('return', p[2])

# Обработка ошибок
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}' (line {p.lineno})")
    else:
        print("Syntax error at EOF")    # чисто для последнего символа

# Парсер
parser = yacc.yacc()

# Тестирование
if __name__ == "__main__":
    data = """
    #include <iostream>

    int main() {
        int a;
        std::cin >> a;
        std::cout << a << std::endl;
        std::cout << "Hello, World!" << std::endl;
        return 0;
    }
    """
    result = parser.parse(data)
    print(result)