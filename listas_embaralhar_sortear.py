import random
alunos=['joão', 'maria', 'pedro', 'ana', 'lucas', 'mariana',]
print(f'lista: {alunos}')
# embaralhar a lista 
random.shuffle(alunos)
print(f' lista embaralhada: {alunos}')
#escolhe um aluno aleatoriamente 
aluno_sorteado = random.choice(alunos)
print(f' aluno sorteado: {aluno_sorteado}')