# Primeira versão do Sistema Bancário (versão simples)

print('\n\n ########################### BANCO FICTÍCIO ###########################')

# Bibliotecas:
import datetime
data_hora_atual = datetime.datetime.now()
data_hora_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")

tentativas = 3  # Número máximo de tentativas permitidas
while tentativas > 0:
    nome = input("\nPrezado(a) cliente, digite seu usuário de acesso: ")
    senha = input(f"\n ==> {nome}, digite sua senha de acesso: ")
    
    if nome == "Flávio" and senha == "123456":
        print("\nFlávio, bem-vindo ao Banco Fictício.")
        print(" ==> Data e Horário de Acesso:", data_hora_formatada)

        print("\nMENU dos serviços do banco:")
        break  # Sai do loop quando as credenciais estão corretas
    else:
        print("Usuário não encontrado. Por favor, tente novamente.")
        tentativas -= 1

if tentativas == 0:
    print("Número máximo de tentativas atingido. Acesso negado.")

menu = '''
|| SELECIONE A OPÇÃO DESEJADA ||:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Escolha a opção do menu =>   '''
# parêmtros
saldo = 0
limite = 500
extrato = ''
numeros_saques = 0
LIMITES_SAQUES = 3
    
while True:
    opcao = input(menu)
    if opcao == '1':
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print(f'\n{nome}, a operação falhou! O valor do depósito deve ser positivo.\n')
     
    elif opcao == '2':
        valor = float(input(f'{nome}, informe o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numeros_saques >= LIMITES_SAQUES
    
        if excedeu_saldo:
            print(f'{nome}, a operação falhou. Você não possui saldo suficiente.')
        
        elif excedeu_limite:
            print(f'{nome}, a operação falhou. O valor do saque excedeu o limite.')

        elif excedeu_saques:
            print(f'{nome}, a operação falhou. Número máximo de saques excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R${valor:.2f}\n'
            numeros_saques +=1

        else:
            print(f'{nome}, a operação falhou! O valor informado é inválido')

    elif opcao == '3':
        print('\n||| ################# EXTRATO ################# ||| ')
        print('\n Descrição do extrato \n')
        print(f'\n{nome},não foram realizadas movimentações até o momento.' if not extrato else extrato)
        print(f'{nome}, seu saldo é de: R${saldo:.2f}')
        print('\n#########################################################')

    elif opcao == '4':
        print(f'\n{nome}, agradecemos por utilizar o sistema bancário online.\n')
        print('################## SISTEMA ENCERRADO #######################\n')
        break

    else:
        print(f'{nome}, operação inválida. Por favor, selecione novamente a operação desejada.') 
         



            


    