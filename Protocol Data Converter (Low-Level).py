def decimal_a_binario(n):
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        residuo = n % 2
        binario = str(residuo) + binario
        n = n // 2
    return binario

def decimal_a_hexadecimal(n):
    if n == 0:
        return "0"
    digitos = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        residuo = n % 16
        hexadecimal = digitos[residuo] + hexadecimal
        n = n // 16
    return hexadecimal

num = 255
print(decimal_a_binario(num))      # 11111111
print(decimal_a_hexadecimal(num))  # FF