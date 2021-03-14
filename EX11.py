larg = float (input('Digite a largura da parede: '))
alt = float (input('Digite a altura da parede: '))
metr1 = larg*2
metr2 = alt*2
total = metr1 + metr2
litros = total / 2
print(f'A metragem total da sua parede é: {total:.0f} m²')
print(f'Você precisa de {litros} litros de tinta para pintar a sua parede')