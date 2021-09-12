from timeit import timeit

from ordenacao import Ordenacao

entrada_do_usuario = input().split()
vetor = [int(i) for i in entrada_do_usuario[:]]

elementos = Ordenacao(vetor)

# Antes
print(elementos)

tempo_de_inicio = timeit()
elementos.bubble_short()
tempo_de_finalizacao = timeit()

# Depois
print(elementos)

tempo_de_duracao = tempo_de_inicio - tempo_de_finalizacao
print(f'{tempo_de_duracao} segundos')
