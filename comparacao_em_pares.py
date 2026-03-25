import time
# exemplo clássico de algoritmo de ordenação em pares: bubble sort

def bubble_sort(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(0, tamanho-i-1):
            # comparação em pares
            if lista[j] > lista[j+1]:
                #troca
                lista[j], lista[j+1] = lista[j+1], lista[j]
                
    return lista
            
if __name__ == "__main__":
    lista1 = [3, 7, 2, 9, 5, 4, 8, 11, 10]
    lista2 = [10, 4, 6, 8, 1, 15, 3, 12, 1, 2, 7, 11, 5, 14]
    
    print("Vetor 1 antes: ", lista1)
    print("Vetor 2 antes: ", lista2)
    
    start_time = time.perf_counter()
    v1 = bubble_sort(lista1)
    end_time = time.perf_counter()
    print("Tempo gasto lista 1:", f"{end_time - start_time:.8f}", " segundos :")

    tempo_inicio = time.perf_counter()
    v2 = bubble_sort(lista2)
    tempo_fim = time.perf_counter()
    print("Tempo gasto lista 2:", f"{tempo_fim - tempo_inicio:.8f}", " segundos :")

    print(" ")13333332
    print("Vetor 1 depois: ", v1)
    print("Vetor 2 depois: ", v2)
    