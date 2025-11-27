def calcular_factorial_recursivo(n):
    """
    Calcula el factorial de un número entero no negativo 'n' de forma recursiva.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    
    # Caso base: El factorial de 0 es 1. ¡Crucial para detener la recursión!
    if n == 0:
        return 1
    
    # Caso recursivo: n * factorial(n-1)
    else:
        return n * calcular_factorial_recursivo(n - 1)
