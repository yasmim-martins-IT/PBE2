#exercicio 22
class Estoque :
    produtos_estoque = {}
    def __init__(self):
        pass
        
    def armazenar_estoque (self,nome,quantidade):
        if nome in Produto.produtos_disponiveis():
            try:
                Estoque.produtos_estoque[nome] = {'nome' : nome,'quantidade' : quantidade } 
                return 'Produto adicionado com sucesso'
            except:
                return 'Erro ao adicionar o produto ao sistema'
        else :
            return 'Esse produto não é fornecido por nenhum dos nossos fornecedors'
    def gerar_relatorio (self):
        try:
            print(Estoque.produtos_estoque)
        except:
            return 'Erro ao gerar relatorio'

class Produto ():
    produtos_disponiveis = []
    def __init__(self,nome,preco_unitario,codigo_produto):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.codigo_produto = codigo_produto
        if nome in Fornecedor.fornecedores['produto']:
            try:
                Produto.produtos_disponiveis.append(nome)
                return 'produto cadastrado com sucesso'
            except:
                return 'Erro ao cadastrar produto'
        else :
            return 'Esse produto não é fornecido por nenhum fornecedor'

class Categoria ():
    categorias = {}
    def __init__(self,nome_categoria,produto):
        self.nome_categoria = nome_categoria

        if produto in Produto.produtos_disponiveis :
            try :
                Categoria.categorias[produto] = {'Produto' : produto , 'categoria' : self.nome_categoria}

                return 'Produto adicionado a categoria com sucesso'
            except:
                return  'Erro a adicionar o produto a sua categoria correspondente'
        else:
            return 'Esse produto não existe'
        

class Fornecedor ():
    fornecedores = {}
    def __init__(self,nome_fornecedor,produtos_responsaveis,local):
        self.nome_fornecedor = nome_fornecedor
        self.produtos_responsaveis = produtos_responsaveis
        self.local = local
        try:
            Fornecedor.fornecedores[self.nome_fornecedor] = {'nome' : self.nome_fornecedor,'produto' : self.produtos_responsaveis,'local' : self.local}
            return 'Cadastro de fornecedores concluido com sucessdo'
        except :
            return 'Erro ao realizar o cadastro'


        
    