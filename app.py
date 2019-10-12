## Importando arquivo funções (functions.py)
from functions import *

## Constantes
OPCAO_ENCERRAR_PROGRAMA = 7

## Variáveis
menuInicial  = True
opcaoEscolhida = 0

while menuInicial:
    ## Limpa o console
    limpaConsole()

    exibeMenuInicial()

    opcaoEscolhida = int(input('\nOpção desejada: '))

    if getArrayOpcoes().count(opcaoEscolhida) > 0:
        menuInicial = False

        if opcaoEscolhida != OPCAO_ENCERRAR_PROGRAMA:
            exibeObjetosByOpcao(opcaoEscolhida)
    else:
        exibeMensagemErro('Opção inexistente. Tente novamnete.')

