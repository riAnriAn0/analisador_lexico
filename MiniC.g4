grammar MiniC;

// Regra inicial: um programa é uma sequência de comandos
program: statement* EOF;

// Um comando pode ser declaração de variável, if, bloco ou expressão
statement
    : varDecl
    | ifStmt
    | block
    | exprStmt
    ;

// Declaração de variável: tipo nome (= valor)? ;
varDecl
    : type ID ('=' expr)? ';'
    ;

// Tipos básicos suportados
type
    : TP_INT | TP_FLOAT | TP_CHAR | TP_BOOL
    ;

// Estrutura if-else
ifStmt
    : KW_IF '(' expr ')' statement (KW_ELSE statement)?
    ;

// Bloco delimitado por chaves
block
    : '{' statement* '}'
    ;

// Expressão seguida de ponto e vírgula
exprStmt
    : expr ';'
    ;

// Expressões com precedência no estilo C
expr
    : ID '=' expr                               # assignment
    | expr ('==' | '!=' | '<' | '>' | '<=' | '>=') expr  # comparison
    | expr ('+' | '-') expr                     # additive
    | expr ('*' | '/') expr                     # multiplicative
    | ID                                        # identifier
    | INT                                       # integerLiteral
    | '(' expr ')'                              # parens
    ;

// ------------------- Lexer -------------------

TP_INT   : 'int';
TP_FLOAT : 'float';
TP_CHAR  : 'char';
TP_BOOL  : 'bool';
KW_IF    : 'if';
KW_ELSE  : 'else';

ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;

WS           : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;