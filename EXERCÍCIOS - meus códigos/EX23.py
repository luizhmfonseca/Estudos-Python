# Faça um programa que leia de 0 à 9999 e mostre da tela cada um dos digitos separados. 
# Exemplo: Digite um número: 1834

#Unidade: 4, Dezena:  3, Centena: 8, Milhar:  1
#Pode fazer como String ou Matematicamente.

num = str (input('Digite um numero de 1.000 à 9.000:'))
uni = num[3]
dez = num[2]
cen = num[1]
mil = num[0]
print('A unidade é: {}'.format(uni))
print('A dezena é: {}'.format(dez))
print('A centena é: {}'.format(cen))
print('O milhar é: {}'.format(mil))