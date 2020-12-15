dias = int(input('Qual foi a quantidade de dias: '))
km = float(input('Qual foi a quantidade de km percorrido: '))
total = (km * 0.15) + (dias * 60)

print('O total a ser pago é de R${:.2f}'.format(total))
