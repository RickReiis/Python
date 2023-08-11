d = int(input('O carro foi alugado por quantos dias?'))
km = float(input('Quantos Km foram rodados?'))
p = d*60 + km*0.15
print('O aluguel do carro por {} dias e {} Km rodados é R$ {:.2f}.'.format(d, km, p))
