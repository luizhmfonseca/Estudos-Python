#Faça um programa que calcule a soma entre todos os números impares que 
# são múltiplos de três e que se encontram no intervalo de 1 até 500

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c # ou (soma +=c')
        cont = cont + 1 # ou (cont +=1*)
        print(c, end=' ')
print('A soma de todos os {} valores solicitados é: {}'.format(cont, soma))