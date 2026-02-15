def fibonacci_backoff(n):
    a, b = 1, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# Ejemplo
for i in range(1, 8):
    print(f"Reintento {i}: esperar {fibonacci_backoff(i)}s")