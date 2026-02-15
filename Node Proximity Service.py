import math

def distancia_proxima(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia < 10

# Ejemplo
print(distancia_proxima(0, 0, 3, 4))   # True (distancia 5)
print(distancia_proxima(0, 0, 10, 10)) # False (distancia ~14.14)