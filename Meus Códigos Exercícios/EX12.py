price = float (input("Digite o valor do produto: "))
desc = price / 100*5
vt = price - desc
print(f'O valor do produto é {price:.0f} reais, porém com desconto de 5% fica em {vt:.0f} reais') 