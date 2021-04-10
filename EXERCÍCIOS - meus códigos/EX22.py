# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúculas.
# O nome com todas minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome =  str (input('Digite seu nomec completo: ')).strip()
print('Analisando seu nome....')
print('O seu nome com letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'. format(separa[0], len(separa[0])))