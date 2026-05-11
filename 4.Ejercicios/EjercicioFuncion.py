'''
Ejercicio: El Simulador "Python Coffee Shop"

El estudiante debe construir un programa que gestione la venta de un café. Para ello, 
deberá programar 4 funciones específicas, cada una representando uno de los 4 tipos de 
funciones que aprendimos.

/>.   El Flujo de Trabajo

El programa debe funcionar así:

1. Se muestra un saludo.
2. Se le pregunta al usuario qué tamaño de café quiere.
3. Se calcula el precio sumando impuestos.
4. Se confirma que el pedido está listo.

1. Sin parámetros y Sin retorno: mostrar_bienvenida()

¿Qué debe hacer el estudiante?
Crear una función que solo imprima texto decorativo.

Instrucción: Debe imprimir el nombre de la cafetería y el menú de tamaños 
(Pequeño: $2.00, Mediano: $3.00, Grande: $4.00).

Objetivo: Entender que hay funciones que solo sirven para comunicar información fija al usuario.

2. Sin parámetros y Con retorno: elegir_tamano()

¿Qué debe hacer el estudiante?
Crear una función que interactúe con el teclado y "envíe" la respuesta hacia afuera.

Instrucción: Debe preguntar al usuario: "¿Qué tamaño desea? (P/M/G):". La función debe capturar la letra con un input() y devolverla usando return.

Objetivo: Entender que una función puede obtener datos del mundo exterior y entregarlos al programa.

3. Con parámetros y Con retorno: calcular_precio(letra_tamano)

¿Qué debe hacer el estudiante?
Crear la lógica matemática del negocio.

Instrucción: La función recibe la letra (P, M o G).

Si es 'P', el precio es 2.0.

Si es 'M', es 3.0.

Si es 'G', es 4.0.

Al final, debe sumarle un 10% de impuesto y retornar el total final.

Objetivo: Entender el procesamiento: entra un dato crudo (letra) y sale un dato procesado (dinero).

4. Con parámetros y Sin retorno: preparar_pedido(letra_tamano, total)

¿Qué debe hacer el estudiante?
Crear la acción final que cierra el proceso.

Instrucción: La función recibe el tamaño y el precio final. Debe imprimir un mensaje como: "Preparando su café [tamaño]... El total fue $[total]. ¡Disfrute!".

Objetivo: Entender que una función puede usar resultados previos para ejecutar una acción de cierre.
'''

import time
import os

# 1. FUNCIÓN SIN PARÁMETROS Y SIN RETORNO
def mostrar_bienvenida():
    # Limpia la pantalla para un efecto más profesional
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=" * 60)
    print("          ☕  SISTEMA DE VENTAS PYTHON COFFEE  ☕")
    print("=" * 60)
    print(r"""
      PEQUEÑO (P)          MEDIANO (M)           GRANDE (G)
        $2.00                 $3.00                $4.00
                                               
         ( (                  ) )                  ( (
          ) )                ( (                    ) )
        .---.                .---.                .------.
       |     |__            |     |__            |        |__
       |     |--|           |     |--|           |        |--|
       |     |  |           |     |  |           |        |  |
        '---' --'            '---' --'            '------' --'
    """)
    print("=" * 60)

# 2. FUNCIÓN SIN PARÁMETROS Y CON RETORNO
def elegir_tamano():
    opciones_validas = {'P': 'Pequeño', 'M': 'Mediano', 'G': 'Grande'}
    seleccion = ""
    
    while seleccion not in opciones_validas:
        seleccion = input(" ➤  Seleccione el tamaño deseado [P, M, G]: ").upper()
        if seleccion not in opciones_validas:
            print(" ⚠️  Error: Por favor, elija una letra válida del menú.")
            
    return seleccion

# 3. FUNCIÓN CON PARÁMETROS Y CON RETORNO
def calcular_precio(letra):
    tarifas = {'P': 2.0, 'M': 3.0, 'G': 4.0}
    subtotal = tarifas[letra]
    impuesto = subtotal * 0.15  # 15% de impuesto
    return subtotal + impuesto

# 4. FUNCIÓN CON PARÁMETROS Y SIN RETORNO
def preparar_pedido(letra, total):
    # Diccionario interno para la parte visual del llenado
    detalles = {
        'P': {"lineas": 4, "ancho": 7, "nombre": "PEQUEÑO"},
        'M': {"lineas": 6, "ancho": 7, "nombre": "MEDIANO"},
        'G': {"lineas": 8, "ancho": 11, "nombre": "GRANDE"}
    }
    
    config = detalles[letra]
    print(f"\n[SISTEMA]: Iniciando proceso de llenado para tamaño {config['nombre']}...")
    time.sleep(1)

    # Simulación de llenado ASCII dinámico
    for i in range(config['lineas'], 0, -1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n   --- LLENANDO TAZA {config['nombre']} ---")
        
        # Dibujar el vapor
        print("          (  (  )")
        print("           )  )  )")
        
        # Dibujar la parte vacía (arriba)
        for _ in range(i):
            print(f"         |{' ' * config['ancho']}|__")
            
        # Dibujar la parte con café (abajo)
        for _ in range(config['lineas'] - i):
            print(f"         |{'~' * config['ancho']}|--|")
            
        print(f"         |{'_' * config['ancho']}|__|")
        time.sleep(0.4)

    # Ticket Final Gráfico
    print("\n" + "╔══════════════════════════════════════════╗")
    print("║          COMPROBANTE DE PAGO             ║")
    print("╠══════════════════════════════════════════╣")
    print(f"║ PRODUCTO: Café {config['nombre']:<15}       ║")
    print(f"║ TOTAL (IVA Incluido): ${total:>10.2f}        ║")
    print("╠══════════════════════════════════════════╣")
    print("║      ¡Gracias por preferirnos!           ║")
    print("╚══════════════════════════════════════════╝\n")

# --- FLUJO LÓGICO ---
mostrar_bienvenida()
tamaño_elegido = elegir_tamano()
precio_total = calcular_precio(tamaño_elegido)
preparar_pedido(tamaño_elegido, precio_total)



'''
import time
import os

# 1. FUNCIÓN SIN PARÁMETROS Y SIN RETORNO (Interfaz de Selección)
def mostrar_bienvenida():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 65)
    print("             ☕  PYTHON PREMIUM COFFEE SHOP  ☕")
    print("=" * 65)
    print(r"""
      [ PEQUEÑO - P ]        [ MEDIANO - M ]         [ GRANDE - G ]
          $2.00                  $3.00                   $4.00
          
         (  )  )                (  )  )                 (  )  )
          )  (  (                )  (  (                 )  (  (
       .----------.           .----------.            .-----------.
      |            |         |            |          |             |
      |    (P)     |===|     |    (M)     |===|      |     (G)     |===|
      |            |   |     |            |   |      |             |   |
       \          / ==='      \          / ==='       \           / ==='
        '--------'             '--------'              '---------'
    """)
    print("=" * 65)

# 2. FUNCIÓN SIN PARÁMETROS Y CON RETORNO (Captura de datos)
def elegir_tamano():
    while True:
        opcion = input(" ➤  Escriba el tamaño deseado (P / M / G): ").upper()
        if opcion in ['P', 'M', 'G']:
            return opcion
        print(" ❌ Error: Selección no reconocida. Por favor, use P, M o G.")

# 3. FUNCIÓN CON PARÁMETROS Y CON RETORNO (Cálculo lógico)
def calcular_precio(letra):
    precios = {'P': 2.0, 'M': 3.0, 'G': 4.0}
    tasa_iva = 0.12 # 12% de impuesto
    total = precios[letra] * (1 + tasa_iva)
    return total

# 4. FUNCIÓN CON PARÁMETROS Y SIN RETORNO (Animación y Ticket)
def preparar_pedido(letra, total):
    config = {
        'P': {"alto": 4, "ancho": 12, "msg": "Pequeño"},
        'M': {"alto": 6, "ancho": 12, "msg": "Mediano"},
        'G': {"alto": 9, "ancho": 16, "msg": "Grande"}
    }[letra]

    # Simulación de llenado
    for nivel in range(config['alto'] + 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n   ⏳ PROCESANDO CAFÉ {config['msg']}...")
        
        # Vapor animado
        v = "   (  (  " if nivel % 2 == 0 else "    )  ) "
        print(f"\n{v.center(30)}")
        
        # Dibujar parte vacía
        for _ in range(config['alto'] - nivel):
            print(f"      |{' ' * config['ancho']}|")
            
        # Dibujar parte llena (con textura de café)
        for _ in range(nivel):
            print(f"      |{'█' * config['ancho']}|")
            
        # Base de la taza
        print(f"       \\{'_' * (config['ancho']-2)}/ \n")
        time.sleep(0.4)

    # Ticket de salida estilizado
    print(" ╔" + "═" * 38 + "╗")
    print(" ║         RECIBO DE CONSUMO            ║")
    print(" ╠" + "═" * 38 + "╣")
    print(f" ║ TAMAÑO: {config['msg']:<28} ║")
    print(f" ║ TOTAL A PAGAR: ${total:>19.2f} ║")
    print(" ╚" + "═" * 38 + "╝")
    print("\n   ✨ ¡Disfrute su café recién hecho! ✨\n")

# --- FLUJO PRINCIPAL ---
mostrar_bienvenida()
opcion = elegir_tamano()
precio = calcular_precio(opcion)
preparar_pedido(opcion, precio)
'''