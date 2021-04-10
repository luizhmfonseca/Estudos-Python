# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza Primeiro = Ana Último =

n = str (input('Digite um nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome: {} '.format(nome[0]))
print('Seu último nome: {}'.format(nome[len(nome)-1])) # conta um nome a menos
print('Seu usuário de rede será {}'.format(nome[0]) + (nome[3]))