import numpy as np

def area_triangulo(base, altura):
    base = np.array(base, dtype=float)
    altura = np.array(altura, dtype=float)
    return np.divide(np.multiply(base, altura), 2)


def area_rectangulo(base, altura):
    base = np.array(base, dtype=float)
    altura = np.array(altura, dtype=float)
    return np.multiply(base, altura)


def area_circulo(radio):
    radio = np.array(radio, dtype=float)
    return np.multiply(np.pi, np.power(radio, 2))
