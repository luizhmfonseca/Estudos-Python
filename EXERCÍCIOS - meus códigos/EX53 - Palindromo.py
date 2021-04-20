# Crie um programa que leia uma frase qualquer e diga se ela é
# um palíndromo, desconsiderando os espaços. (Palindromo)
# Exemplo: APOS A SOPA (Ao inverter a frase é mesma frase.)

frase = str(input('Digite um frase: ')).strip().upper() # Eliminou os espaços antes e depois, alterei para maiúsculas
palavras = frase.split() #criou um lista
junto =''.join(palavras) #junto a lista para eliminar os espaços antes
inverso ='' 
for letra in range(len(junto) - 1, -1, -1): #criou a inversou da frase junto com a linha abaixo.
    inverso += junto[letra]
# as linhas 9 e 10 podem ser alteradas para os comandos (inverso = junto[::-1])
print('O inverso de {} é {}'.format(junto, inverso))
if inverso  == junto:  #Mostrou se o inverso é mesma coisa.
    print('É um palindromo!')
else:
    print('A frase não é um palindromo!')
