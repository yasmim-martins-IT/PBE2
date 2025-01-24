class Carro(): #classe abstrata
    def __init__(self,marca,modelo,velocidade_atual): #metodo contrutor
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual
    def acelerar(self,km_acelerados): #metodo que acelera o carro
        self.km_acelerado = km_acelerados
        self.velocidade_atual += self.km_acelerado #altera a velocidade atual
        return self.velocidade_atual

    def frear(self,km_desacelerados): #metodo que freia o carro
        self.km_desacelerados = km_desacelerados
        self.velocidade_atual -= km_desacelerados #altera a velocidade atual
        return self.velocidade_atual

    def exibir_velocidade(self): #retorna a velocidade atual para o usuário
        return "a velocidade atual é {self.velocidade_atual}km/h"
    
class Carro_combustao(Carro): #classe de carros movidos a combustao
    def __init__(self,marca,modelo,velocidade_atual):
        super().__init__(marca,modelo,velocidade_atual) #herda os parametros  atributos da classe abstrata
        self.combustivel = 'gasolina'  #modo de combustivel
      

class Carro_eletrico(Carro):#classe de carros movidos a eletricidade
    def __init__(self,nome,marca,modelo,velocidade_atual):
        super().__init__(nome,marca,modelo,velocidade_atual)
        self.combustivel = 'bateria (eletricidade)'
      

carro = Carro_combustao('honda','Civic',50)

velocidade_pista = carro.acelerar(50) 

velocidade_bairro = carro.frear(60)

print(f'No bairro eu dirijo meu {carro.modelo} a {velocidade_bairro}km/h e na pista eu dirijo a {velocidade_pista}km/h e utiliza {carro.combustivel}')