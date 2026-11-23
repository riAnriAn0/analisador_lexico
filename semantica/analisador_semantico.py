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
        no_id = ctx.ID()
        tipo_ret = ctx.tipoRet().getText()
        self.ts.declarar(no_id.getText(), tipo_ret, no_id.getSymbol().line)
        self.ts.entrar_escopo()
        self._escopo_funcao_aberto = True
        if ctx.params():
            self.visit(ctx.params())
        self.visit(ctx.bloco())
        self._escopo_funcao_aberto = False
        self.ts.sair_escopo()
        return None

    def visitParam(self, ctx: BC546Parser.ParamContext):
        no_id = ctx.ID()
        tipo = ctx.tipo().getText()
        self.ts.declarar(no_id.getText(), tipo, no_id.getSymbol().line)
        return None

    def visitVarDecl(self, ctx: BC546Parser.VarDeclContext):
        self.visit(ctx.expr())
        no_id = ctx.ID()
        tipo = ctx.tipo().getText()
        self.ts.declarar(no_id.getText(), tipo, no_id.getSymbol().line)
        return None

    def visitAtrib(self, ctx: BC546Parser.AtribContext):
        no_id = ctx.ID()
        self.ts.verificar_uso(no_id.getText(), no_id.getSymbol().line)
        self.visit(ctx.expr())
        return None

    def visitIf(self, ctx: BC546Parser.IfContext):
        self.visit(ctx.expr())
        self.visit(ctx.bloco())
        return None

    def visitWhile(self, ctx: BC546Parser.WhileContext):
        self.visit(ctx.expr())
        self.visit(ctx.bloco())
        return None

    def visitInput(self, ctx: BC546Parser.InputContext):
        return self.visitChildren(ctx)

    def visitFator(self, ctx: BC546Parser.FatorContext):
        if ctx.ID():
            no_id = ctx.ID()
            self.ts.verificar_uso(no_id.getText(), no_id.getSymbol().line)
        return self.visitChildren(ctx)

    def visitChFun(self, ctx: BC546Parser.ChFunContext):
        no_id = ctx.ID()
        self.ts.verificar_uso(no_id.getText(), no_id.getSymbol().line)
        return self.visitChildren(ctx)