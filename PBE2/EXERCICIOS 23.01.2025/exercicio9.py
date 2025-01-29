#exercicio 9
class Paciente(): #classe que representa o pasciente
    def __init__(self,nome,idade,historico=None): #metodo construtor
        #historico está atribuido como None caso o pasciente não haja nenhuma consulta não seja nescessário inseri-lo
        self.nome = nome
        self.idade = idade
        self.historico = historico
    def nova_consulta(self,especialidade,data,medico): #metodo que adicionar novas consultas no historico
        self.especialidades = especialidade
        self.data = data
        self.medico = medico
        historico_consultas ={'especialidade': self.especialidades,
                              'data' : self.data,
                              'medico': self.medico} #dicionario com os dados da consulta
     
        self.historico = historico_consultas #adiciona o dicionario ao parametro historico 
        
        return self.historico #retorna o parametro contrutor historico
    
    def exibir_consultas(self): #exibe o historico de consultas para o usuáriio
        for i in self.historico :
            print(self.historico[i] )
    
paciente = Paciente('yasmim',17)     

paciente.nova_consulta('otorrinolaringologista','31/09/2024','Ivan')

paciente.exibir_consultas()