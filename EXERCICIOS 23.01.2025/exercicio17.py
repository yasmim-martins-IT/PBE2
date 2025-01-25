#exercicio 17
class Biblioteca():
    def __init__(self):
        self.livros ={}
        self.livros_emprestados = {}
    def cadastrar_livros (self,titulo,autor,genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

        try :
            self.livros[titulo] = {'titulo': self.titulo , 'autor' : self.autor ,'genero':self.genero}
            return f'Livro "{titulo}" foi cadastrado com sucesso '
        except:
            return 'Erro ao cadastrar o livro'
   
    def emprestar_livros(self, titulo):
        if titulo in self.livros:
            # Adiciona o livro emprestado ao dicionário de livros emprestados
            self.livros_emprestados[titulo] = self.livros.pop(titulo)
            return f'Livro "{titulo}" foi emprestado com sucesso'
        else:
            return f'Livro "{titulo}" não está disponível em nosso acervo'
    def devolver_livros(self, titulo):
        if titulo in self.livros_emprestados:
            # Adiciona o livro de volta ao acervo de livros
            self.livros[titulo] = self.livros_emprestados.pop(titulo)
            return 'Livro devolvido com sucesso'
        else:
            return 'Erro ao devolver o livro ou o livro não foi emprestado'
    def verificar_disponibilidade (self,titulo):
        if titulo in self.livros:
            return 'Livro disponivel para o emprestimo'
        else:
            return 'O livro está indisponivel no momento'
        
senai = Biblioteca()
print(senai.cadastrar_livros('Harry Potter e a Pedra filosofal','JC ROWCKIS','fantasia'))
print(senai.cadastrar_livros('pequenoprincipe','Antonie de Saint-Exupéry','fantasia'))
print(senai.verificar_disponibilidade('pequenoprincipe' ))
print(senai.verificar_disponibilidade('bela e a fera'))
print(senai.emprestar_livros('pequenoprincipe'))
print(senai.devolver_livros('pequenoprincipe'))

        