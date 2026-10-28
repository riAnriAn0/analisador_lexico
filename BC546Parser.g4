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

bloco      : CHA statement* CHF ;
print : PRINT PA expr PF ;
input : INPUT PA expr PF;

tipo       : T_STR | T_NUM | T_BOOL ;
tipoRet    : tipo | VOID ;

varDecl    : tipo ID (ATRIB expr)? ;
atrib      : ID ATRIB expr ;

funcDecl   : tipoRet FUNC ID PA params? PF bloco ;
params     : param (V param)* ;
param      : tipo ID ;
return : RETURN expr? ;

if     : IF PA expr PF statement ;
while  : WHILE PA expr PF statement ;

expr    : exprOr ;
exprOr  : exprAnd (OR exprAnd)* ;
exprAnd : exprNot (AND exprNot)* ;
exprNot : NOT exprNot| exprRel;
exprRel : exprArt ((IGUAL | DIF | MAIORIG | MENORIG | MENOR | MAIOR) exprArt)? ;
exprArt : termo ((ADD_OP | SUB_OP) termo)* ;
termo   : fator ((MULT_OP | DIV_OP | MOD_OP) fator)* ;

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

chFun : ID PA (expr (V expr)*)? PF ;

