class PilhaSimbolos:
    def __init__(self):
        self.pilha: list[dict[str, dict]] = [{}]
        self.erros: list[str] = []

    def entrar_escopo(self) -> None:
        self.pilha.append({})

    def sair_escopo(self) -> None:
        if len(self.pilha) > 1:
            self.pilha.pop()
        else:
            raise RuntimeError("Erro: Não é possível desempilhar o escopo global.")

    def declarar(
        self,
        nome: str,
        tipo: str,
        linha: int,
        qnt_params: int | None = None,
        tipo_params: list[str] | None = None,
    ) -> bool:
        escopo_atual = self.pilha[-1]
        if nome in escopo_atual:
            self.erros.append(
                f"Erro Semântico [Linha {linha}]: Declaração duplicada de '{nome}'."
            )
            return False
        escopo_atual[nome] = {
            "tipo": tipo,
            "qnt_params": qnt_params,
            "tipo_params": tipo_params,
        }
        return True

    def verificar_uso(self, nome: str, linha: int) -> dict | None:
        for escopo in reversed(self.pilha):
            if nome in escopo:
                return escopo[nome]
        self.erros.append(
            f"Erro Semântico [Linha {linha}]: Identificador '{nome}' usado antes da declaração."
        )
        return None

    def exibir_tabela(self) -> None:
        print("=== Tabela de Símbolos (Topo -> Base) ===")
        for nivel in range(len(self.pilha) - 1, -1, -1):
            rotulo = "Escopo Global" if nivel == 0 else f"Escopo Local (Nível {nivel})"
            if nivel == len(self.pilha) - 1:
                rotulo += " [TOPO]"
            escopo = self.pilha[nivel]
            print(f"{rotulo}:")
            if not escopo:
                print("  (vazio)")
            else:
                for nome, dados in escopo.items():
                    if dados["qnt_params"] is not None:
                        print(
                            f"  {nome} -> tipo: {dados['tipo']} | "
                            f"qnt_params: {dados['qnt_params']} | "
                            f"tipo_params: {dados['tipo_params']}"
                        )
                    else:
                        print(f"  {nome} -> tipo: {dados['tipo']}")

    def exibir_erros(self) -> None:
        if not self.erros:
            print("Nenhum erro semântico encontrado.")
        else:
            for erro in self.erros:
                print(erro)