# Generated from BC546Parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BC546Parser import BC546Parser
else:
    from BC546Parser import BC546Parser

# This class defines a complete listener for a parse tree produced by BC546Parser.
class BC546ParserListener(ParseTreeListener):

    # Enter a parse tree produced by BC546Parser#program.
    def enterProgram(self, ctx:BC546Parser.ProgramContext):
        pass

    # Exit a parse tree produced by BC546Parser#program.
    def exitProgram(self, ctx:BC546Parser.ProgramContext):
        pass


    # Enter a parse tree produced by BC546Parser#statement.
    def enterStatement(self, ctx:BC546Parser.StatementContext):
        pass

    # Exit a parse tree produced by BC546Parser#statement.
    def exitStatement(self, ctx:BC546Parser.StatementContext):
        pass


    # Enter a parse tree produced by BC546Parser#bloco.
    def enterBloco(self, ctx:BC546Parser.BlocoContext):
        pass

    # Exit a parse tree produced by BC546Parser#bloco.
    def exitBloco(self, ctx:BC546Parser.BlocoContext):
        pass


    # Enter a parse tree produced by BC546Parser#print.
    def enterPrint(self, ctx:BC546Parser.PrintContext):
        pass

    # Exit a parse tree produced by BC546Parser#print.
    def exitPrint(self, ctx:BC546Parser.PrintContext):
        pass


    # Enter a parse tree produced by BC546Parser#input.
    def enterInput(self, ctx:BC546Parser.InputContext):
        pass

    # Exit a parse tree produced by BC546Parser#input.
    def exitInput(self, ctx:BC546Parser.InputContext):
        pass


    # Enter a parse tree produced by BC546Parser#tipo.
    def enterTipo(self, ctx:BC546Parser.TipoContext):
        pass

    # Exit a parse tree produced by BC546Parser#tipo.
    def exitTipo(self, ctx:BC546Parser.TipoContext):
        pass


    # Enter a parse tree produced by BC546Parser#tipoRet.
    def enterTipoRet(self, ctx:BC546Parser.TipoRetContext):
        pass

    # Exit a parse tree produced by BC546Parser#tipoRet.
    def exitTipoRet(self, ctx:BC546Parser.TipoRetContext):
        pass


    # Enter a parse tree produced by BC546Parser#varDecl.
    def enterVarDecl(self, ctx:BC546Parser.VarDeclContext):
        pass

    # Exit a parse tree produced by BC546Parser#varDecl.
    def exitVarDecl(self, ctx:BC546Parser.VarDeclContext):
        pass


    # Enter a parse tree produced by BC546Parser#atrib.
    def enterAtrib(self, ctx:BC546Parser.AtribContext):
        pass

    # Exit a parse tree produced by BC546Parser#atrib.
    def exitAtrib(self, ctx:BC546Parser.AtribContext):
        pass


    # Enter a parse tree produced by BC546Parser#funcDecl.
    def enterFuncDecl(self, ctx:BC546Parser.FuncDeclContext):
        pass

    # Exit a parse tree produced by BC546Parser#funcDecl.
    def exitFuncDecl(self, ctx:BC546Parser.FuncDeclContext):
        pass


    # Enter a parse tree produced by BC546Parser#params.
    def enterParams(self, ctx:BC546Parser.ParamsContext):
        pass

    # Exit a parse tree produced by BC546Parser#params.
    def exitParams(self, ctx:BC546Parser.ParamsContext):
        pass


    # Enter a parse tree produced by BC546Parser#param.
    def enterParam(self, ctx:BC546Parser.ParamContext):
        pass

    # Exit a parse tree produced by BC546Parser#param.
    def exitParam(self, ctx:BC546Parser.ParamContext):
        pass


    # Enter a parse tree produced by BC546Parser#return.
    def enterReturn(self, ctx:BC546Parser.ReturnContext):
        pass

    # Exit a parse tree produced by BC546Parser#return.
    def exitReturn(self, ctx:BC546Parser.ReturnContext):
        pass


    # Enter a parse tree produced by BC546Parser#if.
    def enterIf(self, ctx:BC546Parser.IfContext):
        pass

    # Exit a parse tree produced by BC546Parser#if.
    def exitIf(self, ctx:BC546Parser.IfContext):
        pass


    # Enter a parse tree produced by BC546Parser#while.
    def enterWhile(self, ctx:BC546Parser.WhileContext):
        pass

    # Exit a parse tree produced by BC546Parser#while.
    def exitWhile(self, ctx:BC546Parser.WhileContext):
        pass


    # Enter a parse tree produced by BC546Parser#expr.
    def enterExpr(self, ctx:BC546Parser.ExprContext):
        pass

    # Exit a parse tree produced by BC546Parser#expr.
    def exitExpr(self, ctx:BC546Parser.ExprContext):
        pass


    # Enter a parse tree produced by BC546Parser#exprOr.
    def enterExprOr(self, ctx:BC546Parser.ExprOrContext):
        pass

    # Exit a parse tree produced by BC546Parser#exprOr.
    def exitExprOr(self, ctx:BC546Parser.ExprOrContext):
        pass


    # Enter a parse tree produced by BC546Parser#exprAnd.
    def enterExprAnd(self, ctx:BC546Parser.ExprAndContext):
        pass

    # Exit a parse tree produced by BC546Parser#exprAnd.
    def exitExprAnd(self, ctx:BC546Parser.ExprAndContext):
        pass


    # Enter a parse tree produced by BC546Parser#exprNot.
    def enterExprNot(self, ctx:BC546Parser.ExprNotContext):
        pass

    # Exit a parse tree produced by BC546Parser#exprNot.
    def exitExprNot(self, ctx:BC546Parser.ExprNotContext):
        pass


    # Enter a parse tree produced by BC546Parser#exprRel.
    def enterExprRel(self, ctx:BC546Parser.ExprRelContext):
        pass

    # Exit a parse tree produced by BC546Parser#exprRel.
    def exitExprRel(self, ctx:BC546Parser.ExprRelContext):
        pass


    # Enter a parse tree produced by BC546Parser#exprArt.
    def enterExprArt(self, ctx:BC546Parser.ExprArtContext):
        pass

    # Exit a parse tree produced by BC546Parser#exprArt.
    def exitExprArt(self, ctx:BC546Parser.ExprArtContext):
        pass


    # Enter a parse tree produced by BC546Parser#termo.
    def enterTermo(self, ctx:BC546Parser.TermoContext):
        pass

    # Exit a parse tree produced by BC546Parser#termo.
    def exitTermo(self, ctx:BC546Parser.TermoContext):
        pass


    # Enter a parse tree produced by BC546Parser#fator.
    def enterFator(self, ctx:BC546Parser.FatorContext):
        pass

    # Exit a parse tree produced by BC546Parser#fator.
    def exitFator(self, ctx:BC546Parser.FatorContext):
        pass


    # Enter a parse tree produced by BC546Parser#chFun.
    def enterChFun(self, ctx:BC546Parser.ChFunContext):
        pass

    # Exit a parse tree produced by BC546Parser#chFun.
    def exitChFun(self, ctx:BC546Parser.ChFunContext):
        pass



del BC546Parser