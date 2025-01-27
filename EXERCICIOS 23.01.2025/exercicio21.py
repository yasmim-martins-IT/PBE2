class Cliente: 
    produtos_disponiveis = []  

    def __init__(self, nome, idade, genero, estado_civil, data_nascimento):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.estado_civil = estado_civil
        self.data_nascimento = data_nascimento
        self.historico_compras = []
        self.carrinho = {}

    def comprar(self, produto):
        if produto in self.carrinho:
            try:
                self.historico_compras.append(produto)
                del self.carrinho[produto]
                return 'Compra realizada com sucesso'
            except:
                return 'Erro ao realizar a compra'
        else:
            return 'esse produto não está disponível no carrinho'

    def adicionar_ao_carrinho(self, produto, quantidade):
        if produto in Cliente.produtos_disponiveis: 
            try:
                self.carrinho[produto] = {'nome': produto.nome, 'quantidade': quantidade}
                print({self.carrinho[produto]})
                return 'produto adicionado ao carrinho com sucesso'
            except:
                return 'erro ao adicionar produto ao carrinho'
        else:
            return 'Produto não está disponivel no catalogo'

class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
       
        Cliente.produtos_disponiveis.append(self)


produto1 = Produto("camisa", 50.0, 100)
produto2 = Produto("Calça", 120.0, 50)
produto3 = Produto("tenis", 180.0, 30)


cliente = Cliente('yasmim', 17, 'feminino', 'solteira', '31/08/2007')


print(cliente.adicionar_ao_carrinho(produto1, 10)) 
print(cliente.adicionar_ao_carrinho(produto2, 2))  

print(cliente.comprar(produto1))  