# mostra em tela uma previa do arquivo
def mostra_lista(lista):
    tamanho = len(lista)
    j = 0
    for i in range(0, tamanho):
        print('{}. {}'.format(j, lista[i]))
        j += 1


# grava um arquivo com cada posição da lista sendo uma linha
def grava(lista):
    arquivo = open('grava_lista.txt', 'w')
    for i in lista:
        arquivo.write(i)
        arquivo.write('\n')
    arquivo.close()


# continua uma lista ou monta coso a lista esteja vazia e ao terminar grava a lista em um arquivo
# sair grava a lista e para a construção da lista
# ler mostra a lista
# limpa deleta todos os elementos da lista
# delete vai retirar uma linha da lista
def continua_lista(lista):
    frase = input('digite um texto ou digite sair para sair, ler para mostrar em tela o '
                  'texto, limpa para limpar o texto e delete para deletar uma linha\n')
    while True:
        if frase == 'sair':
            break
        elif frase == 'ler':
            mostra_lista(lista)
        elif frase == 'limpa':
            lista.clear()
        elif frase == 'delete':
            try:
                linha = int(input('digite o numero da linha a ser deletada: '))
                if len(lista) > linha >= 0:
                    lista.pop(linha)
                else:
                    print('a linha escolida não existe')
            except ValueError:
                print('letras e frases não são aceitas')
        else:
            lista.append(frase)
        frase = input()
    return lista


# retorna uma lista de acordo com o arquivo grava_lista.txt
def monta_lista():
    # caso o arquivo no exista retorna uma lista vazia
    try:
        arquivo = open('grava_lista.txt', 'r')
        frase = arquivo.read()
        lista = frase.split('\n')
        # o arquivo é gravado com um \n a mais, que forma uma posição vazia na lista e essa condição tira ela
        if lista[len(lista) - 1] == '':
            lista.pop(len(lista) - 1)
        return lista
    except FileNotFoundError:
        return []


if __name__ == '__main__':
    lista_montada = monta_lista()
    lista_montada = continua_lista(lista_montada)
    grava(lista_montada)
