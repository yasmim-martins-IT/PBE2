#exercicio 7

class Triangulo(): #classe triangulo
    def __init__(self,lado1,lado2,lado3,base,altura): #metodo construtor
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura
    def verificar_triangulo(self): #função que verifica o triangulo
        if self.lado1 + self.lado2 >3 and self.lado1+self.lado3 > self.lado2 and self.lado2 > self.lado3 > self.lado1:
            triangulo = True #declara como verdade  que ele é um triangulo
            return triangulo #retorna o valor da variavel
        else:
            triangulo = False
            return triangulo
    def calcular_area(self):#função que calcula area do triangulo
        if self.base == 0 and self.altura == 0 :
            area_triangulo = (self.base * self.altura)//2 #calculo da area do triangulo
            return area_triangulo #retorna o valor a area
        else: 
            return "Base ou altura invalidas"

triangulo = Triangulo(7,6,4,6,4)

if triangulo.verificar_triangulo(): #verifica se é um triangulo
    print(f'a area do triangulo é {triangulo.calcular_area()}') #imprime a area do usuário
else:
    print('valores invalidos para fazer esses calculos') #resposta ao usuario em caso de erro