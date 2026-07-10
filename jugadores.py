def crear_jugadores_tenis():
    """Crea una lista con 10 diccionarios de jugadores de tenis."""
    return [
        {"id": 1, "nombre": "Carlos Mendez", "pais": "Colombia", "edad": 24, "partidosGanados": [3, 5, 7], "estado": "ACTIVO"},
        {"id": 2, "nombre": "Ana Torres", "pais": "México", "edad": 27, "partidosGanados": [2, 4, 6], "estado": "ACTIVO"},
        {"id": 3, "nombre": "Luis Ortega", "pais": "Argentina", "edad": 29, "partidosGanados": [1, 3, 8], "estado": "LESIONADO"},
        {"id": 4, "nombre": "Sofía Ruiz", "pais": "España", "edad": 22, "partidosGanados": [4, 6, 9], "estado": "ACTIVO"},
        {"id": 5, "nombre": "Mateo Silva", "pais": "Chile", "edad": 31, "partidosGanados": [5, 7, 10], "estado": "ACTIVO"},
        {"id": 6, "nombre": "Daniela Paz", "pais": "Perú", "edad": 26, "partidosGanados": [2, 5, 7], "estado": "LESIONADO"},
        {"id": 7, "nombre": "Javier León", "pais": "Uruguay", "edad": 28, "partidosGanados": [3, 6, 8], "estado": "ACTIVO"},
        {"id": 8, "nombre": "Paula Gómez", "pais": "Costa Rica", "edad": 25, "partidosGanados": [1, 4, 5], "estado": "ACTIVO"},
        {"id": 9, "nombre": "Nicolás Vega", "pais": "Ecuador", "edad": 30, "partidosGanados": [2, 3, 9], "estado": "LESIONADO"},
        {"id": 10, "nombre": "Valeria Cruz", "pais": "Paraguay", "edad": 23, "partidosGanados": [4, 5, 6], "estado": "ACTIVO"},
    ]


def sumar_partidos(jugador):
    """Devuelve la suma total de partidos ganados por un jugador."""
    return sum(jugador["partidosGanados"])


def mostrar_jugadores(jugadores):
    """Muestra todos los jugadores registrados."""
    if not jugadores:
        print("No hay jugadores registrados.")
        return

    print("\nJugadores registrados:")
    for jugador in jugadores:
        print(
            f"ID: {jugador['id']} | Nombre: {jugador['nombre']} | País: {jugador['pais']} | Edad: {jugador['edad']} | "
            f"Partidos ganados: {sumar_partidos(jugador)} | Estado: {jugador['estado']}"
        )


def ordenar_jugadores_por_partidos(jugadores):
    """Ordena los jugadores por la suma total de partidos ganados de menor a mayor."""
    jugadores_ordenados = list(jugadores)
    jugadores_ordenados.sort(key=sumar_partidos)
    return jugadores_ordenados


def agregar_jugador(jugadores, nuevo_jugador):
    """Agrega un nuevo jugador usando append."""
    jugadores.append(nuevo_jugador)
    print("Jugador agregado correctamente.")


def insertar_jugador(jugadores, nuevo_jugador, indice):
    """Inserta un jugador en una posición específica usando insert."""
    jugadores.insert(indice, nuevo_jugador)
    print("Jugador insertado correctamente.")


def eliminar_jugador(jugadores, jugador_id):
    """Elimina un jugador usando pop o remove."""
    for indice, jugador in enumerate(jugadores):
        if jugador["id"] == jugador_id:
            jugadores.pop(indice)
            print("Jugador eliminado correctamente.")
            return True

    print("Jugador no encontrado.")
    return False
