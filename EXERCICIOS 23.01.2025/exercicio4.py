#exercicio 4
class Aluno (): #classe abastrata Aluno
    def __init__(self,nome,matriculo,notas ): #metodo construtor
        self.nome = nome 
        self.matriculo = matriculo
        self.notas = notas #é uma lista
    
    def calcular_media (self): #metodo de calcular as notas
        soma_notas = 0
        for nota in self.notas : #percorre toda a lista
            soma_notas += nota #soma as notas

        media = soma_notas/len(notas)

        print(f'a media de {self.nome} é : {media}') #retorna o valor da media
    
        if media >= 5: #verificando se a nota foi suficiente para aprovar o aluno
            #resporta ao usuario
            return (f"o aluno(a) {self.nome} foi aprovado")
        else :
            #reposta ao usuario
            return (f'o aluno(a) {self.nome} foi reprovado!!!')


notas = [100,100,100,100]
Aluno1 = Aluno('yasmim','68688686',notas)

print(Aluno1.calcular_media())
