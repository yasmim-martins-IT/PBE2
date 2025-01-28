#exercicio 25
class Jogo_batalha () :
    personagens = {}
    def __init__(self,nome_jogo,idade_indicativa):
        self.nome_jogo = nome_jogo
        self.idade_indicativa = idade_indicativa
    def criar_personagens (self,nome,saude,forca,defesa,habilidade) :
        self.nome = nome
        self.saude = saude
        self.forca = forca
        self.defesa = defesa
        self.habilidade = habilidade
        
        if nome not in Jogo_batalha.personagens :

            Jogo_batalha.personagens[nome] = {'nome' : self.nome , 'saude' : self.saude , "força" : self.forca , 'defesa' : self.defesa , 'habilidade' : self.habilidade}
            return f'Personagem {nome} criado com sucesso'
        else :
            return f'Persongame {nome} já existe'
    def mostrar_personagens (self) :
        print(Jogo_batalha.personagens)
    