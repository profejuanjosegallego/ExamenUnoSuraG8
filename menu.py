from auth import autenticar_usuario, registrar_usuario
from jugadores import (
    agregar_jugador,
    crear_jugadores_tenis,
    eliminar_jugador,
    insertar_jugador,
    mostrar_jugadores,
    ordenar_jugadores_por_partidos,
)


def menu_principal():
    """Ejecuta el menú principal del sistema."""
    usuarios = []
    jugadores_tenis = crear_jugadores_tenis()

    while True:
        print("\n=== Sistema de gestión de academia deportiva de tenis ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            correo = input("Ingrese su correo: ").strip()
            password = input("Ingrese su contraseña: ").strip()
            registrar_usuario(usuarios, correo, password)
        elif opcion == "2":
            correo = input("Correo: ").strip()
            password = input("Contraseña: ").strip()
            if autenticar_usuario(usuarios, correo, password, 3):
                print("Login exitoso")
                menu_gestion_jugadores(jugadores_tenis)
            else:
                print("Programa finalizado.")
                break
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


def menu_gestion_jugadores(jugadores):
    """Muestra el menú para gestionar jugadores."""
    while True:
        print("\n1. Mostrar todos los jugadores")
        print("2. Ordenar jugadores por partidos ganados")
        print("3. Agregar jugador")
        print("4. Insertar jugador")
        print("5. Eliminar jugador")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_jugadores(jugadores)
        elif opcion == "2":
            ordenados = ordenar_jugadores_por_partidos(jugadores)
            print("\nJugadores ordenados por partidos ganados:")
            for jugador in ordenados:
                print(f"{jugador['nombre']}: {sum(jugador['partidosGanados'])}")
        elif opcion == "3":
            nuevo_id = len(jugadores) + 1
            nuevo_jugador = {
                "id": nuevo_id,
                "nombre": input("Nombre del jugador: ").strip(),
                "pais": input("País del jugador: ").strip(),
                "edad": int(input("Edad del jugador: ").strip()),
                "partidosGanados": [int(x) for x in input("Partidos ganados (separados por espacio): ").split()],
                "estado": input("Estado (ACTIVO/LESIONADO): ").strip().upper(),
            }
            agregar_jugador(jugadores, nuevo_jugador)
        elif opcion == "4":
            nuevo_id = len(jugadores) + 1
            nuevo_jugador = {
                "id": nuevo_id,
                "nombre": input("Nombre del jugador: ").strip(),
                "pais": input("País del jugador: ").strip(),
                "edad": int(input("Edad del jugador: ").strip()),
                "partidosGanados": [int(x) for x in input("Partidos ganados (separados por espacio): ").split()],
                "estado": input("Estado (ACTIVO/LESIONADO): ").strip().upper(),
            }
            indice = int(input("Posición de inserción: ").strip())
            insertar_jugador(jugadores, nuevo_jugador, indice)
        elif opcion == "5":
            jugador_id = int(input("ID del jugador a eliminar: ").strip())
            eliminar_jugador(jugadores, jugador_id)
        elif opcion == "6":
            print("Saliendo del módulo de jugadores...")
            break
        else:
            print("Opción inválida")
