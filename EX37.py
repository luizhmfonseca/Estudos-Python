print('\33[1;35;47mBASE DE CONVERSÃO\033[m')
print("\033[0m-=-" * 47)
num = int (input('Digite um número inteiro: '))
print('''Escolha um das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int (input('Sua opção: '))
if opção == 1:
  print('{} convertido para BINÁRIO é igual à {}'.format(num, bin(num) [2:]))
elif opção == 2:
  print('{} convertido para OCTAL é igual à {}'.format(num, oct(num) [2:]))
elif opção == 3:
  print('{} convertido para HEXADECIMAL é igual à {}'.format(num, hex(num) [2:]))
else:
  print('\033[1;31mOpção inválida. Tente novamente')