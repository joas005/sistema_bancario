import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

balance = 0
extract = []
totalWithdraws = 0
menu = ['Ver extrato', 'Depositar', 'Sacar', 'Créditos', 'Sair']

def clearTerminal():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

def showCredits():
    print('\n\033[34mObrigado por querer me conhecer\033[0m 😁✌️\nEste programa foi desenvolvido por \033[35m@joas005\033[0m no github, entre lá para conheça um pouco mais sobre mim e meus projetos!')
    input('\nEnter continua...')

def exitingProgram():
    print('\033[32m\nObrigado por utilizar meu programa!\033[0m\nVolte sempre! 😁')
    exit()

def depositMoney(balance):
    print('\n\033[32mVocê escolheu realizar um deposito!\033[0m\n')
    while True:
        deposit = input('Quanto dinheiro você deseja depositar?\n\nR$ ')
        try:
            if float(deposit) > 0:
                deposit = float(deposit)
                balance += float(deposit)
                print(f'\nVocê acabou de \033[32mdepositar - R$ {deposit:.2f}\033[0m em sua conta!')
                input('Enter continua...')
                registerOp(1, deposit)
                return balance
            else:
                print('\033[31mValor inserido inválido!\033[0m')
                input('\nEnter continua...')
                clearTerminal()
        except:
            print('\033[31mValor inserido inválido!\033[0m')
            clearTerminal()

def withdrawMoney(balance, totalWithdraws):
    print('\n\033[31mVocê escolheu realizar um saque!\033[0m\n')
    print('\033[31mATENÇÃO!\033[0m Seu límite de valor para saque é: \033[35mR$ 500,00\033[0m\n')
    while True:
        withdraw = input('Quanto dinheiro você deseja sacar?\n\nR$ ')
        try:
            for operation in extract:
                if operation[0] == 2:
                    totalWithdraws += 1
            if float(withdraw) <= 500 and float(withdraw) <= balance and totalWithdraws <= 3:
                withdraw = float(withdraw)
                balance += float(withdraw)
                print(f'\nVocê acabou de \033[31msacar - R$ {withdraw:.2f}\033[0m em sua conta!')
                input('Enter continua...')
                registerOp(2, withdraw)
                return balance, totalWithdraws
            else:
                print('\033[31mValor inserido inválido ou total de 3 saques diários já realizados!\033[0m')
                input('\nEnter continua...')
                clearTerminal()
                break
        except:
            print('\033[31mValor inserido inválido!\033[0m')
            clearTerminal()

def registerOp(type, value):
    operation = [type, value]
    extract.append(operation)

def printExtract(extract):
    print('\n\033[33mVocê escolheu ver seu extrato!\033[0m\n')
    if extract:
        print('Operações de hoje:')
        for operation in extract:
            if operation[0] == 1:
                print(f'\033[32mDeposito - R$ {operation[1]}\033[0m')
            else:
                print(f'\033[31mSaque - R$ {operation[1]}\033[0m')
        print('-' * 15)
    print('\nSeu saldo atual é de:')
    print(f'\033[35mR$ {balance:.2f}\033[0m')
    input('\nEnter continua...')
    clearTerminal()

print('Bem-vindo!\n')

while True:
    print('O que você deseja fazer?\n')

    for index, item in enumerate(menu):
        print(f'[{index+1}] {item}.')

    mode = input('>> ').strip().capitalize()
    if mode in menu:
        mode = str(menu.index(mode) + 1)

    match (mode):
        case '1': printExtract(extract)
        case '2': balance = depositMoney(balance)
        case '3': 
            try:
                balance, totalWithdraws = withdrawMoney(balance, totalWithdraws)
            except:
                pass
        case '4': showCredits()
        case '5': exitingProgram()
        case _: print('\033[31mOpção inválida!\033[0m')

    clearTerminal()