preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)

# preço -5%
print('O produto que custava, {:.2f}, na promoção com desconto de 5% vai custar, {:.2f}.'.format(preço, novo))
#exercicio12