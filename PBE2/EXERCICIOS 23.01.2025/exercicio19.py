import random
#exercicio 19
class JogoAdivinhacao ():
    def __init__(self):
        self.numeros = random.random()
    def dar_palpite(self,palpite) :
        if self.numeros ==  palpite:
            return 'Parabens você ganhou'
        elif self.numeros > palpite:
            return 'O numero é mais alto'
        elif self.numeros < palpite:
            return 'O numero  é menor'
yasmim = JogoAdivinhacao()
print(yasmim.dar_palpite(0))