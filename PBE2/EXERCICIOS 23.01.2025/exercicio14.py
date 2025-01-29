#exercicio 14

class MaquinaDeVendas(): 
    def __init__(self):
        self.produtos ={}
    def cadastrar_produtos(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

        try: 
            self.produtos[nome] = {'nome' : nome,'preco':preco,'quantidade':quantidade}
            return 'Produto adicinado com sucesso'
        except:
            return 'Produto não encontrado'
    def selecionar_produtos (self,nome,quantidade):
        if nome in self.produtos :
            try :
                preco_total = self.produtos[nome]['preco'] * quantidade
                self.produtos[nome]['quantidade'] -= quantidade
                self.compras = {'produto':nome,'quantidade' : quantidade,'preco_total' : preco_total}

                for i,j in self.compras.items():
                    print(f'{i} : {j}')
                
                return 'Produto selecionado com sucesso'
            except :
                pass
    def inserir_dinheiro(self,valor):
        try:
            self.valor = valor
            return 'pagamento realizado com sucesso'
        except :
            return 'Erro ao fazer o pagamento'
    def retornar_troco (self):
        valor_troco =  self.valor - self.compras['preco_total']

        if valor_troco > 0:
            return f'Seu troco é de R${valor_troco:.2f}'
            
        else:

            return 'Não a troco'
        
    def estoque_disponivel(self,nome):
        if nome in self.produtos:
            return f'estoque disponivel de {nome} : {self.produtos[nome]['quantidade']}'

yasmim=  MaquinaDeVendas()

print(yasmim.cadastrar_produtos('salgadinho',10,100))
print(yasmim.selecionar_produtos('salgadinho',10))
print(yasmim.inserir_dinheiro(111))
print(yasmim.retornar_troco())
print(yasmim.estoque_disponivel('salgadinho'))