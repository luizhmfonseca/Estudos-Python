print("\033[0m-=-" * 47)
print('\33[1;35;47mCOMPARAÇÃO DE NÚMEROS\033[m')
print("\033[0m-=-" * 47)
n1 = int (input("Digite o 1º número: "))
n2 = int (input('Digite o 2º número: '))
if n1 > n2:
  print('\033[1;32mO primeiro valor é maior')
elif n1 < n2:
  print('\033[1;32mO segundo valor é maior')
elif n1 == n2:
  print('\033[1;32mNão existe valor maior. Os dois são iguais')