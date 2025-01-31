import math
#exercicio 1

class Circulo (): #classe de circulo
    def __init__(self,raio): #metodo construtor com o atributo que armazena o raio
        self.raio = raio #variavel do raio
    def calcular_area(self): # metodo que calcula a area
        area = self.raio**2 *math.pi #calcula a area do triangulo
        area_formatada = "{:.2f}".format(area) #formata a variavel area e armazena
        return area_formatada
    def calcular_perimetro(self):
        perimetro = (self.raio*2)*math.pi
        perimetro_formatado = "{:.2f}".format(perimetro)
        return perimetro_formatado
pizza = Circulo(5)

print(f'valor da area:',pizza.calcular_area(),'\nvalor do perimetro:',pizza.calcular_perimetro()) #calculo do perimetro da pizza