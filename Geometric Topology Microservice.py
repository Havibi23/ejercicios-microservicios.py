def clasificar_triangulo(a, b, c):
    if a + b + c != 180:
        return "No es un triángulo válido"
    
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        if a == 90 or b == 90 or c == 90:
            return "Isósceles con ángulo recto"
        return "Isósceles"
    else:
        if a == 90 or b == 90 or c == 90:
            return "Escaleno con ángulo recto"
        return "Escaleno"

# Ejemplo
print(clasificar_triangulo(60, 60, 60))   # Equilátero
print(clasificar_triangulo(90, 45, 45))   # Isósceles con ángulo recto