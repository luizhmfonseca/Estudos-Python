km = float (input('Digite quantos KM terá a sua viagem: '))
pr1 = km*0.45
pr2 = km*0.50
if km >= 200:
  print('O preço da sua viagem é: {:.2f} reais'.format(pr2))
else:
  print('O preço da sua viagem é: {:.2f} reais'.format(pr1))