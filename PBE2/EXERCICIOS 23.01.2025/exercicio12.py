#exercicio 12
class LojaVirtual (): #classe da loja virtual
    def __init__(self):
        self.produtos = {}
        self.carrinho = {}
    def cadastrar_produtos(self,nome,preco,quantidade_estoque): #metodo para cadastrar o produto
        self.nome = nome
        self.preco  = preco
        self.quantidade_estoque =  quantidade_estoque

        try:
            if nome in self.produtos: #verifica se o produto já foi cadastrado
                return 'Esse produto já foi cadastrado'
            else:
                self.produtos[nome] = {'nome' : self.nome,'preco' :self.preco,'quantidade_estoque':self.quantidade_estoque} #adiciona as informações ao  dicionario produtos 
            return 'Produto cadastrado com sucesso!!'
        except:
            return 'Erro ao cadastrar o produto '
    def gerar_carrinho (self,nome,quantidade_desejada):#metodo que cria o carrinho de compras
        self.quantidade_desejada = quantidade_desejada 
  
        if nome in self.produtos: #verifica se o produto existe na loja
                self.carrinho[nome] =  {'nome': nome ,'preco':self.preco,'quantidade':self.quantidade_desejada} #adiciona o item ao dicioinario do carrinho
                return f'produto adicionado com sucesso '
        else:
                return 'produto não disponivel para a compra'
    
    def adicionar_descontos(self,porcentagem_desconto):
        self.porcentagem_desconto = porcentagem_desconto

        return self.porcentagem_desconto  
    def calcula_valor_total(self,nome): #calcula total desconto
        if nome in self.carrinho :
            self.valor_total = self.carrinho[nome]['preco'] * self.carrinho[nome]['quantidade'] #calcula o preço
            if self.porcentagem_desconto > 0 : #verifica se há algum desconto
                self.valor_total -= self.porcentagem_desconto
            return f'O valor total da compra é: {self.valor_total:.2f}'
        

yasmim = LojaVirtual()
print(yasmim.cadastrar_produtos('pato de croche',100,100))
print(yasmim.gerar_carrinho('pato de croche',100))
yasmim.adicionar_descontos(10)
print(yasmim.calcula_valor_total('pato de croche'))
