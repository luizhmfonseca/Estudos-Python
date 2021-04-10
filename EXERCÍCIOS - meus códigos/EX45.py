# CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.

print('\33[1;35;47mJOGO JOKENPÔ') # ^ código de centralização
print("\033[0m-=-" * 47)
import  random #/ CHAMANDO A FUNÇÃO RANDOM
from time import sleep #/ CHAMANDO A FUNÇÃO SLEEP
#TABELA
print("INFORME 0 PARA PEDRA\n""INFORME 1 PARA PAPEL\n""INFORME 2 PARA TESOURA")
print("-="*10)
#ENTRADA
itens = ["PEDRA","PAPEL","TESOURA"]
pedra = itens[0]
papel = itens[1]
tesoura = itens[2]
jogador = int(input("Escolha sua opção: "))
while jogador < 0 or jogador > 2:
    jogador = int(input("Digite novamente!!!: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO""")
sleep(1)
print("-="*10)
maquina = random.randint(0,2)
#CONDIÇÃO
if maquina == 0: #COMPUTADOR PEDRA
    if jogador == 0:
        print("Empate")
    elif jogador == 1:
        print("Jogador Ganhou")
    elif jogador == 2:
        print("Maquina Ganhou")
if maquina == 1: #COMPUTADOR PAPEL
    if jogador == 0:
        print("Maquina Ganhou")
    elif jogador == 1:
        print("Empate")
    elif jogador == 2:
        print("Jogador Ganhou")
if maquina == 2: #COMPUTADOR TESOURA
    if jogador == 0:
        print("Jogador Ganhou")
    elif jogador == 1:
        print("Maquina Ganhou")
    elif jogador == 2:
        print("Empate")
print("Jogador jogou:",format(itens[jogador]))
print("Maquina jogou:",format(itens[maquina]))