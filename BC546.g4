parser grammar BC546;

/*
Requisitos mínimos
    Declaração de variável
    Atribuição
    Expressões aritméticas
    Expressões relacionais
    Pelo menos uma estrutura condicional
    Pelo menos uma estrutura de repetição
    Definição de funções com argumentos e retorno
*/

// Regra inicial
program : (funcDecl | statement)* EOF ;

// Comandos
statement: 
    varDecl PV| atrib PV| expr PV| returnStmt PV| ifStmt| whileStmt| bloco;

// Bloco de comandos
bloco : '{' statement* '}' ;

// Tipos
tipo : T_STR | T_NUM | T_BOOL ;

// Declaração de variável
varDecl : tipo ID expr ;

// Atribuição
atrib : ID ATRIB expr ;

// Função
funcDecl :tipo FUNC ID PA params? PF bloco ;
params   : param (V param)* ;
param    : tipo ID ;
returnStmt : RETURN expr ;

// Condicional
ifStmt : IF PA expr PF statement ;

// Repetição
whileStmt : WHILE PA expr PF statement ;

// Expressões
expr    : exprArt ((IGUAL | DIF | MAIORIG | MENORIG | MENOR | MAIOR) exprArt)? ;
exprArt : termo ((ADD_OP | SUC_OP) termo)* ;
termo   : fator ((MULT_OP | DIV_OP | MOD_OP) fator)* ;
fator
    : NUM| STR| TRUE| FALSE| chFun| ID| PA expr PF;

// Chamada de função
chFun : ID PA (expr (V expr)*)? PF ;

