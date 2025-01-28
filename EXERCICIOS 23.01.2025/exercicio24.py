#exercicio24
class Zoologico ():
    funcionarios = {}
    animais_zoologico = {}
    def __init__(self):
        pass

class Animal ():
    def __init__(self,nome,especie,idade,peso,genero,tipo_alimentação):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.genero = genero
        self.alimentação = tipo_alimentação
    def colocar_zoologico (self):
        try:
            Zoologico.animais_zoologico[self.nome] = {'nome': self.nome , 'especie' : self.especie,'idade' : self.idade, 'peso' : self.peso, 'genero' : self.genero, 'tipo alimentação' : self.alimentação}
            return 'Animal criado com sucesso'
        except :
            return 'Erro ao criar o animal'
class Funcionario ():
    def __init__(self,nome,idade,genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

        Zoologico.funcionarios[nome] = {"nome" : nome, 'idade' : idade , 'genero' : genero}
    def alimentar_animais (self,nome_animal):
        if nome_animal in Zoologico.animais_zoologico :
            if Zoologico.animais_zoologico[nome_animal]['tipo alimentação'] == 'carnivoro':
                print('alimentar animal com pedaço de carne')

                return f'{nome_animal} alimentado com sucesso'
            elif Zoologico.animais_zoologico[nome_animal]['tipo alimentação'] == 'herbivoro':
                print('alimentar animal com algum tipo de planta')

                return f'{nome_animal} alimentado com sucesso'
            elif Zoologico.animais_zoologico[nome_animal]['tipo alimentação'] == 'onivoro':
                print('alimentar animal com algum tipo de planta ou carne')

                return f'{nome_animal} alimentado com sucesso'
class Veterinario ():
    veterinarios = {}
    def __init__(self,nome,genero):
        self.nome = nome
        self.genero = genero

        Veterinario.veterinarios[nome] = {'nome':nome , 'genero' : genero}
    def curar_animais (self,animal,veterinario) :
        if veterinario in Veterinario.veterinarios :
            if animal in Zoologico.animais_zoologico :
                return f'Animal {animal} curado com sucesso'
            else :
                return f'Animal {animal} não encontrado'
        else :
            return f'{veterinario} não está habilitado para tratar esse animal'

    

animal1 = Animal("Leão", "Panthera leo", 5, 200,"Masculino","carnivoro")
animal2 = Animal("Zebra", "Equus zebra", 3, 300,"Feminino","herbivoro")
animal3 = Animal("Urso","Ursus arctos", 4, 450, "Masculino","onivoro")

print(animal1.colocar_zoologico())  
print(animal2.colocar_zoologico()) 

funcionario1 = Funcionario(nome="João", idade=30, genero="Masculino")
veterinario1 = Veterinario(nome="Dra. Ana", genero="Feminino")


print(funcionario1.alimentar_animais("Leão",))  
print(funcionario1.alimentar_animais("Zebra")) 


print(veterinario1.curar_animais("Leão",'Dra. Ana'))  
print(veterinario1.curar_animais("Zebra", 'Dra. Ana')) 
print(veterinario1.curar_animais("Urso", 'Dra. Ana'))  