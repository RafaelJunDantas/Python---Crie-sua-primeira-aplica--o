import os

# funcoes
def print_nome_restaurante():
    '''Funcao para printar o nome do restaurante'''

    print('Bom dia restaurante\n')

def print_opcoes():
    '''Funcao para printar as opcoes'''

    print('1: Cadastrar restaurante')
    print('2: Listar restaurante')
    print('3: Alternar estado do  restaurante')
    print('4: Sair \n')

def voltar_menu_principal():
    '''Funcao para voltar ao menu principal'''

    input('Digite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(subtitulo):
    '''
    Funcao para exibir o subtitulo

    Argumentos:
    - subtitulo (String): subtitulo que deseja exibir
    '''

    os.system('clear')
    print('*' * len(subtitulo))
    print(subtitulo)
    print('*' * len(subtitulo))
    print()

def cadastrar_restaurante():
    '''
    Funcao para cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante: nome -> String
    - Categoria do restaurante: categoria -> String
    
    Outputs: 
    - Cria um restaurante: dict
    - Adiciona o restaurante criado a lista de restaurantes
    '''

    exibir_subtitulo('Cadastro de restaurante')
    nome = input('Nome do restaurante: ')
    categoria = input('Categoria do restaurante: ')
    restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False}
    restaurantes.append(restaurante)
    print(f'Restaurante {nome} foi cadastrado com sucesso \n')
    voltar_menu_principal()

def listar_restaurante():
    '''Funcao para listar os restaurantes cadastrados'''

    exibir_subtitulo('Restaurantes cadastrados')
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    print()
    voltar_menu_principal()

def alternar_estado_restaurante():
    '''
    Funcao para alternar o statud do restaurante (ativo ou inativo)

    Inputs:
    - Nome do restaurante: nome -> String

    Outputs:
    - Se existir um restaurante com o nome recebido, altera o status dele
        - Se estiver ativo (restaurante['ativo'] == True), desativa: restaurante['ativo'] = False
        - Se estiver desativado (restaurante['ativo'] == False), ativa: restaurante['ativo'] = True
    '''

    exibir_subtitulo('Alterando estado do restaurante')
    nome = input('Nome do restaurante para alternar o estado: ')
    encontrado = False
    for restaurante in restaurantes:
        if nome == restaurante['nome']:
            encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome} foi desativado com sucesso'
            print(mensagem + '\n')
    if not encontrado:
        print('O restaurante nao foi encontrado\n')
    voltar_menu_principal()

def finalizar_app():
    '''Funcao para finalizar o app'''

    exibir_subtitulo('Finalizando o app')

def opcao_invalida():
    '''Funcao para opcao invalida'''

    print('Opcao invalida \n')
    voltar_menu_principal()

def escolher_opcao(): 
    '''
    Funcao para escolher a opcao desejada

    Input:
    - Opcao escolhida: opcao_escolhida -> int
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida() 

# variaveis
#restaurantes = ['chocolate', 'pizza', 'teste']
restaurantes = [
    {'nome': 'chocolate', 'categoria': 'chocolate', 'ativo': False}, 
    {'nome': 'pizza', 'categoria': 'pizza', 'ativo': True},
    {'nome': 'teste', 'categoria': 'teste', 'ativo': False}
]

def main():
    os.system('clear')
    print_nome_restaurante()
    print_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()