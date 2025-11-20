# ====================================================================
# Algoritmos Matemáticos (Implementación de Funciones)
# ====================================================================

#1 -- Calcula el n-ésimo número de Fibonacci.
def calcular_fibonacci(n):
    #aqui va la el algoritmo
    return n

#2 -- Calcula el factorial de un número.
def calcular_factorial(n):
    #aqui va la el algoritmo
    return n

#3 -- Determina si un número es primo.
def es_primo(n):
    #aqui va la el algoritmo
    return n

#4 -- Verifica si un número es perfecto.
def generar_numeros_perfectos(n):
    #aqui va la el algoritmo
    return n

#5 -- Genera el número invertido de un número dado.
def generar_numero_invertido(n):
    #aqui va la el algoritmo
    return n

#6 -- Calcula el n-ésimo número de la serie Lucas.
def calcular_lucas(n):
    # Validar que n no sea negativo
    if n < 0:
        print("El número debe ser mayor o igual a 0.")
        return None

    # Casos básicos de la serie de Lucas
    if n == 0:
        return 2
    if n == 1:
        return 1

    # Para n >= 2 usamos un ciclo sencillo
    anterior = 2  # L(0)
    actual = 1    # L(1)

    # Recorremos desde 2 hasta n
    for i in range(2, n + 1):
        siguiente = anterior + actual
        anterior = actual
        actual = siguiente

    # Al final, en "actual" queda L(n)
    return actual

# ====================================================================
# Menú Principal (Implementado por Luis Carlos Cabezas)
# ====================================================================

def mostrar_menu():
    """Muestra las opciones del menú."""
    print("---------------------------------------------------------------")
    print("\n--- Taller Colaborativo Git: Algoritmos Matemáticos ---")
    print("---------------------------------------------------------------")
    print("1. Cálculo de Fibonacci")
    print("2. Cálculo del Factorial")
    print("3. Determinar si un número es Primo")
    print("4. Generar la serie de N números Perfectos")
    print("5. Generar el número invertido de un número")
    print("6. Cálculo de la serie de Lucas")
    print("7. Salir")
    print("---------------------------------------------------------------")

def obtener_entrada(mensaje):
    """Función helper para obtener entrada y manejar errores básicos."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

def main():
    """Función principal que ejecuta el menú de opciones."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        if opcion == '1': # Fibonacci
            n = obtener_entrada("Ingrese el valor de N para conocer el número de la serie Fibonacci: ")
            resultado = calcular_fibonacci(n)
            print("////////////////////////////////////////////////////////")
            print(f"El número de Fibonacci en la posición {n} es: {resultado}")
            print("////////////////////////////////////////////////////////")
        
        elif opcion == '2': # Factorial
            n = obtener_entrada("Ingrese el número para calcular el Factorial: ")
            resultado = calcular_factorial(n)
            print("////////////////////////////////////////////////////////")
            print(f"El Factorial de {n} es: {resultado}")
            print("////////////////////////////////////////////////////////")

        elif opcion == '3': # Primos
            n = obtener_entrada("Ingrese el número a verificar si es Primo: ")
            resultado = es_primo(n)
            estado = "es Primo" if resultado else "NO es Primo"
            print("////////////////////////////////////////////////////////")
            print(f"El número {n} {estado}.")
            print("////////////////////////////////////////////////////////")
            
        elif opcion == '4': # Números Perfectos
            n = obtener_entrada("Ingrese cuántos números Perfectos desea generar (N): ")
            resultado = generar_numeros_perfectos(n)
            print("////////////////////////////////////////////////////////")
            print(f"Los primeros {n} números perfectos son: {resultado}")
            print("////////////////////////////////////////////////////////")

        elif opcion == '5': # Número Invertido
            n = obtener_entrada("Ingrese un número para generar su invertido: ")
            resultado = generar_numero_invertido(n)
            print("////////////////////////////////////////////////////////")
            print(f"Los primeros {n} números perfectos son: {resultado}")
            print("////////////////////////////////////////////////////////")

        elif opcion == '6': # Serie Lucas
            n = obtener_entrada("Ingrese el valor de N para conocer el número la serie Lucas: ")
            resultado = calcular_lucas(n)
            print("////////////////////////////////////////////////////////")
            print(f"El número de la serie Lucas en la posición {n} es: {resultado}")
            print("////////////////////////////////////////////////////////")
            
        elif opcion == '7': # Salir
            print("////////////////////////////////////////////////////////")
            print("Saliendo del programa. ¡Adiós!")
            print("////////////////////////////////////////////////////////")
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()