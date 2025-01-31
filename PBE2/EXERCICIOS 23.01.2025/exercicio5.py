#exercicio 5 

class Funcionario():#classe funcionario
    def __init__(self,nome,cargo_funcionario,salario): #metodo construtor
        self.nome = nome
        self.cargo_funcionario = cargo_funcionario
        self.salario = salario
    def calcular_salarioLiquido (self,impostos,beneficios): #calcula o salario liquido
        self.impostos = impostos
        self.beneficios = beneficios

        self.salario -= self.impostos #calcula o salario descontando os impostos
        self.salario -= self.beneficios #calcula o salario descontando os beneficio

        return self.salario
#chamando a classe
funcionario1 = Funcionario('yasmim','jovem aprendiz',1480)

print(f'o salario liquido da {funcionario1.nome} é: {funcionario1.calcular_salarioLiquido(20,150)}')