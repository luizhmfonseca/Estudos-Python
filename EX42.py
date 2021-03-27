print('\33[1;35;47mTIPOS E MEDIDAS DE TRIÂNGULOS.\033[m')
print("\033[0m-=-" * 47)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Primeiro segmento: '))
r3 = float(input('Primeiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('Os segmentos acima podem forma um triângulo', end='')
  if r1 == r2 == r3:
    print(' EQUILÁTERO!')
  elif r1 != r2 != r3 != r1:  # != (Código que representas DIFERENTE)
    print(' ESCALENO!')
  else:
    print(' ISÓSCELES!')
else:
  print('Os seguimentos acima não podem formar um triângulo')