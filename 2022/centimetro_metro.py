# converte centimetro para metro
def converte_C(num):
    return num / 100


# converte metro em centimetro
def converte_M(num):
    return num * 100


if __name__ == '__main__':
    # registra o numero
    numero = float(input("digite um numero a ser convertido: "))
    # regitra o formato do numero
    tipo = input("digite c caso a unidade esteja em centimetro e m para metro: ")
    # verifica se esta em centimetro, metro ou fora de formato
    if tipo == 'c' or tipo == 'C':
        numero = converte_C(numero)
        print('{} metros'.format(numero))
    elif tipo == 'm' or tipo == 'M':
        numero = converte_M(numero)
        print('{} centimetros'.format(numero))
    else:
        print('tipo não previsto')
