import os
import time

# Definições
extract = []
totalWithdraws = 0

# Funções -
def clearTerminal():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def getBalance(acount):
    money, balance = acount[2].split(' : ')
    return float(balance)


def updateBalance(acount, balance):
    oldAcount = acount[0] + ' | ' + acount[1] + ' | ' + acount[2] + ' | ' + acount[3]
    acount[2] = 'R$ : ' + str(balance)
    newAcount = acount[0] + ' | ' + acount[1] + ' | ' + acount[2] + ' | ' + acount[3]
    with open('acountsDataBase.txt', 'r') as acountsDataBase:
        content = acountsDataBase.read()
    content = content.replace(oldAcount, newAcount)
    with open('acountsDataBase.txt', 'w') as acountsDataBase:
        acountsDataBase.write(content)

def depositMoney(acount):
    print('\n\033[32mVocê escolheu realizar um deposito!\033[0m\n')
    while True:
        deposit=input('Quanto dinheiro você deseja depositar?\n\nR$ ')
        try:
            if float(deposit) > 0:
                balance=getBalance(acount)
                deposit=float(deposit)
                balance += float(deposit)
                print(
                    f'\nVocê acabou de \033[32mdepositar - R$ {deposit:.2f}\033[0m em sua conta!')
                input('Enter continua...')
                registerOp(1, deposit)
                updateBalance(acount, balance)
                return acount
            else:
                print('\033[31mValor inserido inválido!\033[0m')
                input('\nEnter continua...')
                clearTerminal()
        except:
            print('\033[31mValor inserido inválido!\033[0m')
            clearTerminal()

def withdrawMoney(acount, totalWithdraws):
    print('\n\033[31mVocê escolheu realizar um saque!\033[0m\n')
    print(
        '\033[31mATENÇÃO!\033[0m Seu límite de valor para saque é: \033[35mR$ 500,00\033[0m\n')
    while True:
        withdraw = input('Quanto dinheiro você deseja sacar?\n\nR$ ')
        balance = getBalance(acount)
        try:
            for operation in extract:
                if operation[0] == 2:
                    totalWithdraws += 1
            if float(withdraw) <= 500 and float(withdraw) <= balance and totalWithdraws <= 3:
                withdraw = float(withdraw)
                balance -= float(withdraw)
                print(
                    f'\nVocê acabou de \033[31msacar - R$ {withdraw:.2f}\033[0m em sua conta!')
                input('Enter continua...')
                registerOp(2, withdraw)
                updateBalance(acount, balance)
                return acount, totalWithdraws
            else:
                print(
                    '\033[31mValor inserido inválido ou total de 3 saques diários já realizados!\033[0m')
                input('\nEnter continua...')
                clearTerminal()
                break
        except:
            print('\033[31mValor inserido inválido!\033[0m')
            clearTerminal()


def registerOp(type, value):
    operation = [type, value]
    extract.append(operation)


def printExtract(acount, extract):
    balance = getBalance(acount)
    print('\n\033[33mVocê escolheu ver seu extrato!\033[0m\n')
    if extract:
        print('Operações de hoje:')
        for operation in extract:
            if operation[0] == 1:
                print(f'\033[32mDeposito - R$ {operation[1]}\033[0m')
            else:
                print(f'\033[31mSaque - R$ {operation[1]}\033[0m')
        print('-' * 15)
    else:
        print('Nenhum movimentação foi realizada hoje ainda!')
    print('\nSeu saldo atual é de:')
    print(f'\033[35mR$ {balance:.2f}\033[0m')
    input('\nEnter continua...')
    clearTerminal()
