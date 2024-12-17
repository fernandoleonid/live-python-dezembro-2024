import os

banco_dados = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input('Presione ENTER para continuar...')  

def mostrar_tarefas():
    contador = 1
    for item in banco_dados:
        print (f'{contador} - {item}')
        contador += 1

def selecionar_menu(opcao):
    if (opcao == '1'):
        tarefa = input ('Digite a tarefa nova: ')
        banco_dados.append(tarefa)
    elif (opcao == '2'):
        limpar_tela()
        mostrar_tarefas()
        pausar()
    elif (opcao == '3'):
        mostrar_tarefas()
        numero_tarefa = int(input ('Digite o número da tarefa para excluir: '))
        del banco_dados[numero_tarefa - 1]
    elif (opcao == '4'):
        mostrar_tarefas()
        numero_tarefa = int(input('Digite o número da tarefa para editar: '))
        nova_tarefa = input('Digite a nova tarefa: ')
        banco_dados[numero_tarefa - 1] = nova_tarefa
    elif (opcao == '0'):
        print ('Saindo do sistemas...')
        exit(0)
    else:
        print ('Opção incorreta, tente novamente!')
    

def exibir_menu():
    limpar_tela()
    print ('---> MENU <---')
    print ('1 - Adicionar tarefa')
    print ('2 - Listar tarefas')
    print ('3 - Excluir tarefas')
    print ('4 - Editar tarefas')
    print ('0 - Sair')
    opcao = input('Escolha uma opção: ')
    selecionar_menu(opcao)
    exibir_menu()

exibir_menu()