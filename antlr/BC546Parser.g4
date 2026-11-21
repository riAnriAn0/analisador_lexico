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

parser grammar BC546Parser;
options { tokenVocab = BC546Lexer; }

program : (funcDecl | statement)* EOF ;

statement
    : varDecl PV
    | atrib PV
    | print PV
    | return PV
    | expr PV
    | if
    | while
    | bloco
    ;

// bloco de coódigo
bloco : CHA statement* CHF ;

// print
print : PRINT PA expr PF ;

// input
input : INPUT PA expr PF;

// tipos de variaveis
tipo       : T_STR | T_NUM | T_BOOL ;

// tipos de retorno
tipoRet    : tipo | VOID ;

// delclaração de variaveis
varDecl    : tipo ID (ATRIB expr)? ;

// atribuição
atrib      : ID ATRIB expr ;

// declaração de função
funcDecl   : tipoRet FUNC ID PA params? PF bloco ;

// parametros de função
params     : param (V param)* ;
param      : tipo ID ;

// retorno de função
return : RETURN expr? ;

// condicional if
if     : IF PA expr PF statement ;

// repetição while
while  : WHILE PA expr PF statement ;

// expreções algebrigas / logicas
expr    : exprOr ;
exprOr  : exprAnd (OR exprAnd)* ;
exprAnd : exprNot (AND exprNot)* ;
exprNot : NOT exprNot| exprRel;
exprRel : exprArt ((IGUAL | DIF | MAIORIG | MENORIG | MENOR | MAIOR) exprArt)? ;
exprArt : termo ((ADD_OP | SUB_OP) termo)* ;
termo   : fator ((MULT_OP | DIV_OP | MOD_OP) fator)* ;

// chamada de função
chFun : ID PA (expr (V expr)*)? PF ;

// fatores
fator
    : INT
    | TEXT
    | TRUE
    | FALSE
    | NULL
    | chFun
    | ID
    | PA expr PF
    ;


