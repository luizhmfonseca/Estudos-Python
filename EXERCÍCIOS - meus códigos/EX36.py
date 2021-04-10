# ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. 
# O PROGRAMA VAI PERGUNTAR O 'VALOR DA CASA', O 'SALÁRIO' DO COMPRADOR E EM 'QUANTOS ANOS' ELE VAI PAGAR. 
# CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO.

print('\33[1;35;47mSISTEMA DE SIMULAÇÃO DE FINANCIAMENTO DE IMÓVEIS 2021 - CASAS TÉRREAS, SOBRADOS, APARTAMENTOS, STUDIOS.\033[m')
print("\033[0m-=-" * 47)
casa = float (input('Valor da casa: '))
salário = float(input('Salário do comprado: '))
anos = int (input('Quantos anos de financiamento: '))
prestação = casa / (anos * 12) # Quantidade de meses que irá pagar
mínimo = salário * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos e'.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
  print('\033[1;33mEmpréstimo pode ser concedido!')
else:
  print('\033[1;31mEmpréstimo Negado')