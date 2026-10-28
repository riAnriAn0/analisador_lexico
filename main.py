import sys
from antlr4 import CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from lexer import Lexer, construir_regras
from ponte import ListaTokenSource, converter
from BC546Parser import BC546Parser


class ErroSintatico(ErrorListener):
    def syntaxError(self, recognizer, offending, line, column, msg, e):
        print(f"Erro sintático L{line}:C{column + 1}: {msg}")


def main():
    with open(sys.argv[1], encoding="utf-8") as f:
        codigo = f.read()

    meus_tokens = Lexer(codigo, construir_regras()).tokenizar()

    fonte  = ListaTokenSource(converter(meus_tokens), sys.argv[1])
    stream = CommonTokenStream(fonte)
    parser = BC546Parser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(ErroSintatico())

    arvore = parser.program()
    print(arvore.toStringTree(recog=parser))


if __name__ == "__main__":
    main()