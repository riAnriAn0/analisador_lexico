from antlr.BC546Parser import BC546Parser
from antlr.BC546ParserVisitor import BC546ParserVisitor
from semantica.pilha_simbolos import PilhaSimbolos

class AnalisadorSemantico(BC546ParserVisitor):
    def __init__(self):
        self.ts = PilhaSimbolos()
        self._escopo_funcao_aberto = False
        self._tipo_retorno_atual: str | None = None

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
        nome_func = no_id.getText()
        tipo_ret = ctx.tipoRet().getText()
        linha = no_id.getSymbol().line
        tipos_params = [p.tipo().getText() for p in ctx.params().param()] if ctx.params() else []
        self.ts.declarar(
            nome_func,
            tipo_ret,
            linha,
            qnt_params=len(tipos_params),
            tipo_params=tipos_params,
        )
        retorno_anterior = self._tipo_retorno_atual
        self._tipo_retorno_atual = tipo_ret
        self.ts.entrar_escopo()
        self._escopo_funcao_aberto = True
        if ctx.params():
            self.visit(ctx.params())
        self.visit(ctx.bloco())
        self._escopo_funcao_aberto = False
        self.ts.sair_escopo()
        self._tipo_retorno_atual = retorno_anterior
        return None

    def visitParam(self, ctx: BC546Parser.ParamContext):
        no_id = ctx.ID()
        tipo = ctx.tipo().getText()
        self.ts.declarar(no_id.getText(), tipo, no_id.getSymbol().line)
        return None

    def visitVarDecl(self, ctx: BC546Parser.VarDeclContext):
        tipo_expr = self.visit(ctx.expr())
        no_id = ctx.ID()
        nome_var = no_id.getText()
        tipo_var = ctx.tipo().getText()
        linha = no_id.getSymbol().line
        if tipo_expr is not None and tipo_expr != tipo_var and tipo_expr != "null":
            self.ts.erros.append(
                f"Erro Semântico [Linha {linha}]: Não é possível inicializar '{nome_var}' "
                f"do tipo '{tipo_var}' com valor do tipo '{tipo_expr}'."
            )
        self.ts.declarar(nome_var, tipo_var, linha)
        return None

    def visitAtrib(self, ctx: BC546Parser.AtribContext):
        no_id = ctx.ID()
        nome_var = no_id.getText()
        linha = no_id.getSymbol().line
        info = self.ts.verificar_uso(nome_var, linha)
        tipo_expr = self.visit(ctx.expr())
        if info is not None:
            if info["qnt_params"] is not None:
                self.ts.erros.append(
                    f"Erro Semântico [Linha {linha}]: Não é possível atribuir valor à função '{nome_var}'."
                )
            elif tipo_expr is not None and info["tipo"] != tipo_expr and tipo_expr != "null":
                self.ts.erros.append(
                    f"Erro Semântico [Linha {linha}]: Não é possível atribuir '{tipo_expr}' "
                    f"à variável '{nome_var}' do tipo '{info['tipo']}'."
                )
        return None

    def visitReturn(self, ctx: BC546Parser.ReturnContext):
        linha = ctx.start.line
        if self._tipo_retorno_atual is None:
            self.ts.erros.append(
                f"Erro Semântico [Linha {linha}]: Comando 'return' usado fora de uma função."
            )
            return None
        tipo_retornado = self.visit(ctx.expr()) if ctx.expr() else "void"
        if tipo_retornado is not None and tipo_retornado != self._tipo_retorno_atual and tipo_retornado != "null":
            self.ts.erros.append(
                f"Erro Semântico [Linha {linha}]: Retorno incompatível. "
                f"Função espera '{self._tipo_retorno_atual}', mas recebeu '{tipo_retornado}'."
            )
        return None

    def visitIf(self, ctx: BC546Parser.IfContext):
        tipo_cond = self.visit(ctx.expr())
        if tipo_cond is not None and tipo_cond != "bool":
            self.ts.erros.append(
                f"Erro Semântico [Linha {ctx.start.line}]: Condição do 'if' deve ser 'bool', "
                f"mas recebeu '{tipo_cond}'."
            )
        self.visit(ctx.bloco())
        return None

    def visitWhile(self, ctx: BC546Parser.WhileContext):
        tipo_cond = self.visit(ctx.expr())
        if tipo_cond is not None and tipo_cond != "bool":
            self.ts.erros.append(
                f"Erro Semântico [Linha {ctx.start.line}]: Condição do 'while' deve ser 'bool', "
                f"mas recebeu '{tipo_cond}'."
            )
        self.visit(ctx.bloco())
        return None

    def visitInput(self, ctx: BC546Parser.InputContext):
        return self.visitChildren(ctx)

    def visitExpr(self, ctx: BC546Parser.ExprContext):
        return self.visit(ctx.exprOr())

    def visitExprOr(self, ctx: BC546Parser.ExprOrContext):
        itens = ctx.exprAnd()
        if len(itens) == 1:
            return self.visit(itens[0])
        for item in itens:
            tipo = self.visit(item)
            if tipo is not None and tipo != "bool":
                self.ts.erros.append(
                    f"Erro Semântico [Linha {ctx.start.line}]: Operador lógico 'or' exige 'bool', "
                    f"mas recebeu '{tipo}'."
                )
                return None
        return "bool"

    def visitExprAnd(self, ctx: BC546Parser.ExprAndContext):
        itens = ctx.exprNot()
        if len(itens) == 1:
            return self.visit(itens[0])
        for item in itens:
            tipo = self.visit(item)
            if tipo is not None and tipo != "bool":
                self.ts.erros.append(
                    f"Erro Semântico [Linha {ctx.start.line}]: Operador lógico 'and' exige 'bool', "
                    f"mas recebeu '{tipo}'."
                )
                return None
        return "bool"

    def visitExprNot(self, ctx: BC546Parser.ExprNotContext):
        if ctx.NOT():
            tipo = self.visit(ctx.exprNot())
            if tipo is not None and tipo != "bool":
                self.ts.erros.append(
                    f"Erro Semântico [Linha {ctx.start.line}]: Operador 'not' exige 'bool', "
                    f"mas recebeu '{tipo}'."
                )
                return None
            return "bool"
        return self.visit(ctx.exprRel())

    def visitExprRel(self, ctx: BC546Parser.ExprRelContext):
        exprs = ctx.exprArt()
        if len(exprs) == 1:
            return self.visit(exprs[0])
        tipo_esq = self.visit(exprs[0])
        tipo_dir = self.visit(exprs[1])
        operador = ctx.getChild(1).getText()
        linha = ctx.start.line
        if tipo_esq is None or tipo_dir is None:
            return None
        if operador in (">", "<", ">=", "<="):
            if tipo_esq != "num" or tipo_dir != "num":
                self.ts.erros.append(
                    f"Erro Semântico [Linha {linha}]: Operador '{operador}' exige operandos 'num', "
                    f"mas recebeu '{tipo_esq}' e '{tipo_dir}'."
                )
                return None
        elif tipo_esq != tipo_dir and "null" not in (tipo_esq, tipo_dir):
            self.ts.erros.append(
                f"Erro Semântico [Linha {linha}]: Comparação '{operador}' incompatível "
                f"entre '{tipo_esq}' e '{tipo_dir}'."
            )
            return None
        return "bool"

    def visitExprArt(self, ctx: BC546Parser.ExprArtContext):
        termos = ctx.termo()
        if len(termos) == 1:
            return self.visit(termos[0])
        tipo_acumulado = self.visit(termos[0])
        for i in range(1, len(termos)):
            tipo_dir = self.visit(termos[i])
            operador = ctx.getChild(2 * i - 1).getText()
            if tipo_acumulado is None or tipo_dir is None:
                return None
            if tipo_acumulado != "num" or tipo_dir != "num":
                self.ts.erros.append(
                    f"Erro Semântico [Linha {ctx.start.line}]: Operador '{operador}' inválido "
                    f"entre '{tipo_acumulado}' e '{tipo_dir}'."
                )
                return None
        return "num"

    def visitTermo(self, ctx: BC546Parser.TermoContext):
        fatores = ctx.fator()
        if len(fatores) == 1:
            return self.visit(fatores[0])
        tipo_acumulado = self.visit(fatores[0])
        for i in range(1, len(fatores)):
            tipo_dir = self.visit(fatores[i])
            operador = ctx.getChild(2 * i - 1).getText()
            if tipo_acumulado is None or tipo_dir is None:
                return None
            if tipo_acumulado != "num" or tipo_dir != "num":
                self.ts.erros.append(
                    f"Erro Semântico [Linha {ctx.start.line}]: Operador '{operador}' inválido "
                    f"entre '{tipo_acumulado}' e '{tipo_dir}'."
                )
                return None
        return "num"

    def visitFator(self, ctx: BC546Parser.FatorContext):
        if ctx.INT():
            return "num"
        if ctx.TEXT():
            return "str"
        if ctx.TRUE() or ctx.FALSE():
            return "bool"
        if ctx.NULL():
            return "null"
        if ctx.chFun():
            return self.visit(ctx.chFun())
        if ctx.ID():
            no_id = ctx.ID()
            nome_var = no_id.getText()
            linha = no_id.getSymbol().line
            info = self.ts.verificar_uso(nome_var, linha)
            if info is not None:
                if info["qnt_params"] is not None:
                    self.ts.erros.append(
                        f"Erro Semântico [Linha {linha}]: Função '{nome_var}' "
                        f"usada como variável sem chamada '()'."
                    )
                    return None
                return info["tipo"]
            return None
        if ctx.expr():
            return self.visit(ctx.expr())
        return None

    def visitChFun(self, ctx: BC546Parser.ChFunContext):
        no_id = ctx.ID()
        nome_func = no_id.getText()
        linha = no_id.getSymbol().line
        info = self.ts.verificar_uso(nome_func, linha)
        args = ctx.expr() or []
        tipos_args = [self.visit(arg) for arg in args]
        if info is not None:
            if info["qnt_params"] is None:
                self.ts.erros.append(
                    f"Erro Semântico [Linha {linha}]: '{nome_func}' não é uma função e não pode ser chamada."
                )
                return None
            if len(args) != info["qnt_params"]:
                self.ts.erros.append(
                    f"Erro Semântico [Linha {linha}]: Função '{nome_func}' espera "
                    f"{info['qnt_params']} argumento(s), mas recebeu {len(args)}."
                )
            else:
                for indice, (tipo_arg, tipo_param) in enumerate(zip(tipos_args, info["tipo_params"]), start=1):
                    if tipo_arg is not None and tipo_arg != tipo_param and tipo_arg != "null":
                        self.ts.erros.append(
                            f"Erro Semântico [Linha {linha}]: Argumento {indice} de '{nome_func}' "
                            f"espera '{tipo_param}', mas recebeu '{tipo_arg}'."
                        )
            return info["tipo"]
        return None