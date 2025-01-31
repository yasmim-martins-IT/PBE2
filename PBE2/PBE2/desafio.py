
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

def bubble_sort(values) : #função que ordena a lista utilizando o metodo sort
    tamanho = len(values) #variavel que armazena o tamanho da lista
    for i in range(tamanho - 1): #loop que rodara até o ultimo indice da lista
        for j in range(tamanho -i - 1): #verifica um elemento a menos
            if values[j] > values[j+1]: #se o elemento for maior que o proximo da lista
                values[j],values[j+1] = values [j+1],values[j] #inverte de valor

            
sla = [1.22,15,2,1,1,2,1,1,333,3,333,7]

bubble_sort(sla)

print(sla)

def busca_linear(lista, elemento_desejado): #função de busca linear
    tamanho = len(lista) #armazena o tamanho da lista

    for i in range(tamanho - 1 ): #roda toda a lista
        if lista[i] == elemento_desejado : #compara com elemento desejado
            print(f'elemento localizado com sucesso! : {lista[i]} ') #resposta ao usuario
            break #fim do loop

elemento = 7

busca_linear(sla,elemento)

elemento = 1

def busca_binaria (lista,elemento): #função busca binaria
    inicio = 0 #variavel zerada (elemento inicial)
    fim = len(lista)-1 #armazena o elemento final da lista
    
    while fim >= inicio: #se o fim for maior ou igual o começo (garante que não haja conjuntos vazio)
        meio = (fim + inicio) // 2  #arazena elemento meio da lista
        
       
        if lista[meio] == elemento: #se o meio for igual o elemento
            print(f'O numero foi encontrado com sucesso na posição: {meio}') #resposta usuário
            return meio  #retorna a variavel meio
        
   
        elif lista[meio] > elemento: #compara se a variavel do meio é igual o elemento desejado
            fim = meio - 1 #o final se torna o elemento anterior ao meios
        

        else:
            inicio = meio + 1 #o inicio se torna o elemento posterior ao meiio


lista = [1, 3, 5, 7, 9, 11, 13, 15]
busca_binaria(lista, elemento)

