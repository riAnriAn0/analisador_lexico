# Generated from BC546Parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BC546Parser import BC546Parser
else:
    from BC546Parser import BC546Parser

# This class defines a complete generic visitor for a parse tree produced by BC546Parser.

class BC546ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BC546Parser#program.
    def visitProgram(self, ctx:BC546Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#statement.
    def visitStatement(self, ctx:BC546Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#bloco.
    def visitBloco(self, ctx:BC546Parser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#print.
    def visitPrint(self, ctx:BC546Parser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#input.
    def visitInput(self, ctx:BC546Parser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#tipo.
    def visitTipo(self, ctx:BC546Parser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#tipoRet.
    def visitTipoRet(self, ctx:BC546Parser.TipoRetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#varDecl.
    def visitVarDecl(self, ctx:BC546Parser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#atrib.
    def visitAtrib(self, ctx:BC546Parser.AtribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#funcDecl.
    def visitFuncDecl(self, ctx:BC546Parser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#params.
    def visitParams(self, ctx:BC546Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#param.
    def visitParam(self, ctx:BC546Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#return.
    def visitReturn(self, ctx:BC546Parser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#if.
    def visitIf(self, ctx:BC546Parser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#while.
    def visitWhile(self, ctx:BC546Parser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#expr.
    def visitExpr(self, ctx:BC546Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#exprOr.
    def visitExprOr(self, ctx:BC546Parser.ExprOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#exprAnd.
    def visitExprAnd(self, ctx:BC546Parser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#exprNot.
    def visitExprNot(self, ctx:BC546Parser.ExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#exprRel.
    def visitExprRel(self, ctx:BC546Parser.ExprRelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#exprArt.
    def visitExprArt(self, ctx:BC546Parser.ExprArtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#termo.
    def visitTermo(self, ctx:BC546Parser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#fator.
    def visitFator(self, ctx:BC546Parser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BC546Parser#chFun.
    def visitChFun(self, ctx:BC546Parser.ChFunContext):
        return self.visitChildren(ctx)



del BC546Parser