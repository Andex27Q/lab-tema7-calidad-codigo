
import math

def area_circulo(radio):
    return math.pi * radio ** 2

def area_rectangulo(base, altura):
    return base * altura

if __name__ == "__main__":
    print("Área del círculo (r=3):", round(area_circulo(3), 2))
    print("Área del rectángulo (4x5):", area_rectangulo(4, 5))

def area_triangulo(base, altura):
    return base * altura / 2