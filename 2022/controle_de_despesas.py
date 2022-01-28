# estrutura de registros de qualque despesa ou receita
class Conta:
    def __init__(self, cod, receita_despesa, nome):
        self.codigo = cod
        self.valor = receita_despesa
        self.nome = nome


# cria uma lista de contas com todas as despesa e receitas
def lista_de_contas():
    contas = []
    while True:
        try:
            codigo = int(input("digite o codigo de sua conta ou numero negativo para terminar: "))
            break
        except ValueError:
            print("apenas numeros inteiros são aceitos")
    while codigo >= 0:
        while True:
            try:
                valor = float(input("digite o valor de sua conta: "))
                break
            except ValueError:
                print("esse valor não é aceito apenas numeros")
        nome = input('digite o nome de identificação da conta: ')
        contas.append(Conta(codigo, valor, nome))
        while True:
            try:
                codigo = int(input("digite o codigo de sua conta ou numero negativo para terminar: "))
                break
            except ValueError:
                print("apenas numeros inteiros são aceitos")
    return contas


# continua a colocar contas no entrato
def continua_lista_de_contas(contas):
    while True:
        try:
            codigo = int(input("digite o codigo de sua conta ou numero negativo para terminar: "))
            break
        except ValueError:
            print("apenas numeros inteiros são aceitos")
    while codigo >= 0:
        while True:
            try:
                valor = float(input("digite o valor de sua conta: "))
                break
            except ValueError:
                print("esse valor não é aceito apenas numeros")
        nome = input('digite o nome de identificação da conta: ')
        contas.append(Conta(codigo, valor, nome))
        while True:
            try:
                codigo = int(input("digite o codigo de sua conta ou numero negativo para terminar: "))
                break
            except ValueError:
                print("apenas numeros inteiros são aceitos")
    return contas


# mostra formatada o estrato
def mostrar_contas(contas):
    total = 0
    for conta in contas:
        print("codigo: {}".format(conta.codigo))
        print("nome: {}".format(conta.nome))
        print("valor: {}\n".format(conta.valor))
        total += conta.valor
    print("total: {}\n".format(total))


# deleta com base no codigo de uma conta na lista
def deleta_conta(contas, cod):
    tamanho = len(contas)
    i = 0
    while i < tamanho:
        if contas[i].codigo == cod:
            contas.pop(i)
            break
        i += 1
    if i == tamanho:
        print("o codigo {} não esta registrado".format(cod))
    else:
        print("conta removida")
    return contas


# função para alterações no estrato
def modificador():
    estrato = lista_de_contas()
    while True:
        escolha = input("para adicionar contas ao boleto digite (a) para retirar (r) para mostra o estrato (m) "
                        "ou (e) para finalizar o programa: ")
        if escolha == "a" or escolha == "A":
            estrato = continua_lista_de_contas(estrato)
        elif escolha == "r" or escolha == "R":
            escolha = int(input("digite o codigo da conta a ser deletada: "))
            deleta_conta(estrato, escolha)
        elif escolha == "m" or escolha == "M":
            mostrar_contas(estrato)
        elif escolha == "e" or escolha == "E":
            break
        else:
            print("não esta registrada essa alternativa")


if __name__ == '__main__':
    modificador()
