import random

class JogoCartas():
    def __init__(self):
        self.cartas = [1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6]
        self.jogadores = {}
        self.turno = 0
        self.pilha_cartas = []
        self.lista_jogadores = []

    def embaralhar_cartas(self):
        random.shuffle(self.cartas)  # Apenas embaralha a lista

        return 'Cartas embaralhadas com sucesso'

    def distribuir_cartas(self, quantidade_jogadores):
        try:
            self.quantidade_jogadores = quantidade_jogadores

            total_cartas = len(self.cartas) 
            self.cartas_por_jogador = total_cartas // quantidade_jogadores

            for i in range(quantidade_jogadores):
                jogador = f'jogador {i+1}'
                self.jogadores[jogador] = {'cartas': []}
                self.lista_jogadores.append(jogador)

            for jogador in self.jogadores:
                for j in range(self.cartas_por_jogador):
                    if self.cartas:
                        carta = self.cartas.pop()
                        self.jogadores[jogador]['cartas'].append(carta)
            return 'Cartas distribuidas com sucesso'

        except Exception as e:
            return f'Erro ao distribuir cartas: {str(e)}'

    def mostrar_cartas(self):
        for i, j in self.jogadores.items():
            print(f'{i} : {j["cartas"]}')

    def jogar_carta(self, jogador, carta_jogada):
        if jogador not in self.jogadores: 
            return 'Esse jogador não está jogando essa rodada'
        if carta_jogada not in self.jogadores[jogador]['cartas']:
            return 'Essa carta não está no seu baralho'

        self.pilha_cartas.append(carta_jogada)
        self.jogadores[jogador]['cartas'].remove(carta_jogada)

        print(f'{jogador} jogou a carta {carta_jogada}')

    def turno_seguinte(self):
        if len(self.lista_jogadores) == 0:
            return 'Não há jogadores para jogar'
        
        self.turno += 1
        jogador_atual = self.lista_jogadores[self.turno % len(self.lista_jogadores)]

        return f'vez do {jogador_atual}'

    def visualizar_jogo(self):
        print(f'turno : {self.turno}')
        print('cartas dos jogadores')

        for i, j in self.jogadores.items():
            print(f'{i} : {j["cartas"]}')

# Teste
yasmim = JogoCartas()
print(yasmim.embaralhar_cartas())
print(yasmim.distribuir_cartas(2))
print(yasmim.mostrar_cartas())
print(yasmim.turno_seguinte())
print(yasmim.visualizar_jogo())
