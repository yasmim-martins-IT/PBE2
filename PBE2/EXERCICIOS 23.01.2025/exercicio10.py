#exercicio 10
class Livro(): #classe  que representa o livro
    def __init__(self,titulo,autor,numeros_paginas): #metodo construtor
        self.titulo = titulo
        self.autor = autor
        self.numeros_paginas = numeros_paginas
        self.livro_armazenado = True
    def emprestar_livro(self): #metodo de emprestar o livros
        try: #tratamento de erros, caso seja sucesso
            self.livro_armazenado = False

            return f"livro '{self.titulo}' foi emprestado com sucesso!"
        except:#caso ocorra um erro
            return f'Erro ao emprestar o livro'

        
    
    def devolver_livro (self): #metrodo de devover o livro
        try :
            self.livro_armazenado = True
            return f"livro '{self.titulo}' devolvido com sucesso!"
        except:
            return f'Erro ao devolver o livro'
        

livro = Livro('Harry Potter e a Pedra Filosofal','JC ROWLISS',350)

print(livro.emprestar_livro())

print(livro.devolver_livro())
