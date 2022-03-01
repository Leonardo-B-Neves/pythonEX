from datetime import date


# retorna o nome do dia da semana
def diaDaSemana():
    semana = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo")
    data = date.today()
    diaNumero = data.weekday()
    diaSemana = semana[diaNumero]
    return diaSemana


# retorna o nome do mes
def nomeMes():
    meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio",
             "Junho", "Julho", "Agosto", "Setembro", "Outubro",
             "Novembro", "Dezembro")
    data = date.today()
    return meses[data.month]


# retorna a data no formato dia/mes/anoCompleto
def dataFormatada():
    data = date.today()
    return data.strftime("%d/%m/%Y")


if __name__ == "__main__":
    print("testes")
    print("data: " + dataFormatada())
    print("mes: " + nomeMes())
    print("dia: " + diaDaSemana())
