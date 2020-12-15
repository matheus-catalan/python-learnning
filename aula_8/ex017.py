from math import sqrt, pow, hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h1 = hypot(co, ca)
h2 = sqrt(pow(co, 2) + pow(ca, 2))

print(
    '\n#1 alternativa \nhypot({}, {}) -> A hipotenusa vai medir {:.2f}'.format(
        co, ca, h1))
print(
    '\n#2 alternativa \nsqrt(pow({}), pow({})) -> A hipotenusa vai medir {:.2f}'
    .format(co, ca, h2))
