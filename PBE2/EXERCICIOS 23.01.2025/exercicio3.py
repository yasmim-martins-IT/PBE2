#exercicio 3

class Retangulo(): #classe retangulo
    def __init__(self, altura, largura): #metodo contrutor
        self.altura = altura
        self.largura = largura

    def area_retangulo(self): #metodo que calcula a area do retangulo
        area = self.altura * self.largura #calculo da area
        return area

    def perimetro_retangulo(self):#metodo que calcua a area do retangulo
        perimetro = (self.altura * 2) + (self.largura * 2) #calculo do perimeto
        return perimetro

retangulo1 = Retangulo(5, 2)

print(retangulo1.area_retangulo())  # Área do retângulo
print(retangulo1.perimetro_retangulo())  # Perímetro do retângulo
