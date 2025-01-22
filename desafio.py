
def desafio_mergesort(lista, inicio=0, fim=None): #função que dividira e fara a ordenação da lista
    if fim is None: #para pode iniciar a função com o fim sem ser definido pois a lista também é um parametro
        fim = len(lista) #lê o tamanho da lista e armazena na variavel

    if fim - inicio > 1: #se haver mais de um caracter na lista 
        meio = (fim + inicio) // 2 #cria a variavel que é o meio da lista
        desafio_mergesort(lista, inicio, meio)  #lado "esquerdo da lista
        desafio_mergesort(lista, meio, fim)     #lado "direito " da lista
        merge(lista, inicio, meio, fim) #chama a função merge        

def merge(lista, inicio, meio, fim): #função que compara os dois lado da lista
    left = lista[inicio:meio] #lado esquerdo que corresponde do inicio até o meio da lista
    rigth = lista[meio:fim] #lado direito que corresponde do meio até o ultimo caracter da lista
    i, j = 0, 0 

    for k in range(inicio, fim): #vai rodar a lista do inicio até o fim
        if i >= len(left): #caso
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

def insertion_sort(valores): #função que realiza a ordenação da lista com o metodo insertion sort
    for i in range(1, len(valores)):  #vai rodar de um até o numero de elementos presente na lista
        
        j = i  #variavel j recebe o valor de i para o loop seguinte terminar junto com esse

      
        while j > 0 and valores[j] < valores[j - 1]: #loop que funcionara enquanto o j for maior que 10 e os valores passados na lista for menor que o anterior
            # Troca os valores
            auxiliadora = valores[j] #ajuda na troca de valores
            valores[j] = valores[j - 1] #troca o valor pelo anterior
            valores[j - 1] = auxiliadora 
            j -= 1  #descrementa a variavewl


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
            print(f'O numero foi encontrado com sucesso na posição: {meio}')
            return meio  
        
   
        elif lista[meio] > elemento:
            fim = meio - 1
        

        else:
            inicio = meio + 1


lista = [1, 3, 5, 7, 9, 11, 13, 15]
busca_binaria(lista, elemento)

