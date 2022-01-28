from poligonos import Area_retangulo, Area_triangulo

# retorna o volume de um paralelepipedo lado1 e lado2 de um retangulo
Volume_paralelepipedo = lambda lado1, lado2, altura: Area_retangulo(lado1, lado2) * altura
# retorna o volume de uma piramide de base triangular equilatera
Volume_piramide = lambda lado, altura: Area_triangulo(lado) * altura
