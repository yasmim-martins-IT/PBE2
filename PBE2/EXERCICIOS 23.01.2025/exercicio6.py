#exercio 6

class Produto():
    def __init__(self, nome, preco, quantidade_em_estoque):  # Método construtor
        # Definindo os atributos
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

    def calcular_estoque(self, quantidade_vendida):  # Método que calcula o valor do estoque
        self.quantidade_vendida = quantidade_vendida
        if self.quantidade_vendida > 0:
            self.quantidade_em_estoque -= self.quantidade_vendida  # Calcula o novo valor do estoque
        return self.quantidade_em_estoque

    def comprar_produto(self, quantidade_desejada):  # Método que verifica a disponibilidade do produto
        self.quantidade_desejada = quantidade_desejada
        if self.quantidade_desejada <= self.quantidade_em_estoque:
            print(f'Produto {self.nome} está disponível para compra.')
        else:
            print(f'O produto {self.nome} não está disponível no momento.')

# Testando o código

produto1 = Produto('Furadeira', 200, 200)  # Criando o produto com 200 unidades em estoque

# Verificando se o produto está disponível para compra
produto1.comprar_produto(10)  # Tentando comprar 10 unidades

# Atualizando o estoque após a compra
print(f'Estoque após compra: {produto1.calcular_estoque(10)} unidades')

# Verificando novamente se o produto está disponível
produto1.comprar_produto(200)  # Tentando comprar 200 unidades
