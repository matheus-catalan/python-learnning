n = float(input('Qual é o preço do produto? R$'))
print(
    'O produto custava R${:.2f}, na promoção com descont de 5% vai custar R${:.2f}'
    .format(n, (n - (n * 0.05))))
