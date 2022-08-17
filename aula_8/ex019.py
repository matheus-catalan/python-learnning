from random import choice

alunos = ['', '', '', '']

alunos[0] = str(input('Digite o nome do primeiro aluno: '))
alunos[1] = str(input('Digite o nome do segundo aluno: '))
alunos[2] = str(input('Digite o nome do terceiro aluno: '))
alunos[3] = str(input('Digite o nome do quarto aluno: '))

print('O aluno escolhido foi o {}'.format(choice(alunos)))
