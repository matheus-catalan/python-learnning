from random import randint
alunos = ['', '', '', '']
order = [0, 1, 2, 3]
alunos[0] = input('Digite o nome do primeiro aluno: ')
alunos[1] = input('Digite o nome do segundo aluno: ')
alunos[2] = input('Digite o nome do terceiro aluno: ')
alunos[3] = input('Digite o nome do quarto aluno: ')

order = [randint(0, 3), randint(0, 3), randint(0, 3), randint(0, 3)]

print('A ordem de apresentação será:')
print('1 - {} \n2 - {} \n3 - {} \n4 - {}'.format(alunos[order[0]],
                                                 alunos[order[1]],
                                                 alunos[order[2]],
                                                 alunos[order[3]]))
