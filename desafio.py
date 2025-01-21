
def desafio_mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)

    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        desafio_mergesort(lista, inicio, meio) 
        desafio_mergesort(lista, meio, fim)     
        merge(lista, inicio, meio, fim)         

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    rigth = lista[meio:fim]
    i, j = 0, 0

    for k in range(inicio, fim):
        if i >= len(left):
            lista[k] = rigth[j]
            j += 1
        elif j >= len(rigth):
            lista[k] = left[i]
            i += 1
        elif left[i] < rigth[j]:
            lista[k] = left[i]
            i += 1
        else:
            lista[k] = rigth[j]
            j += 1

# Lista de números aleatórios
numeros_aleatorios = [1, 2, 4, 55, 66, 9898, 1, 2.5]

# Chamando o algoritmo de Merge Sort
desafio_mergesort(numeros_aleatorios)

print(numeros_aleatorios)


#insertion sort

def insertion_sort(valores):
    for i in range(1, len(valores)):  
        
        j = i  

      
        while j > 0 and valores[j] < valores[j - 1]:
            # Troca os valores
            auxiliadora = valores[j]
            valores[j] = valores[j - 1]
            valores[j - 1] = auxiliadora
            j -= 1  


numeros_insertions = [1, 5, 6, 88, 99, 666, 77, 441, 11, 1]


insertion_sort(numeros_insertions)


print(numeros_insertions)

def bubble_sort(values) :
    tamanho = len(values)
    for i in range(tamanho - 1):
        for j in range(tamanho -i - 1):
            if values[j] > values[j+1]:
                values[j],values[j+1] = values [j+1],values[j]

            
sla = [1.22,15,2,1,1,2,1,1,333,3,333,7]

bubble_sort(sla)

print(sla)

'''def busca_linear(lista, elemento_desejado):
    tamanho = len(lista)

    for i in range(tamanho - 1 ):
        if lista[i] == elemento_desejado :
            print(f'elemento localizado com sucesso! : {lista[i]} ')
            break

elemento = 7

busca_linear(sla,elemento)'''

elemento = 1

def busca_binaria (lista,elemento):
    inicio = 0
    fim = len(lista)-1
    
    while fim >= inicio:
        meio = (fim + inicio) // 2  
        
       
        if lista[meio] == elemento:
            print(f'Valor encontrado com sucesso na posição: {meio}')
            return meio  
        
   
        elif lista[meio] > elemento:
            fim = meio - 1
        

        else:
            inicio = meio + 1


lista = [1, 3, 5, 7, 9, 11, 13, 15]
busca_binaria(lista, elemento)