#exercicio 21

class Clientes ():
  def __init__(self,nome,idade,genero,estado_civil,data_nascimento) :
    self.nome = nome
    self.idade = idade
    self.genero = genero
    self.estado_civil = estado_civil
    data_nascimento = data_nascimento
    self.historico_compras = []
    self.produtos_disponiveis = [Produtos.nome()]
    self.carrinho = {}
  def comprar (self,produto):
    self.produto = produto
    if self.produto in self.carrinho :
      self.historico_compras.append(produto)

      self.carrinho.remove(pop)
      
  def adicionar_ao_carrinho(self,produto):
    
    

class Produtos ():
  def __init__(self,nome,preco,quantidade_estoque) :
    self.nome = nome
    self.preco =  preco
    self.quantidade_estoque = quantidade_estoque

class Pedidos ():
  def __init__(self) -> None:
    self.clientes = Clientes().nome()
    self.produtos = Produtos().nome().clientes()
    