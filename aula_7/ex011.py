l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
m = l * a

print('Sua parade tem a dimensão de {}x{} e sua área é de {}.'.format(l, a, m))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(m / 2))
