## Importações
import os

## Exibe o menu principal da aplicação
def exibeMenuInicial():
    print(
        """Digite o número de uma opção abaixo:
        
        [1] - Plástico
        [2] - Metal
        [3] - Vidro
        [4] - Papel
        [5] - Eletrônicos
        [6] - Outros
        [7] - Encerrar o programa"""
    )

## Obtem um array/vetor contendo o número das opções disponíveis
def getArrayOpcoes():
    return [ 1, 2, 3, 4, 5, 6, 7 ]

## Converte uma opção de menu (1, 2, 3, etc.) para um tipo específico (papel, vidro, etc.)
def convertOpcaoToTipo(opcao):
    if opcao == 1:
        return 'plastico'
    elif opcao == 2:
        return 'metal'
    elif opcao == 3:
        return 'vidro'
    elif opcao == 4:
        return 'papel'
    elif opcao == 5:
        return 'eletronico'
    elif opcao == 6:
        return 'outro'
    else:
        return ''

## Retorna um array/vetor contendo todos os objetos disponíveis para serem reciclados
def getObjetos():
    return  [
        { 'id': 1, 'descricao': 'Garrafa PET', 'tipo': 'plastico' },
        { 'id': 2, 'descricao': 'Potes de plástico', 'tipo': 'plastico' },
        { 'id': 3, 'descricao': 'Tampa de embalagem', 'tipo': 'plastico' },
        { 'id': 4, 'descricao': 'Cano PVC', 'tipo': 'plastico' },
        { 'id': 5, 'descricao': 'Saco plástico', 'tipo': 'plastico' },
        { 'id': 6, 'descricao': 'Peça de brinquedo', 'tipo': 'plastico' },
        { 'id': 7, 'descricao': 'Balde', 'tipo': 'plastico' },
        { 'id': 8, 'descricao': 'Lata de alumínio', 'tipo': 'metal' },
        { 'id': 9, 'descricao': 'Lata de aço', 'tipo': 'metal' },
        { 'id': 10, 'descricao': 'Tampa', 'tipo': 'metal' },
        { 'id': 11, 'descricao': 'Ferragem', 'tipo': 'metal' },
        { 'id': 12, 'descricao': 'Cano', 'tipo': 'metal' },
        { 'id': 13, 'descricao': 'Moldura de quadro', 'tipo': 'metal' },
    ]

## Retorna um array/vetor contendo os objetos disponíveis para serem reciclados baseado num tipo específico (plástico, vidro, etc.)
def getObjetosByTipo(opcao):
    objetos = []
    tipo = convertOpcaoToTipo(opcao)

    for objeto in getObjetos():
        if objeto['tipo'] == tipo:
            objetos.append(objeto)

    return objetos

## Exibe o banco de objetos a partir de uma opção escolhida (plástico, vidro, etc.)
def exibeObjetosByOpcao(numeroOpcao):
    objetos = getObjetosByTipo(numeroOpcao)

    limpaConsole()

    print('Exibindo os materiais recicláveis para a categoria informada..\n')

    for objeto in objetos:
        print("""   * """ + str(objeto['descricao']))
    
## Exibe uma mensagem de erro no console
def exibeMensagemErro(msg):
    limpaConsole()
    print('[ERRO] => ' + str(msg))
    print('\nPrecione qualquer tecla para continuar')
    input()

## Limpa o console
def limpaConsole():
    clear = lambda: os.system('cls')
    clear()
