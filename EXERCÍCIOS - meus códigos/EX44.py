#  ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:

#À VISTA DINHEIRO/ CHEQUE: 10% DE DESCONTO
# À VISTA NO CARTÃO: 5% DE DESCONTO
# EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
# 3X OU MAIS NO CARTÃO: 20% DE JUROS

print('\33[1;35;47mCRM / LF CONSULTORIA - FORMAS DE PAGAMENTO') # ^ código de centralização
print("\033[0m-=-" * 47)
preço = float (input('Preço das compras: '))
print('''\033[1;36mFORMAS DE PAGAMENTO\033[m
[ 1 ] à vista dinheiro/ cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int (input('Qual é a opção? '))
if opção == 1:
  total = preço - (preço * 10/100)
elif opção == 2:
  total = preço - (preço * 5/100)
elif opção == 3:
  total = preço
  parcela = total / 2
  print('\033[32mSua será parcelada em 2 vezes de R${:.2f}.'.format(parcela))
elif opção == 4:
  total = preço + (preço * 20 / 100)
  totparc = int (input("Quantas parcelas? "))
  parcela = total / totparc
  print('\033[33mSua compra será parcelada em {}x de R${:.2f}'.format(totparc, parcela))
else:
  total = preço
  print('\033[31mOPÇÃO INVÁLIDA de pagamento. Tente novamente')
print('\033[31mSua compra de R${:.2f} vai custar R${:.2f}'.format(preço, total))