def validar_token(token):
    if len(token) <= 12:
        return False
    if not any(c.isdigit() for c in token):
        return False
    if token.startswith("TEST"):
        return False
    return True

# Ejemplo
print(validar_token("Token12345678"))    # True
print(validar_token("TEST12345678"))     # False