#exercicio 13
class Agenda():
    def __init__(self): #metodo construtor
        self.contatos = {} #dicionario para adicionar os contatos
    def adicionar_contatos (self,nome,numero): #metodo para adiconar os contatos
    
        if numero in self.contatos : #verifica se esse numero de contato já existe
            return'Esse contato já existe'
        else:
            self.contatos[numero] = {'nome' :nome,'numero':numero}
            return 'Contato adicionado com sucesso'
    def editar_contato(self, numero, novo_nome=None, novo_numero=None):
        if numero in self.contatos:
            if novo_nome:
                
                self.contatos[numero]['nome'] = novo_nome
                return 'Nome alterado com sucesso'
            if novo_numero:
               
                self.contatos[novo_numero] = self.contatos.pop(numero)
                self.contatos[novo_numero]['numero'] = novo_numero
                return 'Número alterado com sucesso'
            return 'Escolha inválida'
        else:
            return 'Contato não encontrado'
    def buscar_contato(self, nome=None, numero=None):
        if nome:
           
            for n, c in self.contatos.items():
                if c['nome'].lower() == nome.lower():
                    return f'{c["nome"]}: {c["numero"]}'
            return 'Contato não encontrado'
        elif numero:
          
            if numero in self.contatos:
                return f'{self.contatos[numero]["nome"]}: {self.contatos[numero]["numero"]}'
            return 'Contato não encontrado'
yasmim = Agenda()
print(yasmim.adicionar_contatos('ny','19 xxxxx-xxxx'))
print(yasmim.editar_contato('19 xxxxx-xxxx',novo_nome ='Nicolly'))
print(yasmim.buscar_contato(nome='Nicolly'))
