class Ordenacao:
    """Ordena uma lista de numeros ou palavras"""

    def __init__(self, vetor: list) -> None:
        self.vetor = vetor

    def __str__(self) -> str:
        return str(self.vetor)

    def bubble_short(self) -> None:
        """
        Compara em ordem adjacente e muda os elementos fora de ordem
        A cada passagem pela lista troca o valor em ordem correta
        """
        for index in range(len(self.vetor) - 1):
            for elemento in range(0, len(self.vetor) - index - 1):
                if self.vetor[elemento] > self.vetor[elemento + 1]:
                    self.vetor[elemento], self.vetor[elemento + 1] = self.vetor[elemento + 1], self.vetor[elemento]

    def selection_sort(self) -> None:
        """
        Passa o menor valor para a primeira posicao,
        depois o segundos menor valor para segunda posicao, assim por diante
        """
        for index in range(len(self.vetor)):
            menor_index = index

            for elemento in range(index + 1, len(self.vetor)):
                if self.vetor[elemento] < self.vetor[menor_index]:
                    menor_index = elemento
            self.vetor[index], self.vetor[menor_index] = self.vetor[menor_index], self.vetor[index]

    def insertion_sort(self) -> None:
        """Percorre a lista da esqueda para direita, deixando os alementos mais a esquerda ordenados """
        for index in range(len(self.vetor)):
            elemento = self.vetor[index]

            while index > 0 and self.vetor[index - 1] > elemento:
                self.vetor[index] = self.vetor[index - 1]
                index -= 1
            self.vetor[index] = elemento

    @staticmethod
    def quick_sort(vetor):
        if len(vetor) <= 1:
            return vetor

        pivo = vetor[len(vetor) // 2]
        esquerda = [x for x in vetor if x < pivo]
        meio = [x for x in vetor if x == pivo]
        direita = [x for x in vetor if x > pivo]

        return Ordenacao.quick_sort(esquerda) + meio + Ordenacao.quick_sort(direita)
