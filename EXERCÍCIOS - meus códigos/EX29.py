km = float (input('Digite a velocidade do seu carro: ')) #minha solução
cal = km - 80
multa = cal*7
if km >= 80:
  print('Você foi multado em R$ {:.2f} reais'.format(multa))
else:
  print('Parabéns por ser um motorista que segue os limites de velocidade')