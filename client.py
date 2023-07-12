import os
import time

# Definições - 
usersData = []

# Funções - 
def checkUsers():
    if os.path.isfile('usersDataBase.txt'):
        with open('usersDataBase.txt', 'r') as usersDataBase:
            usersDataBase.seek(0, os.SEEK_END)
            isempty = usersDataBase.tell() == 0
            usersDataBase.seek(0)
        if isempty == False:
            with open("usersDataBase.txt", "r", encoding='utf=8') as data:
                for lines in data.readlines():
                    user, space = lines.split('\n')
                    usersData.append(user)


def clearTerminal():
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')


def logIn():
    while True:
        userName = input('\nInsira o CPF informado (APENAS OS NÚMEROS): ').strip()
        for user in usersData:
            userInfo = user.split(' | ')
            if userName == userInfo[2]:
                password = input('Insira pin do usuário: ').strip()
                if password == userInfo[-1]:
                    return userInfo
                else:
                    print('\033[31mSenha incorreta!\033[0m')
                    clearTerminal()
                    continue
        print('\n\033[31mCPF não encontrado na base de usuários!\033[0m')
        clearTerminal()


def validateName(name):
    if ' ' in name:
        namesList = name.split(' ')
        name = ''.join(namesList)
    if name.isalpha() and len(name) > 5:
        return True
    return False


def validateBirth(dateBirth):
    if '/' in dateBirth:
        digitsList = dateBirth.split('/')
        dateBirth = ''.join(digitsList)
    if dateBirth.isdigit() and len(dateBirth) == 8:
        return True
    return False


def validateCPF(CPF):
    if CPF.isdigit() and len(CPF) == 11:
        for user in usersData:
            userInfo = user.split(' | ')
            if CPF == userInfo[2]:
                print('\033[35mEste CPF já foi cadastrado!\033[0m')
                time.sleep(2)
                return False
            return True
    return False


def createAdress(street, number, neighbor, city, state):
    adress = street + ', ' + number + ' - ' + neighbor + ' - ' + city + '/' + state
    return adress


def saveUser(name, dateBirth, CPF, adress, password):
    usersData.append(name + ' | ' + dateBirth + ' | ' +
                            CPF + ' | ' + adress + ' | ' + password)
    with open('usersDataBase.txt', 'w+', encoding='utf=8') as usersDataBase:
        for user in usersData:
            usersDataBase.write(user + '\n')


def createUser():
    clearTerminal()
    print('Olá novo usuário!')
    print('\nPara poder criar um cadastro dentro do nosso banco precisaremos de algumas informações suas, então vamos lá!\n')
    while True:
        name = input('Nome completo: ').title()
        if validateName(name):
            break
        print('Informação colocada inválida!')
        clearTerminal()

    while True:
        dateBirth = input('Data de nascimento (DD/MM/AAAA): ').strip()
        if validateBirth(dateBirth):
            break
        print('Informação colocada inválida!')
        clearTerminal()

    while True:
        CPF = input('CPF (APENAS NÚMEROS): ')
        if validateCPF(CPF):
            break
        print('Informação colocada inválida!')
        clearTerminal()

    print('-' * 8, ' Endereço ', '-' * 8)
    while True:
        street = input('Nome da rua: ').capitalize()
        if len(street) > 3:
            break
        print('Informação colocada inválida!')
        clearTerminal()

    while True:
        number = input('Número: ')
        if number.isdigit():
            break
        print('Número inserido inválido!')
        clearTerminal()

    while True:
        neighbor = input('Nome do bairro: ').capitalize()
        if len(neighbor) > 3:
            break
        print('Informação colocada inválida!')
        clearTerminal()

    while True:
        city = input('Cidade: ').title()
        if len(city) > 3:
            break
        print('Informação colocada inválida!')
        clearTerminal()

    while True:
        state = input('Estado (APENAS SIGLA): ').upper().strip()
        if state.isalpha() and len(state) == 2:
            break
        print('Insira apenas a sigla do estado!')
        clearTerminal()
    adress = createAdress(street, number, neighbor, city, state)

    while True:
        password = input('Insira um PIN de 4 dígitos para ser sua senha: ')
        if len(password) == 4 and password.isdigit():
            break
        print('PIN inválido!')
        clearTerminal()

    saveUser(name, dateBirth, CPF, adress, password)

# Main - 
checkUsers()