class Estoque:
    produtos_estoque = {}

    def __init__(self):
        pass

    def armazenar_estoque(self, nome, quantidade):
        if nome in Produto.produtos_disponiveis:
            try:
                if nome in Estoque.produtos_estoque:
                    Estoque.produtos_estoque[nome]['quantidade'] += quantidade
                else:
                    Estoque.produtos_estoque[nome] = {'nome': nome, 'quantidade': quantidade}
                return 'Produto adicionado com sucesso'
            except:
                return 'Erro ao adicionar o produto ao sistema'
        else:
            return 'Esse produto não é fornecido por nenhum dos nossos fornecedores'

    def gerar_relatorio(self):
        try:
            print(Estoque.produtos_estoque)
        except:
            return 'Erro ao gerar relatório'

class Produto:
    produtos_disponiveis = {}

    def __init__(self, nome, preco_unitario_compra, codigo_produto, preco_unitario_venda):
        self.nome = nome
        self.preco_unitario_venda = preco_unitario_venda
        self.preco_unitario_compra = preco_unitario_compra
        self.codigo_produto = codigo_produto
        
    
        Produto.produtos_disponiveis[nome] = {'nome': self.nome, 'preço compra': self.preco_unitario_compra, 'preço venda': self.preco_unitario_venda, 'codigo': self.codigo_produto}

    @staticmethod
    def cadastrar_produto(nome, preco_unitario_compra, codigo_produto, preco_unitario_venda):
        try:
            if nome not in Fornecedor.fornecedores:
                return f'Erro: O produto "{nome}" não é fornecido por nenhum fornecedor.'
            Produto.produtos_disponiveis[nome] = {
                'nome': nome,
                'preço compra': preco_unitario_compra,
                'preço venda': preco_unitario_venda,
                'codigo': codigo_produto
            }
            return f'Produto {nome} cadastrado com sucesso.'
        except Exception as e:
            return f'Erro ao cadastrar produto: {e}'

class Categoria:
    categorias = {}

    def __init__(self, nome_categoria, produto):
        if not nome_categoria:  # Verifica se o nome da categoria está vazio
            raise ValueError("O nome da categoria não pode ser vazio")
        
        self.nome_categoria = nome_categoria
        if produto in Produto.produtos_disponiveis:
            try:
                Categoria.categorias[produto] = {'Produto': produto, 'categoria': self.nome_categoria}
                print(f'Produto {produto} adicionado à categoria {self.nome_categoria} com sucesso.')
            except Exception as e:
                print(f'Erro ao adicionar o produto à categoria: {e}')
        else:
            print('Esse produto não existe')

class Compras:
    historico_compras = {}

    def __init__(self):
        pass

    def comprar_produtos(self, nome, produto, quantidade):
        if produto in Fornecedor.fornecedores:
            try:
                Compras.historico_compras[nome] = {'produto': nome, 'quantidade': quantidade, 'fornecedor': Fornecedor.fornecedores[produto]['nome']}
                return 'Compra registrada com sucesso'
            except Exception as e:
                return f'Erro ao registrar a compra: {e}'
        else:
            return 'Produto não fornecido'

class Fornecedor:
    fornecedores = {}

    def __init__(self, nome_fornecedor, produtos_responsaveis, local):
        self.nome_fornecedor = nome_fornecedor
        self.produtos_responsaveis = produtos_responsaveis
        self.local = local
        Fornecedor.fornecedores[self.nome_fornecedor] = {'nome': self.nome_fornecedor, 'produto': self.produtos_responsaveis, 'local': self.local}

class Vendas:
    historico_compras = {}
    clientes = {}

    def __init__(self):
        pass

    def cadastrar_cliente(self, nome, idade, cpf):
        if nome not in Vendas.clientes:
            try:
                Vendas.clientes[nome] = {'nome': nome, 'idade': idade, 'cpf': cpf}
                return 'Cliente cadastrado com sucesso'
            except Exception as e:
                return f'Erro ao cadastrar o cliente: {e}'
        else:
            return 'Esse cliente já foi cadastrado'

    def realizar_compra(self, produto, nome, quantidade):
        if produto in Estoque.produtos_estoque and nome in Vendas.clientes:
            try:
                valor_total = quantidade * Produto.produtos_disponiveis[produto]['preço venda']
                Vendas.historico_compras[nome] = {'Cliente': nome, 'Produto': produto, 'Quantidade': quantidade, 'Valor total': valor_total}
                print(Vendas.historico_compras[nome])
                Estoque.produtos_estoque[produto]['quantidade'] -= quantidade
                return 'Venda realizada com sucesso'
            except:
                return f'Falha ao realizar a venda'
        else:
            return 'Cliente ou produto não encontrados'


fornecedor1 = Fornecedor("Yasmim", ["pato borracha", "mochi de pato"], "Senai")
fornecedor2 = Fornecedor("nicolly", ["Coca-cola"], "Polo norte")

produto1 = Produto("pato borracha", 10.0, "001", 15.0)
produto2 = Produto("mochi de pato", 12.0, "002", 18.0)
produto3 = Produto("Coca-cola", 8.0, "003", 12.0)

categoria1 = Categoria("Fofura", "pato borracha")
categoria2 = Categoria("Delícia", "mochi de pato")

estoque = Estoque()
print(estoque.armazenar_estoque("pato borracha", 50))  
print(estoque.armazenar_estoque("Coca-cola", 30))  
print(estoque.armazenar_estoque("mochi de pato", 10))  

estoque.gerar_relatorio()

compras = Compras()
print(compras.comprar_produtos("Compra1", "pato borracha", 10))  

vendas = Vendas()
print(vendas.cadastrar_cliente("Cliente1", 30, "12345678900"))  
print(vendas.realizar_compra("pato borracha", "Cliente1", 5))  
print(vendas.realizar_compra("mochi de pato", "Cliente1", 15))
