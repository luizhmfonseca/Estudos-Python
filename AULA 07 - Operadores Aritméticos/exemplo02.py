n1 = int (input('Digite um número: '))
n2 = int (input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n a multiplicação é {}, a divisão entre os 2 números é {:.3f},'.format(s, m, d),  end=' ')
print('Divisão inteira {} e a potência {}'.format(di, e))