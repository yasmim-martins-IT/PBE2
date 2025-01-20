import time


#revisão LOPAL
#estrutura básica de dados
#int,float,str,list,dict


#EXERCICIOS 1

'''print('bem-vindo a calculadora da Yasmim') #imprime mensagem de boas vindas na tela


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

#loop para saber se quer adicionat medias
while True:
    escolha = input('Deseja calcular a média de um aluno? (S/N)  ')
    
    if escolha == 'S':
        nota1 = float(input('Insira a nota: '))
        nota2 = float(input('Insira a nota: '))
        nota3 = float(input('Insira a nota: '))
        nota4 = float(input('Insira a nota: '))
        nota5 = float(input('Insira a nota: '))

     
        media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
        print(f'\nA média desse aluno é: {media:.2f}')

        if media >= 5:
            print('APROVADO!!!')
        elif media >= 2.5:
            print('RECUPERAÇÃO')
        else:
            print('REPROVADO')

    elif escolha == 'N':
        break'''
        
#laços de repetição

#exercicio 1 

'''num1  = int(input('digite o numero que deseja fazer a contagem: '))

for i in range(0,num1+1):
    print(i)
    time.sleep(1)

#exercicio 2 

maior = 0
contador = 0

while contador < 1:
    num1 = float(input('digite o numero:'))

    if num1 >= 0 :
        if num1 > maior :
            maior = num1
    else :
        contador +=1 

print(f'o maior numero foi : {maior}')'''

def inverter_string(s):
    nova_palavra = ""

    for i in s:
        nova_palavra = i + nova_palavra

    print(nova_palavra)

inverter_string('oi')

def contar_caracteres(s):
    caracter_dicionario = {}
    for caracter in s :
        if caracter in caracter_dicionario:
            caracter_dicionario[caracter]+=1
        else:
            caracter_dicionario[caracter] = 1
    return caracter_dicionario

print(contar_caracteres('ana'))