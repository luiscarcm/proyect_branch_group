# ====================================================================
# Algoritmos Matemáticos (Implementación de Funciones)
# ====================================================================

import os
#1 -- Calcula el n-ésimo número de Fibonacci.
from fibonacci import fibonacci   # Importamos la función desde fibonacci.py

def limpiar_pantalla():
    # Para Windows
    if os.name == "nt":
        os.system("cls")
    # Para Linux / Mac
    else:
        os.system("clear")

#3 -- Determina si un número es primo.
from feature_primos import es_primo

#2 -- Calcula el factorial de un número.
from factorial import calcular_factorial_recursivo

#4 -- Verifica si un número es perfecto.
def generar_numeros_perfectos(limite: int) -> list:
    perfectos = []

    for num in range(2, limite + 1):
        suma_divisores = 0
        
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                suma_divisores += i
                otro = num // i
                if otro != i and otro != num:
                    suma_divisores += otro
        
        if suma_divisores == num:
            perfectos.append(num)

    return perfectos

#5 -- Genera el número invertido de un número dado.
def generar_numero_invertido(n):
    numero_str = str(abs(n))
    numero_invertido_str = numero_str[::-1]
    numero_invertido = int(numero_invertido_str)
    if n < 0:
        return -numero_invertido
    else:
        return numero_invertido

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
            #n = obtener_entrada("Ingrese el valor de N para conocer el número de la serie Fibonacci: ")
            #resultado = calcular_fibonacci(n)
            #print("////////////////////////////////////////////////////////")
            #print(f"El número de Fibonacci en la posición {n} es: {resultado}")
            #print("////////////////////////////////////////////////////////")
            while True:
                limpiar_pantalla()
                print("=== Serie de Fibonacci ===")
                try:
                    n = int(input("Ingrese el número de términos que desea calcular: "))
                    if n <= 0:
                        print("Por favor ingrese un número entero positivo.")
                    else:
                        resultado = fibonacci(n)
                        print(f"Los primeros {n} términos de la serie Fibonacci son:")
                        print(resultado)
                except ValueError:
                    print("Entrada inválida. Debe ingresar un número entero.")
                # Preguntar si desea continuar
                opcion = input("¿Desea calcular otra serie? (s/n): ").strip().lower()
                limpiar_pantalla()
                if opcion != "s":
                    limpiar_pantalla()
                    break
                

        
        elif opcion == '2': # Factorial
            n = obtener_entrada("Ingrese el número para calcular el Factorial: ")
            resultado = calcular_factorial_recursivo(n)
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
            n = obtener_entrada("Ingrese un número para conocer los números perfectos (N): ")
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