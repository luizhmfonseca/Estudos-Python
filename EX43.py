print('\33[1;35;47mANÁLISE DE IMC- CONTROLE DE SAÚDE.\033[m')
print("\033[0m-=-" * 47)
peso = float (input('Qual é o seu peso? (kg) '))
altura = float (input("Qual é a sua altura? (m) "))
imc = peso / (altura ** 2)
print('Seu imc é de {:.1f}.'. format(imc))
if imc < 18.5:
  print('Você está ABAIXO do PESO NORMAL')
elif 18.5 <= imc < 25:                                    #ou elif imc >= 18.5 and imc < 25: para facilitar.
  print('Parabéns você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
  print('Você está na faixa de SOBREPESO') 
elif 30 <= imc < 40:
  print('Você está na faixa de OBESIDADE. CUIDADO !!!')
elif imc >= 40:
  print('Você está na faixa de OBESIDADE MORDIDA. CUIDADO !!!') 