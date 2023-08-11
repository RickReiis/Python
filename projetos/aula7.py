nome = input('Qual o seu nome?')
print('Prazer em te conhecer {:20}!'.format(nome))
# :20 escreve com total de caracteres igual a 20
print('Prazer em te conhecer {:>20}!'.format(nome))
# > Alinha a direita
print('Prazer em te conhecer {:<20}!'.format(nome))
# < alinha a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome))
# ^ centraliza
print('Prazer em te conhecer {:=^20}!'.format(nome))
# preenche com o o sinal escolhido
