from auth import autenticar_usuario, registrar_usuario
from jugadores import (
    crear_jugadores_tenis,
    ordenar_jugadores_por_partidos,
)
from menu import menu_gestion_jugadores, menu_principal

__all__ = [
    "registrar_usuario",
    "autenticar_usuario",
    "crear_jugadores_tenis",
    "ordenar_jugadores_por_partidos",
    "menu_principal",
    "menu_gestion_jugadores",
]


if __name__ == "__main__":
    menu_principal()
