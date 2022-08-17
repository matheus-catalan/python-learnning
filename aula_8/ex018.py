from math import sin, cos, tan, radians
an = float(input('Digite um angulo que voce deseja: '))

print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cos(radians(an))))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, sin(radians(an))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tan(radians(an))))
