class PilhaSimbolos:
    def __init__(self):
        self.pilha: list[dict[str, str]] = [{}]
        self.erros: list[str] = []

    def entrar_escopo(self) -> None:
        self.pilha.append({})

    def sair_escopo(self) -> None:
        if len(self.pilha) > 1:
            self.pilha.pop()
        else:
            raise RuntimeError("Erro: Não é possível desempilhar o escopo global.")

    def declarar(self, nome: str, tipo: str, linha: int) -> bool:
        escopo_atual = self.pilha[-1]
        if nome in escopo_atual:
            self.erros.append(
                f"Erro Semântico [Linha {linha}]: Declaração duplicada da variável '{nome}'."
            )
            return False
        escopo_atual[nome] = tipo
        return True

    def verificar_uso(self, nome: str, linha: int):
        for escopo in reversed(self.pilha):
            if nome in escopo:
                return escopo[nome]
        self.erros.append(
            f"Erro Semântico [Linha {linha}]: Variável '{nome}' usada antes da declaração."
        )
        return None

    def exibir_erros(self) -> None:
        print("=== Relatório de Erros ===")
        if not self.erros:
            print("Nenhum erro semântico encontrado.")
        else:
            for erro in self.erros:
                print(erro)
