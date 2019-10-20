## Importação de bibliotecas
import os

## Constantes
OPCAO_VOLTAR = 'VOLTAR'

## Exibe o menu principal da aplicação (solicita ao usuário a escolha de uma categoria)
def exibeMenuInicial():
    ## http://patorjk.com/software/taag (converte texto para ASCII)
    print(
    r"""
    ______          _      _             
    | ___ \        (_)    | |        _   
    | |_/ /___  ___ _  ___| | __ _ _| |_ 
    |    // _ \/ __| |/ __| |/ _` |_   _|
    | |\ \  __/ (__| | (__| | (_| | |_|  
    \_| \_\___|\___|_|\___|_|\__,_|       
    """)
    print(
        """O objetivo deste programa é facilitar o processo de reciclagem, desde a identificação do reciclável até a localização de um ponto para coleta. É tudo muito fácil, vamos começar!?\n""")
    print(
        """Digite o número de uma categoria abaixo:
        
        [1] - Plástico
        [2] - Metal
        [3] - Vidro
        [4] - Papel
        [5] - Eletrônicos
        [6] - Outros
        [7] - Encerrar o programa"""
    )

## Obtem um array/vetor contendo o número das categorias disponíveis
def getOpcoesCategorias():
    return [ 1, 2, 3, 4, 5, 6, 7 ]

## Obtem um array/vetor contendo o número das opções disponíveis de uma dada lista de objetos
def getOpcoesByObjetos(objetos):
    opcoesDisponiveis = []

    for objeto in objetos:
        opcoesDisponiveis.append(objeto['id'])

    return opcoesDisponiveis

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

## Retorna um array/vetor contendo os objetos disponíveis para serem reciclados baseado num tipo específico (plástico, vidro, etc.)
def getObjetosByTipo(opcao):
    objetos = []
    tipo = convertOpcaoToTipo(opcao)

    for objeto in getObjetos():
        if objeto['tipo'] == tipo:
            objetos.append(objeto)

    return objetos

## Retorna um objeto realizando uma busca em uma dada lista e por um dado id
def getObjetoById(objetos, id):
    for objeto in objetos:
        if objeto['id'] == id:
            return objeto

## Exibe o banco de objetos a partir de uma opção escolhida (plástico, vidro, etc.)
def exibeObjetosByOpcao(numeroOpcao):
    ## Variáveis
    objetos = getObjetosByTipo(numeroOpcao)
    opcoesDisponiveis = getOpcoesByObjetos(objetos)
    opcaoEscolhida = 0
    opcaoValida = False
    objetoEscolhido = {}

    ## Solicita ao usuário escolher um objeto a ser reciclado 
    while not(opcaoValida):
        limpaConsole()

        print('Exibindo os materiais recicláveis para a categoria informada..\n')

        for objeto in objetos:
            print("""   * """ + '[{id}] - {nome}'.format(id = objeto['id'], nome = objeto['descricao']))

        print('\nNOTA: Se quiser voltar para o menu inicial, digite a palavra VOLTAR ;)')

        opcaoEscolhida = input('\nDigite o nº do objeto que deseja reciclar: ')

        ## Converte para inteiro (int) caso o usuário tenha digitado somente números
        opcaoEscolhida = int(opcaoEscolhida) if opcaoEscolhida.isnumeric() else str(opcaoEscolhida)

        if opcoesDisponiveis.count(opcaoEscolhida):
            opcaoValida = True
            objetoEscolhido = getObjetoById(objetos, opcaoEscolhida)
        elif opcaoEscolhida.upper() == OPCAO_VOLTAR:
            ## Volta para o menu inicial
            return True
        else:
            opcaoValida = False
            exibeMensagemErro('Opção inexistente. Tente novamente.')
    
    ## Reseta variável 'opcaoValida'
    opcaoValida = False

    ## Exibe os detalhes do objeto e solicita a localização (coordenadas) do usuário
    while not(opcaoValida):
        ## Variáveis
        latitude = ''
        longitude = ''

        limpaConsole()

        print('Dados do material a ser reciclado:\n')
        exibeDetalhesObjeto(objetoEscolhido)
    
        print('\nAgora iremos precisar que você digite as suas coordenadas geográficas (latitude e longitude), ok?\n')
        latitude = str(input('Digite a sua latitude: '))
        longitude = str(input('Digite a sua longitude: '))

        if len(latitude) > 0 and len(longitude) > 0:
            opcaoValida = True


        else:
            opcaoValida = False
            exibeMensagemErro('Certifique-se de digitar os dados corretamente.')
    
    ## Retorna True, assim redireciona o usário para o menu inicial da aplicação
    return True

## Exibe os detalhes do objeto a ser reciclado
def exibeDetalhesObjeto(objeto):
    print("""   => Código interno: """ + str(objeto['id']))
    print("""   => Material a ser reciclado: """ + str(objeto['descricao']))
    
## Exibe uma mensagem de erro no console
def exibeMensagemErro(msg):
    limpaConsole()
    print('Ops... Algo deu errado :(')
    print('[ERRO] => ' + str(msg))
    print('\nPrecione qualquer tecla para continuar')
    input()

## Limpa o console
def limpaConsole():
    os.system('cls') ## Executa o comando 'cls' no console

## Retorna um array/vetor contendo todos os objetos disponíveis para serem reciclados
def getObjetos():
    return  [
        { 'id': 1, 'descricao': 'Garrafa PET', 'obs': '', 'tipo': 'plastico', },
        { 'id': 2, 'descricao': 'Potes de plástico', 'obs': '', 'tipo': 'plastico' },
        { 'id': 3, 'descricao': 'Tampa de embalagem', 'obs': '', 'tipo': 'plastico' },
        { 'id': 4, 'descricao': 'Cano PVC', 'obs': '', 'tipo': 'plastico' },
        { 'id': 5, 'descricao': 'Saco plástico', 'obs': '', 'tipo': 'plastico' },
        { 'id': 6, 'descricao': 'Peça de brinquedo', 'obs': '', 'tipo': 'plastico' },
        { 'id': 7, 'descricao': 'Balde', 'obs': '', 'tipo': 'plastico' },
        { 'id': 8, 'descricao': 'Lata de alumínio', 'obs': '', 'tipo': 'metal' },
        { 'id': 9, 'descricao': 'Lata de aço', 'obs': '', 'tipo': 'metal' },
        { 'id': 10, 'descricao': 'Tampa', 'obs': '', 'tipo': 'metal' },
        { 'id': 11, 'descricao': 'Ferragem', 'obs': '', 'tipo': 'metal' },
        { 'id': 12, 'descricao': 'Cano', 'obs': '', 'tipo': 'metal' },
        { 'id': 13, 'descricao': 'Moldura de quadro', 'obs': '', 'tipo': 'metal' },
    ]

## Retorna um array/vetor contendo todos os pontos de coleta disponíveis
def getPontosDeColeta():
    return [
        { 'id': 1, 'nome': '', 'endereco': '', 'latitude': '', 'longitude': '', 'categoria': '' }
    ]