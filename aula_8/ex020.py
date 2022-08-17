from random import shuffle
alunos = ['', '', '', '']
alunos[0] = input('Digite o nome do primeiro aluno: ')
alunos[1] = input('Digite o nome do segundo aluno: ')
alunos[2] = input('Digite o nome do terceiro aluno: ')
alunos[3] = input('Digite o nome do quarto aluno: ')

shuffle(alunos)

print('A ordem de apresentação será: ')
print(alunos)