import random

def cria_lista(tamanho): 
    lista = []  
    for i in range(tamanho):
        lista.append(random.randint(0, 1000000000))

    return lista

def eh_primo(num):
    if num <= 1:
        return False
    # testar divisores de 2 até a metade do número
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# faz todos os pares possíveis
def testar_todos_os_pares(lista):
    resultados = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            resultados.append((lista[i], lista[j]))

    return resultados

# força bruta condicional, encontra para em que o resultado da soma é um número primo
def forca_bruta_condicional(lista):
    resultados = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            
            soma = lista[i] + lista[2]
            if soma > 1 and eh_primo(soma):
                resultados.append((lista[i], lista[j]))

    return resultados

# exemplo de problema otimizado: soma
def soma_otimizada(lista, alvo):
    vistos = set()
    
    for num in lista:
        if (alvo - num) in vistos:
            return num, alvo - num
        vistos.add(num)
    
    return None

if __name__ == "__main__":
    lista = cria_lista(10000) # pode alterar o tamanho da lista nos testes
    
    resultado = testar_todos_os_pares(lista)
    #resultado = forca_bruta_condicional(lista)
    
    for i in resultado:
        print(i)
        
    print(len(resultado))
    
    
    """
    resultado = soma_otimizada(lista, 7)
    print("Resultado: ", resultado)
    """
    