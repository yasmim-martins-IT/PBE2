#exercicio 2
class Conta_Bancaria(): #classe abastrata conta bancaria
    def __init__(self,numero_conta,nome_titular,saldo): #metodo contrutor passando os atributos
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
    def sacar(self,valor_saque): #metodo de sacar
        if self.saldo > 0: #verificando se o saldo é positivo
            self.valor_saque = valor_saque #parametro do valor de saque
            self.saldo -=self.valor_saque #correção para o novo saldo da conta bancaria
        else:
            #resposta caso seja impossivel realizar essa ação
            print('saldo insuficiente para realizar essa ação')

    def depositar(self,valor_deposito): #metodo de depositar
        self.valor_deposito = valor_deposito #valor a ser depositado

        self.saldo +=self.valor_deposito #atualiza o saldo da conta bancaria

conta1 = Conta_Bancaria('5454445','yasmim Sampaio Martins',100)

conta1.sacar(50) #saque do dinheiro
conta1.depositar(2)#deposito do dinheiro

print(conta1.saldo)