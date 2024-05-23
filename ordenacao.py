import random
alunos=['joão', 'maria', 'pedro', 'ana', 'lucas', 'mariana',]
print(f'lista: {alunos}')
# embaralhar a lista 
random.shuffle(alunos)
print(f' lista embaralhada: {alunos}')
#ordena a lista cres
alunos.sort()
print(f' lista crescente: {alunos}')
#ordena a lista decrescente
alunos.sort(reverse=True)
print(f' lista descrescente: {alunos}')
