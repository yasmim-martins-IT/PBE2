#exercicio 1
class Banco (): #classe que representa o banco
    def __init__(self):
        pass
    def cadastrar_clientes(self,nome,idade,cpf,estado_civil,data_nascimento,nome_pai,nome_mae,dependentes,ocupacao) : #metodo para cadastrar um cliente
        try: #verfica se o procedimento deu certo u não 
            self.nome = nome
            self.idade = idade
            self.cpf = cpf 
            self.estado_civil = estado_civil
            self.data_nascimento = data_nascimento
            self.nome_pai = nome_pai
            self.nome_mae = nome_mae
            self.dependentes = dependentes
            self.ocupacao = ocupacao

            return 'Cadastro concluido com sucesso' #resposta ao usuário
        except:
            return 'Erro ao fazer o Cadastro' 
    def criar_conta (self,saldo=0.0): #metodo para criar uma conta no Banco
        self.saldo = saldo 
        return "Conta criada com sucesso" #resposta ao usuário
       
    def depositar(self,valor_deposito): #metodo para depositar saldo na conta bancaria
        try: #verifica se o procedimento deu certo
            self.valor_depositado = valor_deposito
            self.saldo += self.valor_depositado #altera valor do saldo
            return('Deposito feito com sucesso') #resposta ao usuario
        except:
            return('Erro ao fazer o deposito') #resposta ao usuario
    def sacar(self,valor_saque): #metodo para sacar dinheiro
        self.valor_saque = valor_saque
        try: 
             if self.saldo >= self.valor_saque : #condicional para a realiação do saque

                self.saldo -= self.valor_saque #altera o valor do saldo
                return 'Saque concluido com sucesso !' #resposta ao usuário
             else:
                 return('Valor insuficiente para o saque')
        except:
            return 'Erro ao realizar o saque' #resposta ao usuário
    def transferir(self,valor_transferido,numero_conta_destino): #metodo para tranferir o dinheiro
        self.valor_transferido = valor_transferido
        self.numero_conta_destino = numero_conta_destino

        try:
            if self.saldo >= self.valor_transferido: #condicional para a realização da transferencia
                self.saldo -= self.valor_transferido #altera o valor do saldo
                
                return 'Transferencia concluida com sucesso!!!' #resposta ao usuario
            else:
                return 'valor insuficinte para fazer a tranferencia'
        except:
            return 'Erro ao realizar transferencia' 
    def exibir_saldo(self):
        return f'O valor do saldo atual é: {self.saldo:.2f}'
        


cliente = Banco()
print(cliente.cadastrar_clientes('yasmim Sampaio Martins',18,'xxx.xxx.xxx-xx','solteira','31/0x/200x','Mauricio de Souza','Fernanda Montenegro',False,'jovem aprendiz'))
print(cliente.criar_conta())
print(cliente.depositar(250.99))
print(cliente.transferir(50.99,'2093029930'))
print(cliente.sacar(1500))
print(cliente.exibir_saldo())


            

    