#Faça um Algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
price = float (input("Digite o valor do produto: "))
desc = price / 100*5
vt = price - desc
print(f'O valor do produto é {price:.0f} reais, porém com desconto de 5% fica em {vt:.0f} reais') 