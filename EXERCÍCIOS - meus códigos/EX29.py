# Radar Eletrônico
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar '80 km/h', 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

km = float (input('Digite a velocidade do seu carro: ')) #minha solução
cal = km - 80
multa = cal*7
if km >= 80:
  print('Você foi multado em R$ {:.2f} reais'.format(multa))
else:
  print('Parabéns por ser um motorista que segue os limites de velocidade')