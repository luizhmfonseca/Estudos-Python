# Desenvolva um programa que pergunte a distância de uma viagem em KM. 
# Calcule o preço da passagem, cobrando 0,50 centavos por km para viagens de até 200km e 0,45 centavos para viagens mais longas.

km = float (input('Digite quantos KM terá a sua viagem: '))
pr1 = km*0.45
pr2 = km*0.50
if km >= 200:
  print('O preço da sua viagem é: {:.2f} reais'.format(pr2))
else:
  print('O preço da sua viagem é: {:.2f} reais'.format(pr1))