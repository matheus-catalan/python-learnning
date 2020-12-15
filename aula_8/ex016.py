from math import sqrt, floor, trunc

# primeira alternativa
num = float(input('Digite um numero: '))
print(' #1 alternativa trunc() -> O numero {} tem a parte inteira {}.'.format(
    num, trunc(num)))

#segunda alternativa
print(' #2 alternativa int() -> O numero {} tem a parte inteira {}.'.format(
    num, int(num)))

#terceira alternativa
print(' #3 alternativa floor() -> O numero {} tem a parte inteira {}.'.format(
    num, floor(num)))
