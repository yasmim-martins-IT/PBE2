class Cachorro (): #classe é o molde do objeto contem todas as informações e atributos bases para o cachorro
    #tem os metodos que são as ações que podem ser feitas pelo o objeto
    def __init__(self,nome,fome,sono):
        self.nome = nome #atributos do objeto caracteristicas de um cachorro
        self.fome = fome
        self.sono = sono
    def dormir(self):#metodo dormir que representa o sono do cachorro
        sono -= 1
        
    def comer (self):
        fome = False
    
cachorro1 = Cachorro('jeremias',3,True)

print (cachorro1.nome)

#Polimorfismo
#permite que objetos de diferentes classes possam ser tratados da mesma forma,permitindo usar um unico nome para diferentes tipos de objetos
#teremos uma classe base e diversas outras classes derivadas
#classe base define um conjunto de metodos que será utilizadas e compartilhado pela classe
#assim podemos reutilizar os atributos da base nos outros objetos mesmo que não sejam com os mesmo atributos
#herdando os mesmos metodos mas tratados de jeito diferente

#Herança:
#ela pega os atributos ou metodos de outra classe presente antes no codigo
#exemplo

class Zoologico():  # Classe base
    def jaula(self):
        return True

class Animals():  # Classe base
    def __init__(self, nome, peso, idade, genero):  # Atributos da classe que serão herdados
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero
        self.estar_preso = Zoologico().jaula()  # Herda o método jaula

    def fazer_som(self):
        pass

class Leao(Animals):  # Classe Leão
    def __init__(self, nome, peso, idade, genero):
        super().__init__(nome, peso, idade, genero)  # Herda os atributos da classe Animals

    def fazer_som(self):  # Método de rugir
        return "RAAAWRRRRRRR"  # Rugido

class Pavao(Animals):  # Classe Pavão
    def __init__(self, nome, peso, idade, genero):
        super().__init__(nome, peso, idade, genero)  # Herda atributos de Animals

    def fazer_som(self):
        return "fiufiufiu"  # Som do pavão

# Criando instâncias dos animais
leao = Leao('Alex', '70kg', '10', 'macho')
pavao = Pavao('Pavo', '2kg', '5', 'macho')

animais = [leao, pavao]

for animal in animais:
    print(f'O som do {animal.nome} é: {animal.fazer_som()}')
