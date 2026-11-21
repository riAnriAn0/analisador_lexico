from antlr.BC546Parser import BC546Parser
from antlr.BC546ParserVisitor import BC546ParserVisitor
from semantica.pilha_simbolos import PilhaSimbolos

class AnalisadorSemantico(BC546ParserVisitor):
    def __init__(self):
        self.ts = PilhaSimbolos()
        self._escopo_funcao_aberto = False

    def visitProgram(self, ctx: BC546Parser.ProgramContext):
        self.visitChildren(ctx)
        self.ts.exibir_erros()
        return None

    def visitBloco(self, ctx: BC546Parser.BlocoContext):
        if self._escopo_funcao_aberto:
            self._escopo_funcao_aberto = False
            return self.visitChildren(ctx)
        self.ts.entrar_escopo()
        self.visitChildren(ctx)
        self.ts.sair_escopo()
        return None

    def visitFuncDecl(self, ctx: BC546Parser.FuncDeclContext):
        if hasattr(ctx, "ID") and ctx.ID():
            no_id = ctx.ID()
            tipo_ret = ctx.tipoRet().getText() if hasattr(ctx, "tipoRet") and ctx.tipoRet() else "void"
            self.ts.declarar(no_id.getText(), tipo_ret, no_id.getSymbol().line)
        self.ts.entrar_escopo()
        self._escopo_funcao_aberto = True
        if hasattr(ctx, "params") and ctx.params():
            self.visit(ctx.params())
        if hasattr(ctx, "bloco") and ctx.bloco():
            self.visit(ctx.bloco())
        self.ts.sair_escopo()
        return None

    def visitParam(self, ctx: BC546Parser.ParamContext):
        if hasattr(ctx, "ID") and ctx.ID() and hasattr(ctx, "tipo") and ctx.tipo():
            no_id = ctx.ID()
            tipo = ctx.tipo().getText()
            self.ts.declarar(no_id.getText(), tipo, no_id.getSymbol().line)
        return self.visitChildren(ctx)

    def visitVarDecl(self, ctx: BC546Parser.VarDeclContext):
        if hasattr(ctx, "expr") and ctx.expr():
            expressoes = ctx.expr() if isinstance(ctx.expr(), list) else [ctx.expr()]
            for expressao in expressoes:
                self.visit(expressao)
        if hasattr(ctx, "ID") and ctx.ID() and hasattr(ctx, "tipo") and ctx.tipo():
            tipo = ctx.tipo().getText()
            ids = ctx.ID() if isinstance(ctx.ID(), list) else [ctx.ID()]
            for no_id in ids:
                self.ts.declarar(no_id.getText(), tipo, no_id.getSymbol().line)
        return None

    def visitAtrib(self, ctx: BC546Parser.AtribContext):
        if hasattr(ctx, "ID") and ctx.ID():
            no_id = ctx.ID()
            self.ts.verificar_uso(no_id.getText(), no_id.getSymbol().line)
        return self.visitChildren(ctx)

    def visitInput(self, ctx: BC546Parser.InputContext):
        if hasattr(ctx, "ID") and ctx.ID():
            ids = ctx.ID() if isinstance(ctx.ID(), list) else [ctx.ID()]
            for no_id in ids:
                self.ts.verificar_uso(no_id.getText(), no_id.getSymbol().line)
        return self.visitChildren(ctx)

    def visitFator(self, ctx: BC546Parser.FatorContext):
        if hasattr(ctx, "ID") and ctx.ID():
            no_id = ctx.ID()
            self.ts.verificar_uso(no_id.getText(), no_id.getSymbol().line)
        return self.visitChildren(ctx)

    def visitChFun(self, ctx: BC546Parser.ChFunContext):
        if hasattr(ctx, "ID") and ctx.ID():
            no_id = ctx.ID()
            self.ts.verificar_uso(no_id.getText(), no_id.getSymbol().line)
        return self.visitChildren(ctx)