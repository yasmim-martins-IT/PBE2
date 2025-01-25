class Peca: #socorro ESQUECI DOS COMENTARIO DEMORE 3 HORAS NESSE
    def __init__(self, cor):
        self.cor = cor
        self.posicao = None

    def mover(self, nova_posicao, tabuleiro):
        raise NotImplementedError("Método 'mover' deve ser implementado por subclasses.")

class Peao(Peca):
    def __init__(self, cor):
        super().__init__(cor)
        self.primeiro_movimento = True

    def mover(self, nova_posicao, tabuleiro):
        if self.cor == 'branco':
            if nova_posicao[0] == self.posicao[0] and nova_posicao[1] == self.posicao[1] + 1:
                return True
            if self.primeiro_movimento and nova_posicao[0] == self.posicao[0] and nova_posicao[1] == self.posicao[1] + 2:
                return True
        else:
            if nova_posicao[0] == self.posicao[0] and nova_posicao[1] == self.posicao[1] - 1:
                return True
            if self.primeiro_movimento and nova_posicao[0] == self.posicao[0] and nova_posicao[1] == self.posicao[1] - 2:
                return True
        return False

    def capturar(self, nova_posicao, tabuleiro):

        if self.cor == 'branco' and nova_posicao[1] == self.posicao[1] + 1 and abs(nova_posicao[0] - self.posicao[0]) == 1:
            return True
        elif self.cor == 'preto' and nova_posicao[1] == self.posicao[1] - 1 and abs(nova_posicao[0] - self.posicao[0]) == 1:
            return True
        return False

    def promocao(self):
        if self.cor == 'branco' and self.posicao[1] == 7:
            return True
        elif self.cor == 'preto' and self.posicao[1] == 0:
            return True
        return False

class Torre(Peca):
    def mover(self, nova_posicao, tabuleiro):
        if nova_posicao[0] == self.posicao[0] or nova_posicao[1] == self.posicao[1]:
            return True
        return False

class Cavalo(Peca):
    def mover(self, nova_posicao, tabuleiro):
        if abs(nova_posicao[0] - self.posicao[0]) == 2 and abs(nova_posicao[1] - self.posicao[1]) == 1:
            return True
        if abs(nova_posicao[0] - self.posicao[0]) == 1 and abs(nova_posicao[1] - self.posicao[1]) == 2:
            return True
        return False

class Bispo(Peca):
    def mover(self, nova_posicao, tabuleiro):
        if abs(nova_posicao[0] - self.posicao[0]) == abs(nova_posicao[1] - self.posicao[1]):
            return True
        return False

class Rainha(Peca):
    def mover(self, nova_posicao, tabuleiro):
        if nova_posicao[0] == self.posicao[0] or nova_posicao[1] == self.posicao[1]:
            return True
        if abs(nova_posicao[0] - self.posicao[0]) == abs(nova_posicao[1] - self.posicao[1]):
            return True
        return False

class Rei(Peca):
    def __init__(self, cor):
        super().__init__(cor)
        self.roque_possivel = True

    def mover(self, nova_posicao, tabuleiro):
        if abs(nova_posicao[0] - self.posicao[0]) <= 1 and abs(nova_posicao[1] - self.posicao[1]) <= 1:
            return True
        return False

    def roque(self, torre, tabuleiro):
        if self.roque_possivel and torre.roque_possivel:
           
            return True
        return False

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = {}
        self.inicializar_tabuleiro()

    def inicializar_tabuleiro(self):
     
        for i in range(8):
            self.tabuleiro[(i, 1)] = Peao('preto')
            self.tabuleiro[(i, 6)] = Peao('branco')

        self.tabuleiro[(0, 0)] = Torre('preto')
        self.tabuleiro[(7, 0)] = Torre('preto')
        self.tabuleiro[(0, 7)] = Torre('branco')
        self.tabuleiro[(7, 7)] = Torre('branco')

        self.tabuleiro[(1, 0)] = Cavalo('preto')
        self.tabuleiro[(6, 0)] = Cavalo('preto')
        self.tabuleiro[(1, 7)] = Cavalo('branco')
        self.tabuleiro[(6, 7)] = Cavalo('branco')

        self.tabuleiro[(2, 0)] = Bispo('preto')
        self.tabuleiro[(5, 0)] = Bispo('preto')
        self.tabuleiro[(2, 7)] = Bispo('branco')
        self.tabuleiro[(5, 7)] = Bispo('branco')

        self.tabuleiro[(3, 0)] = Rainha('preto')
        self.tabuleiro[(3, 7)] = Rainha('branco')

        self.tabuleiro[(4, 0)] = Rei('preto')
        self.tabuleiro[(4, 7)] = Rei('branco')

    def mover_peca(self, posicao_origem, posicao_destino):
        if posicao_origem in self.tabuleiro:
            peca = self.tabuleiro[posicao_origem]
            if peca.mover(posicao_destino, self):
                self.tabuleiro[posicao_destino] = peca
                self.tabuleiro[posicao_origem] = None
                peca.posicao = posicao_destino
                return True
        return False

    def checar_xeque(self):
        
        return False

    def checar_xeque_mate(self):
     
        return False

tabuleiro = Tabuleiro()

tabuleiro.mover_peca((1, 6), (1, 4))

tabuleiro.mover_peca((1, 7), (3, 6))
