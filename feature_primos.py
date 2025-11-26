def es_primo(n):
    """
    Determina si un número entero n es primo.
    Un número es primo si es mayor que 1 y solo tiene dos divisores: 1 y sí mismo.
    Optimizado: solo comprueba divisores hasta la raíz cuadrada de n.
    """
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

if __name__ == "__main__":
    # Ejemplo de uso
    for num in range(1, 21):
        print(f"{num} es primo?: {es_primo(num)}")
