def limite_peticiones(tipo_usuario, mantenimiento):
    if mantenimiento:
        return 0
    if tipo_usuario == "Premium":
        return 1000
    elif tipo_usuario == "Standard":
        return 100
    else:
        return 0  # tipo no reconocido

# Ejemplo
print(limite_peticiones("Premium", False))   # 1000
print(limite_peticiones("Standard", True))   # 0