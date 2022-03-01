import time
from Data import dataFormatada

# retorna a hora local no formato hh:mm
horaFormatada = lambda: (time.strftime('%H:%M', time.localtime()))


# retorna a hora local em minutos
def horaEmMinutos ():
    hora = int(time.strftime('%H', time.localtime()))
    return hora * 60 + int(time.strftime('%M', time.localtime()))


# retorna a hora local em segundos
horaEmSegundos = lambda: horaEmMinutos() * 60


# retorna data seguida de hora
def dataHora():
    data = dataFormatada()
    hora = horaFormatada()
    return data + "  " + hora


if __name__ == "__main__":
    print("testes")
    print("data e hora = {}".format(dataHora()))
    print("hora = {}".format(horaFormatada()))
    print("tempo em minutos = {}".format(horaEmMinutos()))
    print("tempo em segundos = {}".format(horaEmSegundos()))
