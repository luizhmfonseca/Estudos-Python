# Escreva uma programa que faça o computador " Pensar' em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever ✍ na tela se o usuário venceu ou perdeu.

from random import randint #Número aleatório(ran) + Número Inteiro (int) = randint - Número aleatório inteiro
computador = randint(0, 5)
print("-=-" * 20)
print("Vou pensar 💭 em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
jogador = int (input("Em que que número eu pensei? "))
if jogador == computador:
  print("PARABÉNS! Você conseguiu me vencer!")
else:
  print("GANHEI! ✌ Eu pensei no múmero {} e não no {}.".format(computador, jogador))