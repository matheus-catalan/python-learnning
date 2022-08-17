frase = 'Curso em Video Python'

print(frase)
print(
    '|  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |'
    .format(frase[0], frase[1], frase[2], frase[3], frase[4], frase[5],
            frase[6], frase[7], frase[8], frase[9], frase[10], frase[11],
            frase[12], frase[13], frase[14], frase[15], frase[16], frase[17],
            frase[18], frase[19], frase[20]))
print(
    '| 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |\n'
)

print('\n----------------- Fatiamento ----------------- \n')

print('frase[0:5] -> {}'.format(frase[0:5]))

print('frase[:5] -> {}'.format(frase[:5]))

print('frase[6:] -> {}'.format(frase[6:]))

print('frase[9::3] -> {}'.format(frase[9::3]))

print('\n----------------- Analise ----------------- \n')

print('len(frase) -> {}'.format(len(frase)))

print("count('o' -> {}".format(frase.count('o')))

print("count('o', 0, 13) -> {}".format(frase.count('o', 0, 13)))

print("find('deo') -> {}".format(frase.find('deo')))

print("find('android') -> {}".format(frase.find('android')))

print("'curso' in frase -> {}".format('Curso' in frase))

print('\n----------------- Transformação ----------------- \n')

print("frase.replace('Python', 'Android') -> {}".format(
    frase.replace('Python', 'Android')))

print("frase.upper() -> {}".format(frase.upper()))

print("frase.lower() -> {}".format(frase.lower()))

print("frase.capitalize() -> {}".format(frase.capitalize()))

print("frase.title() -> {}".format(frase.title()))

frase2 = '   Apredendo Python  '

print(frase)
print(
    '\n|  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |'
    .format(frase2[0], frase2[1], frase2[2], frase2[3], frase2[4], frase2[5],
            frase2[6], frase2[7], frase2[8], frase2[9], frase2[10], frase2[11],
            frase2[12], frase2[13], frase2[14], frase2[15], frase2[16],
            frase2[17], frase2[18], frase2[19], frase2[20]))
print(
    '| 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |\n'
)
print()

print("frase2.strip() -> {}".format(frase2.strip()))
print("frase2.rstrip() -> {}".format(frase2.rstrip()))
print("frase2.lstrip() -> {}".format(frase2.lstrip()))

print('\n----------------- Divisão ----------------- \n')

print("frase.split() -> {}".format(frase.split()))
