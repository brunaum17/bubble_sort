import time
import random

def gerar_lista():
    return [random.randint(0, 10000) for _ in range(10000)]

def bubble_sort(L):

    troca_count = 0  # Contador para a quantidade de trocas

    start_time = time.time()  # Início da medição do tempo

    n = len(L)
    for j in range(1, n):
        for i in range(0,n - 1):
            if L[i] > L[i + 1]:
                # Troca os elementos de posição
                t = L[i]
                L[i] = L[i + 1]
                L[i + 1] = t
                troca_count += 1  # Incrementa o contador de trocas

    end_time = time.time()  # Fim da medição do tempo
    tempo_execucao = end_time - start_time  # Tempo total de execução

    return L, tempo_execucao, troca_count



lista = gerar_lista()

lista_ordenada = bubble_sort(lista)

print("Tempo:", lista_ordenada[1],"segundos")
print("Quantidade de execuções:", lista_ordenada[2])





