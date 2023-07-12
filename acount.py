import os
import time

# Definições - 
acountsData = []
userAcounts = []

# Funções - 
def checkAcounts():
    acountNumber = 1
    if os.path.isfile('acountsDataBase.txt'):
        with open('acountsDataBase.txt', 'r') as acountsDataBase:
            acountsDataBase.seek(0, os.SEEK_END)
            isempty = acountsDataBase.tell() == 0
            acountsDataBase.seek(0)
        if isempty == False:
            with open("acountsDataBase.txt", "r", encoding='utf=8') as data:
                for lines in data.readlines():
                    acountNumber += 1
                    acount, space = lines.split('\n')
                    acountsData.append(acount)
        return acountNumber

def clearTerminal():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def createAcount(userInfo):
    balance = 0
    acountsData.append(userInfo[2] + ' | ' + '0001' + ' | ' +
                       'R$ : ' + str(balance) + ' | ' + str(acountNumber))
    with open('acountsDataBase.txt', 'w+', encoding='utf=8') as acountsDataBase:
        for acount in acountsData:
            acountsDataBase.write(acount + '\n')
    print(f'\n\033[32mConta - {acountNumber} criada\033[0m na agência 0001!')
    input('Enter continua...')

def showUserAcounts(userInfo):
    if not userAcounts:
        for acount in acountsData:
            acountInfo = acount.split(' | ')
            if acountInfo[0] == userInfo[2]:
                userAcounts.append(acountInfo)
    if userAcounts:
        print('\nAqui estão as contas registradas em seu CPF: ')
        for acounts in userAcounts:
            print(f'Conta - {acounts[-1]}')
        print('=' * 15)
        return chooseAcount(userInfo, userAcounts)
    else:
        print('\033[31mVocê não possuí uma conta registrada em seu CPF!\033[0m\n')
        time.sleep(2)
        print('Vamos resolver isso agora mesmo :)')
        createAcount(userInfo)
        showUserAcounts(userInfo)

def chooseAcount(userInfo, userAcounts):
    while True:
        acountChosen = input('Insira \033[31mAPENAS O NÚMERO\033[0m da conta que deseja acessar >> ')
        for userAcount in userAcounts:
            if acountChosen == userAcount[-1]:
                acount = userAcount
                return acount
        else:
            print('\033[31mConta inserida não encontrada!\033[0m')
            clearTerminal()
            showUserAcounts(userInfo)

# Main -
acountNumber = checkAcounts()