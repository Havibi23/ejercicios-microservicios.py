def fibonacci(n):
    a, b = 0, 1
    serie = []
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie

def calcular(operacion, num1, num2=None):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        return num1 / num2 if num2 != 0 else "Error: división por cero"
    elif operacion == "fibonacci":
        return fibonacci(int(num1))
    elif operacion == "conversion":
        return f"Binario: {bin(num1)[2:]}, Hexadecimal: {hex(num1)[2:]}"
    else:
        return "Operación no soportada"

# Ejemplo
print(calcular("suma", 5, 3))
print(calcular("fibonacci", 7))
print(calcular("conversion", 255))