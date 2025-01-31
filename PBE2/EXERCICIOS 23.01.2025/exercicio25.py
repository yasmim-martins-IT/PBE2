import time

class Jogo_batalha():
    personagens = {}

    def __init__(self, nome_jogo, idade_indicativa):
        self.nome_jogo = nome_jogo
        self.idade_indicativa = idade_indicativa

    def criar_personagens(self, nome, saude, forca, defesa, habilidade):
        self.nome = nome
        self.saude = saude
        self.forca = forca
        self.defesa = defesa
        self.habilidade = habilidade
        
        if nome not in Jogo_batalha.personagens:
            Jogo_batalha.personagens[nome] = {'nome': self.nome, 'saude': self.saude, 'forca': self.forca, 'defesa': self.defesa, 'habilidade': self.habilidade}
            return f'Personagem {nome} criado com sucesso'
        else:
            return f'Personagem {nome} já existe'

    def mostrar_personagens(self):
        print(Jogo_batalha.personagens)

    def batalhar(self, nome1, nome2):
        if nome1 in Jogo_batalha.personagens and nome2 in Jogo_batalha.personagens:
            print(f'Atributos dos personagens: \n{Jogo_batalha.personagens[nome1]} \n {Jogo_batalha.personagens[nome2]} ')
            print('\nVai se iniciar a batalha em:')
            time.sleep(1)
            for i in range(0, 5):
                print(i, end=' ')
            print('LUTEM')

            while True:
              
                forca1 = Jogo_batalha.personagens[nome1]['forca']
                forca2 = Jogo_batalha.personagens[nome2]['forca']

                if forca1 >= forca2:
                    dano = forca1 - Jogo_batalha.personagens[nome2]['defesa']
                    Jogo_batalha.personagens[nome2]['saude'] -= max(0, dano)  
                else:
                    dano = forca2 - Jogo_batalha.personagens[nome1]['defesa']
                    Jogo_batalha.personagens[nome1]['saude'] -= max(0, dano)

                print(f'Resultados do round: \n{nome1}: Saúde = {Jogo_batalha.personagens[nome1]["saude"]} '
                      f'\n{nome2}: Saúde = {Jogo_batalha.personagens[nome2]["saude"]}')
                
                if Jogo_batalha.personagens[nome1]['saude'] <= 0:
                    print(f'{nome2} venceu!')
                    break
                elif Jogo_batalha.personagens[nome2]['saude'] <= 0:
                    print(f'{nome1} venceu!')
                    break

jogo = Jogo_batalha("Batalha Final", 12)

print(jogo.criar_personagens("Guerreiro", 100, 20, 5, 10))
print(jogo.criar_personagens("Mago", 80, 25, 3, 15))

jogo.mostrar_personagens()

jogo.batalhar("Guerreiro", "Mago")

    