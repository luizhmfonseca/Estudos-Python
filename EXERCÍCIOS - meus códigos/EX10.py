# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
valor = float (input('Digite o valor em reais:'))
dolar = valor / 5.74
print(f'Com {valor} reais você pode comprar {dolar:.2f} dólares')