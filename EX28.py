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