from random import randrange

entrada = input('Digite o nome de seus alunos separando-os com , :')

alunos = entrada.split(',')

aluno = randrange(0,len(alunos))

print(f'O aluno sorteado para apagar o quadro e o :{alunos[aluno]}')