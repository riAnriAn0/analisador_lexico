lexer grammar BC546Lexer;

PV : ';' ;
PA : '(' ;   
PF : ')' ;
CHA : '{' ;  
CHF : '}' ;  
V : ',' ;

AND : 'and'; 
OR : 'or'; 
NOT : 'not';

IGUAL : '==' ;  
DIF : '!=' ;  
MAIORIG : '>=' ;
MENORIG : '<=' ;  
MAIOR : '>' ;  
MENOR : '<' ;  
ATRIB : '=' ;

ADD_OP : '+' ;  
SUB_OP : '-' ;  
MULT_OP : '*' ;
DIV_OP : '/' ;  
MOD_OP : '%' ;

T_NUM : 'num' ;  
T_STR : 'str' ;  
T_BOOL : 'bool' ;
VOID : 'void' ;  
NULL : 'null' ;
TRUE : 'true' ;  
FALSE : 'false' ;
PRINT : 'print' ;  
WHILE : 'while' ;  
IF : 'if' ; 
INPUT: 'input';
RETURN : 'return' ;  
FUNC : 'func' ;

INT : [0-9]+ ;
TEXT : '"' ~["\r\n]* '"' ;
ID : '_' [a-zA-Z0-9_]* ;

WS : [ \t\r\n]+ -> skip ;