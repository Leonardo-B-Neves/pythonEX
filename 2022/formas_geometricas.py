# testa as funções dos arquivos poligonos.py e volume_de_poligonos.py
import poligonos
import volume_de_poligonos
if __name__ == '__main__':
    lado1 = 10
    lado2 = 20
    altura = 10
    print('area do retangulo {} , {} = {}'.format(lado1, lado2, poligonos.Area_retangulo(lado1, lado2)))
    volume_paralelepipedo = volume_de_poligonos.Volume_paralelepipedo(lado1, lado2, altura)
    print('volume desse retangulo com altura {} = {}'.format(altura, volume_paralelepipedo))
    volume_piramide = volume_de_poligonos.Volume_piramide(lado1, altura)
    print('area do triangulo de lados {} = {}'.format(lado1, poligonos.Area_triangulo(lado1)))
    print('volume de uma piramide de altura {} = {}'.format(altura, volume_de_poligonos.Volume_piramide(lado1, altura)))
    print('area de um circulo1 de raio {} = {}'.format(lado1, poligonos.Area_circulo(lado1)))
    print('area de um circulo2 de raio {} = {}'.format(lado2, poligonos.Area_circulo(lado2)))
