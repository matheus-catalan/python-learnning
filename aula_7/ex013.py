sal = float(input('Qual é o salario do Funcionario ? R$'))
print(
    'Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'
    .format(sal, (sal + (sal * 0.15))))
