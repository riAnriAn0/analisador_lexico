from antlr4.Token import Token, CommonToken
from antlr4.CommonTokenFactory import CommonTokenFactory

from BC546Parser import BC546Parser


class ListaTokenSource:
    def __init__(self, tokens: list[CommonToken], nome: str = "tokens"):
        self._tokens = tokens
        self._i = 0
        self._nome = nome
        self._factory = CommonTokenFactory.DEFAULT

    def nextToken(self) -> CommonToken:
        t = self._tokens[min(self._i, len(self._tokens) - 1)]
        self._i += 1
        return t

    def getSourceName(self) -> str:
        return self._nome


def tipo_por_nome(nome: str) -> int:
    try:
        return BC546Parser.symbolicNames.index(nome)
    except ValueError:
        raise ValueError(f"Token '{nome}' não existe na gramática")


def converter(meus_tokens) -> list[CommonToken]:
    saida = []
    for t in meus_tokens:
        ct = CommonToken(type=tipo_por_nome(t.tipo))
        ct.text = t.valor
        ct.line = t.linha
        ct.column = t.coluna - 1
        saida.append(ct)

    eof = CommonToken(type=Token.EOF)
    eof.text = "<EOF>"
    eof.line = meus_tokens[-1].linha if meus_tokens else 1
    eof.column = 0
    saida.append(eof)
    return saida