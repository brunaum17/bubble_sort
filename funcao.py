import time
import random

def gerar_lista():
    return [random.randint(0, 1000) for _ in range(1000)]

def bubble_sort(L):

    count = 0  

    start_time = time.time()  

    n = len(L)
    for j in range(n):
        for i in range(n - 1):
            count += 1  
            if L[i] > L[i + 1]:
                # Troca os elementos de posição
                t = L[i]
                L[i] = L[i + 1]
                L[i + 1] = t
                

    end_time = time.time()  # Fim da medição do tempo
    tempo_execucao = end_time - start_time  # Tempo total de execução

    return L, tempo_execucao, count



lista = gerar_lista()

lista_ordenada = bubble_sort(lista)

print("Tempo:", lista_ordenada[1],"segundos")
print("Quantidade de execuções:", lista_ordenada[2])





