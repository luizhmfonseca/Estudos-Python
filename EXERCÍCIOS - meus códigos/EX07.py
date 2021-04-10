#Desenvolva um programa que leia as duas notas de um aluno e calcule a sua média.
n1 = float (input('Primeira Nota:'))
n2 = float (input('Segunda Nota:'))
média = (n1 + n2) / 2
print('A média entre {} e {} é igual a {}'.format(n1, n2, média))