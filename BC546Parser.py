# Generated from BC546Parser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,221,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,5,0,51,8,0,10,0,12,0,
        54,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,76,8,1,1,2,1,2,5,2,80,8,2,10,2,12,2,83,
        9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,
        1,6,3,6,101,8,6,1,7,1,7,1,7,1,7,3,7,107,8,7,1,8,1,8,1,8,1,8,1,9,
        1,9,1,9,1,9,1,9,3,9,118,8,9,1,9,1,9,1,9,1,10,1,10,1,10,5,10,126,
        8,10,10,10,12,10,129,9,10,1,11,1,11,1,11,1,12,1,12,3,12,136,8,12,
        1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,
        1,15,1,16,1,16,1,16,5,16,155,8,16,10,16,12,16,158,9,16,1,17,1,17,
        1,17,5,17,163,8,17,10,17,12,17,166,9,17,1,18,1,18,1,18,3,18,171,
        8,18,1,19,1,19,1,19,3,19,176,8,19,1,20,1,20,1,20,5,20,181,8,20,10,
        20,12,20,184,9,20,1,21,1,21,1,21,5,21,189,8,21,10,21,12,21,192,9,
        21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,205,
        8,22,1,23,1,23,1,23,1,23,1,23,5,23,212,8,23,10,23,12,23,215,9,23,
        3,23,217,8,23,1,23,1,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,0,4,1,0,22,24,1,0,10,15,1,
        0,17,18,1,0,19,21,226,0,52,1,0,0,0,2,75,1,0,0,0,4,77,1,0,0,0,6,86,
        1,0,0,0,8,91,1,0,0,0,10,96,1,0,0,0,12,100,1,0,0,0,14,102,1,0,0,0,
        16,108,1,0,0,0,18,112,1,0,0,0,20,122,1,0,0,0,22,130,1,0,0,0,24,133,
        1,0,0,0,26,137,1,0,0,0,28,143,1,0,0,0,30,149,1,0,0,0,32,151,1,0,
        0,0,34,159,1,0,0,0,36,170,1,0,0,0,38,172,1,0,0,0,40,177,1,0,0,0,
        42,185,1,0,0,0,44,204,1,0,0,0,46,206,1,0,0,0,48,51,3,18,9,0,49,51,
        3,2,1,0,50,48,1,0,0,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,
        52,53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,55,56,5,0,0,1,56,1,1,0,
        0,0,57,58,3,14,7,0,58,59,5,1,0,0,59,76,1,0,0,0,60,61,3,16,8,0,61,
        62,5,1,0,0,62,76,1,0,0,0,63,64,3,6,3,0,64,65,5,1,0,0,65,76,1,0,0,
        0,66,67,3,24,12,0,67,68,5,1,0,0,68,76,1,0,0,0,69,70,3,30,15,0,70,
        71,5,1,0,0,71,76,1,0,0,0,72,76,3,26,13,0,73,76,3,28,14,0,74,76,3,
        4,2,0,75,57,1,0,0,0,75,60,1,0,0,0,75,63,1,0,0,0,75,66,1,0,0,0,75,
        69,1,0,0,0,75,72,1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,3,1,0,0,
        0,77,81,5,4,0,0,78,80,3,2,1,0,79,78,1,0,0,0,80,83,1,0,0,0,81,79,
        1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,5,0,0,
        85,5,1,0,0,0,86,87,5,29,0,0,87,88,5,2,0,0,88,89,3,30,15,0,89,90,
        5,3,0,0,90,7,1,0,0,0,91,92,5,32,0,0,92,93,5,2,0,0,93,94,3,30,15,
        0,94,95,5,3,0,0,95,9,1,0,0,0,96,97,7,0,0,0,97,11,1,0,0,0,98,101,
        3,10,5,0,99,101,5,25,0,0,100,98,1,0,0,0,100,99,1,0,0,0,101,13,1,
        0,0,0,102,103,3,10,5,0,103,106,5,37,0,0,104,105,5,16,0,0,105,107,
        3,30,15,0,106,104,1,0,0,0,106,107,1,0,0,0,107,15,1,0,0,0,108,109,
        5,37,0,0,109,110,5,16,0,0,110,111,3,30,15,0,111,17,1,0,0,0,112,113,
        3,12,6,0,113,114,5,34,0,0,114,115,5,37,0,0,115,117,5,2,0,0,116,118,
        3,20,10,0,117,116,1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,120,
        5,3,0,0,120,121,3,4,2,0,121,19,1,0,0,0,122,127,3,22,11,0,123,124,
        5,6,0,0,124,126,3,22,11,0,125,123,1,0,0,0,126,129,1,0,0,0,127,125,
        1,0,0,0,127,128,1,0,0,0,128,21,1,0,0,0,129,127,1,0,0,0,130,131,3,
        10,5,0,131,132,5,37,0,0,132,23,1,0,0,0,133,135,5,33,0,0,134,136,
        3,30,15,0,135,134,1,0,0,0,135,136,1,0,0,0,136,25,1,0,0,0,137,138,
        5,31,0,0,138,139,5,2,0,0,139,140,3,30,15,0,140,141,5,3,0,0,141,142,
        3,2,1,0,142,27,1,0,0,0,143,144,5,30,0,0,144,145,5,2,0,0,145,146,
        3,30,15,0,146,147,5,3,0,0,147,148,3,2,1,0,148,29,1,0,0,0,149,150,
        3,32,16,0,150,31,1,0,0,0,151,156,3,34,17,0,152,153,5,8,0,0,153,155,
        3,34,17,0,154,152,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,
        1,0,0,0,157,33,1,0,0,0,158,156,1,0,0,0,159,164,3,36,18,0,160,161,
        5,7,0,0,161,163,3,36,18,0,162,160,1,0,0,0,163,166,1,0,0,0,164,162,
        1,0,0,0,164,165,1,0,0,0,165,35,1,0,0,0,166,164,1,0,0,0,167,168,5,
        9,0,0,168,171,3,36,18,0,169,171,3,38,19,0,170,167,1,0,0,0,170,169,
        1,0,0,0,171,37,1,0,0,0,172,175,3,40,20,0,173,174,7,1,0,0,174,176,
        3,40,20,0,175,173,1,0,0,0,175,176,1,0,0,0,176,39,1,0,0,0,177,182,
        3,42,21,0,178,179,7,2,0,0,179,181,3,42,21,0,180,178,1,0,0,0,181,
        184,1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,41,1,0,0,0,184,182,
        1,0,0,0,185,190,3,44,22,0,186,187,7,3,0,0,187,189,3,44,22,0,188,
        186,1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,
        43,1,0,0,0,192,190,1,0,0,0,193,205,5,35,0,0,194,205,5,36,0,0,195,
        205,5,27,0,0,196,205,5,28,0,0,197,205,5,26,0,0,198,205,3,46,23,0,
        199,205,5,37,0,0,200,201,5,2,0,0,201,202,3,30,15,0,202,203,5,3,0,
        0,203,205,1,0,0,0,204,193,1,0,0,0,204,194,1,0,0,0,204,195,1,0,0,
        0,204,196,1,0,0,0,204,197,1,0,0,0,204,198,1,0,0,0,204,199,1,0,0,
        0,204,200,1,0,0,0,205,45,1,0,0,0,206,207,5,37,0,0,207,216,5,2,0,
        0,208,213,3,30,15,0,209,210,5,6,0,0,210,212,3,30,15,0,211,209,1,
        0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,217,1,
        0,0,0,215,213,1,0,0,0,216,208,1,0,0,0,216,217,1,0,0,0,217,218,1,
        0,0,0,218,219,5,3,0,0,219,47,1,0,0,0,18,50,52,75,81,100,106,117,
        127,135,156,164,170,175,182,190,204,213,216
    ]

class BC546Parser ( Parser ):

    grammarFileName = "BC546Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "'{'", "'}'", "','", 
                     "'and'", "'or'", "'not'", "'=='", "'!='", "'>='", "'<='", 
                     "'>'", "'<'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'num'", "'str'", "'bool'", "'void'", "'null'", "'true'", 
                     "'false'", "'print'", "'while'", "'if'", "'input'", 
                     "'return'", "'func'" ]

    symbolicNames = [ "<INVALID>", "PV", "PA", "PF", "CHA", "CHF", "V", 
                      "AND", "OR", "NOT", "IGUAL", "DIF", "MAIORIG", "MENORIG", 
                      "MAIOR", "MENOR", "ATRIB", "ADD_OP", "SUB_OP", "MULT_OP", 
                      "DIV_OP", "MOD_OP", "T_NUM", "T_STR", "T_BOOL", "VOID", 
                      "NULL", "TRUE", "FALSE", "PRINT", "WHILE", "IF", "INPUT", 
                      "RETURN", "FUNC", "INT", "TEXT", "ID", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_bloco = 2
    RULE_print = 3
    RULE_input = 4
    RULE_tipo = 5
    RULE_tipoRet = 6
    RULE_varDecl = 7
    RULE_atrib = 8
    RULE_funcDecl = 9
    RULE_params = 10
    RULE_param = 11
    RULE_return = 12
    RULE_if = 13
    RULE_while = 14
    RULE_expr = 15
    RULE_exprOr = 16
    RULE_exprAnd = 17
    RULE_exprNot = 18
    RULE_exprRel = 19
    RULE_exprArt = 20
    RULE_termo = 21
    RULE_fator = 22
    RULE_chFun = 23

    ruleNames =  [ "program", "statement", "bloco", "print", "input", "tipo", 
                   "tipoRet", "varDecl", "atrib", "funcDecl", "params", 
                   "param", "return", "if", "while", "expr", "exprOr", "exprAnd", 
                   "exprNot", "exprRel", "exprArt", "termo", "fator", "chFun" ]

    EOF = Token.EOF
    PV=1
    PA=2
    PF=3
    CHA=4
    CHF=5
    V=6
    AND=7
    OR=8
    NOT=9
    IGUAL=10
    DIF=11
    MAIORIG=12
    MENORIG=13
    MAIOR=14
    MENOR=15
    ATRIB=16
    ADD_OP=17
    SUB_OP=18
    MULT_OP=19
    DIV_OP=20
    MOD_OP=21
    T_NUM=22
    T_STR=23
    T_BOOL=24
    VOID=25
    NULL=26
    TRUE=27
    FALSE=28
    PRINT=29
    WHILE=30
    IF=31
    INPUT=32
    RETURN=33
    FUNC=34
    INT=35
    TEXT=36
    ID=37
    WS=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BC546Parser.EOF, 0)

        def funcDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BC546Parser.FuncDeclContext)
            else:
                return self.getTypedRuleContext(BC546Parser.FuncDeclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BC546Parser.StatementContext)
            else:
                return self.getTypedRuleContext(BC546Parser.StatementContext,i)


        def getRuleIndex(self):
            return BC546Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BC546Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 253398876692) != 0):
                self.state = 50
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 48
                    self.funcDecl()
                    pass

                elif la_ == 2:
                    self.state = 49
                    self.statement()
                    pass


                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(BC546Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(BC546Parser.VarDeclContext,0)


        def PV(self):
            return self.getToken(BC546Parser.PV, 0)

        def atrib(self):
            return self.getTypedRuleContext(BC546Parser.AtribContext,0)


        def print_(self):
            return self.getTypedRuleContext(BC546Parser.PrintContext,0)


        def return_(self):
            return self.getTypedRuleContext(BC546Parser.ReturnContext,0)


        def expr(self):
            return self.getTypedRuleContext(BC546Parser.ExprContext,0)


        def if_(self):
            return self.getTypedRuleContext(BC546Parser.IfContext,0)


        def while_(self):
            return self.getTypedRuleContext(BC546Parser.WhileContext,0)


        def bloco(self):
            return self.getTypedRuleContext(BC546Parser.BlocoContext,0)


        def getRuleIndex(self):
            return BC546Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BC546Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.varDecl()
                self.state = 58
                self.match(BC546Parser.PV)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.atrib()
                self.state = 61
                self.match(BC546Parser.PV)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.print_()
                self.state = 64
                self.match(BC546Parser.PV)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.return_()
                self.state = 67
                self.match(BC546Parser.PV)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.expr()
                self.state = 70
                self.match(BC546Parser.PV)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 72
                self.if_()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 73
                self.while_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 74
                self.bloco()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHA(self):
            return self.getToken(BC546Parser.CHA, 0)

        def CHF(self):
            return self.getToken(BC546Parser.CHF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BC546Parser.StatementContext)
            else:
                return self.getTypedRuleContext(BC546Parser.StatementContext,i)


        def getRuleIndex(self):
            return BC546Parser.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco" ):
                return visitor.visitBloco(self)
            else:
                return visitor.visitChildren(self)




    def bloco(self):

        localctx = BC546Parser.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(BC546Parser.CHA)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 253365322260) != 0):
                self.state = 78
                self.statement()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(BC546Parser.CHF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(BC546Parser.PRINT, 0)

        def PA(self):
            return self.getToken(BC546Parser.PA, 0)

        def expr(self):
            return self.getTypedRuleContext(BC546Parser.ExprContext,0)


        def PF(self):
            return self.getToken(BC546Parser.PF, 0)

        def getRuleIndex(self):
            return BC546Parser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = BC546Parser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(BC546Parser.PRINT)
            self.state = 87
            self.match(BC546Parser.PA)
            self.state = 88
            self.expr()
            self.state = 89
            self.match(BC546Parser.PF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(BC546Parser.INPUT, 0)

        def PA(self):
            return self.getToken(BC546Parser.PA, 0)

        def expr(self):
            return self.getTypedRuleContext(BC546Parser.ExprContext,0)


        def PF(self):
            return self.getToken(BC546Parser.PF, 0)

        def getRuleIndex(self):
            return BC546Parser.RULE_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput" ):
                return visitor.visitInput(self)
            else:
                return visitor.visitChildren(self)




    def input_(self):

        localctx = BC546Parser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_input)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(BC546Parser.INPUT)
            self.state = 92
            self.match(BC546Parser.PA)
            self.state = 93
            self.expr()
            self.state = 94
            self.match(BC546Parser.PF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_STR(self):
            return self.getToken(BC546Parser.T_STR, 0)

        def T_NUM(self):
            return self.getToken(BC546Parser.T_NUM, 0)

        def T_BOOL(self):
            return self.getToken(BC546Parser.T_BOOL, 0)

        def getRuleIndex(self):
            return BC546Parser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = BC546Parser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoRetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(BC546Parser.TipoContext,0)


        def VOID(self):
            return self.getToken(BC546Parser.VOID, 0)

        def getRuleIndex(self):
            return BC546Parser.RULE_tipoRet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoRet" ):
                listener.enterTipoRet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoRet" ):
                listener.exitTipoRet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoRet" ):
                return visitor.visitTipoRet(self)
            else:
                return visitor.visitChildren(self)




    def tipoRet(self):

        localctx = BC546Parser.TipoRetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tipoRet)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.tipo()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.match(BC546Parser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(BC546Parser.TipoContext,0)


        def ID(self):
            return self.getToken(BC546Parser.ID, 0)

        def ATRIB(self):
            return self.getToken(BC546Parser.ATRIB, 0)

        def expr(self):
            return self.getTypedRuleContext(BC546Parser.ExprContext,0)


        def getRuleIndex(self):
            return BC546Parser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = BC546Parser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.tipo()
            self.state = 103
            self.match(BC546Parser.ID)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 104
                self.match(BC546Parser.ATRIB)
                self.state = 105
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BC546Parser.ID, 0)

        def ATRIB(self):
            return self.getToken(BC546Parser.ATRIB, 0)

        def expr(self):
            return self.getTypedRuleContext(BC546Parser.ExprContext,0)


        def getRuleIndex(self):
            return BC546Parser.RULE_atrib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtrib" ):
                listener.enterAtrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtrib" ):
                listener.exitAtrib(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtrib" ):
                return visitor.visitAtrib(self)
            else:
                return visitor.visitChildren(self)




    def atrib(self):

        localctx = BC546Parser.AtribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(BC546Parser.ID)
            self.state = 109
            self.match(BC546Parser.ATRIB)
            self.state = 110
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipoRet(self):
            return self.getTypedRuleContext(BC546Parser.TipoRetContext,0)


        def FUNC(self):
            return self.getToken(BC546Parser.FUNC, 0)

        def ID(self):
            return self.getToken(BC546Parser.ID, 0)

        def PA(self):
            return self.getToken(BC546Parser.PA, 0)

        def PF(self):
            return self.getToken(BC546Parser.PF, 0)

        def bloco(self):
            return self.getTypedRuleContext(BC546Parser.BlocoContext,0)


        def params(self):
            return self.getTypedRuleContext(BC546Parser.ParamsContext,0)


        def getRuleIndex(self):
            return BC546Parser.RULE_funcDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDecl" ):
                listener.enterFuncDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDecl" ):
                listener.exitFuncDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = BC546Parser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.tipoRet()
            self.state = 113
            self.match(BC546Parser.FUNC)
            self.state = 114
            self.match(BC546Parser.ID)
            self.state = 115
            self.match(BC546Parser.PA)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0):
                self.state = 116
                self.params()


            self.state = 119
            self.match(BC546Parser.PF)
            self.state = 120
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BC546Parser.ParamContext)
            else:
                return self.getTypedRuleContext(BC546Parser.ParamContext,i)


        def V(self, i:int=None):
            if i is None:
                return self.getTokens(BC546Parser.V)
            else:
                return self.getToken(BC546Parser.V, i)

        def getRuleIndex(self):
            return BC546Parser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = BC546Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.param()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 123
                self.match(BC546Parser.V)
                self.state = 124
                self.param()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(BC546Parser.TipoContext,0)


        def ID(self):
            return self.getToken(BC546Parser.ID, 0)

        def getRuleIndex(self):
            return BC546Parser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BC546Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.tipo()
            self.state = 131
            self.match(BC546Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BC546Parser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BC546Parser.ExprContext,0)


        def getRuleIndex(self):
            return BC546Parser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)




    def return_(self):

        localctx = BC546Parser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(BC546Parser.RETURN)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 240987931140) != 0):
                self.state = 134
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BC546Parser.IF, 0)

        def PA(self):
            return self.getToken(BC546Parser.PA, 0)

        def expr(self):
            return self.getTypedRuleContext(BC546Parser.ExprContext,0)


        def PF(self):
            return self.getToken(BC546Parser.PF, 0)

        def statement(self):
            return self.getTypedRuleContext(BC546Parser.StatementContext,0)


        def getRuleIndex(self):
            return BC546Parser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = BC546Parser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(BC546Parser.IF)
            self.state = 138
            self.match(BC546Parser.PA)
            self.state = 139
            self.expr()
            self.state = 140
            self.match(BC546Parser.PF)
            self.state = 141
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BC546Parser.WHILE, 0)

        def PA(self):
            return self.getToken(BC546Parser.PA, 0)

        def expr(self):
            return self.getTypedRuleContext(BC546Parser.ExprContext,0)


        def PF(self):
            return self.getToken(BC546Parser.PF, 0)

        def statement(self):
            return self.getTypedRuleContext(BC546Parser.StatementContext,0)


        def getRuleIndex(self):
            return BC546Parser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = BC546Parser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(BC546Parser.WHILE)
            self.state = 144
            self.match(BC546Parser.PA)
            self.state = 145
            self.expr()
            self.state = 146
            self.match(BC546Parser.PF)
            self.state = 147
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprOr(self):
            return self.getTypedRuleContext(BC546Parser.ExprOrContext,0)


        def getRuleIndex(self):
            return BC546Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BC546Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.exprOr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BC546Parser.ExprAndContext)
            else:
                return self.getTypedRuleContext(BC546Parser.ExprAndContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(BC546Parser.OR)
            else:
                return self.getToken(BC546Parser.OR, i)

        def getRuleIndex(self):
            return BC546Parser.RULE_exprOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprOr" ):
                listener.enterExprOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprOr" ):
                listener.exitExprOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprOr" ):
                return visitor.visitExprOr(self)
            else:
                return visitor.visitChildren(self)




    def exprOr(self):

        localctx = BC546Parser.ExprOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exprOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.exprAnd()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 152
                self.match(BC546Parser.OR)
                self.state = 153
                self.exprAnd()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprNot(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BC546Parser.ExprNotContext)
            else:
                return self.getTypedRuleContext(BC546Parser.ExprNotContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(BC546Parser.AND)
            else:
                return self.getToken(BC546Parser.AND, i)

        def getRuleIndex(self):
            return BC546Parser.RULE_exprAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAnd" ):
                listener.enterExprAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAnd" ):
                listener.exitExprAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAnd" ):
                return visitor.visitExprAnd(self)
            else:
                return visitor.visitChildren(self)




    def exprAnd(self):

        localctx = BC546Parser.ExprAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exprAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.exprNot()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 160
                self.match(BC546Parser.AND)
                self.state = 161
                self.exprNot()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprNotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BC546Parser.NOT, 0)

        def exprNot(self):
            return self.getTypedRuleContext(BC546Parser.ExprNotContext,0)


        def exprRel(self):
            return self.getTypedRuleContext(BC546Parser.ExprRelContext,0)


        def getRuleIndex(self):
            return BC546Parser.RULE_exprNot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprNot" ):
                listener.enterExprNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprNot" ):
                listener.exitExprNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNot" ):
                return visitor.visitExprNot(self)
            else:
                return visitor.visitChildren(self)




    def exprNot(self):

        localctx = BC546Parser.ExprNotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exprNot)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(BC546Parser.NOT)
                self.state = 168
                self.exprNot()
                pass
            elif token in [2, 26, 27, 28, 35, 36, 37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.exprRel()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprRelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprArt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BC546Parser.ExprArtContext)
            else:
                return self.getTypedRuleContext(BC546Parser.ExprArtContext,i)


        def IGUAL(self):
            return self.getToken(BC546Parser.IGUAL, 0)

        def DIF(self):
            return self.getToken(BC546Parser.DIF, 0)

        def MAIORIG(self):
            return self.getToken(BC546Parser.MAIORIG, 0)

        def MENORIG(self):
            return self.getToken(BC546Parser.MENORIG, 0)

        def MENOR(self):
            return self.getToken(BC546Parser.MENOR, 0)

        def MAIOR(self):
            return self.getToken(BC546Parser.MAIOR, 0)

        def getRuleIndex(self):
            return BC546Parser.RULE_exprRel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprRel" ):
                listener.enterExprRel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprRel" ):
                listener.exitExprRel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRel" ):
                return visitor.visitExprRel(self)
            else:
                return visitor.visitChildren(self)




    def exprRel(self):

        localctx = BC546Parser.ExprRelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exprRel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.exprArt()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 64512) != 0):
                self.state = 173
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64512) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 174
                self.exprArt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprArtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BC546Parser.TermoContext)
            else:
                return self.getTypedRuleContext(BC546Parser.TermoContext,i)


        def ADD_OP(self, i:int=None):
            if i is None:
                return self.getTokens(BC546Parser.ADD_OP)
            else:
                return self.getToken(BC546Parser.ADD_OP, i)

        def SUB_OP(self, i:int=None):
            if i is None:
                return self.getTokens(BC546Parser.SUB_OP)
            else:
                return self.getToken(BC546Parser.SUB_OP, i)

        def getRuleIndex(self):
            return BC546Parser.RULE_exprArt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprArt" ):
                listener.enterExprArt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprArt" ):
                listener.exitExprArt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprArt" ):
                return visitor.visitExprArt(self)
            else:
                return visitor.visitChildren(self)




    def exprArt(self):

        localctx = BC546Parser.ExprArtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exprArt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.termo()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 178
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 179
                self.termo()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BC546Parser.FatorContext)
            else:
                return self.getTypedRuleContext(BC546Parser.FatorContext,i)


        def MULT_OP(self, i:int=None):
            if i is None:
                return self.getTokens(BC546Parser.MULT_OP)
            else:
                return self.getToken(BC546Parser.MULT_OP, i)

        def DIV_OP(self, i:int=None):
            if i is None:
                return self.getTokens(BC546Parser.DIV_OP)
            else:
                return self.getToken(BC546Parser.DIV_OP, i)

        def MOD_OP(self, i:int=None):
            if i is None:
                return self.getTokens(BC546Parser.MOD_OP)
            else:
                return self.getToken(BC546Parser.MOD_OP, i)

        def getRuleIndex(self):
            return BC546Parser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermo" ):
                return visitor.visitTermo(self)
            else:
                return visitor.visitChildren(self)




    def termo(self):

        localctx = BC546Parser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.fator()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0):
                self.state = 186
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 187
                self.fator()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BC546Parser.INT, 0)

        def TEXT(self):
            return self.getToken(BC546Parser.TEXT, 0)

        def TRUE(self):
            return self.getToken(BC546Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BC546Parser.FALSE, 0)

        def NULL(self):
            return self.getToken(BC546Parser.NULL, 0)

        def chFun(self):
            return self.getTypedRuleContext(BC546Parser.ChFunContext,0)


        def ID(self):
            return self.getToken(BC546Parser.ID, 0)

        def PA(self):
            return self.getToken(BC546Parser.PA, 0)

        def expr(self):
            return self.getTypedRuleContext(BC546Parser.ExprContext,0)


        def PF(self):
            return self.getToken(BC546Parser.PF, 0)

        def getRuleIndex(self):
            return BC546Parser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFator" ):
                return visitor.visitFator(self)
            else:
                return visitor.visitChildren(self)




    def fator(self):

        localctx = BC546Parser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_fator)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(BC546Parser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(BC546Parser.TEXT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.match(BC546Parser.TRUE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.match(BC546Parser.FALSE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 197
                self.match(BC546Parser.NULL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 198
                self.chFun()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 199
                self.match(BC546Parser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 200
                self.match(BC546Parser.PA)
                self.state = 201
                self.expr()
                self.state = 202
                self.match(BC546Parser.PF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChFunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BC546Parser.ID, 0)

        def PA(self):
            return self.getToken(BC546Parser.PA, 0)

        def PF(self):
            return self.getToken(BC546Parser.PF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BC546Parser.ExprContext)
            else:
                return self.getTypedRuleContext(BC546Parser.ExprContext,i)


        def V(self, i:int=None):
            if i is None:
                return self.getTokens(BC546Parser.V)
            else:
                return self.getToken(BC546Parser.V, i)

        def getRuleIndex(self):
            return BC546Parser.RULE_chFun

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChFun" ):
                listener.enterChFun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChFun" ):
                listener.exitChFun(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChFun" ):
                return visitor.visitChFun(self)
            else:
                return visitor.visitChildren(self)




    def chFun(self):

        localctx = BC546Parser.ChFunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_chFun)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(BC546Parser.ID)
            self.state = 207
            self.match(BC546Parser.PA)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 240987931140) != 0):
                self.state = 208
                self.expr()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 209
                    self.match(BC546Parser.V)
                    self.state = 210
                    self.expr()
                    self.state = 215
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 218
            self.match(BC546Parser.PF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





