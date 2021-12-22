def converte_C(num):
    return num / 100


def converte_M(num):
    return num * 100


if __name__ == '__main__':
    numero = float(input("digite um numero a ser convertido: "))
    tipo = input("digite c caso a unidade esteja em centimetro e m para metro: ")
    if tipo == 'c' or tipo == 'C':
        numero = converte_C(numero)
        print('{} metros'.format(numero))
    elif tipo == 'm' or tipo == 'M':
        numero = converte_M(numero)
        print('{} centimetros'.format(numero))
    else:
        print('tipo não previsto')
