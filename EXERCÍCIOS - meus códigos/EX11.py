# Faça um programa que leia a largura e a altura de uma parede em metros. 
# Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
larg = float (input('Digite a largura da parede: '))
alt = float (input('Digite a altura da parede: '))
metr1 = larg*2
metr2 = alt*2
total = metr1 + metr2
litros = total / 2
print(f'A metragem total da sua parede é: {total:.0f} m²')
print(f'Você precisa de {litros} litros de tinta para pintar a sua parede')