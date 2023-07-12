import os
import time
import operations
import client
import acount
os.system('cls' if os.name == 'nt' else 'clear')

# Definições - 
totalWithdraws = 0
menuInit = ['Logar usuário', 'Criar usuário', 'Sair']
menuAcount = ['Entrar em uma conta', 'Criar nova conta', 'Sair']
menuOp = ['Ver extrato', 'Depositar', 'Sacar', 'Créditos', 'Sair']

# Funções - 
def clearTerminal():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def showCredits():
    print('\n\033[34mObrigado por querer me conhecer\033[0m 😁✌️\nEste programa foi desenvolvido por \033[35m@joas005\033[0m no github, entre lá para conheça um pouco mais sobre mim e meus projetos!')
    input('\nEnter continua...')


def exitingProgram():
    print('\033[32m\nObrigado por utilizar meu programa!\033[0m\nVolte sempre! 😁')
    exit()

# Main - 
print('\033[35mBem-vindo ao Joas Bank!\033[0m\n')
while True:
    print('Conecte-se para utilizar nosso programa!')

    for index, item in enumerate(menuInit):
        print(f'[{index+1}] {item}.')

    mode = input('>> ').strip().capitalize()
    if mode in menuInit:
        mode = str(menuInit.index(mode) + 1)

    match (mode):
        case '1':
            userInfo = client.logIn()
            break
        case '2': client.createUser()
        case '3': exitingProgram()
        case _: print('\033[31mOpção inválida!\033[0m')

    clearTerminal()


while True:
    clearTerminal()
    print(f'\033[35mBem-vindo {userInfo[0]}!\033[0m')
    for index, item in enumerate(menuAcount):
        print(f'[{index+1}] {item}.')

    mode = input('>> ').strip().capitalize()
    if mode in menuAcount:
        mode = str(menuAcount.index(mode) + 1)

    match (mode):
        case '1':
            acount = acount.showUserAcounts(userInfo)
            break
        case '2': acount.createAcount(userInfo)
        case '3': exitingProgram()
        case _: print('\033[31mOpção inválida!\033[0m')

print(f'Você agora está movimentando a conta - \033[35m{acount[-1]}\033[0m')

while True:
    clearTerminal()
    print('\n\033[96mO que você deseja fazer?\033[0m\n')

    for index, item in enumerate(menuOp):
        print(f'[{index+1}] {item}.')

    mode = input('>> ').strip().capitalize()
    if mode in menuOp:
        mode = str(menuOp.index(mode) + 1)

    match (mode):
        case '1':
            extract = operations.extract
            operations.printExtract(acount, extract)
        case '2': acount = operations.depositMoney(acount)
        case '3':
            try:
                acount, totalWithdraws = operations.withdrawMoney(
                    acount, totalWithdraws)
            except:
                pass
        case '4': showCredits()
        case '5': exitingProgram()
        case _: print('\033[31mOpção inválida!\033[0m')
