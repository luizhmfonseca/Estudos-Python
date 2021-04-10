#  Escreva um programa que leia o sálario de um funcionário e calcule o valor do seu aumento.
# Para salários superiores à '1.250,00', calcule um aumento de 10%. Para os inferior ou iguais, o aumento é de 15%.

sal = float (input('Digite o seu salário atual: '))
alt1 = sal*10/100
alt2 = sal*15/100
if sal <= 1.250:
  print('Você teve um acréscimo de {:.2f} reais'.format(alt1))
  print('O seu salário foi reajustado para {:.2f} reais'.format(alt1+sal))
else:
  print('Você teve um acréscimo de {:.2f} reais'.format(alt2))
  print('O seu salário foi reajustado para {:.2f} reais'.format(alt2+sal))