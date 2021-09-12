from timeit import timeit

from ordenacao import Ordenacao

entrada_do_usuario = input().split()
vetor = [int(i) for i in entrada_do_usuario[:]]

# Antes
print(vetor)

tempo_de_inicio = timeit()
print(Ordenacao.quick_sort(vetor))
tempo_de_finalizacao = timeit()

tempo_de_duracao = tempo_de_inicio - tempo_de_finalizacao
print(f'{tempo_de_duracao} segundos')
