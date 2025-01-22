import time


#revisão LOPAL
#estrutura básica de dados
#int,float,str,list,dict


#EXERCICIOS 1

print('bem-vindo a calculadora da Yasmim') #imprime mensagem de boas vindas na tela


#armazenando valores inseridos pelo o usuário
num1 =  int(input('digite o primeiro numero que deseja somar: '))
num2 = int(input('digite o segundo numero que deseja somar: '))

#efetuando os calculos com os operadores 
resultado = num1+num2

#retornando resposta ao usuário
print(f'resultado de: {num1} + {num2} = {resultado}\n \n ')

#EXERCICIO 2 

#loop caso ocorra a entrada de valor invalido
while True:
    ano = int(input('digite o ano de seu nascimento:')) #entrada de dados correspondente ao ano
    
    if ano >=2025:#verificando se o numero correspondente ao ano de nascimento é maior ou igual 2025
        print('data de nascimento invalida! \ndigite novamente:')#mensagem de resposta para o usuário
    else :
        #caso seja um valor valido fim do loop 
        break

idade_usuário =  2025-ano #calcula idade

print(f'sua idade em 2025 será: {idade_usuário}')#resposta do resultado para o usuário


#operadores lógicos e condicionais 

#exercicio 3 

#entrada do numero
num1 = float(input('insira o numero:'))

#condicional 
if num1 % 2 == 0 :#checa se o numero inserido pelo o usuário dividio por 2 é zero
    #respsta ao usuário
    print(f'o numero {num1} é um numero par')
else :
     #resposta ao usuário
     print(f'o numero {num1} é um numero impar')


#exercicio 4

#loop para saber se quer adicionar medias
while True:
    escolha = input('Deseja calcular a média de um aluno? (S/N)  ')#variavel que armazenara a escolha do usuário
    
    if escolha == 'S': #condicional para adicionar as notas
        #variaveis de armazenamento das notas
        nota1 = float(input('Insira a nota: '))
        nota2 = float(input('Insira a nota: '))
        nota3 = float(input('Insira a nota: '))
        nota4 = float(input('Insira a nota: '))
        nota5 = float(input('Insira a nota: '))

        
        media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5 #variavel que calculara a média do aluno
        print(f'\nA média desse aluno é: {media:.2f}')

        if media >= 5: #compara a média do aluno
            #resposta ao usuário
            print('APROVADO!!!')
        elif media >= 2.5:
            print('RECUPERAÇÃO')
        else:
            print('REPROVADO')

    elif escolha == 'N': 
        #fim do loop
        break
        
#laços de repetição

#exercicio 1 

num1  = int(input('digite o numero que deseja fazer a contagem: ')) #variavel para armazenar o numero

for i in range(0,num1+1): #loop que rodara até o numero solicitado pelo o usuário
    #resposta ao usuário
    print(i)
    #tempo de delay de 1 segundo
    time.sleep(1)

#exercicio 2 

maior = 0 #variavel que armazenara o maior valor zerada
contador = 0 #contador para o loop

while contador < 1: #loop para digitar os numeros
    num1 = float(input('digite o numero:')) #variavel que armazenara o numero

    if num1 >= 0 : #verifica se o numero é positivo
        if num1 > maior : #verifica se o valor armazenado no num1 é maior que o valor armazenado na variavel maior
            maior = num1 #atribuiu o valor de num1 na variavel maior
    else :
        contador +=1 #incrementa a variavel contador

print(f'o maior numero foi : {maior}') #retorna para o maior numero para o usuário

def inverter_string(s): #função que inverte a string
    nova_palavra = "" #variavel vazia para armazenar a palavra invertida

    for i in s: #que irá passar todas as letras da palavra
        #armazena a letra 
        nova_palavra = i + nova_palavra

    print(nova_palavra) #retorna a palavra invertida

inverter_string('oi')

def contar_caracteres(s): #função para contar os caracteres de uma palavra, e etc.
    caracter_dicionario = {} #dicionario para armazenar as letras e quantidade de vezes
    for caracter in s : #vai percorres a palavra
        if caracter in caracter_dicionario: #se já for encontrada essa letra
            caracter_dicionario[caracter]+=1# adiciona 1 ao indice q a correspode
        else:
            caracter_dicionario[caracter] = 1 #cria a chave com a letra e o valor 1
    return caracter_dicionario #retorna o valor do dicionario

print(contar_caracteres('ana')) 