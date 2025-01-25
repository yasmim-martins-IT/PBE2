#exercio 18
import calendar
from datetime import datetime
class Calendario :
    def __init__(self,ano):
        self.ano = ano
        self.feriados  = [(1,1),(7,9),(21,4),(31,12),(1,5),(15,11),]

    def exibir_calendario(self,mes):
        if 1 <= mes and mes <=12:
            print(calendar.month(self.ano,mes))
        else:
            print('Esse mes não está presente no sistema de calendario gregoriano')
        
  
    def verificar_feriado(self, data):
        try:
            dia, mes = map(int, data.split('/'))
            if (dia, mes) in self.feriados:
                return 'É feriado'
            else:
                return 'Não é feriado'
        except ValueError:
            return 'Formato de data inválido. '
    def calcular_diferenca(self, data1, data2):
        try:
            data1 = datetime.strptime(data1, "%d/%m/%Y")
            data2 = datetime.strptime(data2, "%d/%m/%Y")
            diferenca = abs((data2 - data1).days)  # Diferença absoluta em dias
            return f'A diferença entre {data1.strftime("%d/%m/%Y")} e {data2.strftime("%d/%m/%Y")} é de {diferenca} dias.'
        except ValueError:
            return 'Formato de data inválido. '


calendario = Calendario(2025)

calendario.exibir_calendario(12)


print(calendario.verificar_feriado("01/01")) 
print(calendario.verificar_feriado("07/09"))  
print(calendario.verificar_feriado("25/12"))  
print(calendario.verificar_feriado("31/08"))  

print(calendario.calcular_diferenca("24/01/2025", "23/08/2025"))
    