# Crie um programa que leia o 'ano de nascimento' de sete pessoas.
# No final mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores. (Considerar 21 anos a maioridade)
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0    
for pess in range(1, 8):
    nasc1 = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc1
    print('Você tem {} anos'.format(idade))
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Temos {} pessoas maiores de idade'.format(totmaior))
print('Temos {} pessoas menores de idade'.format(totmenor))