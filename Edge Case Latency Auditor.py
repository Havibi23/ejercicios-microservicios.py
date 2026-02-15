def alerta_latencia(tiempos, umbral):
    promedio = sum(tiempos) / len(tiempos)
    if promedio > umbral:
        return True
    for t in tiempos:
        if t > 3 * promedio:
            return True
    return False

# Ejemplo
latencia = [100, 200, 300, 1000, 150]
print(alerta_latencia(latencia, 250))  # True (porque 1000 > 3*promedio)