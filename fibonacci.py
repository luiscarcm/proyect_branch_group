def fibonacci(n):
    """
    Calcula la serie de Fibonacci hasta n términos.
    Parámetro:
        n (int): cantidad de términos de la serie
    Retorna:
        list: lista con la serie de Fibonacci
    """
    serie = []
    a, b = 0, 1
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie
