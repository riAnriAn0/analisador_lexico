import sys
from antlr4 import CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from antlr.BC546Parser import BC546Parser
from lexer.lexer import Lexer, construir_regras
from lexer.ponte import ListaTokenSource, converter
from semantica.analisador_semantico import AnalisadorSemantico

class ErroSintatico(ErrorListener):
    def syntaxError(self, recognizer, offending, line, column, msg, e):
        print(f"Erro sintático L{line}:C{column + 1}: {msg}")

def main():
    with open(sys.argv[1], encoding="utf-8") as f:
        codigo = f.read()
        
    meus_tokens = Lexer(codigo, construir_regras()).tokenizar()
    fonte = ListaTokenSource(converter(meus_tokens), sys.argv[1])
    stream = CommonTokenStream(fonte)
    parser = BC546Parser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ErroSintatico())
    arvore = parser.program()
    
    if parser.getNumberOfSyntaxErrors() == 0:
        analisador = AnalisadorSemantico()
        analisador.visit(arvore)

if __name__ == "__main__":
    main()