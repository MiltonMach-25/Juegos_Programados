# TORRE DE HANOI - JUEGO

import random
import json

# Variedades de discos
colores = ["ROJO", "AZUL", "VERDE", "AMARILLO",
           "NARANJA", "MORADO", "ROSADO", "CAFE",
           "GRIS", "BLANCO"]

tamanos = ["BAJO", "MEDIO", "ALTO", "SUPERIOR",
           "MINI", "GRANDE", "ENORME", "PEQUEÑO",
           "LARGO", "CORTO"]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Reglas del juego
def reglas():
    print("\n===== TORRE DE HANOI =====")
    print("REGLAS DEL JUEGO:")
    print("1. Puedes elegir entre 3 y 10 torres.")
    print("2. Solo se mueve un disco a la vez.")
    print("3. No poner un disco grande sobre uno pequeño.")
    print("4. El objetivo es pasar todos los discos de la primera torre a otra torre.")

# Preparar discos
def preparar_discos(n, tipo, orden, total_torres):
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

    torres = [[] for _ in range(total_torres)]
    torres[0] = seleccion[::-1]
    return torres

# Mostrar torres
def mostrar_torres(torres):
    print("\nEstado actual:")
    for i in range(len(torres)):
        print(f"Torre {chr(65+i)}:", torres[i])

# Mover disco
def mover(origen, destino, torres):
    if len(torres[origen]) == 0:
        print("Movimiento inválido: torre vacía.")
        return torres, False

    disco = torres[origen][-1]
    if len(torres[destino]) == 0 or disco < torres[destino][-1]:
        torres[destino].append(torres[origen].pop())
        return torres, True
    else:
        print("Movimiento inválido: disco grande sobre pequeño.")
        return torres, False

# Resumen final
def resumen(jugadores, torres, discos, turnos, turnos_por_jugador, completo):
    print("\nRESUMEN FINAL")
    print(f"Total de torres: {torres}")
    print(f"Total de discos: {discos}")
    print(f"Total de jugadores: {jugadores}")
    print(f"Total de turnos: {turnos}")
    if completo:
        print("Resultado: Juego completado con éxito")
    else:
        print("Resultado: Juego incompleto (se salió antes de terminar)")
    print("\nTurnos por jugador:")
    for i in range(jugadores):
        print(f"Jugador {i+1}: {turnos_por_jugador[i]} turnos")

# Guardar partida
def guardar_partida(torres, n, total_torres, jugadores, turnos, turnos_por_jugador, jugador_actual):
    partida = {
        "torres": torres,
        "n": n,
        "total_torres": total_torres,
        "jugadores": jugadores,
        "turnos": turnos,
        "turnos_por_jugador": turnos_por_jugador,
        "jugador_actual": jugador_actual
    }
    with open("partida_guardada.json", "w") as f:
        json.dump(partida, f)
    print("Partida guardada correctamente.")

# Cargar partida
def cargar_partida():
    try:
        with open("partida_guardada.json", "r") as f:
            partida = json.load(f)
        print("Partida cargada correctamente.")
        return partida
    except:
        print("No hay partida guardada disponible.")
        return None

# Juego principal
def jugar(torres, n, total_torres, jugadores, turnos=0, turnos_por_jugador=None, jugador_actual=0):
    if turnos_por_jugador is None:
        turnos_por_jugador = [0] * jugadores

    while True:
        mostrar_torres(torres)

        # Condición de victoria: todos los discos en cualquier torre (menos la inicial A)
        for i in range(1, total_torres):
            if len(torres[i]) == n:
                print("\nFELICITACIONES, se completó el juego de Hanoi.")
                resumen(jugadores, total_torres, n, turnos, turnos_por_jugador, True)
                return None

        print(f"\nTurno del Jugador {jugador_actual+1}")
        mov = input("Mover de (ej: A C), 'GUARDAR' o 'SALIR': ").upper()

        if mov == "SALIR":
            print("\nJuego terminado sin completar. Puedes continuar después.")
            resumen(jugadores, total_torres, n, turnos, turnos_por_jugador, False)
            return torres

        if mov == "GUARDAR":
            guardar_partida(torres, n, total_torres, jugadores, turnos, turnos_por_jugador, jugador_actual)
            continue

        try:
            o, d = mov.split()
            o = ord(o) - 65
            d = ord(d) - 65
            if 0 <= o < total_torres and 0 <= d < total_torres:
                torres, valido = mover(o, d, torres)
                if valido:
                    turnos += 1
                    turnos_por_jugador[jugador_actual] += 1
                    jugador_actual = (jugador_actual + 1) % jugadores
            else:
                print("Movimiento inválido: torre no existe.")
        except:
            print("Formato incorrecto. Ejemplo válido: A C")

# Menú principal
def menu():
    reglas()
    while True:
        print("\nMENÚ PRINCIPAL")
        print("1. Iniciar juego nuevo")
        print("2. Continuar juego guardado")
        print("3. Salir")
        opcion = input("Seleccione: ")

        if opcion == "1":
            print("\nElige tipo de discos:")
            print("1. Colores")
            print("2. Tamaños")
            print("3. Números")
            tipo = input("Opción: ")

            print("\nElige orden de los discos:")
            print("1. Ordenado")
            print("2. Aleatorio")
            orden = input("Opción: ")

            n = int(input("¿Cuántos discos? (3 a 10): "))
            if n < 3 or n > 10:
                print("Número inválido, se jugará con 3 discos.")
                n = 3

            total_torres = int(input("¿Cuántas torres? (3 a 10): "))
            if total_torres < 3 or total_torres > 10:
                print("Número inválido, se jugará con 3 torres.")
                total_torres = 3

            jugadores = int(input("¿Cuántos jugadores? (1 a 5): "))
            if jugadores < 1 or jugadores > 5:
                print("Número inválido, se jugará con 1 jugador.")
                jugadores = 1

            if jugadores == 1:
                print("Recomendación: usa entre 3 y 6 torres para un jugador.")
            else:
                print("Recomendación: usa entre 4 y 10 torres para varios jugadores.")

            torres = preparar_discos(n, tipo, orden, total_torres)
            jugar(torres, n, total_torres, jugadores)

        elif opcion == "2":
            partida = cargar_partida()
            if partida:
                jugar(partida["torres"],
                      partida["n"],
                      partida["total_torres"],
                      partida["jugadores"],
                      partida["turnos"],
                      partida["turnos_por_jugador"],
                      partida["jugador_actual"])
        elif opcion == "3":
            print("Hasta pronto.")
            break
        else:
            print("Opción inválida, intente otra vez.")

# Iniciar programa
menu()
