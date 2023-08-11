lar = float(input('Digite a largura da parede:'))
alt = float(input('Digite a altura da parede'))
area = lar * alt
tinta = area/2
print('A parede tem {}m² e será preciso {}L de tinta para pintá-la'.format(area, tinta))