#  A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UMA ATLETA E MOSTRE SUA CATEGORIA DE ACORDO COM A IDADE:
# ATÉ 9 ANOS: MIRIM
# ATÉ 14 ANOS: INFANTIL
# ATÉ 19 ANOS: JUNIOR
# ATÉ 20 ANOS: SÊNIOR
# ACIMA: MASTER

print("\033[0m-=-" * 47)
print('\33[1;31mCATEGORIA DE ATLETAS')
print("\033[0m-=-" * 47)
from datetime import date
atual = date.today().year
nascimento = int (input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
  print('Classificação: MIRIM')
elif idade <= 14:
  print('Classificação: INFANTIL')
elif idade <= 19:
  print('Classificação: JUNIOR')
elif idade <= 25:
  print('Classificação: SÊNIOR')
else:
  print('Classificação: MASTER')  