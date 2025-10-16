# Torre de  Hanoi - Versión Recursiva y Práctica
import random

colores = ["ROJO", "AZUL", "VERDE", "AMARILLO",
        "NARANJA", "MORADO", "ROSADO", "CAFE",
        "GRIS", "BLANCO"]
tamanos = ["BAJO", "MEDIO", "ALTO", "SUPERIOR",
        "MINI", "GRANDE", "ENORME", "PEQUEÑO",
        "LARGO", "CORTO"]
numeros = [1,2,3,4,5,6,7,8,9,10]

def reglas():
    print("\nTORRE DE HANOI - REGLAS")
    print("1. Mover un disco a la vez")
    print("2. No poner disco grande sobre pequeño")
    print("3. Pasar todos los discos de A hasta C")

def preparar_discos(n, tipo, orden):
    if tipo == "1":
        base = colores
    elif tipo == "2":
        base = tamanos
    else:
        base = [str(x) for x in numeros]

    if n <= len(base):
        seleccion = random.sample(base, n)
    else:
        seleccion = random.choices(base, k=n)

    if orden == "1":
        seleccion.sort()
    else:
        random.shuffle(seleccion)

    return [seleccion[::-1], [], []]

def mostrar_torres(torres):
    print("A:", torres[0])
    print("B:", torres[1])
    print("C:", torres[2])

def mover(origen, destino, torres):
    if not torres[origen]:
        print("Torre vacía")
        return False
    disco = torres[origen][-1]
    if not torres[destino] or disco < torres[destino][-1]:
        torres[destino].append(torres[origen].pop())
        return True
    else:
        print("Movimiento no permitido")
        return False

# Recursividad aplicada
def hanoi_recursivo(n, origen, destino, auxiliar):
    if n == 1:              # Caso base
        print(f"Mover disco de {origen} a {destino}")
    else:                   # Paso recursivo
        hanoi_recursivo(n-1, origen, auxiliar, destino)
        print(f"Mover disco de {origen} a {destino}")
        hanoi_recursivo(n-1, auxiliar, destino, origen)

def jugar_recursivo():
    n = int(input("Número de discos (3 a 10): "))
    if n < 3 or n > 10:
        n = 3
    print("\nSolución automática con recursividad:\n")
    hanoi_recursivo(n, "A", "C", "B")
    print("\nFin del proceso recursivo")

def jugar_interactivo():
    tipo = input("Tipo discos (1 colores, 2 tamaños, 3 números): ")
    orden = input("Orden (1 ordenado, 2 aleatorio): ")
    n = int(input("Número de discos (3 a 10): "))
    if n < 3 or n > 10:
        n = 3
    torres = preparar_discos(n, tipo, orden)

    while True:
        mostrar_torres(torres)
        if len(torres[2]) == n:
            print("Juego completado, ¡felicitaciones!")
            break
        mov = input("Mover (ej: A C) o SALIR: ").upper()
        if mov == "SALIR":
            print("Juego terminado por el usuario")
            break
        try:
            o, d = mov.split()
            o, d = ord(o) - 65, ord(d) - 65
            mover(o, d, torres)
        except:
            print("Movimiento inválido, intenta de nuevo")

def menu():
    reglas()
    while True:
        print("\nMENU PRINCIPAL")
        print("1. Jugar manualmente")
        print("2. Resolver con recursividad")
        print("3. Salir")
        op = input("Opción: ")
        if op == "1":
            jugar_interactivo()
        elif op == "2":
            jugar_recursivo()
        elif op == "3":
            print("Hasta pronto")
            break
        else:
            print("Opción inválida")

menu()
