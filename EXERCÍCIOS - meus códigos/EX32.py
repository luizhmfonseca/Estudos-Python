# Faça um programa que leia um ano qualquer e mostre se ele é "bissexto".

from datetime import date #pegar o ano atual registro no seu computador💻
ano = int (input('Que ano quer analisar: '))
if ano == 0:
    ano = date.today().year # Esse comando busca apenas o 'ano' da data de hoje no seu computador💻 
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('O ano {} é BISSEXTO!'.format(ano))
else:
  print('O ano {} não é BISSEXTO!'.format(ano)) 