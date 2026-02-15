def checksum_par(mensaje):
    suma = sum(ord(c) for c in mensaje)
    return suma % 2 == 0

# Ejemplo
print(checksum_par("Hola"))   # Depende de los valores ASCII
print(checksum_par("abc"))