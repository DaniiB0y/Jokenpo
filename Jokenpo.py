from random import randint
import os
c  = 0
escolha = 1
perdeu = 0
ganhou = 0
empate = 0
while escolha != 4:
    dic = ["","Pedra", "Papel", "Tesoura"]
    bot = randint(1, 3)
    if c == 0:
        escolha = int(input('\n                    '+'\033[1;31m'+'  ✌ '+'\033[1;36m'+'[-   jokenpô  じゃんけんぽん      -]'+'✌  '+'\n'+'\033[1;97m'+'\n1-Jogar'+'\n4-Sair'+'\033[1;36m'+'\n\nEscolha: '))
        os.system('cls')
        c+=1
    x = int(input("Pedra: 1\nPapel: 2\nTesoura: 3\n~>"))
    os.system('cls')
    if dic[x] == dic[bot]:
        print('\033[1;97m'+'----------------------------------------')
        print('\033[1;97m'+f'{dic[x]} = {dic[bot]}, EMPATE!')
        empate += 1
    elif dic[bot] != "Papel" and x == 1:
        print('\033[1;97m'+'----------------------------------------')
        print(f'\033[1;97m'+f'Pedra ganha de {dic[bot]}, você ganhou!')
        print('\033[1;97m'+'----------------------------------------')
        ganhou += 1
    elif dic[bot] != "Pedra" and x == 3:
        print('\033[1;97m'+'----------------------------------------')
        print(f'\033[1;97m'+f'Tesoura ganha de {dic[bot]}, você ganhou!')
        print('\033[1;97m'+'----------------------------------------')
    elif dic[bot] != "Tesoura" and x == 2:
        print('\033[1;97m'+'----------------------------------------')
        print(f'\033[1;97m'+f'Papel ganha de {dic[bot]}, você ganhou!')
        print('\033[1;97m'+'----------------------------------------')
        ganhou += 1
    else:
        print('\033[1;97m'+'----------------------------------------')
        print(f"Perdeu! {dic[x]} perde para {dic[bot]}")
        print('\033[1;97m'+'----------------------------------------')
        perdeu += 1
    print(f"Perdeu {perdeu} Ganhou {ganhou} Empate: {empate} vezes jogadas {c}")

