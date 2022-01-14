# inicia a classe
class Calcula:
    # inicia as variaveis
    def __init__(self, a, b):
        self.valor_a = a
        self.valor_b = b

    # metodos da classe
    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicasao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b


# testa os metodos
if __name__ == '__main__':
    numeros = Calcula(15, 20)
    print('valores a serem usados nas contas\n{}'.format(numeros.valor_a))
    print('{}'.format(numeros.valor_b))
    print('soma: {}'.format(numeros.soma()))
    print('subtração: {}'.format(numeros.subtracao()))
    print('multiplicasão: {}'.format(numeros.multiplicasao()))
    print('divisão: {}'.format(numeros.divisao()))
