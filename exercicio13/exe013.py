salário = float(input('Qual é o salário do funcionário?'))
novo = salário + (salário * 15 / 100)
print('O funcionário que ganhava {:.2f}R$, com o novo salário, passou a ganhar {:.2f}R$'.format(salário, novo))