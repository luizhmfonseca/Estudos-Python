print("\033[0m-=-" * 47)
print('\33[1;32;43m CONTROLE DE ALISTAMENTO MILITAR - EXÉRCITO BRASILEIRO - MARINHA DO BRASIL - FORÇA ÁREA BRASILEIRA                                                                     \033[m')
print("\033[0m-=-" * 47)
from datetime import date #pegar data atual no seu computador💻
atual = date.today().year
nasc = int (input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
  print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
  saldo = 18 - idade
  print('Ainda faltam {} anos para o alistamento.'.format(saldo))
  ano = atual + 2
  print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
  saldo = idade - 18
  print('Você ja deveria ter se alistado há {} anos.'.format(saldo))
  ano = atual - saldo
  print('Seu alistamento foi em {}'.format(ano))   