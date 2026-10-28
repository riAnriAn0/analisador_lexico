from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import sys


# =====================================================================
# 1. TOKEN
# =====================================================================

@dataclass
class Token:
    tipo: str
    valor: str
    linha: int
    coluna: int

    def __repr__(self) -> str:
        return f"<{self.tipo}, {self.valor!r}> @ {self.linha}:{self.coluna}"

# =====================================================================
# 2. AFD — tabela de transições
# =====================================================================

class AFD:
    def __init__(self, nome: str):
        self.nome = nome
        self.transicoes: dict[tuple[int, str], int] = {}
        self.finais: set[int] = set()
        self.inicial: int = 0
        self._prox: int = 1

    def novo_estado(self) -> int:
        e = self._prox
        self._prox += 1
        return e

    def transicao(self, origem: int, simbolos: str, destino: int) -> None:
        for c in simbolos:
            self.transicoes[(origem, c)] = destino

    def marcar_final(self, estado: int) -> None:
        self.finais.add(estado)

    def maior_prefixo(self, texto: str) -> int:
        estado = self.inicial
        ultimo = 0 if estado in self.finais else -1

        for i, c in enumerate(texto):
            prox = self.transicoes.get((estado, c))
            if prox is None:
                break
            estado = prox
            if estado in self.finais:
                ultimo = i + 1

        return ultimo


# =====================================================================
# 3. CONFIGURAÇÃO DA LINGUAGEM
# =====================================================================

LETRAS_ID      = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
INICIAIS_ID    = "_"
CONTINUACAO_ID = LETRAS_ID + "0123456789_"

DIGITOS = "0123456789"

# Palavras-chave alfanuméricas (reclassificadas a partir de ID)
PALAVRAS_RESERVADAS: dict[str, str] = {
    "if": "IF",
    "while": "WHILE",
    "break": "BREAK",
    "num": "T_NUM",
    "str": "T_STR",
    "bool": "T_BOOL",
    "print": "PRINT",
    "input": "INPUT",
    "void": "VOID",
    "int": "INT",
    "func": "FUNC",
    "return": "RETURN",
    "and": "AND",
    "or": "OR",
    "not": "NOT",
    "true": "TRUE",
    "false": "FALSE",
}

# Operadores de pontuação e símbolos compostos
OPERADORES: dict[str, str] = {
    "==": "IGUAL",
    "=":  "ATRIB",
    "!=": "DIF",
    "<=": "MENORIG",
    ">=": "MAIORIG",
    "<":  "MENOR",
    ">":  "MAIOR",
}

# Símbolos simples (1 caractere)
SIMBOLOS: dict[str, str] = {
    "(": "PA",
    ")": "PF",
    "{": "CHA",
    "}": "CHF",
    ";": "PV",
    # ":": "DP",  REMOVIDOS POR FALTE DE UTILIZAÇÃO NA LINGUAGEM
    # ".": "P",
    ",": "V",
    "[": "COA",
    "]": "COF",
    "+": "ADD_OP",
    "-": "SUB_OP",
    "/": "DIV_OP",
    "*": "MULT_OP",
    "%": "MOD_OP",
}

FIXOS: dict[str, str] = {**PALAVRAS_RESERVADAS,**OPERADORES, **SIMBOLOS}


# =====================================================================
# 4. CONSTRUTORES GENÉRICOS DE AFDs
# =====================================================================

def afd_string() -> AFD:
    afd = AFD("TEXT")
    q1 = afd.novo_estado()
    q2 = afd.novo_estado()
    afd.transicao(afd.inicial, '"', q1)

    caracteres = "".join(chr(i) for i in range(32, 127) if chr(i) != '"')
    
    afd.transicao(q1, caracteres, q1)
    afd.transicao(q1, '"', q2)
    afd.marcar_final(q2)
    return afd


def afd_literal(nome: str, texto: str) -> AFD:
    afd = AFD(nome)
    atual = afd.inicial
    for c in texto:
        prox = afd.novo_estado()
        afd.transicao(atual, c, prox)
        atual = prox
    afd.marcar_final(atual)
    return afd


def afd_conjunto_literais(nome: str, textos: list[str]) -> AFD:
    afd = AFD(nome)
    for texto in textos:
        atual = afd.inicial
        for c in texto:
            prox = afd.transicoes.get((atual, c))
            if prox is None:
                prox = afd.novo_estado()
                afd.transicao(atual, c, prox)
            atual = prox
        afd.marcar_final(atual)
    return afd


# =====================================================================
# 5. CONSTRUTORES ESPECÍFICOS — ID e NUM
# =====================================================================

def afd_identificador() -> AFD:
    afd = AFD("ID")
    q1 = afd.novo_estado()
    afd.transicao(afd.inicial, INICIAIS_ID, q1)
    afd.transicao(q1, CONTINUACAO_ID, q1)
    afd.marcar_final(q1)
    return afd


def afd_numero() -> AFD:
    afd = AFD("INT")
    q1 = afd.novo_estado()
    
    afd.transicao(afd.inicial, DIGITOS, q1)
    afd.transicao(q1, DIGITOS, q1)
    afd.marcar_final(q1)
    
    return afd


# =====================================================================
# 6. LEXER
# =====================================================================

class Lexer:
    def __init__(self, entrada: str, regras: list[tuple[str, AFD]]):
        self.entrada = entrada
        self.regras = regras
        self.pos = 0
        self.linha = 1
        self.coluna = 1

    def _avancar(self, n: int) -> None:
        for _ in range(n):
            if self.pos >= len(self.entrada):
                return
            if self.entrada[self.pos] == "\n":
                self.linha += 1
                self.coluna = 1
            else:
                self.coluna += 1
            self.pos += 1

    def _reclassificar(self, tipo: str, valor: str) -> str:
        if tipo == "ID" and valor in PALAVRAS_RESERVADAS:
            return PALAVRAS_RESERVADAS[valor]
        if tipo == "FIXO":
            return FIXOS[valor]
        return tipo

    def proximo_token(self) -> Token | None:
        # 1) Ignorar espaços em branco
        while self.pos < len(self.entrada) and self.entrada[self.pos] in " \t\r\n":
            self._avancar(1)
            
        if self.pos >= len(self.entrada):
            return None

        linha, coluna = self.linha, self.coluna
        resto = self.entrada[self.pos:]

        # 2) Maximal Munch: encontra o maior casamento entre as regras
        melhor_tipo: str | None = None
        melhor_tam = 0
        for tipo, afd in self.regras:
            tam = afd.maior_prefixo(resto)
            if tam > melhor_tam:
                melhor_tam = tam
                melhor_tipo = tipo

        if melhor_tam <= 0 or melhor_tipo is None:
            raise SyntaxError(
                f"Caractere inesperado {resto[0]!r} em L{linha}:C{coluna}"
            )

        valor = resto[:melhor_tam]
        self._avancar(melhor_tam)

        # 3) Reclassificação
        tipo_final = self._reclassificar(melhor_tipo, valor)

        return Token(tipo_final, valor, linha, coluna)

    def tokenizar(self) -> list[Token]:
        tokens: list[Token] = []
        while True:
            token = self.proximo_token()
            if token is None:
                break
            tokens.append(token)
        return tokens


# =====================================================================
# 7. PROGRAMA PRINCIPAL
# =====================================================================

def construir_regras() -> list[tuple[str, AFD]]:
    return [
        ("FIXO", afd_conjunto_literais("FIXO", sorted(FIXOS))),
        ("TEXT", afd_string()),
        ("INT",  afd_numero()),
        ("ID",   afd_identificador()),
    ]

def formatar_tabela(tokens: list[Token]) -> str:
    linhas = [
        f"{'TEXTO':<20} {'TOKEN':<15}",
        "-" * 24 ,
    ]
    for tok in tokens:
        linhas.append(f"{tok.valor:<20} {tok.tipo:<15}")
    return "\n".join(linhas) + "\n"


def main() -> None:
    arquivo_saida = "tabela_sainda.txt"

    if len(sys.argv) > 1:
        caminho_entrada = sys.argv[1]
        with open(caminho_entrada, "r", encoding="utf-8") as f:
            codigo = f.read()
            arquivo_saida = f"{Path(caminho_entrada).stem}_tokens.txt"
    else:
        codigo = ("int _val= 0; if(true and true){ return 1.2;}else{return 0;}")

    tokens = Lexer(codigo, construir_regras()).tokenizar()
    tabela = formatar_tabela(tokens)

    print(tabela)

    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(tabela)


if __name__ == "__main__":
    main()