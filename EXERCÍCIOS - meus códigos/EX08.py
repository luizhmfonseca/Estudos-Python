#Escreva um programa que leia um valor em metroe e o exiba convertido em centímetros e milímetros.
n1 = float (input('Diga uma distância em metros: '))
c = n1*100
m = n1*1000
print('A medida de {} metros corresponde é {} centimetros e {} milimetros.'.format(n1, c, m))