#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
sal1 = float (input('Digite o valor do seu salário atual: '))
acresc = sal1 / 100*15
reaj = sal1 + acresc
print(f'O seu salário teve um reajuste de 15% totalizando o valor de {reaj:.2f} reais')