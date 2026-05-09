
'''
EJERCICIO DE PROGRAMACIÓN INTERMEDIA - FUNCIONES

El ejercicio consite en la implementación de una calculadora que permita realizar las siguientes 
operaciones: 

1. Sumar Dos Números
2. Restar Dos Números
3. Multiplicar Dos Números
4. Dividir Dos Números
5. Calcular el factorial de un número
6. Calcular la potencia de un número elevado a otro

Para la implementación del ejercicio vamos a utilizar las siguientes funciones:

Función Sumar: se encargará de realizar todo el proceso de suma, incluyendo la solicitud de los 
dos números al usuario que se van a sumar.

Función Restar: se encargará de realizar todo el proceso de resta, incluyendo la solicitud del minuendo
y el sustraendo al usuario.

Función Multiplicar: se encargará de realizar todo el proceso de multiplicación, incluyendo la solicitud
de los factores al usuario.

Función Dividir: se encargará de realizar todo el proceso de división, incluyendo la solicitud del dividendo
y el divisor al usuario. Validar que no se realice una división por cero.

Función Factorial: Se encargará de solicitar el número del que se quiere calcular el factorial.
Una Vez tenga el numero invocará a la función de calcular factorial, validar que el número sea positivo 
y entero.

Función FactorialCalculo: función recursiva que se realiza en el cálculo del factorial del número que 
recibe por parámetro.

Función Potencia: se encargará de solicitar la base y el exponente al usuario e invocará a la 
función de calcular potencia,validar que el exponente sea un número entero.

Función PotenciaCalculo: función recursiva que se realiza en el cálculo de la potencia de los números
pasados como parámetros.

Función Calculadora: función principal que se encargará de mostrar el menú de opciones al usuario, 
solicitar la opción deseada y llamar a la función correspondiente según la opción seleccionada. 
La función debe continuar mostrando el menú hasta que el usuario decida salir.

Importante: tanto el menú como los mensajes de solicitud de datos y resultados deben ser claros 
y amigables para el usuario, y se deben manejar adecuadamente los casos de error, como la división 
por cero o la entrada de datos no válidos.

Utilizar diseño de Interfaz de Usuario mediante la consola utilizando ASCII Art para hacer el menú 
más atractivo visualmente.

Solución del Ejercicio:
'''

import os
import time

# ==========================================
# INTERFAZ DE USUARIO Y ARTE ASCII
# ==========================================

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_encabezado():
    """Muestra el arte ASCII de la calculadora."""
    limpiar_pantalla()
    print("""
    ╔═════════════════════════════════════════════════╗
    ║  _____________________________________________  ║
    ║ |  _________________________________________  | ║
    ║ | |                                         | | ║
    ║ | |          CALCULADORA AVANZADA           | | ║
    ║ | |          Funciones y Recursión          | | ║
    ║ | |_________________________________________| | ║
    ║ |  ___ ___ ___   ___   ___________________    | ║
    ║ | | 7 | 8 | 9 | | + | | (!) Factorial     |   | ║
    ║ | |___|___|___| |___| | (^) Potencia      |   | ║
    ║ | | 4 | 5 | 6 | | - | |___________________|   | ║
    ║ | |___|___|___| |___|                         | ║
    ║ | | 1 | 2 | 3 | | x |   [ Menú Principal ]    | ║
    ║ | |___|___|___| |___|                         | ║
    ║ | | . | 0 | = | | / |                         | ║
    ║ | |___|___|___| |___|                         | ║
    ║ |_____________________________________________| ║
    ╚═════════════════════════════════════════════════╝
    """)

# ==========================================
# FUNCIONES MATEMÁTICAS RECURSIVAS
# ==========================================

def FactorialCalculo(n):
    """Calcula el factorial de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * FactorialCalculo(n - 1)

def PotenciaCalculo(base, exponente):
    """Calcula la potencia de forma recursiva."""
    if exponente == 0:
        return 1
    elif exponente > 0:
        return base * PotenciaCalculo(base, exponente - 1)
    else:
        # Maneja exponentes negativos (b^-n = 1 / b^n)
        return 1 / (base * PotenciaCalculo(base, abs(exponente)))

# ==========================================
# FUNCIONES DE OPERACIÓN INTERACTIVAS
# ==========================================

def Sumar():
    print("\n--- OPERACIÓN: SUMA ---")
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"\n[✔] El resultado de la suma es: {resultado}")
    except ValueError:
        print("\n[✘] Error: Por favor ingrese valores numéricos válidos.")
    input("\nPresione ENTER para continuar...")

def Restar():
    print("\n--- OPERACIÓN: RESTA ---")
    try:
        minuendo = float(input("Ingrese el minuendo: "))
        sustraendo = float(input("Ingrese el sustraendo: "))
        resultado = minuendo - sustraendo
        print(f"\n[✔] El resultado de la resta es: {resultado}")
    except ValueError:
        print("\n[✘] Error: Por favor ingrese valores numéricos válidos.")
    input("\nPresione ENTER para continuar...")

def Multiplicar():
    print("\n--- OPERACIÓN: MULTIPLICACIÓN ---")
    try:
        factor1 = float(input("Ingrese el primer factor: "))
        factor2 = float(input("Ingrese el segundo factor: "))
        resultado = factor1 * factor2
        print(f"\n[✔] El resultado de la multiplicación es: {resultado}")
    except ValueError:
        print("\n[✘] Error: Por favor ingrese valores numéricos válidos.")
    input("\nPresione ENTER para continuar...")

def Dividir():
    print("\n--- OPERACIÓN: DIVISIÓN ---")
    try:
        dividendo = float(input("Ingrese el dividendo: "))
        divisor = float(input("Ingrese el divisor: "))
        
        if divisor == 0:
            print("\n[✘] Error Matemático: No es posible dividir por cero.")
        else:
            resultado = dividendo / divisor
            print(f"\n[✔] El resultado de la división es: {resultado}")
    except ValueError:
        print("\n[✘] Error: Por favor ingrese valores numéricos válidos.")
    input("\nPresione ENTER para continuar...")

def Factorial():
    print("\n--- OPERACIÓN: FACTORIAL ---")
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print("\n[✘] Error: El factorial no está definido para números negativos.")
        else:
            resultado = FactorialCalculo(numero)
            print(f"\n[✔] El factorial de {numero}! es: {resultado}")
    except ValueError:
        print("\n[✘] Error: Debe ingresar un número ENTERO válido.")
    input("\nPresione ENTER para continuar...")

def Potencia():
    print("\n--- OPERACIÓN: POTENCIA ---")
    try:
        base = float(input("Ingrese el número base: "))
        exponente = int(input("Ingrese el exponente (debe ser un número entero): "))
        
        # Validar el caso de 0 elevado a 0 o a un número negativo
        if base == 0 and exponente <= 0:
            print("\n[✘] Error: Cero elevado a cero o a un exponente negativo no está definido.")
        else:
            resultado = PotenciaCalculo(base, exponente)
            print(f"\n[✔] {base} elevado a la {exponente} es: {resultado}")
    except ValueError:
        print("\n[✘] Error: Asegúrese de que la base sea un número y el exponente un ENTERO.")
    input("\nPresione ENTER para continuar...")

# ==========================================
# FUNCIÓN PRINCIPAL (MAIN LOOP)
# ==========================================

def Calculadora():
    """Función principal que controla el flujo del programa."""
    while True:
        mostrar_encabezado()
        print("Seleccione la operación que desea realizar:\n")
        print("  [ 1 ] Sumar dos números")
        print("  [ 2 ] Restar dos números")
        print("  [ 3 ] Multiplicar dos números")
        print("  [ 4 ] Dividir dos números")
        print("  [ 5 ] Calcular el factorial de un número")
        print("  [ 6 ] Calcular la potencia")
        print("  [ 7 ] Salir del programa\n")
        
        opcion = input(" Ingrese el número de su opción: ")
        
        if opcion == '1':
            Sumar()
        elif opcion == '2':
            Restar()
        elif opcion == '3':
            Multiplicar()
        elif opcion == '4':
            Dividir()
        elif opcion == '5':
            Factorial()
        elif opcion == '6':
            Potencia()
        elif opcion == '7':
            print("\n ¡Gracias por usar la calculadora! Cerrando el sistema...\n")
            time.sleep(1.5)
            limpiar_pantalla()
            break
        else:
            print("\n[✘] Opción no válida. Por favor, seleccione un número del 1 al 7.")
            time.sleep(1.5)

# ==========================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ==========================================
if __name__ == "__main__":
    Calculadora()