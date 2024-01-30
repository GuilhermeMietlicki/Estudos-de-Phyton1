valor_dias = float(input('Quantos dias alugado?'))
valor_km = float(input('Quantos km rodados?'))

preço_dia = 60.00
custo_km = 0.15
total_diarias = valor_dias * preço_dia
total_kilometros = valor_km * custo_km
total_a_pagar = total_diarias + total_kilometros

#Olá, {nome}, o seu carro foi alugado por um período de {dias} dias e fe
#z com {quilômetros} quilômetros rodados. O preço da diária é de R$60,00 e o custo p
#or quilo de combustível é de R$0,15.
#Portanto, o valor a ser pago pelo locador é de:
#R${:.2f}.
#Por favor, faça o pagamento em até 10 (dez) dias corridos após a entrega do veículo. Ap
#s após esse prazo, o carro voltará ao local onde foi alugado.
#Atenciosamente, Guilherme!

print ('O total a pagar é de R$ {:.2f}'.format(total_a_pagar))