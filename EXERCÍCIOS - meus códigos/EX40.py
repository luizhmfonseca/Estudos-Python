#  CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL DE ACORDO COM A MÉDIA ATINGIDA:
# MÉDIA ABAIXO DE 5.0: REPROVADO
# MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
# MÉDIA 7.0 OU SUPERIOR: APROVADO

print("\033[0m-=-" * 47)
print('\33[1;31mHARVARD - NOTAS FINAIS DE SEMESTRE')
print("\033[0m-=-" * 47)
n1 = float (input('Primeira nota: '))
n2 = float (input('Segunda nota: '))
med = (n1+n2)/2
if med < 5.0:
  print('REPROVADO')
elif med == 5.0 or 5.1 or 5.2 or 5.3 or 5.4 or 5.5 or 5.6 or 5.7 or 5.8 or 5.9:
  print('RECUPERAÇÃO')
elif med == 6.0 or 6.1 or 6.2 or 6.3 or 6.4 or 6.5 or 6.6 or 6.7 or 6.8 or 6.9:
  print('RECUPERAÇÃO')  
elif med == 7.0:
  print('APROVADO')
elif med > 7.0:
  print('APROVADO')