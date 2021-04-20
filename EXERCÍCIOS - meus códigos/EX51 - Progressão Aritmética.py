# Desenvolva um programa que leia o primeiro termo e a razão de um PA. 
# No final, mostre os 10 primeiros termos dessa progressão. (Progressão Aritmética)


print('='*21)
print('10 TERMOS DE UMA P.A')
print('='*21)

primeiro = int(input('Digite um termo númerico: '))
razão = int(input('Digite a razão númerica: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(' {} '. format(c), end='> ' )
print('FIM DA ANÁLISE')